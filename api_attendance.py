from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import pymysql

app = Flask(__name__)
api = Api(app)

connection = pymysql.connect(host='localhost', user='trungdong', password='trungdong', db='classicmodels')

class tbl_employee(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

    def put(self):
        return

api.add_resource(tbl_employee,'/tbl_employee/')


class tbl_job(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

    def put(self):
        return

api.add_resource(tbl_job, '/tbl_job/')


class tbl_holiday(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

api.add_resource(tbl_holiday, '/tbl_holiday/')


class tbl_attendance(Resource):
    def get(self):
        return

    def post(self):
        return


api.add_resource(tbl_attendance, '/tbl_attendance/')


class tbl_payment(Resource):
    def get(self):
        return

    def post(self):
        return

api.add_resource(tbl_payment, '/tbl_payment/')


class tbl_position(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

    def put(self):
        return

api.add_resource(tbl_position, '/tbl_position/')