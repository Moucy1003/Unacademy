import time
from behave import *
from hamcrest import *
from features.pages.SearchOptionClass import SearchOptionClass
from features.pages.SubjectClass import SubjectClass
from selenium.webdriver.common.keys import Keys

@given(u'Chrome is opened and Unacademy app is opened')
def step_impl(context):
     pass
@then("User navigates onto the site and the Search Option is visible")
def step_impl(context):
    time.sleep(3)
    expectedTitle = "Goals | Unacademy"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
@when(u'User navigates onto the Search Option of the Site')
def step_impl(context):
    pass
@when(u'User clicks onto the Search Option of the Site')
def step_impl(context):
    time.sleep(2)
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.click_SearchBox()
@then(u'It shows the list of popular searches available in the Site')
def step_impl(context):
    time.sleep(2)
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.click_SearchBox()
    time.sleep(2)
    expectedTitle = "Goals | Unacademy"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
@step('User types the name "{coursename}" of the desired Course')
def step_impl(context, coursename):
    time.sleep(2)
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.enter_coursename(coursename)
    time.sleep(5)
@then(u'It shows the Courses as a dropdown list to choose from')
def step_impl(context):
    context.driver.implicitly_wait(10)
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.click_SearchBox()
    time.sleep(5)
    expectedTitle = "Goals | Unacademy"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when('User clicks onto the Search Option and enters"{validcoursename}"')
def step_impl(context, validcoursename):
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.enter_validcoursename(validcoursename)
    time.sleep(2)

@step("User clicks onto the desired Course name")
def step_impl(context):

    Subject = SearchOptionClass(context.driver)
    Subject.click_subject()
    time.sleep(2)

@then("It shows the desired course webpage")
def step_impl(context):

    FullStack = SubjectClass(context.driver)
    FullStack.click_FullStack()

    time.sleep(2)
    expectedTitle = "Full Stack Development | Unacademy"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
@when("User enters {invalidcoursename}")
def step_impl(context, invalidcoursename):
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.enter_invalidcoursename(invalidcoursename)
    time.sleep(2)
@then("It gives the No goals found message")
def step_impl(context):
    SearchOption = SearchOptionClass(context.driver)
    SearchOption.click_SearchBox()
    time.sleep(2)
@step("Chrome is closed")
def step_impl(context):
    pass






