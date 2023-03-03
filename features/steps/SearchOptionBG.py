import time
from behave import *
from DDF import ExcelUtils
from features.utility.ConfigClass import ConfigClass
from features.pages.SearchOptionClass import SearchOptionClass
from features.pages.SubjectClass import SubjectClass
@step("User send {coursename}")
def step_impl(context, coursename):
    time.sleep(5)
    ExcelUtils.get_row_count(ConfigClass.datafilePath, "Sheet1")
    coursename = ExcelUtils.read_data(ConfigClass.datafilePath, "Sheet1", 3, 1)
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.enter_coursename(coursename)
@then("It shows the Courses")
def step_impl(context):
    expectedURL = "https://unacademy.com/explore"
    pageURL = context.driver.current_url
    try:
        if (expectedURL == pageURL):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.datafilePath, "Sheet1", 3, 2, "Passed")
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.datafilePath, "Sheet1", 3, 3, "Failed")
            assert False
    finally:
        time.sleep(5)
        print(pageURL)







