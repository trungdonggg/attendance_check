from flask import request
from flask_restful import Resource
# from cs311.attendance.utils import command_format
from utils import command_format


class Job(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
                # get all
                if request.args['jid'] == "*":
                    drive = []
                    sql = "SELECT * FROM `tbl_job`"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'jid': i[0],
                            'title': i[1],
                            'based_salary': i[2],
                            'from_hour': str(i[3]),
                            'to_hour': str(i[4]),
                            'late_coefficient': i[5],
                            'overtime_coefficient': i[6]
                        }
                        drive.append(data)
                    return drive, 200

                # get by id
                else:
                    sql = "SELECT * FROM `tbl_job` WHERE `jid`=%s"
                    cursor.execute(sql, (request.args['jid']))
                    i = cursor.fetchone()
                    data = {
                        'jid': i[0],
                        'title': i[1],
                        'based_salary': i[2],
                        'from_hour': str(i[3]),
                        'to_hour': str(i[4]),
                        'late_coefficient': i[5],
                        'overtime_coefficient': i[6]
                    }
                    return data, 200
        else:
            return {"status": "error"}

    def post(self):
        if request.is_json:
            data = request.get_json(force=True)
            with self.connection.cursor() as cursor:
                sql_post = "INSERT INTO `tbl_job` (`jid`, `title`, `based_salary`, `from_hour`, " \
                           "`to_hour`, `late_coefficient`, `overtime_coefficient`) " \
                           "VALUES ('{}', '{}','{}', '{}','{}','{}', '{}');"
                sql_post = sql_post.format(data['jid'], data['title'],data['based_salary'], data['from_hour'],
                                           data['to_hour'], data['late_coefficient'],data['overtime_coefficient'])
                cursor.execute(sql_post)
                self.connection.commit()
            return {'status':'success'}, 201
        else:
            return {"status":"error"}

    def delete(self):
        if request.is_json:
            # convert to json
            data = request.get_json(force=True)
            jid = data['jid']
            with self.connection.cursor() as cursor:
                sql_delete = "DELETE FROM `tbl_job` WHERE `jid`=%s"
                # Execute the query
                cursor.execute(sql_delete, jid)
                # the connection is not autocommited by default. So we must commit to save our changes.
                self.connection.commit()
            return {"status": "success"}, 200
        else:
            return {"status":"error"}

    def put(self):
        if request.is_json:
            # convert to json
            data = request.get_json(force=True)
            sql_put = "UPDATE tbl_job SET `title`=%s, `based_salary`=%s, `from_hour`=%s, `to_hour`=%s, `late_coefficient`=%s, `overtime_coefficient`=%s WHERE `jid`=%s;"
            with self.connection.cursor() as cursor:
                cursor.execute(sql_put, (
                    data['title'], data['basedsalary'], data['fromhour'], data['tohour'], data['latecoefficient'],
                    data['overtimecoefficient'], data['jid']
                ))
                self.connection.commit()
            return {'status':'success'}, 200
        else:
            return {"status":"error"}
