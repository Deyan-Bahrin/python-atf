import configparser

import requests


class ApiClient:

    def __init__(self):
        self.base_url = self.init_config()

    def request(self, method, endpoint, request_properties):
        url = f"{self.base_url}{endpoint}"
        print("The request url is:", url)
        print(request_properties)
        response = requests.request(method, url, verify=False)

        return response

    def get(self, endpoint, request_properties):
        return self.request("GET", endpoint, request_properties)

    def post(self, endpoint, request_properties):
        return self.request("POST", endpoint, request_properties)

    def put(self, endpoint, request_properties):
        return self.request("PUT", endpoint, request_properties)

    def delete(self, endpoint, request_properties):
        return self.request("DELETE", endpoint, request_properties)

    @staticmethod
    def init_config():
        config = configparser.ConfigParser()
        config.read("/home/dbahr001/atf-pyton/config/test_properties.ini")
        return config.get("api", "api_url")
