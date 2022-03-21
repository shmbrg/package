## package

This is a **test** package. It doesn't do much. You can do the following:

* Run tests with ``python -m pytest tests/``.
* Build package with ``python -m build`` (make sure you have ``build`` installed: ``python3 -m pip install --upgrade build``)
* (Alternatively: ``python -m sdist``)
* Test installing package with ``pip install .`` on root level.
* For uploading the package follow instructions: https://towardsdatascience.com/how-to-package-your-python-code-df5a7739ab2e

In Zeit Cosmos:

* To upload use `twine upload -r zeit dist/<.tar.gz>` (`zeit` has to be configured in `.pypirc`)
* Install `pip install --index=https://devpi.zeit.de/zeit/default package`
