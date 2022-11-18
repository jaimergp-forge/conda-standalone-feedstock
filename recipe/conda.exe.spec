# -*- mode: python ; coding: utf-8 -*-
import os
import sys

block_cipher = None

# Non imported files need to be added manually via datas or binaries
# Datas are not analyzed, just copied over. Binaries go through some linkage analysis to also bring necessary libs
# This includes plain text files like JSON, modules never imported, or standalone binaries
# Shared objects and DLLs should have been caught by pyinstaller import hooks, but if not, add them
# Format a list of tuples like (file-path, target-DIRECTORY)
binaries = []
datas = [
    (os.path.join(os.getcwd(), 'menuinst_src', 'menuinst', 'data', 'menuinst.menu_item.default.json'), 'menuinst/data'),
    (os.path.join(os.getcwd(), 'menuinst_src', 'menuinst', 'data', 'menuinst.schema.json'), 'menuinst/data'),
]
if sys.platform == "win32":
    datas += [
        (os.path.join(os.getcwd(), 'constructor', 'constructor', 'nsis', '_nsis.py'), 'Lib'),
        (os.path.join(os.getcwd(), 'entry_point_base.exe'), '.'),
    ]
elif sys.platform == "darwin":
    datas += [
        (os.path.join(os.getcwd(), 'menuinst_src', 'menuinst', 'data', 'osx_launcher_arm64'), 'menuinst/data'),
        (os.path.join(os.getcwd(), 'menuinst_src', 'menuinst', 'data', 'osx_launcher_x86_64'), 'menuinst/data'),
    ]

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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
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
          console=True )
