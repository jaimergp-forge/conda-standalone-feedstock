# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import site

block_cipher = None
sitepackages = os.environ.get(
    "SP_DIR", # site-packages in conda-build's host environment
    # if not defined, get running Python's site-packages 
    # Windows puts sys.prefix in this list first
    next(
        path for path in site.getsitepackages()
        if path.endswith("site-packages")
    )
)

extra_exe_kwargs = {}

# Non imported files need to be added manually via datas or binaries
# Datas are not analyzed, just copied over. Binaries go through some linkage analysis to also bring necessary libs
# This includes plain text files like JSON, modules never imported, or standalone binaries
# Shared objects and DLLs should have been caught by pyinstaller import hooks, but if not, add them
# Format a list of tuples like (file-path, target-DIRECTORY)
binaries = []
datas = [
    (os.path.join(sitepackages, 'menuinst', 'data', 'menuinst.menu_item.default.json'), 'menuinst/data'),
    (os.path.join(sitepackages, 'menuinst', 'data', 'menuinst.schema.json'), 'menuinst/data'),
]
if sys.platform == "win32":
    datas += [
        (os.path.join(os.getcwd(), 'constructor', 'constructor', 'nsis', '_nsis.py'), 'Lib'),
        (os.path.join(os.getcwd(), 'entry_point_base.exe'), '.'),
    ]
elif sys.platform == "darwin":
    datas += [
        (os.path.join(sitepackages, 'menuinst', 'data', 'osx_launcher_arm64'), 'menuinst/data'),
        (os.path.join(sitepackages, 'menuinst', 'data', 'osx_launcher_x86_64'), 'menuinst/data'),
    ]
    target_platform = os.environ.get("target_platform")
    if target_platform and target_platform != os.environ.get("build_platform"):
        extra_exe_kwargs["target_arch"] = "arm64" if target_platform == "osx-arm64" else "x86_64"
    extra_exe_kwargs["entitlements_file"] = "entitlements.plist"


a = Analysis(['entry_point.py', 'imports.py'],
             pathex=['.'],
             binaries=binaries,
             datas=datas,
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['test'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


if "target_arch" in extra_exe_kwargs:
    # Patch paths for cross-building; assumes IDENTICAL BUILD and HOST environments 
    for attr in "scripts", "pure", "binaries", "zipfiles", "zipped_data", "datas", "dependencies":
    # for attr in ("binaries",):
        toc = getattr(a, attr)
        new_toc = []
        for entry in toc:
            path, abspath, kind = entry
            if hasattr(abspath, "replace"):
                abspath = abspath.replace(os.environ["BUILD_PREFIX"], os.environ["PREFIX"])
            new_toc.append((path, abspath, kind))
        setattr(a, attr, new_toc)

    # Patch which bootloader is found (pyinstaller will look into its sys.prefix)
    # We could also replace the files in BUILD_PREFIX, but this is less destructive
    def replace_build_prefix(func):
        def wraps(*args):
            return str(func(*args)).replace(os.environ["BUILD_PREFIX"], os.environ["PREFIX"])
        return wraps
    EXE._bootloader_file = replace_build_prefix(EXE._bootloader_file)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='conda.exe',
          icon="icon.ico",
          debug=False,
          bootloader_ignore_signals=False,
          strip=(sys.platform!="win32"),
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          **extra_exe_kwargs)
