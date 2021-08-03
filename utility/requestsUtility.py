import json

import requests
import delayed_assert
import allure
import logging as logger
from resource import constants
from utility.credentialsUtility import CredentialsUtility
from requests_oauthlib import OAuth1


class RequestUtility(object):

    # def __init__(self):
    #     self.base_url = constants.QA_TALECH_HOST

        # api_cred = CredentialsUtility.get_api_keys()         Its not required here if required please uncomment
        # self.auth = OAuth1(api_cred['API_KEY'], api_cred['API_SECRETE'])  Its not required here if required please remove comment

    def get(self, host, endpoint, headers=None, expected_status_code=200, params=None):
        with allure.step(f"Making a get call for endpoint {endpoint}"):

            if not headers:
                headers = {"Content-Type":"application/json", "Accept":"application/json"}

            self.url = host + endpoint

            rs_api = requests.get(url=self.url, headers=headers, params=params, allow_redirects=False)  #include auth=self.auth if required in the paramenter here
            print(rs_api.url)
            logger.info(f"URL used for test is {rs_api.url}")
            self.status_code = rs_api.status_code
            logger.info(f"Status code: {self.status_code}")
            self.expected_status_code = int(expected_status_code)
            self.validate_status_code("get", self.expected_status_code, self.status_code)
            return rs_api
            # self.rs_json = rs_api.json()

    def post(self, endpoint, headers=None, expected_status_code=200,params=None):
       pass

    def put(self, endpoint, headers=None, expected_status_code=200, params=None):
        pass


    def validate_status_code(self, method, expected_code, actual_code):
        with allure.step(f"Validate https Status Code for {method} api"):
            delayed_assert.expect(self.expected_status_code == self.status_code,
                              f"Expected status code: {self.expected_status_code} and actual status code: {self.status_code} not matching")
            logger.info(f"Expected status code: {self.expected_status_code} and actual status code: {self.status_code} ")



