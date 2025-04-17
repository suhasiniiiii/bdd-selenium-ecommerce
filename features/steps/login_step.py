from behave import given, when, then
from features.pages.login_page import LoginPage
import os

@given("I am on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load(context.base_url)

@when("I enter valid username and password")
def step_enter_credentials(context):

    context.login_page.enter_username()
    context.login_page.enter_password()

@when("I click the login button")
def step_click_login(context):
    context.login_page.click_login()

@then("I should be logged in successfully")
def step_verify_login(context):

    assert context.login_page.is_logged_in(), "Login failed!"
