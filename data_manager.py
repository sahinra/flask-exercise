import db_connection


@db_connection.handle_connection
def get_all_questions(cursor, orderby):
    cursor.execute(f"""
        SELECT title, description FROM questions
        order by title {orderby}
    """)
    result = cursor.fetchall()
    return result


@db_connection.handle_connection
def get_all_answers(cursor, orderby):
    cursor.execute(f"""
        SELECT description FROM answers
        order by description {orderby}
    """)
    result = cursor.fetchall()
    return result


@db_connection.handle_connection
def get_all_users(cursor):
    cursor.execute("SELECT username FROM users")
    result = cursor.fetchall()
    return result


@db_connection.handle_connection
def get_question_by_id(cursor, id):
    cursor.execute(f"""
        SELECT title, description FROM questions
        where question_id = {id}
    """)
    result = cursor.fetchall()
    return result


@db_connection.handle_connection
def get_question_with_answers(cursor, index):
    cursor.execute(f"""
        select q.title, q.description, a.description from questions q
        join answers a on a.question_id = q.question_id
        where q.question_id = {index}
    """)
    result = cursor.fetchall()
    return result