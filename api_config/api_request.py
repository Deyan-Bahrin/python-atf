import base64


class ApiRequest:
    def __init__(self):
        self.data = {}
        self.headers = {}
        self.params = {}

    def add_json(self, json_data):
        self.data = json_data
        self.headers["Content-type"] = "application/json"
        return self

    def add_query_param(self, key, value):
        self.params[key] = value
        return self

    def add_path_param(self, endpoint, key, value):
        endpoint = endpoint.replace(f"{{{key}}}", value)
        return self

    def add_form_data(self, form_data):
        self.data = form_data
        self.headers["Content-type"] = "application/x-www-form-urlencoded"
        return self

    def add_basic_auth(self, username, password):
        auth_str = f"{username}:{password}"
        auth_bytes = auth_str.encode("utf-8")
        auth_encoded = base64.b64encode(auth_bytes).decode("utf-8")
        self.headers["Authorization"] = f"Basic {auth_encoded}"
        return self

    def build(self):
        return self.__dict__
