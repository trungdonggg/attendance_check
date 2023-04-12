from flask import Flask,request, jsonify
from flask_restful import Resource, Api, reqparse
import pymysql
import json

app = Flask(__name__)
api = Api(app)

connection = pymysql.connect(   # sua cai nay
    host='localhost',
    user='trungdong',
    password='trungdong',
    db='cs311')

def command_format(d,s):
    l = (list(d.keys()))
    c = ""
    t = "{}='{}'"
    for i in l[1:]:
        b = "{}='{}'"
        b=b.format(i, d[i])
        c = c+ "," +b
    c = c[1:]
    t = t.format(l[0], d[l[0]])
    s = s.format(c,t)
    return s

class tbl_employee(Resource):
    def get(self):   #sua cai nay
        with connection.cursor() as cursor:
            # get all
            if request.args['eid'] == "*":
                drive = []
                sql = "SELECT * FROM `tbl_employee`"
                cursor.execute(sql)
                result = cursor.fetchall()
                for i in result:
                    data = {
                        'eid':i[0],
                        'name':i[1],
                        'phone':i[2]
                    }
                    drive.append(data)
                return drive, 200

            # get by id
            else:
                sql = "SELECT * FROM `tbl_employee` WHERE `eid`=%s"
                cursor.execute(sql, (request.args['eid']))
                result = cursor.fetchone()
                data = {
                    'eid':result[0],
                    'name': result[1],
                    'phone': result[2]
                }
                return data,200

    def post(self):  # sua cai nay
        parser.add_argument('data')
        data = parser.parse_args()['data']
        # convert to json
        data = json.loads(data.replace("'", '"'))
        with connection.cursor() as cursor:
            sql_post = "INSERT INTO `tbl_employee` (`eid`, `name`, `phone`) " \
                       "VALUES ('{}', '{}', '{}');"
            sql_post = sql_post.format(data['eid'], data['name'], data['phone'])
            cursor.execute(sql_post)
            connection.commit()
        return {'status':'success'}, 201

    def delete(self):
        parser.add_argument('eid')
        eid = parser.parse_args()['eid']
        with connection.cursor() as cursor:
            sql_delete = "DELETE FROM `tbl_employee` WHERE `eid`=%s"
            # Execute the query
            cursor.execute(sql_delete, eid)
            # the connection is not autocommited by default. So we must commit to save our changes.
            connection.commit()
        return {"status": "success"}, 200

    def put(self):   #sua cai nay
        parser.add_argument('data')
        data = parser.parse_args()['data']
        data = json.loads(data.replace("'", '"'))
        sql_put = "update tbl_employee set {} where {};"
        with connection.cursor() as cursor:
            cursor.execute(command_format(data, sql_put))
            connection.commit()

        return {'status':'success'}, 200

api.add_resource(tbl_employee,'/employee')


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