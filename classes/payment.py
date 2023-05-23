from flask import request
from flask_restful import Resource
import pandas
import calendar, datetime
# from cs311.attendance.utils import getIndex

class Payment(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']

    def get(self):
        if request.query_string is not None or request.query_string != "":

            workday = None
            position = None
            holiday_init = None
            jid_init = ""
            job = []
            with self.connection.cursor() as cursor:
            # get workday in month
                sql = "SELECT * FROM cs311.tbl_attendance where `eid`='{}' and `monthh`={};"
                cursor.execute(sql.format(request.args['eid'], int(request.args['month'])))
                workday = pandas.DataFrame(cursor.fetchall())

            # get from_date in month (-1) (position) =>(jid init =>holiday init)
                sql1 = "SELECT * FROM cs311.tbl_position where `eid`='{}';"
                cursor.execute(sql1.format(request.args['eid']))
                position = pandas.DataFrame(cursor.fetchall())
                position[0] = pandas.to_datetime(position[0], format='%Y%m%d')

                a = None
                for i in position[0]:
                    if i.month == int(request.args['month']):
                        a = i
                        pass


                index = (position.index[position[0] == a].tolist()[0])-1
                fromdate = position.iloc[index].to_list()[0]
                jid_init = position.iloc[index].to_list()[2]

                sql2 = "SELECT * FROM `tbl_holiday` WHERE `jid`=%s"
                cursor.execute(sql2, jid_init)
                holiday_init = pandas.DataFrame(cursor.fetchall())

                sql3 = "SELECT * FROM `tbl_job` WHERE `jid`=%s"
                cursor.execute(sql3, jid_init)
                job = pandas.DataFrame(cursor.fetchall())


                print ("workday \n",workday)
                print ("position \n" ,position)
                print ("fromdate \n" , fromdate)
                print("holiday \n", holiday_init)
                print ("job\n", job)

            # (position[0][1])

            # so sanh each workday voi from_date
            #     neu < :
            #             neu trong holiday: tinh tien
            #             neu khong trong holiday: tinh tien

            #     neu >= : doi (jid init =>holiday init) : tinh tien
                b = True
                while b:
                    try: pass
                    except:
                        b = False
















            return 200



