import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect("dolist.db")
        self.cursor = self.con.cursor()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks

    def add_new_task(self, new_title, new_description):
        try:
            query = f"INSERT INTO tasks (title,desc) VALUES('{new_title}', '{new_description}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False


    def task_done(self, id): ...
