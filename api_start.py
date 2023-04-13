import pymysql
from flask import Flask
from flask_restful import Resource, Api, reqparse
from classes.employee import Employee
from utils import *

app = Flask(__name__)
api = Api(app)



conf = read_config()

connection = pymysql.connect(
    host='localhost',
    user='trungdong',
    password='trungdong',
    db='cs311')

api.add_resource(Employee(connection),'/employee')

class tbl_job(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

    def put(self):
        return

api.add_resource(tbl_job, '/job')


class tbl_holiday(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

api.add_resource(tbl_holiday, '/holiday')


class tbl_attendance(Resource):
    def get(self):
        return

    def post(self):
        return


api.add_resource(tbl_attendance, '/attendance')


class tbl_payment(Resource):
    def get(self):
        return

    def post(self):
        return

api.add_resource(tbl_payment, '/payment')


class tbl_position(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

    def put(self):
        return

api.add_resource(tbl_position, '/position')


if __name__ == '__main__':
    parser = reqparse.RequestParser()
    app.run(debug=True)