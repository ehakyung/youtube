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

    def readLoggedIdPlaylistInfo(self):
        self.cursor.execute("SELECT nameOfList, indexOflist FROM playlist WHERE id=?", [self.loggedId]) 
        self.playlistOfLoggedId = self.cursor.fetchall()

    def readName(self):
        self.cursor.execute("SELECT name FROM account WHERE id=?", [self.loggedId])
        self.nameOfLoggedId = (self.cursor.fetchall())[0][0]

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

    def checkJoinId(self):
        self.cursor.execute("SELECT id FROM account WHERE id=?", [self.joinId]) 
        result = self.cursor.fetchall()
        self.checkJoinIdIndex = len(result)

    def checkJoinMail(self):
        self.cursor.execute("SELECT mail FROM account WHERE mail=?", [self.joinMail])
        result = self.cursor.fetchall() 
        self.checkJoinMailIndex = len(result)

    def createJoinInfo(self):
        self.cursor.execute("INSERT INTO account VALUES (?, ?, ?, ?, ?, datetime('now','localtime'))", [self.joinInfo[0], self.joinInfo[1], self.joinInfo[2], self.joinInfo[3], self.joinInfo[4]])
        self.connect.commit()

    def readProfileInfo(self):
        self.cursor.execute("SELECT name, id, dateTimeOfJoin, phone, mail FROM account WHERE id=?", [self.loggedId])
        self.profileInfoRead = self.cursor.fetchall()

        self.cursor.execute("SELECT indexOfList FROM playlist WHERE id=?", [self.loggedId])
        self.numOfPlaylistRead = self.cursor.fetchall()


    def checkPlaylistName(self):                
        self.cursor.execute("SELECT indexOfList FROM playlist WHERE id=? AND nameOfList=?", [self.loggedId, self.playlistName]) 
        result = self.cursor.fetchall()
        self.checkPlaylistNameIndex = len(result)

    def createPlaylist(self):
        self.cursor.execute("INSERT INTO playlist (id, nameOfList) VALUES (?, ?)", [self.loggedId, self.playlistName])
        self.connect.commit()

    def readIndiceOfPlaylist(self):
        self.cursor.execute("SELECT indexOfList FROM playlist WHERE id=?", [self.loggedId]) 
        self.indiceOfPlaylist = self.cursor.fetchall()

    def deletePlaylist(self):
        self.cursor.execute("DELETE FROM playlist WHERE indexOfList =?", [self.indexOfDeletedPlaylist])
        self.connect.commit()

    def readNameOfPlaylist(self):
        self.cursor.execute("SELECT nameOfList FROM playlist WHERE indexOfList=?", [self.indexOfSelectedPlaylist]) 
        result = self.cursor.fetchall()
        self.selectedPlaylistName = result[0][0]

    def logoutSetting(self):
        self.loginInfo = None
        self.matchLoginIndex = None
        self.loggedId = None
        self.playlistOfLoggedId = None
        self.nameOfLoggedId = None

        self.findIdInfo = None
        self.matchFindIdIndex = None
        self.idFinded = None

        self.findPwInfo = None
        self.matchFindPwIndex = None
        self.pwFinded = None
        
        self.joinId = None
        self.joinMail = None
        self.joinInfo = None

        self.profileInfoRead = None

        self.playlistName = None
        self.checkPlaylistNameIndex = None
        self.indiceOfPlaylist = None
        self.indexOfDeletedPlaylist = None

        self.indexOfSelectedPlaylist = None
        self.selectedPlaylistName = None

# if __name__ == "__main__":
#     db=Database()
#     db.cursor.execute("DELETE FROM playlist WHERE indexOfList < 10;")
#     db.connect.commit()