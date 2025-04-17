import os

from behave import given, when, then
from dotenv import load_dotenv

from features.pages.login_page import LoginPage
from features.pages.search_page import SearchPage


load_dotenv()
username = os.getenv("SAUCE_USERNAME")
password = os.getenv("SAUCE_PASSWORD")
@given("user is on homepage")
def step_user_on_homepage(context):
    context.login_page = LoginPage(context.driver)
    context.search_page = SearchPage(context.driver)
    context.login_page.load(context.base_url)
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()
    assert context.login_page.is_logged_in(), "Login failed!"

@when('user searches for "{product}"')
def step_user_searches_product(context, product):
    context.search_page.filter_products(product)
    context.searched_product = product.lower()

@then('products related to "{product}" should be displayed')
def step_products_displayed(context, product):
    results = context.search_page.get_displayed_product_names()
    assert any(product.lower() in name.lower() for name in results), f"No products found for {product}"
