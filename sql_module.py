import pymysql
from pymysql.cursors import DictCursor

SQL_password = "Qwerty123" # local server

def Connect_to_DB(with_dict_cursor = True):
    if with_dict_cursor == True:
        connection = pymysql.connect(
                host='chudotech.beget.tech',
                user = 'chudotech_gb',
                db='chudotech_gb',
                charset='utf8mb4',
                password = SQL_password,
                cursorclass=DictCursor
                )
    else:
        connection = pymysql.connect(
                host='chudotech.beget.tech',
                user = 'chudotech_gb',
                db='chudotech_gb',
                charset='utf8mb4',
                password = SQL_password
                )
    return connection

def Get_user(message):

    User = SELECT("users", where_param1 = "telegram_id", where_value1 = message.from_user.id)
    if len(User) > 0:
        User = User[0]
    else:
        User = None
    return User


def SELECT(table, select_param1 = None, select_param2 = None, select_param3 = None,
where_param1 = None, where_value1 = None, where_param2 = None, where_value2 = None, where_param3 = None, where_value3 = None,
wherenot_param1 = None, wherenot_value1 = None, wherenot_param2 = None, wherenot_value2 = None, order_param = None, orderasc = True, with_dict_cursor = True):
    """Выполняет запрос в базу данных из Connect_to_DB к таблице table выбирая параметры select_param123
    где where_param123 = where_value123, и wherenot_param12 <> wherenot_value12 упорядочивая по order_param"""
    try:
        connection = Connect_to_DB(with_dict_cursor)
        with connection.cursor() as cursor:
            query = "SELECT "
            if select_param1 == None:
                query += "* "
            else:
                query += "`{}` ".format(select_param1)
                if select_param2 != None:
                    query += ", `{}` ".format(select_param2)
                if select_param3 != None:
                    query += ", `{}` ".format(select_param3)

            query += "FROM  {}  WHERE ".format(table)

            if where_param1 != None and where_value1 != None:
                query += "`{}` = '{}' ".format(where_param1, where_value1)
                if where_param2 != None and where_value2 != None:
                    query += "AND `{}` = '{}' ".format(where_param2, where_value2)
                if where_param3 != None and where_value3 != None:
                    query += "AND `{}` = '{}' ".format(where_param3, where_value3)

            if wherenot_param1 != None and wherenot_value1 != None:
                if where_param1 != None and where_value1 != None:
                    query += "AND "
                query += "`{}` <> '{}' ".format(wherenot_param1, wherenot_value1)
                if wherenot_param2 != None and wherenot_value2 != None:
                    query += "AND `{}` <> '{}' ".format(wherenot_param2, wherenot_value2)

            if where_param1 == None and wherenot_param1 == None:
                query += "1 "

            if order_param != None:
                query += "ORDER BY `{}`.`{}` ".format(table, order_param)
                if orderasc == True:
                    query += "ASC"
                else:
                    query += "DESC"

            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        connection.close()
        return result
    except Exception as e:
        print(e)
        connection.close()


def INSERT(table, insert_param1 = None, insert_param2 = None, insert_param3 = None, insert_param4 = None, insert_param5 = None,
insert_value1 = None, insert_value2 = None, insert_value3 = None, insert_value4 = None, insert_value5 = None):
    """Выполняет INSERT в базу данных из Connect_to_DB к таблице table с параметрами insert_param1234 равными insert_value1234"""
    try:
        connection = Connect_to_DB()
        with connection.cursor() as cursor:
            query = "INSERT INTO {} (".format(table)
            if insert_param1 != None:
                query += "`{}` ".format(insert_param1)
                if insert_param2 != None:
                    query += ", `{}` ".format(insert_param2)
                if insert_param3 != None:
                    query += ", `{}` ".format(insert_param3)
                if insert_param4 != None:
                    query += ", `{}` ".format(insert_param4)
                if insert_param5 != None:
                    query += ", `{}` ".format(insert_param5)
            query += ") VALUES ("



            if insert_param1 != None:
                query += "'{}' ".format(insert_value1)
                if insert_param2 != None:
                    query += ", '{}' ".format(insert_value2)
                if insert_param3 != None:
                    query += ", '{}' ".format(insert_value3)
                if insert_param4 != None:
                    query += ", '{}' ".format(insert_value4)
                if insert_param5 != None:
                    query += ", '{}' ".format(insert_value5)
            query += ")"

            cursor.execute(query)
            connection.commit()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()

def UPDATE(table, update_param1 = None, update_param2 = None, update_param3 = None, update_param4 = None, update_param5 = None,
update_value1 = None, update_value2 = None, update_value3 = None, update_value4 = None, update_value5 = None, where_param1 = None,
where_value1 = None, where_param2 = None, where_value2 = None, where_param3 = None, where_value3 = None, wherenot_param1 = None,
wherenot_value1 = None, wherenot_param2 = None, wherenot_value2 = None):
    """Выполняет UPDATE в базу данных из Connect_to_DB к таблице table с параметрами update_param1234 равными update_value1234"""
    try:
        connection = Connect_to_DB()
        with connection.cursor() as cursor:
            query = "UPDATE `{}` SET ".format(table)
            if update_param1 != None:
                query += "`{}` = '{}' ".format(update_param1, update_value1)
                if update_param2 != None:
                    query += ",`{}` = '{}' ".format(update_param2, update_value2)
                if update_param3 != None:
                    query += ",`{}` = '{}' ".format(update_param3, update_value3)
                if update_param4 != None:
                    query += ",`{}` = '{}' ".format(update_param4, update_value4)
                if update_param5 != None:
                    query += ",`{}` = '{}' ".format(update_param5, update_value5)
            query += "WHERE "

            if where_param1 != None and where_value1 != None:
                query += "`{}` = '{}' ".format(where_param1, where_value1)
                if where_param2 != None and where_value2 != None:
                    query += "AND `{}` = '{}' ".format(where_param2, where_value2)
                if where_param3 != None and where_value3 != None:
                    query += "AND `{}` = '{}' ".format(where_param3, where_value3)

            if wherenot_param1 != None and wherenot_value1 != None:
                if where_param1 != None and where_value1 != None:
                    query += "AND "
                query += "`{}` <> '{}' ".format(wherenot_param1, wherenot_value1)
                if wherenot_param2 != None and wherenot_value2 != None:
                    query += "AND `{}` <> '{}' ".format(wherenot_param2, wherenot_value2)

            if where_param1 == None and wherenot_param1 == None:
                query += "1 "

            cursor.execute(query)
            connection.commit()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()