from flask import request
from flask_restful import Resource
from datetime import datetime


class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        # we check if the now.month is after or equal the query month
        # if it equal: return the sum of the paid col of query month
        # if it after: check if it exist in the payment table
        #                     if it not, calculate, post in the tbl_payment, return it
        if request.query_string is not None or request.query_string != "":

            with self.connection.cursor() as cursor:
                data = request.args
                eid = data['eid']
                mth = int(data['month'])
                yr = int(data['year'])

                s1 = '{}-{}-01'.format(yr, mth)
                s2 = '{}-{}-01'.format(yr, mth+1)


                if datetime.now().year>= yr and datetime.now().month > mth:
                    sql_check = 'select * from tbl_payment where eid ="{}" and yearr="{}" and monthh="{}" ;'
                    cursor.execute(sql_check.format(eid,yr,mth))
                    res = cursor.fetchone()
                    if res is None:
                        sql_cal = 'SELECT sum(paid) as total ' \
                                  'FROM cs311.tbl_attendance ' \
                                  'where eid = "{}" and dayy >= "{}" and dayy< "{}";'
                        cursor.execute(sql_cal.format(eid,s1,s2))
                        total = cursor.fetchone()[0]


                        sql_post = "insert into tbl_payment " \
                                   "set eid = '{}'," \
                                   "salary = '{}'," \
                                   "monthh = '{}'," \
                                   "yearr = '{}';"
                        cursor.execute(sql_post.format(eid,total, mth,yr))
                        self.connection.commit()
                        return {'eid':eid,
                                'salary':total},200
                    else:
                        return {'eid':res[0],
                                'salary':res[1]},200

                else:
                    sql_cal = 'SELECT sum(paid) as total ' \
                              'FROM cs311.tbl_attendance ' \
                              'where eid="{}" and dayy >= "{}" and dayy< "{}";'
                    cursor.execute(sql_cal.format(eid, s1, s2))
                    total = cursor.fetchone()[0]
                    return {'eid':eid,
                            'salary':total},200





