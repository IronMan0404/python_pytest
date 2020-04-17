**Type this into your bash window/terminal**
~~~~
git clone https://github.com/IronMan0404/python_pytest.git
1. change directory to "python_pytest"
2. git fetch origin
3. git checkout master
~~~~
"After Clone" 

# Please install all required packages from requirements.txt file

Run Command `pytest --reruns 2 --reruns-delay 1 --html=pytest_selenium_test_report.html tests/test_get_api.py  -v`

# Parallel execution: (example: --workers auto, --workers 2 )


~~~~
# runs 2 workers with 1 test per worker at a time
pytest --workers 2

# runs 4 workers (assuming a quad-core machine) with 1 test per worker
pytest --workers auto

~~~~
`pytest --workers auto --reruns 2 --reruns-delay 1 --html=pytest_selenium_test_report.html tests/test_get_api.py  -v`
~~~~
 