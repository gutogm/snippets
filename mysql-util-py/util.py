# -*- coding: utf-8 -*-

from .connection import connection
class MySqlUtils(object):

    @staticmethod
    def select_many(query):
        results = []
        with connection() as db, cursor:
            cursor.execute(query.encode('utf-8'))
            results = cursor.fetchall()
        return results

    @staticmethod
    def select_one(query):
        result = None
        with connection() as db, cursor:
            cursor.execute(query.encode('utf-8'))
            result = cursor.fetchone()
        return result

    @staticmethod
    def p_select_many(query, fields):
        p_results = []
        with connection() as db, cursor:
            cursor.execute(query.encode('utf-8'))
            results = cursor.fetchall()
            for result in results:
                p_result = {}
                idx = 0
                for field in fields:
                    p_result[field] = result[idx]
                    idx += 1
                p_results.append(p_result)
        return p_results

    @staticmethod
    def execute_one(query, params=None):
        with connection() as db, cursor:
            if params is not None:
                cursor.execute(query.encode('utf-8'), params)
            else:
                cursor.execute(query.encode('utf-8'))
            db.commit()
            return True

    @staticmethod
    def execute_one_with_results(query):
        with connection() as db, cursor:
            results = cursor.execute(query.encode('utf-8'))
            db.commit()
            return cursor.lastrowid

    @staticmethod
    def execute_many(querys):
        with connection() as db, cursor:
            for query in querys:
                if query.strip() != '':
                    cursor.execute(query.encode('utf-8'))
            db.commit()
