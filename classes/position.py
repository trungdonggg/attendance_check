from flask import request
from flask_restful import Resource

class Position(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            with self.connection.cursor() as cursor:
                # get all
                if request.args['eid'] == "*":
                    drive = []
                    sql = "SELECT * FROM `tbl_position`"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'eid':i[1],
                            'jid':i[2],
                            'from_date':i[0].isoformat(),
                        }
                        drive.append(data)
                    return drive, 200

                # get by id
                else:
                    sql = "SELECT * FROM `tbl_position` WHERE `eid`=%s"
                    drive = []
                    cursor.execute(sql, (request.args['eid']))
                    result = cursor.fetchall()
                    for i in result:
                        data = {
                            'eid':i[1],
                            'jid':i[2],
                            'from_date':i[0].isoformat()
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
                sql_post = "INSERT INTO `tbl_position` (`eid`, `jid`, `from_date`) " \
                           "VALUES ('{}', '{}', '{}');"
                sql_post = sql_post.format(data['eid'], data['jid'],data['from_date'])
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
                sql_delete = "DELETE FROM `tbl_position` WHERE `eid`=%s"
                # Execute the query
                cursor.execute(sql_delete, eid)
                # the connection is not autocommited by default. So we must commit to save our changes.
                self.connection.commit()
            return {"status": "success"}, 200
        else:
            return {"status":"error"}

