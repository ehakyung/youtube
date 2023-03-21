import sqlite3

class Database:
    def __init__(self):
        pass
        self.loggedId = None

        self.connect=sqlite3.connect("database.db")
        self.cursor=self.connect.cursor()

        #unique key와 primary key는 다름/autoincreament를 써서 primary key로 만드는 것도 방법임/가입데이터에 가입 date도 넣기
        self.cursor.execute("CREATE TABLE IF NOT EXISTS account (name TEXT, id TEXT PRIMARY KEY, pw TEXT, phone TEXT, mail TEXT, dateTimeOfJoin TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist (id TEXT REFERENCES userInfo(id), nameOfList TEXT, indexOfList INTEGER)")


