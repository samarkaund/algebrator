import sqlite3
from msilib import add_data


class OpenTableDB:
    def __init__(self):
        self.connection = sqlite3.connect("algebrator_db.sql")

    def add_user(self, username, password):
        cursor = self.connection.cursor()
        sql_query_zero_id = "SELECT ID FROM alegbrator_users WHERE ID = 0"
        sql_query = "INSERT INTO alegbrator_users (ID, user, password, mmr) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_query_zero_id)
        res_zero_id = cursor.fetchall()
        if len(res_zero_id) == 0:
            cursor.execute(sql_query, (0, username, password, 0))
            self.connection.commit()
        else:
            sql_query_id = "SELECT MAX(ID) FROM alegbrator_users"
            cursor.execute(sql_query_id)
            res_id = cursor.fetchall()
            new_id = int(str(res_id)[2:-3:]) + 1
            cursor.execute(sql_query, (new_id, username, password, 0))
            self.connection.commit()
        cursor.close()

    def up_mmr(self, mmr, user):
        cur = self.connection.cursor()
        query = f"""UPDATE alegbrator_users
                    SET mmr = mmr + {mmr}
                    WHERE user = '{user}'"""
        cur.execute(query)
        self.connection.commit()
        cur.close()

    def return_mmr(self, user):
        cur = self.connection.cursor()
        query = f"SELECT mmr FROM alegbrator_users WHERE user = '{user}'"
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        return int(str(res)[2:-3])

    def user_in_db(self, username2):
        cursor2 = self.connection.cursor()
        sql_user_query = f"SELECT user FROM alegbrator_users WHERE user = '{username2}'"
        cursor2.execute(sql_user_query)
        res_user = cursor2.fetchall()
        if len(res_user) != 0:
            return True
        return False

    def corr_log_and_pswrd(self, log, pswrd):
        cursor3 = self.connection.cursor()
        sql_log_and_password_query = f"SELECT password FROM alegbrator_users WHERE user = '{log}';"
        cursor3.execute(sql_log_and_password_query)
        res_pswrd = cursor3.fetchall()
        if str(res_pswrd)[3:-4:] == pswrd:
            return True
        return False

    def select_not_resolved_task(self, type_ur, hard, user):
        cur = self.connection.cursor()
        query = f"""SELECT MIN(number) FROM tasks 
                        WHERE type = '{type_ur}' AND
                        hard = '{hard}' AND
                        tasks_id NOT IN 
                        (SELECT t_id FROM completed_tasks WHERE user_id = 
                        (SElECT ID FROM alegbrator_users WHERE user = '{user}')) 
                        """
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        return str(res)[2:-3]

    def count_resolved_tasks(self, typ, user):
        cur = self.connection.cursor()
        query = f"""SELECT COUNT(*) FROM completed_tasks WHERE 
                    user_id = (SELECT ID FROM alegbrator_users WHERE user = '{user}') AND
                    t_id IN (SELECT tasks_id FROM tasks WHERE type = '{typ}_ur')"""
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        return str(res)[2:-3]

    def hard_to_int(self, hard):
        if hard == 'a':
            return 1
        if hard == 'b':
            return 2
        if hard == 'c':
            return 3

    def sum_mmr(self, typ, user):
        s_mmr = 0
        cur = self.connection.cursor()

        query_a = f"""SELECT time, attempts FROM completed_tasks 
                    WHERE ct_id IN (SELECT ct_id FROM completed_tasks 
                    WHERE user_id = (SELECT ID FROM alegbrator_users WHERE user = '{user}') 
                    AND t_id IN (SELECT tasks_id FROM tasks WHERE type = '{typ}_ur' AND hard = 'a'))"""
        cur.execute(query_a)
        res = cur.fetchall()
        for i in res:
            sec = int(i[0][:2:]) * 3600 + int(i[0][3:-3:]) * 60 + int(i[0][-2::])
            rating_change = int(1000 / (sec / 60 * int(i[1])) * 1 / 3)
            s_mmr += rating_change

        query_b = f"""SELECT time, attempts FROM completed_tasks 
                    WHERE ct_id IN (SELECT ct_id FROM completed_tasks 
                    WHERE user_id = (SELECT ID FROM alegbrator_users WHERE user = '{user}') 
                    AND t_id IN (SELECT tasks_id FROM tasks WHERE type = '{typ}_ur' AND hard = 'b'))"""
        cur.execute(query_b)
        res = cur.fetchall()
        for i in res:
            sec = int(i[0][:2:]) * 3600 + int(i[0][3:-3:]) * 60 + int(i[0][-2::])
            rating_change = int(1000 / (sec / 60 * int(i[1])) * 2 / 3)
            s_mmr += rating_change

        query_c = f"""SELECT time, attempts FROM completed_tasks 
                    WHERE ct_id IN (SELECT ct_id FROM completed_tasks 
                    WHERE user_id = (SELECT ID FROM alegbrator_users WHERE user = '{user}') 
                    AND t_id IN (SELECT tasks_id FROM tasks WHERE type = '{typ}_ur' AND hard = 'c'))"""
        cur.execute(query_c)
        res = cur.fetchall()
        for i in res:
            sec = int(i[0][:2:]) * 3600 + int(i[0][3:-3:]) * 60 + int(i[0][-2::])
            rating_change = int(1000 / (sec / 60 * int(i[1])) * 3 / 3)
            s_mmr += rating_change

        cur.close()
        return s_mmr

    def id_tasks(self, type, hard, number):
        cur = self.connection.cursor()
        query = f"""SELECT tasks_id FROM tasks 
                                WHERE type = '{type}' AND
                                hard = '{hard}' AND
                                number = {number}"""
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        return str(res)[2:-3]

    def id_user(self, username):
        cur = self.connection.cursor()
        query = f"""SELECT ID FROM alegbrator_users 
                                        WHERE user = '{username}'"""
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        return str(res)[2:-3]

    def add_resolve_task(self, t_id, user_id, time, attempts):
        cur = self.connection.cursor()
        max_ctid_query = "SELECT MAX(ct_id) FROM completed_tasks"
        cur.execute(max_ctid_query)
        max_ctid = cur.fetchall()

        if str(max_ctid)[2:-3] == 'None':
            max_ctid = 1
        else:
            max_ctid = int(str(max_ctid[0])[1:-2]) + 1

        col = "ct_id, t_id, user_id, time, attempts"
        query = f"INSERT INTO completed_tasks ({col}) VALUES (?, ?, ?, ?, ?)"
        cur.execute(query, (int(max_ctid), int(t_id), int(user_id), time, int(attempts)))
        self.connection.commit()
        cur.close()

    def close_connection(self):
        self.connection.close()
