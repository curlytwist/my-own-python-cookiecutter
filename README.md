# My Own Python Cookiecutter

_For the children of tomorrow..._

### Requirements
-----------
 - Python 3.5+

 ``` python
 python -V  # check current version
 ```

 - Miniconda (Conda + setuptools)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0

 ``` bash
 conda config --add channels conda-forge    # add conda-forge on top of channel lists
 conda install -c conda-forge cookiecutter  # install cookiecutter from conda-forge
 ```


### Generate the scaffolding
------------

Inside an empty folder for the new project, run:
``` python
cookiecutter https://github.com/curlytwist/my-own-python-cookiecutter
```

Thanks for reading!
