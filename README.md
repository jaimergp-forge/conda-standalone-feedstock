About conda-standalone-feedstock
================================

Feedstock license: [BSD-3-Clause](https://github.com/conda-forge/conda-standalone-feedstock/blob/main/LICENSE.txt)

Home: https://github.com/AnacondaRecipes/conda-standalone-feedstock

Package license: BSD-3-Clause

Summary: Entry point and dependency collection for PyInstaller-based standalone conda.

Current build status
====================


<table>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-conda--standalone-green.svg)](https://anaconda.org/napari/conda-standalone) | [![Conda Downloads](https://img.shields.io/conda/dn/napari/conda-standalone.svg)](https://anaconda.org/napari/conda-standalone) | [![Conda Version](https://img.shields.io/conda/vn/napari/conda-standalone.svg)](https://anaconda.org/napari/conda-standalone) | [![Conda Platforms](https://img.shields.io/conda/pn/napari/conda-standalone.svg)](https://anaconda.org/napari/conda-standalone) |

Installing conda-standalone
===========================

Installing `conda-standalone` from the `napari` channel can be achieved by adding `napari` to your channels with:

```
conda config --add channels napari
conda config --set channel_priority strict
```

Once the `napari` channel has been enabled, `conda-standalone` can be installed with `conda`:

```
conda install conda-standalone
```

or with `mamba`:

```
mamba install conda-standalone
```

It is possible to list all of the versions of `conda-standalone` available on your platform with `conda`:

```
conda search conda-standalone --channel napari
```

or with `mamba`:

```
mamba search conda-standalone --channel napari
```

Alternatively, `mamba repoquery` may provide more information:

```
# Search all versions available on your platform:
mamba repoquery search conda-standalone --channel napari

# List packages depending on `conda-standalone`:
mamba repoquery whoneeds conda-standalone --channel napari

# List dependencies of `conda-standalone`:
mamba repoquery depends conda-standalone --channel napari
```




Updating conda-standalone-feedstock
===================================

If you would like to improve the conda-standalone recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`napari` channel, whereupon the built conda packages will be available for
everybody to install and use from the `napari` channel.
Note that all branches in the conda-forge/conda-standalone-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================

* [@jaimergp](https://github.com/jaimergp/)

