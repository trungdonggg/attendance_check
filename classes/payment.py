from flask import request
from flask_restful import Resource
import pandas
import calendar, datetime
# from cs311.attendance.utils import mod_workdays


class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):


        return 200



