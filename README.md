About conda-standalone
======================

Home: https://github.com/AnacondaRecipes/conda-standalone-feedstock

Package license: BSD-3-Clause

Feedstock license: [BSD-3-Clause](https://github.com/conda-forge/conda-standalone-feedstock/blob/master/LICENSE.txt)

Summary: Entry point and dependency collection for PyInstaller-based standalone conda.

Current build status
====================


<table><tr>
    <td>Travis</td>
    <td>
      <a href="https://travis-ci.com/conda-forge/conda-standalone-feedstock">
        <img alt="macOS" src="https://img.shields.io/travis/com/conda-forge/conda-standalone-feedstock/master.svg?label=macOS">
      </a>
    </td>
  </tr>

  <tr>
    <td>Azure</td>
    <td>
      <details>
        <summary>
          <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=8444&branchName=master">
            <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/conda-standalone-feedstock?branchName=master">
          </a>
        </summary>
        <table>
          <thead><tr><th>Variant</th><th>Status</th></tr></thead>
          <tbody><tr>
              <td>linux_64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=8444&branchName=master">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/conda-standalone-feedstock?branchName=master&jobName=linux&configuration=linux_64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>linux_aarch64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=8444&branchName=master">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/conda-standalone-feedstock?branchName=master&jobName=linux&configuration=linux_aarch64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>linux_ppc64le</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=8444&branchName=master">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/conda-standalone-feedstock?branchName=master&jobName=linux&configuration=linux_ppc64le_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>osx_64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=8444&branchName=master">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/conda-standalone-feedstock?branchName=master&jobName=osx&configuration=osx_64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>win_64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=8444&branchName=master">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/conda-standalone-feedstock?branchName=master&jobName=win&configuration=win_64_" alt="variant">
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </details>
    </td>
  </tr>
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

Once the `napari` channel has been enabled, `conda-standalone` can be installed with:

```
conda install conda-standalone
```

It is possible to list all of the versions of `conda-standalone` available on your platform with:

```
conda search conda-standalone --channel napari
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

* [@forrestwaters](https://github.com/forrestwaters/)
* [@jakirkham](https://github.com/jakirkham/)
* [@msarahan](https://github.com/msarahan/)
* [@nehaljwani](https://github.com/nehaljwani/)

