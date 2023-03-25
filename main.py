import video

class Main:
    def __init__(self, ui, database, account):
        self.ui = ui
        self.database = database
        self.account = account
        self.video = None

        self.ui.mainPageProfileBtn.clicked.connect(self.profileBtnEvent)
        self.ui.mainPageProfileBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.mainPageProfileBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        self.ui.mainPageLogoutBtn.clicked.connect(self.logoutBtnEvent)
        self.ui.mainPageLogoutBtn.enterEvent = lambda event: self.enterEvent2(event)
        self.ui.mainPageLogoutBtn.leaveEvent = lambda event: self.leaveEvent2(event)

        for index in range (0, len(self.ui.homeBtns)):
            self.ui.homeBtns[index].clicked.connect(self.homeBtnEvent)
            self.ui.homeBtns[index].enterEvent = lambda event, i=index: self.enterEvent4(event, i)
            self.ui.homeBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent4(event, i)

        self.ui.mainPageAddPlaylistBtn.clicked.connect(self.addPlaylistBtnEvent)
        self.ui.mainPageAddPlaylistBtn.enterEvent = lambda event: self.enterEvent3(event)
        self.ui.mainPageAddPlaylistBtn.leaveEvent = lambda event: self.leaveEvent3(event)

        for index in range (0, len(self.ui.mainPagePlaylistBtns)):
            self.ui.mainPagePlaylistBtns[index].clicked.connect(lambda event, i=index: self.playlistBtnEvent(event, i))
            #enterevent, leaveevent 추가하기

        for index in range(0, len(self.ui.mainPageDeletePlaylistBtns)):
            self.ui.mainPageDeletePlaylistBtns[index].clicked.connect(self.deletePlaylistBtnEvent)

            self.ui.mainPageDeletePlaylistBtns[index].enterEvent = lambda event, i=index: self.enterEvent5(event, i)
            self.ui.mainPageDeletePlaylistBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent5(event, i)

    def profileBtnEvent(self):
        self.ui.screen.setCurrentIndex(5)
        self.account.loadProfileInfo()

    def homeBtnEvent(self):
        self.ui.screen.setCurrentIndex(4)

    def logoutBtnEvent(self):
        self.ui.messageBoxPopUp(0)

        if self.ui.reply == 1:
            self.ui.screen.setCurrentIndex(0)
            self.ui.mainPageLogoutBtn.clicked.disconnect()
            self.ui.clearMainPage()
            self.ui.logoutSetting()
            self.database.logoutSetting()
            self.ui.reply = None
        elif self.ui.reply == 0:
            self.ui.reply = None
            

    def addPlaylistBtnEvent(self):
        self.ui.inputDialogPopUp()

        if self.ui.reply == 1:
            self.ui.reply = None
            if len(self.ui.tmpPlaylistName) > 20:
                self.ui.messageBoxPopUp(3)
            else:
                self.database.cursor.execute("SELECT indexOfList FROM playlist WHERE id=? AND nameOfList=?", [self.database.loggedId, self.ui.tmpPlaylistName]) 
                result=self.database.cursor.fetchall()
                if len(result) > 0:
                    self.ui.messageBoxPopUp(4)
                else:
                    self.database.cursor.execute("INSERT INTO playlist (id, nameOfList) VALUES (?, ?)", [self.database.loggedId, self.ui.tmpPlaylistName])
                    self.database.connect.commit()

                    self.database.cursor.execute("SELECT indexOfList FROM playlist WHERE id=?", [self.database.loggedId]) 
                    result=self.database.cursor.fetchall()
                    self.ui.indexOfNewList = result[len(result)-1][0]
                    print(self.ui.indexOfNewList)
                    self.ui.indexOfNewBtn = len(result)-1

                    self.ui.addPlaylist()

        elif self.ui.reply == 0:
            self.ui.reply = None

    def playlistBtnEvent(self, event, index):
        self.ui.screen.setCurrentIndex(6)
        self.video = video.Video(self.ui)

    def deletePlaylistBtnEvent(self):
        self.ui.messageBoxPopUp(1)

        tmpIndex =self.ui.mainWindow.sender().objectName()
        self.ui.deletedPlaylistIndex = tmpIndex

        self.database.cursor.execute("SELECT indexOflist, nameOfList FROM playlist WHERE id=?", [self.database.loggedId]) 
        result=self.database.cursor.fetchall()

        tmpList=[]
        for index in range(0, len(result)):
            tmpList.append(result[index][0])
        self.ui.deletedPlaylistBtnIndex = tmpList.index(int(tmpIndex))

        # self.ui.mainPageDeletePlaylistBtns[self.ui.deletedPlaylistBtnIndex].clicked.disconnect()

        if self.ui.reply == 1:
            self.database.cursor.execute("DELETE FROM playlist WHERE indexOfList =?", [tmpIndex])
            self.database.connect.commit()

            self.ui.deletePlaylist()
            self.ui.reply = None

        elif self.ui.reply == 0:
            self.ui.reply = None

    def enterEvent1(self, event):
        self.ui.mainPageProfileBtn.setStyleSheet(self.ui.profileBtnEnteredStyle)

    def leaveEvent1(self, event):
        self.ui.mainPageProfileBtn.setStyleSheet(self.ui.profileBtnStyle)

    def enterEvent2(self, event):
        self.ui.mainPageLogoutBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/logoutBtnBlue.png)")

    def leaveEvent2(self, event):
        self.ui.mainPageLogoutBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/logoutBtn.png)")

    def enterEvent3(self, event):
        self.ui.mainPageAddPlaylistBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/addPlaylistBtnBlue.png)")

    def leaveEvent3(self, event):
        self.ui.mainPageAddPlaylistBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/addPlaylistBtn.png)")

    def enterEvent4(self, event, index):
        self.ui.homeBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/homeBtnBlue.png)")

    def leaveEvent4(self, event, index):
        self.ui.homeBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/homeBtn.png)")

    def enterEvent5(self, event, index):
        self.ui.mainPageDeletePlaylistBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtnBlue.png)")

    def leaveEvent5(self, event, index):
        self.ui.mainPageDeletePlaylistBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png)")
