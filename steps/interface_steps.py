import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://serenity.is/demo/")


@when('I enter my user credentials "{username}" and password "{password}"')
def step_impl(context, username, password):
    username_field = context.driver.find_element(By.NAME, "Username")
    username_field.clear()
    password_field = context.driver.find_element(By.NAME, "Password")
    password_field.clear()
    username_field.send_keys(username)
    password_field.send_keys(password)


@when('I click the "Log in" button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]")
    login_button.click()


@then('I should see the title "{expected_title}"')
def step_impl(context, expected_title):
    time.sleep(3)
    assert context.driver.title == expected_title


@then('there should be at least one icon visible on the page')
def step_impl(context):
    icons = context.driver.find_elements(By.XPATH, "//*[contains(@class, \"fa\")]")
    assert len(icons) > 0


@then('there should be at least one button visible on the page')
def step_impl(context):
    buttons = context.driver.find_elements(By.XPATH, "//button")
    assert len(buttons) > 0


@then('there should be at least one text field visible on the page')
def step_impl(context):
    text_fields = context.driver.find_elements(By.TAG_NAME, "input")
    assert len(text_fields) > 0


@then('there should be at least one image visible on the page')
def step_impl(context):
    images = context.driver.find_elements(By.TAG_NAME, "img")
    assert len(images) > 0


@then('I should see the title "Dashboard" on the page')
def step_impl(context):
    title = context.driver.find_element(By.TAG_NAME, "h1")
    assert title.text == "Dashboard"
