import sqlite3

class UserManager:
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        self.conn.commit()

    def insert_user(self, name, age):
        c = self.conn.cursor()
        c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def get_users(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        return users

    def update_user(self, user_id, name, age):
        c = self.conn.cursor()
        c.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        c = self.conn.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    manager = UserManager()
    manager.insert_user('Alice', 30)
    manager.insert_user('Bob', 25)
    users = manager.get_users()
    print(users)
    manager.update_user(1, 'Alice', 31)
    manager.delete_user(2)
    users = manager.get_users()
    print(users)
    manager.close()