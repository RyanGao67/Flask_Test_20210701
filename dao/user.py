import psycopg2
from instance import config
class User():
    TABLE_NAME = 'user'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = None
        cur = None
        result = None
        line = None
        try:
            conn = psycopg2.connect(
                host=config.db_host,
                database=config.db_name,
                user=config.db_user,
                password=config.db_password)
            cur = conn.cursor()                              # cur execute command
            command = '''
                SELECT * FROM users WHERE username='{}'
            '''.format(username)
            cur.execute(command)
            conn.commit()                                    # conn commit changes
            rows_num = cur.rowcount;   print("find {} rows".format(rows_num));
            line = cur.fetchone();     print(line);
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
            if line is not None:
                result = cls(*line)
            return result

    @classmethod
    def delete_by_username(cls, username):
        conn = None
        cur = None
        result = None
        line = None
        try:
            conn = psycopg2.connect(
                host=config.db_host,
                database=config.db_name,
                user=config.db_user,
                password=config.db_password)
            cur = conn.cursor()                              # cur execute command
            command = '''
                DELETE FROM users WHERE username='{}'
            '''.format(username)
            cur.execute(command)
            conn.commit()                                    # conn commit changes
            rows_num = cur.rowcount; print("find {} rows".format(rows_num));
            # line = cur.fetchone(); print(line);
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
            if rows_num is not None:
                result = rows_num
            return result

    @classmethod
    def update_by_username(cls, username, password):
        conn = None
        cur = None
        result = None
        line = None
        try:
            conn = psycopg2.connect(
                host=config.db_host,
                database=config.db_name,
                user=config.db_user,
                password=config.db_password)
            cur = conn.cursor()                              # cur execute command
            command = '''
                UPDATE users set password='{}' where username='{}'
            '''.format(password, username)
            cur.execute(command)
            conn.commit()                                    # conn commit changes
            rows_num = cur.rowcount; print("find {} rows".format(rows_num));
            # line = cur.fetchone(); print(line);
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
            if rows_num is not None:
                result = rows_num
            return result


    @classmethod
    def create_by_username(cls, username, password):
        conn = None
        cur = None
        result = None
        line = None
        try:
            conn = psycopg2.connect(
                host=config.db_host,
                database=config.db_name,
                user=config.db_user,
                password=config.db_password)
            cur = conn.cursor()                              # cur execute command
            command = '''
                INSERT INTO users(username, password)
                 VALUES('{}','{}')
            '''.format(username, password)
            cur.execute(command)
            conn.commit()                                    # conn commit changes
            rows_num = cur.rowcount;   print("find {} rows".format(rows_num));
            # line = cur.fetchone();     print(line);
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
            if rows_num is not None:
                result = rows_num
            return result