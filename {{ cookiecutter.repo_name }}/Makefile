#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
CONDA_ENV_NAME = {{ cookiecutter.conda_env_name }}

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

# echo $(shell echo HAS_CONDA)
#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Delete all compiled Python files
# clean: test_environment
# 	find . -type f -name "*.py[co]" -delete
# 	find . -type d -name "__pycache__" -delete

## Set up python interpreter environment
create_environment: test_environment
ifeq (True,$(HAS_CONDA))
	@echo ">>> Detected conda, creating conda environment."
	conda env create --name $(CONDA_ENV_NAME) -f ${PROJECT_DIR}/environment.yml
	# conda install -n $(CONDA_ENV_NAME) package1 package2
endif
	@echo "\n>>> New conda env created. Activate with:\nconda activate $(CONDA_ENV_NAME)"

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py
