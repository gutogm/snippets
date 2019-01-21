# -*- coding: utf-8 -*-

from MySQLdb    import connect
from yaml       import load

class connection(object):
    def __init__(self, database, _yaml_path):
        _yaml_file = open(_yaml_path)
        _map = load(_yaml_file)
        _yaml_file.close()

        self.host = _map["DB_HOST"]
        self.user = _map["DB_USERNAME"]
        self.password = _map["DB_PASSWORD"]
        self.database = _map["DB_DATABASE"]

    def __enter__(self):
        self.db = connect(self.host, self.user, self.password, self.database)
        self.db.autocommit(False)
        self.cursor = db.cursor()
        return db, self.cursor

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()
        if exc_type is not None:
            filename, line_num, func_name, text = extract_tb(exc_tb)[-1]
            message= """[exc_type] %s
            [exc_value] %s
            [filename] %s
            [line_num] %s
            [func_name] %s
            [text] %s""" % (exc_type, exc_value, filename, line_num, func_name, text)
            return True