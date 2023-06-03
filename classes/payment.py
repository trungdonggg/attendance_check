from flask import request
from flask_restful import Resource
from datetime import datetime


class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":

            with self.connection.cursor() as cursor:
                data = request.get_json(force=True)
                yr = int(data['year'])
                mth = int(data['month'])
                eid = data['eid']
                if datetime.now().year>= yr and datetime.now().month > mth:
                    sql_check = 'select * from tbl_payment' \
                                'where eid="{}" and yearr={} and monthh={}'
                    cursor.execute(sql_check.format(eid,yr,mth))
                    res =  cursor.fetchone()
                    if res is None:
                        sql_cal = ''
                        cursor.execute(sql_cal)
                        total = cursor.fetchone()

                        sql_put = ''
                        cursor.execute(sql_put)
                        self.connection.commit()
                        return #self.post()
                    else:
                        return res

                else:
                    sql_cal = ''
                    cursor.execute(sql_cal)
                    res = cursor.fetchone()
                    return res
            return 200

    def post(self):
        return


