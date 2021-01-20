# My Own Python Cookiecutter

_For the projects of tomorrow._


### Requirements
-----------
 - Python 3.5+
 - `Conda`, the environment/package manager
 - [Cookiecutter package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0

 ``` bash
 conda config --add channels conda-forge    # add conda-forge on top of channel lists
 conda install -c conda-forge cookiecutter  # install cookiecutter from conda-forge
 ```

 - OPTIONAL: `setuptools` package for installing a pkg with `setup.py` (currently installed automatically thanks to `environment.yml`)

<br />

### Generate the Scaffolding
------------

In the terminal, run the following command to create the root folder for your new project:
``` bash
cookiecutter https://github.com/curlytwist/my-own-python-cookiecutter
```

<br />

### Create a Dedicated Conda Environment
------------

Execute the Makefile inside your new repo in order to create its own Conda environment:
``` bash
make -f Makefile    
```

For Mac users, if [this error](https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a) occurs, you might have to install the Command Line Tools package:

 ``` bash
xcode-select --install 
xcode-select --reset      # if --install does not work 
```

------------

### Thanks for reading!
