import json

import requests
from behave import given, when, then
from features.steps.Config import Config

from features.steps.common import RequestEncoder


@given('I create an access token')
def step_impl(context):
    body = {
                "client_id":"uxCtUucHK12z41A8yAxvINbY65068nGv",
                "client_secret":"piWwiLB7bu-MRcOYLCxpZ2qFYG9t5ONwdN7OvR2Z_txcnDg4yxjsjTLVTdoyC1-i",
                "audience":"https://forex2.bexs.com.br",
                "grant_type": "client_credentials"
            }
    value = json.dumps(body, indent=4, cls=RequestEncoder)
    context.response = requests.post(data=body,
                                     url=f'{Config.authentication_url()}')
    context.response_json = context.response.json()
    access_token = context.response_json.get('access_token')
    context.header = {"Authorization": "Bearer " + access_token}


@when('I send a GET request')
def step_impl(context):
    context.response = requests.get(url=f'https://forex2.bexs.com.br/v1/counterparties/0201041vMJnA9XWKLEYKiuEZ12KrTgT5n')


@then('I receive a "{code}" status code')
def step_impl(context, code):
    int(context.response.status_code) == int(code)
