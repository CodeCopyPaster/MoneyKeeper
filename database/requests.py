from db_connect import connection

def select_data(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return None

select_query = "SELECT testchar FROM test"
testiki = select_data(connection, select_query)

for testiki in testiki:
    print(testiki)