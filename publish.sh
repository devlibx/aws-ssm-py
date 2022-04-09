rm -rf flask_cdc_devlibx.egg-info dist
python3 -m build
python3 -m twine upload --verbose --repository pypi dist/*