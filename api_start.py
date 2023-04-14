import pymysql
from flask import Flask
from flask_restful import Api
from classes.employee import Employee
from classes.job import Job
from utils import *

app = Flask(__name__)
api = Api(app)

conf = read_config()

connection = pymysql.connect(
    host=conf['DATABASE_00']['host'],
    user=conf['DATABASE_00']['user'],
    password=conf['DATABASE_00']['password'],
    db=conf['DATABASE_00']['db'])

api.add_resource(Employee(connection), '/employee')

api.add_resource(Job(connection), '/job')


if __name__ == '__main__':
    app.run(debug=True)
