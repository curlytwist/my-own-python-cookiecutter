# setup.py comes in handy for (publishing and) installing packages
# so that you can use them in other projects too
# (what about other Conda envs? Probably would not work there, should test)

from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
)
