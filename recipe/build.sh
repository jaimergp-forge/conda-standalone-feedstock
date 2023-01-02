set -euxo pipefail

# patched conda files
# new files in patches need to be added here
for fname in "core/path_actions.py" "utils.py"; do
  mv "$SP_DIR/conda/${fname}" "$SP_DIR/conda/${fname}.bak"
  cp "conda_src/conda/${fname}" "$SP_DIR/conda/${fname}"
done

# make sure pyinstaller finds Apple's codesign first in PATH
# some base installations have 'sigtool', which ships a
# 'codesign' binary that might shadow Apple's codesign
if [[ $target_platform == osx-* && ! -f "$BUILD_PREFIX/bin/codesign" ]]; then
  ln -s /usr/bin/codesign "$BUILD_PREFIX/bin/codesign"
fi

if [[ $build_platform != $target_platform ]]; then
  export PYTHONPATH="$PREFIX/lib/python3.9/site-packages"
  export PYTHON="$BUILD_PREFIX/bin/python"
fi
"${PYTHON}" -m PyInstaller conda.exe.spec
mkdir -p "$PREFIX/standalone_conda"
mv dist/conda.exe "$PREFIX/standalone_conda"
# clean up .pyc files that pyinstaller creates
rm -rf "$PREFIX/lib"
