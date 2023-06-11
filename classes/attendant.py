from flask import request
from flask_restful import Resource


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
                            'date': str(i[1]),
                            'clock_in': str(i[2]),
                            'clock_out': str(i[3])
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
                           "dayy = date(now())," \
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

                # update the paid col when check_out
                eid = data['eid']
                paid = 0

                sql1 = 'SELECT * FROM cs311.tbl_attendance\
                        where eid="{}" and paid is null;'
                cursor.execute(sql1.format(eid))
                result = cursor.fetchone()
                day = result[1]
                clock_in = result[2]
                clock_out = result[3]
                print(result)

                sql2 = 'select j.jid, j.based_salary, j.from_hour, j.to_hour, j.late_coefficient, j.overtime_coefficient\
                            from \
                                (SELECT * FROM cs311.tbl_position \
                                where "{}" >=  tbl_position.from_date and eid="{}"\
                                order by from_date desc\
                                limit 1) as x\
                                inner join tbl_job as j\
                                    on j.jid = x.jid;'
                cursor.execute(sql2.format(day, eid))
                res = cursor.fetchone()
                jid = res[0]
                based_salary = res[1]
                from_hour = res[2]
                to_hour = res[3]
                late_coe = res[4]
                overtime_coe = res[5]
                print(res)

                sql3 = 'select * from tbl_holiday where jid="{}" and \
                                        holiday_month = month("{}") and holiday_date = day("{}");'
                cursor.execute(sql3.format(jid, day, day))
                res2 = cursor.fetchone()

                if clock_in <= from_hour:
                    if clock_out >= to_hour:
                        w = int((to_hour - from_hour).total_seconds()) / 3600
                        paid = w * based_salary

                    else:
                        s = int((to_hour - clock_out).total_seconds()) / 3600
                        w = int((to_hour - from_hour).total_seconds()) / 3600
                        paid = w * based_salary - s * based_salary * late_coe

                else:
                    if clock_out >= to_hour:
                        l = int((clock_in - from_hour).total_seconds()) / 3600
                        w = int((to_hour - from_hour).total_seconds()) / 3600
                        paid = w * based_salary - l * based_salary * late_coe

                    else:
                        w = int((to_hour - from_hour).total_seconds()) / 3600
                        l = int((clock_in - from_hour).total_seconds()) / 3600
                        s = int((to_hour - clock_out).total_seconds()) / 3600
                        paid = w * based_salary - l * based_salary * late_coe - s * based_salary * late_coe

                if res2 is not None:
                    paid = paid*overtime_coe
                else:
                    pass

                paid = 0 if paid<0 else paid

                sql_put2 = "UPDATE tbl_attendance SET paid = {} " \
                          "WHERE eid = '{}' AND paid IS NULL " \
                          "ORDER BY clock_in DESC LIMIT 1"
                cursor.execute(sql_put2.format(paid, eid))
                self.connection.commit()


                # Check if any rows were affected
                if cursor.rowcount == 0:
                    return {'status': 'error', 'message': 'No matching records found for the specified eid.'}, 404

            return {'status': 'success'}, 200
        else:
            return {'status': 'error', 'message': 'Invalid JSON payload.'}, 400
