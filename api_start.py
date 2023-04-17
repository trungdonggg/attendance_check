from flask import Flask
from flask_restful import Api

from classes.employee import Employee
from utils import *

app = Flask(__name__)
api = Api(app)

conf = read_config()

connection = pymysql.connect(
    host=conf['DATABASE_00']['host'],
    user=conf['DATABASE_00']['user'],
    password=conf['DATABASE_00']['password'],
    db=conf['DATABASE_00']['db'])


api.add_resource(Employee, '/employee', resource_class_args=(connection,))


if __name__ == '__main__':
    app.run(debug=True)
