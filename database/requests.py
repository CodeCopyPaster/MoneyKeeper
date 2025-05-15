from utils.logger import write_log as lg

def log_data(connection):
    cursor = connection.cursor()

    data_for_log = lg()

    number = data_for_log["balance"]
    current_time = data_for_log["date"]


    query = """
    INSERT INTO datetime_storage (number_value, datetime_value)
    VALUES (%s, %s);
    """

    cursor.execute(query, (number, current_time))

    connection.commit()

    cursor.close()
