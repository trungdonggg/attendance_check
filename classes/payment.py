from flask import request
from flask_restful import Resource
import pandas
import calendar, datetime
# from cs311.attendance.utils import mod_workdays


class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":
            total = 0
            jid = ''
            holiday = None
            workday = None
            fromdate = None

            eid = request.args['eid']
            month = int(request.args['month'])
            month_r = 1 if month == 12 else month + 1
            year = request.args['year']

            s1 = '{}-{}-01'.format(year, month)
            s2 = '{}-{}-01'.format(year, month_r)


            # get workday in month
            with self.connection.cursor() as cursor:
                sql = "select clock_in, clock_out from tbl_attendance where eid = '{}';"
                cursor.execute(sql.format(eid))
                workday = pandas.DataFrame(cursor.fetchall())
                workday = workday.loc[(workday[0] >= s1) & (workday[0] < s2)]
            # get from_date in month (-1) (position) =>(jid init =>holiday init)
                sql_1 = "select from_date, jid from tbl_position where eid = '{}';"
                cursor.execute(sql_1.format(eid))
                tbl_fromdate = pandas.DataFrame(cursor.fetchall())
                tbl_fromdate[0] = pandas.to_datetime(tbl_fromdate[0], format='%Y%m%d')
                # fromdate = tbl_fromdate.query(tbl_fromdate[0]>=s1 & tbl_fromdate<s2)

            print(fromdate)


            # so sanh each workday voi from_date
            #     neu < :
            #             neu trong holiday: tinh tien
            #             neu khong trong holiday: tinh tien



            #     neu >= : doi (jid init =>holiday init) : tinh tien
















            return 200



