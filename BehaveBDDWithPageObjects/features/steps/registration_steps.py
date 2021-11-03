import time
from behave import *

from BehaveBDDWithPageObjects.Utilities import configReader
from BehaveBDDWithPageObjects.features.pageobjects.RegistrationPage import RegistrationPage


@given('I navigate to qa.way2automation.com')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.open(configReader.readConfig("basic info", "testsiteurl"))


@when('I enter the name as "{name}"')
def step_impl(context, name):
    context.reg.setName(name)


@when('I enter the phone number as "{phoneNumber}"')
def step_impl(context, phoneNumber):
    context.reg.setPhoneNumber(phoneNumber)


@when('I enter the email as "{email}"')
def step_impl(context, email):
    context.reg.setEmail(email)


@when('I enter the country as "{country}"')
def step_impl(context, country):
    context.reg.setCountry(country)


@when('I enter the city as "{city}"')
def step_impl(context, city):
    context.reg.setCity(city)


@when('I enter the username as "{email}"')
def step_impl(context, email):
    context.reg.setUsername(email)


@when('I enter the password as "{password}"')
def step_impl(context, password):
    context.reg.setPassword(password)


@then('I click on the submit button')
def step_impl(context):
    context.reg.submitForm()
    time.sleep(3)


