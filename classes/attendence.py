from flask import request
from flask_restful import Resource
from attendance.utils import command_format


class Employee(Resource):
    def __init__(self, db_con):
        self.connection = db_con

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
                    drive = []
                    sql = "SELECT * FROM `tbl_attendence` WHERE `eid`=%s"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'eid': i[0],
                            'clock_in': i[1],
                            'clock_out': i[2],
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
                sql_post = "INSERT INTO `tbl_attendence` (`eid`, `clock_in`, `clock_out`) " \
                           "VALUES ('{}', '{}','{}');"
                sql_post = sql_post.format(data['eid'], data['clock_in'], data['clock_out'])
                cursor.execute(sql_post)
                self.connection.commit()
            return {'status':'success'}, 201
        else:
            return {"status":"error"}

    def delete(self):
        return {"status":"no support"}

    def put(self):
        return {"status":"no support"}