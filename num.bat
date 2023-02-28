pytest -s -v -m "sanity and regression" --html=./reports/reprot.html test_cases/ --browser Chrome

rem pytest -s -v -m "sanity or regression" --html=./reports/reprot.html test_cases/ --browser Chrome


rem pytest -s -v -m "sanity" --html=./reports/reprot.html test_cases/ --browser Chrome

rem pytest -s -v -m "regression" --html=./reports/reprot.html test_cases/ --browser Chrome

rem pytest -s -v -m "regression" --html=./reports/reprot.html test_cases/ --browser fireFox
