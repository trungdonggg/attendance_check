from flask import request
from flask_restful import Resource
import pandas
import calendar, datetime

class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            eid = request.args['eid']
            month = int(request.args['month'])
            month_r = 1 if month == 12 else month + 1
            year = request.args['year']

            s1 = '{}-{}-01'.format(year, month)
            s2 = '{}-{}-01'.format(year, month_r)

            with self.connection.cursor() as cursor:
                sql = "select clock_in, clock_out from tbl_attendance where eid = '{}';"
                cursor.execute(sql.format(eid))
                workdays = pandas.DataFrame(cursor.fetchall())
                workdays = workdays.loc[(workdays[0] >= s1) & (workdays[0] < s2)]
                print (workdays)


                sql_1 = "select from_date, jid from tbl_position where eid = '{}';"
                cursor.execute(sql_1.format(eid))
                fromdate = pandas.DataFrame(cursor.fetchall())
                fromdate[0] = pandas.to_datetime(fromdate[0], format='%Y%m%d')
                frdate = fromdate.loc[(fromdate[0] >= s1) & (fromdate[0] < s2)]


                idx = fromdate[fromdate[0] < s1].index.tolist()[-1]
                val = fromdate.iloc[idx]

                print (frdate)
                print (val[0])








                return 200



