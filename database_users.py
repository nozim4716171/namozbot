from sqlite3 import connect


def get_date():
    con = connect('users.db')
    cursor = con.cursor()
    all_users = []
    cursor.execute(f"SELECT * FROM users")
    res = cursor.fetchall()
    con.close()
    for i in res:
        all_users.append(i[2])
    return all_users


def add(first_name, id):
        con = connect('users.db')
        users = get_date()
        cursor = con.cursor()
        if id not in users:
            try:
                cursor.execute("INSERT INTO users (first_name ,user_id ) VALUES (:first_name , :id)",
                               {'first_name':first_name , 'id': id})
                con.commit()
            except:
                print("There is something wrong with your code")
        con.close()
