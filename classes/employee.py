from flask import request
from flask_restful import Resource
from attendance.utils import command_format


class Employee(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
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
                            'phone':i[2],
                            'email':i[3],
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
                        'phone':result[2],
                        'email':result[3],
                    }
                    return data,200
        else:
            return {"status":"error"}

    def post(self):
        if request.is_json:
            # convert to json
            data = request.get_json(force=True)
            with self.connection.cursor() as cursor:
                sql_post = "INSERT INTO `tbl_employee` (`eid`, `name`, `phone`, `email`) " \
                           "VALUES ('{}', '{}','{}', '{}');"
                sql_post = sql_post.format(data['eid'], data['name'],data['phone'], data['email'])
                cursor.execute(sql_post)
                self.connection.commit()
            return {'status':'success'}, 201
        else:
            return {"status":"error"}

    def delete(self):
        if request.is_json:
            # convert to json
            data = request.get_json(force=True)
            eid = data['eid']
            with self.connection.cursor() as cursor:
                sql_delete = "DELETE FROM `tbl_employee` WHERE `eid`=%s"
                # Execute the query
                cursor.execute(sql_delete, eid)
                # the connection is not autocommited by default. So we must commit to save our changes.
                self.connection.commit()
            return {"status": "success"}, 200
        else:
            return {"status":"error"}

    def put(self):
        if request.is_json:
            # convert to json
            data = request.get_json(force=True)
            sql_put = "update tbl_employee set {} where {};"
            with self.connection.cursor() as cursor:
                cursor.execute(command_format(data, sql_put))
                self.connection.commit()
            return {'status':'success'}, 200
        else:
            return {"status":"error"}
