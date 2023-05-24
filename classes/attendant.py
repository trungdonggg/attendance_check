from flask import request
from flask_restful import Resource
from utils import myconverter


class Attendance(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
                    drive = []
                    sql = "SELECT * FROM `tbl_attendance` WHERE `eid`=%s"
                    cursor.execute(sql, (request.args['eid'],))
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'eid': i[0],
                            'date': str(i[2])+" / "+str(i[3])+" / "+str(i[1]),
                            'clock_in': str(i[4]),
                            'clock_out': str(i[5])
                        }
                        drive.append(data)
                    return drive, 200
        else:
            return {"status":"error"}

    def post(self):
        if request.is_json:
            data = request.get_json(force=True)
            with self.connection.cursor() as cursor:
                sql_post = "insert into tbl_attendance " \
                           "set eid = '{}'," \
                           "yearr = year(now())," \
                           "monthh = month(now())," \
                           "datee = day(now())," \
                           "clock_in = time(now());"

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
            with self.connection.cursor() as cursor:
                # Check if there are any records for the given eid
                sql_check = "SELECT COUNT(*) FROM tbl_attendance WHERE eid = %s"
                cursor.execute(sql_check, (data['eid'],))
                result = cursor.fetchone()
                if result[0] == 0:
                    return {'status': 'error', 'message': 'No records found for the specified eid.'}, 404

                # Update the most recent record with null clock_out
                sql_put = "UPDATE tbl_attendance SET clock_out = TIME(NOW()) " \
                        "WHERE eid = %s AND clock_out IS NULL " \
                        "ORDER BY clock_in DESC LIMIT 1"
                cursor.execute(sql_put, (data['eid'],))
                self.connection.commit()

                # Check if any rows were affected
                if cursor.rowcount == 0:
                    return {'status': 'error', 'message': 'No matching records found for the specified eid.'}, 404

            return {'status': 'success'}, 200
        else:
            return {'status': 'error', 'message': 'Invalid JSON payload.'}, 400
