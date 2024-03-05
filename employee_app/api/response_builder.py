from employee_app.api import api
from rest_framework.response import Response
from rest_framework import status

class ResponseBuilder:

    def __init__(self):
        self.status = status.HTTP_200_OK
        self.status_message = ""
        self.status_code = -1
        self.message = ""
        self.data = {}
        self.error = {}




    def set_status(self, status):
        self.status = status
        return self
    
    def ok_200(self):
        self.status = status.HTTP_200_OK
        return self
    
    def create_success(self):
        self.status = status.HTTP_201_CREATED
        return self

    def invalid_input(self):
        self.status = status.HTTP_400_BAD_REQUEST
        return self
    
    def unauthorized_access(self):
        self.status = status.HTTP_401_UNAUTHORIZED
        return self


    def server_error(self):
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return self
    

    def set_status_code(self, status_code):
        self.status_code = status_code
        return self
    
    def set_data(self, data):
        self.data = data
        return self
    

    def set_error(self, error):
        self.error = error
        return self
    

    def set_message(self, message):
        self.message = message
        return self
    

    def get_json(self):
        if self.status != 1:
            self.status_message = api.invalid_messages[self.status_code]
        return {
            "status_code": self.status_code,
            "status message": self.status_message,
            "message": self.message,
            "data": self.data,
            "error": self.error,
        }
    def return_response(self):
        res = self.get_json()
        return Response(res,status=self.status)

    def get_400_bad_request(self, status_code, error, data = None):
        return self.set_error(error).invalid_input().set_status_code(status_code).return_response()
    

    def get_201_data_created_response(self, status_code, message, data):
        return self.set_data(data).create_success().set_message(message).set_status_code(status_code).return_response()
    

    def get_200_ok_response(self, status_code, message, data = None):
        return self.set_data(data).ok_200().set_message(message).set_status_code(status_code).return_response()
    

    def get_401_unauthorized_access_response(self, status_code, error):
        return self.set_error(error).unauthorized_access().set_status_code(status_code).return_response()
    

    def get_500_server_error(self, status_code, error):
        return self.set_status_code(status_code).set_error(error).return_response()
    
    