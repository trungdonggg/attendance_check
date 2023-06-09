from flask import Flask
from flask_restful import Api
from classes.job import Job
from classes.holiday import Holiday
from classes.attendant import Attendance
from classes.employee import Employee
from classes.position import Position
from classes.payment import Payment

import pymysql
from flask_cors import CORS
from utils import *

app = Flask(__name__)

api = Api(app)
cors = CORS(app)
conf = read_config()

connection = pymysql.connect(
    host=conf['DATABASE_01']['host'],
    user=conf['DATABASE_01']['user'],
    password=conf['DATABASE_01']['password'],
    db=conf['DATABASE_01']['db'])


api.add_resource(Employee, '/employee', resource_class_kwargs={"connection":connection})
api.add_resource(Job, '/job', resource_class_kwargs={"connection":connection})
api.add_resource(Holiday, '/holiday', resource_class_kwargs={"connection":connection})
api.add_resource(Attendance, '/attendance', resource_class_kwargs={"connection":connection})
api.add_resource(Position, '/position', resource_class_kwargs={"connection":connection})
api.add_resource(Payment, '/payment', resource_class_kwargs={"connection":connection})


if __name__ == '__main__':
    app.run(debug=True)
