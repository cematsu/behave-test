import json

import behave2cucumber
from behave.__main__ import main as behave_main

code = behave_main(["features/", "-t @test", "-t~@ignore", '-k', '-o', 'target/cucumber-reports/behave.json', '-f', 'json'])
cucumber_json = behave2cucumber.convert(json.load(open("target/cucumber-reports/behave.json")))
with open('target/cucumber-reports/Cucumber-behave.json', 'w') as report:
    report.write(json.dumps(cucumber_json))
    report.flush()
exit(code)