from flask import request
from flask_restful import Resource


class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
                drive = []
                sql = "SELECT * FROM `tbl_employee` WHERE `eid`=%s"
                cursor.execute(sql, (request.args['eid']))
                result = cursor.fetchall()
                for i in result:
                    data = {
                        'eid': i[0],
                        'name': i[1],
                        'phone': i[2],
                        'email': i[3],
                    }
                    drive.append(data)
                return drive, 200


    def post(self):
        # calculate
        return 

    def delete(self):
        return {"status":"method not support"}

    def put(self):
        return {"status":"method not support"}
