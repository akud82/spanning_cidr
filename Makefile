SHELL = /bin/bash

default:
	@echo 'Please select a build target.'

clean:
	@echo 'cleaning up temporary files'
	rm -rf dist/
	rm -rf build/
	find . -name '*.pyc' -exec rm -f {} ';'
	find . -name '*.pyo' -exec rm -f {} ';'

test: clean
	@echo 'running test suite'
	pip install -r requirements.txt
	py.test tests

