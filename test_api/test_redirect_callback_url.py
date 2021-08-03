import delayed_assert
import pytest
import allure
import logging as logger

from resource.read_xls import getcelldata
from utility.requestsUtility import RequestUtility
from resource import constants


class Test_Redirect_Callback_URL(RequestUtility):
    @pytest.mark.apitest
    @allure.story("CT-10 Implement SSO Callback route in old talech")
    @pytest.mark.parametrize("argvals", getcelldata("redirectCallbackTest", constants.DATASHEETPATH))
    def test_redirct_callback_url(self, argvals):
        with allure.step("Validating Redirect Callback URL"):
            logger.info("Inside test_redirect_callback_url function")
            # print("Inside test_redirect_callback_url function")
            api_res = self.get(host=constants.TALECH_HOST, endpoint=argvals['Endpoint'], headers=None, expected_status_code=int(argvals['ExpectedStatusCode']), params={'code':f"{argvals['Code']}"})
            if api_res.status_code == 422:
                rs_json = api_res.json()
                message = rs_json['errors']['code'][0]
                delayed_assert.expect(argvals['ExpectedMessage'] == message,
                                      f"Expected message: {argvals['ExpectedMessage']} and actual message: {message} not matching")
            logger.info("After test_redirect_callback_url function")
            # print("After test_redirect_callback_url function")
            delayed_assert.assert_expectations()

