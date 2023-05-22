from flask import request
from flask_restful import Resource


class Holiday(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
                # get all
                if request.args['jid'] == "*":
                    drive = []
                    sql = "SELECT * FROM `tbl_holiday`"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'jid' : i[0],
                            'holiday_date' : 'month: '+str(i[1])+ ' date: '+str(i[2])
                        }
                        drive.append(data)
                    return drive, 200

                # get by id
                else:
                    sql = "SELECT * FROM `tbl_holiday` WHERE `jid`=%s"
                    drive = []
                    cursor.execute(sql, (request.args['jid']))
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'jid': i[0],
                            'holiday_date': 'month: ' + i[1] + ' date: ' + i[2]
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
                # sql_post = "INSERT INTO `tbl_holiday` (`jid`, `holiday_date`) " \
                #            "VALUES ('{}', '{}');"
                # sql_post = sql_post.format(data['jid'], data['holiday_date'])
                # cursor.execute(sql_post)
                self.connection.commit()
            return {'status':'success'}, 201
        else:
            return {"status":"error"}

    def delete(self):
        if request.is_json:
            # convert to json
            data = request.get_json(force=True)
            jid = data['jid']
            holiday_date = data['holiday_date']
            with self.connection.cursor() as cursor:
                # sql_delete = "DELETE FROM `tbl_holiday` WHERE `jid`='{}' and `holiday_date`='{}'"
                # sql_delete = sql_delete.format(jid,holiday_date)
                # cursor.execute(sql_delete)
                self.connection.commit()
            return {"status": "success"}, 200
        else:
            return {"status":"error"}

    def put(self):
        return {"status":"method not supported"}
