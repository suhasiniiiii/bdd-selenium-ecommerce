from behave import given, when, then
from features.pages.login_page import LoginPage
from features.pages.search_page import SearchPage
from features.pages.checkout_page import CheckoutPage
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("SAUCE_USERNAME")
password = os.getenv("SAUCE_PASSWORD")


@when('user selects "{product}"')
def step_impl(context, product):
    context.login_page = LoginPage(context.driver)
    context.search_page = SearchPage(context.driver)
    context.checkout_page = CheckoutPage(context.driver)
    context.selected_product = f"{product}"
    context.search_page.select_product(product)

@when('adds product to the cart')
def step_impl(context):
    context.checkout_page.add_to_cart()

@when('selects the cart')
def step_impl(context):
    context.checkout_page.go_to_cart()

@then('the product should be displayed there')
def step_impl(context):
    assert context.checkout_page.is_product_in_cart(context.selected_product)

@when('user selects checkout')
def step_impl(context):
    context.checkout_page.proceed_to_checkout()

@when('enters first name')
def step_impl(context):
    context.checkout_page.enter_first_name()

@when('enters last name')
def step_impl(context):
    context.checkout_page.enter_last_name()

@when('enters postal code')
def step_impl(context):
    context.checkout_page.enter_postal_code()

@when('clicks on continue')
def step_impl(context):
    context.checkout_page.click_continue()

@then('the checkout overview should be displayed')
def step_impl(context):
    assert context.checkout_page.is_checkout_overview_displayed()

@when('user clicks on finish')
def step_impl(context):
    context.checkout_page.click_finish()

@then('the order should be placed successfully')
def step_impl(context):
    assert context.checkout_page.is_order_complete()
