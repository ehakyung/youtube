import sqlite3

class Database:
    def __init__(self, ui):
        self.ui = ui

        self.logoutSetting()

        self.connect = sqlite3.connect("database.db")
        self.cursor = self.connect.cursor()

        #unique key와 primary key는 다름/autoincreament를 써서 primary key로 만드는 것도 방법임/가입데이터에 가입 date도 넣기
        self.cursor.execute("CREATE TABLE IF NOT EXISTS account (name TEXT, id TEXT PRIMARY KEY, pw TEXT, phone TEXT, mail TEXT, dateTimeOfJoin TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist (id TEXT REFERENCES account(id), nameOfList TEXT, indexOfList INTEGER PRIMARY KEY AUTOINCREMENT)")

    def matchLoginInfo(self):
        self.cursor.execute("SELECT id, pw FROM account WHERE id=? AND pw=?", self.loginInfo)
        result = self.cursor.fetchall()
        self.matchLoginIndex = len(result)

    def loadLoggedIdPlaylistInfo(self):
        self.cursor.execute("SELECT nameOfList, indexOflist FROM playlist WHERE id=?", [self.loggedId]) 
        result = self.cursor.fetchall()
        self.ui.playlistOfLoggedId = result

    def matchFindIdInfo(self):
        self.cursor.execute("SELECT id FROM account WHERE mail=?", [self.findIdInfo])
        result=self.cursor.fetchall()
        self.matchFindIdIndex = len(result)
        if len(result) == 1:
            self.idFinded = result[0][0]

    def matchFindPwInfo(self):
        self.cursor.execute("SELECT pw FROM account WHERE id=? AND mail=?", self.findPwInfo)
        result=self.cursor.fetchall()
        self.matchFindPwIndex = len(result)
        if len(result) == 1:
            self.pwFinded = result[0][0]

    def logoutSetting(self):
        self.loginInfo = None
        self.matchLoginIndex = None
        self.loggedId = None

        self.findIdInfo = None
        self.matchFindIdIndex = None
        self.idFinded = None

        self.findPwInfo = None
        self.matchFindPwIndex = None
# if __name__ == "__main__":
#     db=Database()
#     db.cursor.execute("DELETE FROM playlist WHERE indexOfList < 10;")
#     db.connect.commit()