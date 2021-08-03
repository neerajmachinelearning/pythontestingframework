import json

import delayed_assert
import pytest
import allure
import logging as logger

from resource.read_xls import getcelldata
from utility.requestsUtility import RequestUtility
from resource import constants


class Test_Web_BE_URL(RequestUtility):
    @pytest.mark.apitest
    @allure.story("CT-22 Create a Endpoint to support forwarding callback URL to Web Be")
    @pytest.mark.parametrize("argvals", getcelldata("web_Be_Test", constants.DATASHEETPATH))
    def test_web_be_api_url(self, argvals):
        with allure.step("Validating Web BE API"):
            logger.info("test_web_be_api_url started")
            print("Inside test_web_be_api_url function")
            api_res = self.get(host=constants.WAPI_BE_HOST, endpoint=argvals['Endpoint'], headers=None, expected_status_code=argvals['ExpectedStatusCode'], params={'code':f"{argvals['Code']}"})
            rs_json = api_res.json()
            logger.info(api_res.json())
        with allure.step(f"Response Payload: {rs_json}"):
            if api_res.status_code != 200:
                message = rs_json['errors']['code'][0]
                with allure.step("Validated error message"):
                    delayed_assert.expect(argvals['ExpectedMessage'] == message,
                                      f"Expected message: {argvals['ExpectedMessage']} and actual message: {message} not matching")
            else:
                code = rs_json['data'][0]
                delayed_assert.expect(argvals['Code'] == code,
                                   f"Expected code: {argvals['Code']} and actual code: {code} not matching")
            # print("After test_web_be_api_url function")
            delayed_assert.assert_expectations()