from flask import request
from flask_restful import Resource


class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":

            with self.connection.cursor() as cursor:
                pass


            return 200



