import json
import requests

class customKeywords:

    def Create_session_with_the_basic_authentication(self, url,username,password):
        self.response = requests.get(url,auth=(username,password))
        return  self.response

    def Call_the_get_API_to_fetch_all_the_rented_numbers(self):
        print("Response can be printed using JSON : ", self.response.json())

    def Validate_the_response_with_the_expected_status_code(self,code):
        assert self.response.status_code == int(code)