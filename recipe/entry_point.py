#!/spare/local/nwani/pyinstaller_stuff/dev/bin/python
# -*- coding: utf-8 -*-
import os
import argparse
import sys
import runpy
from code import InteractiveConsole

from concurrent.futures import Executor
from multiprocessing import freeze_support

# use this for debugging, because ProcessPoolExecutor isn't pdb/ipdb friendly
class DummyExecutor(Executor):
    def map(self, func, *iterables):
        for iterable in iterables:
            for thing in iterable:
                yield func(thing)


if __name__ == '__main__':
    freeze_support()
    # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support
    # Before any more imports, leave cwd out of sys.path for internal 'conda shell.*' commands.
    # see https://github.com/conda/conda/issues/6549
    if len(sys.argv) > 1 and sys.argv[1].startswith('shell.') and sys.path and sys.path[0] == '':
        # The standard first entry in sys.path is an empty string,
        # and os.path.abspath('') expands to os.getcwd().
        del sys.path[0]
        
    if len(sys.argv) > 1 and sys.argv[1] == 'python':
        del sys.argv[1]
        p = argparse.ArgumentParser(description="Python interface emulation.")
        version = "Python " + ".".join([str(x) for x in sys.version_info[:3]])
        p.add_argument("-V", "--version", action="version", version=version)
        group = p.add_mutually_exclusive_group()
        group.add_argument('-c', '--command', action="store")
        group.add_argument('-m', '--module', action="store")
        group.add_argument('script', nargs="?", default=None)
        args, args_unknown = p.parse_known_args()
        if args.command:
            sys.exit(exec(args.command))
        elif args.module:
            _ = runpy.run_module(args.module)
            sys.exit()
        elif args.script:
            _ = runpy.run_path(args.script)
            sys.exit()
        # else, interactive REPL
        class CondaStandaloneConsole(InteractiveConsole):
            pass

        sys.exit(CondaStandaloneConsole().interact(exitmsg=""))
        

    if len(sys.argv) > 1 and sys.argv[1].startswith('constructor'):

       from conda.base.constants import CONDA_PACKAGE_EXTENSIONS
       p = argparse.ArgumentParser(description="constructor args")
       p.add_argument(
               '--prefix',
               action="store",
               required="True",
               help="path to conda prefix")
       p.add_argument(
               '--base-prefix',
               action="store",
               help="path to base installation, needed for make-menus in non-base envs")
       p.add_argument(
               '--extract-conda-pkgs',
               action="store_true",
               help="path to conda prefix")
       p.add_argument(
               '--extract-tarball',
               action="store_true",
               help="extract tarball from stdin")
       p.add_argument(
               '--make-menus',
               nargs='*',
               metavar='MENU_PKG',
               help="make menus")
       p.add_argument(
               '--rm-menus',
               action="store_true",
               help="rm menus")
       args, args_unknown = p.parse_known_args()
       args.prefix = os.path.abspath(args.prefix)
       os.chdir(args.prefix)
       if args.extract_conda_pkgs:
           import tqdm
           from conda_package_handling import api
           from concurrent.futures import ProcessPoolExecutor
           executor = ProcessPoolExecutor()

           os.chdir("pkgs")
           flist = []
           for ext in CONDA_PACKAGE_EXTENSIONS:
               for pkg in os.listdir(os.getcwd()):
                   if pkg.endswith(ext):
                       fn = os.path.join(os.getcwd(), pkg)
                       flist.append(fn)
           with tqdm.tqdm(total=len(flist), leave=False) as t:
               for fn, _ in zip(flist, executor.map(api.extract, flist)):
                   t.set_description("Extracting : %s" % os.path.basename(fn))
                   t.update()

       if args.extract_tarball:
           import tarfile
           t = tarfile.open(mode="r|*", fileobj=sys.stdin.buffer)
           t.extractall()
           t.close()
       if (args.make_menus is not None) or args.rm_menus:
           import importlib.util
           base_prefix = args.base_prefix or args.prefix
           utility_script = os.path.join(base_prefix, "Lib", "_nsis.py")
           spec = importlib.util.spec_from_file_location("constructor_utils", utility_script)
           module = importlib.util.module_from_spec(spec)
           spec.loader.exec_module(module)
           if args.make_menus is not None:
               module.mk_menus(remove=False, prefix=args.prefix, pkg_names=args.make_menus, root_prefix=base_prefix)
           else:
               module.rm_menus(prefix=args.prefix, root_prefix=base_prefix)
       sys.exit()
    else:
       from conda.cli import main
       sys.exit(main())
