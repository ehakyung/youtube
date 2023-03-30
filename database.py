import sqlite3, pafy

class Database:
    def __init__(self, ui):
        self.ui = ui

        self.logoutSetting()

        self.connect = sqlite3.connect("database.db")
        self.cursor = self.connect.cursor()

        #unique key와 primary key는 다름/autoincreament를 써서 primary key로 만드는 것도 방법임/가입데이터에 가입 date도 넣기
        self.cursor.execute("CREATE TABLE IF NOT EXISTS account (name TEXT, id TEXT PRIMARY KEY, pw TEXT, phone TEXT, mail TEXT, dateTimeOfJoin TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist (id TEXT REFERENCES account(id), nameOfList TEXT, indexOfList INTEGER PRIMARY KEY AUTOINCREMENT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS video (indexOfList INTEGER REFERENCES playlist(indexOfList), title TEXT, author TEXT, view INTEGER, thumb TEXT, streamingUrl TEXT, indexOfVideo INTEGER PRIMARY KEY AUTOINCREMENT)")

    def matchLoginInfo(self):
        self.cursor.execute("SELECT id, pw FROM account WHERE id=? AND pw=?", self.loginInfo)
        result = self.cursor.fetchall()
        self.matchLoginIndex = len(result)

    def readLoggedIdPlaylistInfo(self):
        self.cursor.execute("SELECT nameOfList, indexOfList FROM playlist WHERE id=?", [self.loggedId]) 
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

    def readSelectedPlaylistVideoInfo(self):
        self.cursor.execute("SELECT title, author, view, thumb, indexOfVideo FROM video WHERE indexOfList=?", [self.indexOfSelectedPlaylist]) 
        self.videosOfSelectedPlaylist = self.cursor.fetchall()

    def createVideo(self):
        info = pafy.new(self.ui.videoPageUrlEdit.text())
        self.title = info.title
        self.author = info.author
        self.view = info.viewcount
        self.thumb = info.bigthumb
        self.streamingUrl = info.getbest().url

        self.cursor.execute("INSERT INTO video (indexOfList, title, author, view, thumb, streamingUrl) VALUES (?, ?, ?, ?, ?, ?)", [self.indexOfSelectedPlaylist, self.title, self.author, self.view, self.thumb, self.streamingUrl])
        self.connect.commit()

    def readIndiceOfVideo(self):
        self.cursor.execute("SELECT indexOfVideo FROM video WHERE indexOfList=?", [self.indexOfSelectedPlaylist]) 
        self.indiceOfVideo = self.cursor.fetchall()

    def deleteVideo(self):
        self.cursor.execute("DELETE FROM video WHERE indexOfVideo =?", [self.indexOfDeletedVideo])
        self.connect.commit()

    def readNewVideoInfo(self):
        self.cursor.execute("SELECT title, author, view, thumb FROM video WHERE indexOfVideo=?", [self.indiceOfVideo[-1][0]]) 
        result = self.cursor.fetchall()
        self.newTitle = result[0][0]
        self.newAuthor = result[0][1]
        self.newView = result[0][2]
        self.newThumb = result[0][3]

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

        self.title = None
        self.author = None
        self.view = None
        self.thumb = None
        self.streamingUrl = None

        self.videosOfSelectedPlaylist = None

        self.newTitle = None
        self.newAuthor = None
        self.newView = None
        self.newThumb = None

        self.indiceOfVideo = None
        self.indexOfDeletedVideo = None


# if __name__ == "__main__":
#     db=Database()
#     db.cursor.execute("DELETE FROM playlist WHERE indexOfList < 10;")
#     db.connect.commit()