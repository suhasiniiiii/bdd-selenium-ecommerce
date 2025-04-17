from behave import given, when, then
from dotenv import load_dotenv

from features.pages.login_page import LoginPage
import os

load_dotenv()
username = os.getenv("SAUCE_USERNAME")
password = os.getenv("SAUCE_PASSWORD")
@given("the user is on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load(context.base_url)

@when("the user enter valid username and password")
def step_enter_credentials(context):

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when("the user clicks on login button")
def step_click_login(context):
    context.login_page.click_login()

@then("the user should be logged in successfully")
def step_verify_login(context):

    assert context.login_page.is_logged_in(), "Login failed!"
@when('the user logs in with invalid credentials')
def step_impl(context):
    context.login_page.enter_username("wrong_username")
    context.login_page.enter_password("wrong_password")

@then('the login should fail with an error message')
def step_impl(context):
    assert context.login_page.is_login_failed(), "Login should have failed but it didn't"
