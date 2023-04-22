import json

from flask import request
from flask_restful import Resource
from attendance.utils import to_json

class Attendance(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
                    drive = []
                    sql = "SELECT * FROM `tbl_attendance` WHERE `eid`=%s"
                    cursor.execute(sql, request.args['eid'])
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'eid': i[0],
                            'clock_in': (i[1]),
                            'clock_out': (i[2])
                        }
                        drive.append(data)
                    return drive, 200
        else:
            return {"status":"error"}

    def post(self):
        if request.is_json:
            # convert to json
            data = request.get_json(force=True)
            with self.connection.cursor() as cursor:
                sql_post = "INSERT INTO `tbl_attendance` (`eid`, `clock_in`, `clock_out`) " \
                           "VALUES ('{}', now(),null);"
                sql_post = sql_post.format(data['eid'])
                cursor.execute(sql_post)
                self.connection.commit()
            return {'status':'success'}, 201
        else:
            return {"status":"error"}

    def delete(self):
        return {"status":"no support"}

    def put(self):
        if request.is_json:
            data = request.get_json(force=True)
            sql_put = "update tbl_attendance set clock_out = now() " \
                      "where eid = '{}' and clock_out is null " \
                      "order by clock_in desc limit 1;"
            sql_put = sql_put.format(data['eid'])

            with self.connection.cursor() as cursor:
                cursor.execute(sql_put)
                self.connection.commit()
            return {'status': 'success'}, 200
        else:
            return {"status": "error"}