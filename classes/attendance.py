from flask import request
from flask_restful import Resource


class Attendance(Resource):
    def __init__(self, db_con):
        self.connection = db_con

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
                            'clock_in': str(i[1]),
                            'clock_out': str(i[2]),
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
        return {"status":"no support"}