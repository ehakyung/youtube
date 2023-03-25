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
        self.database.readProfileInfo()
        for index in range (0, len(self.database.profileInfoRead[0])):
            self.ui.myInfoPageEdits[index].setText(str(self.database.profileInfoRead[0][index]))

        self.ui.screen.setCurrentIndex(5)

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
        else:
            pass
        self.ui.reply = None            

    def addPlaylistBtnEvent(self):
        self.ui.inputDialogPopUp()

        if self.ui.reply == 1:
            if len(self.ui.tmpPlaylistName) > 20:
                self.ui.messageBoxPopUp(3)
            else:
                self.database.playlistName = self.ui.tmpPlaylistName
                self.database.checkPlaylistName()

                if self.database.checkPlaylistNameIndex > 0:
                    self.ui.messageBoxPopUp(4)
                else:
                    self.database.createPlaylist()

                    self.database.readIndiceOfPlaylist()
                    self.ui.indexOfNewList = self.database.indiceOfPlaylist[-1][0]
                    self.ui.indexOfNewBtn = len(self.database.indiceOfPlaylist)-1

                    self.ui.addPlaylist()

                    self.ui.mainPagePlaylistBtns[self.ui.indexOfNewBtn].clicked.connect(lambda event, i = self.ui.indexOfNewBtn: self.playlistBtnEvent(event, i))

                    self.ui.mainPageDeletePlaylistBtns[self.ui.indexOfNewBtn].clicked.connect(self.deletePlaylistBtnEvent)
                    self.ui.mainPageDeletePlaylistBtns[self.ui.indexOfNewBtn].enterEvent = lambda event, i = self.ui.indexOfNewBtn: self.enterEvent5(event, i)
                    self.ui.mainPageDeletePlaylistBtns[self.ui.indexOfNewBtn].leaveEvent = lambda event, i = self.ui.indexOfNewBtn: self.leaveEvent5(event, i)

        else:
            pass
        self.ui.reply = None

    def playlistBtnEvent(self, event, index):
        self.ui.screen.setCurrentIndex(6)
        self.video = video.Video(self.ui)

    def deletePlaylistBtnEvent(self):
        self.ui.messageBoxPopUp(1)

        tmpIndex = self.ui.mainWindow.sender().objectName()
        self.database.readIndiceOfPlaylist()

        tmpList=[]
        for index in range(0, len(self.database.indiceOfPlaylist)):
            tmpList.append(self.database.indiceOfPlaylist[index][0])
        self.ui.deletedPlaylistBtnIndex = tmpList.index(int(tmpIndex))
        #여기까지 실행되면 어떤 index(db)의 playlist가 삭제됐는지 알 수 있음

        # self.ui.mainPageDeletePlaylistBtns[self.ui.deletedPlaylistBtnIndex].clicked.disconnect()

        if self.ui.reply == 1:
            self.database.indexOfDeletedPlaylist = tmpIndex
            self.database.deletePlaylist()

            self.ui.deletePlaylist()
            self.resetEnterLeaveEvent5()
        else:
            pass
        
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

    def resetEnterLeaveEvent5(self):
        # for index in range (0, len(self.ui.mainPagePlaylistBtns)):
        #     self.ui.mainPagePlaylistBtns[index].clicked.disconnect()
        # for index in range(0, len(self.ui.mainPageDeletePlaylistBtns)):
        #     self.ui.mainPageDeletePlaylistBtns[index].clicked.disconnect()


        # for index in range (0, len(self.ui.mainPagePlaylistBtns)):
        #     self.ui.mainPagePlaylistBtns[index].clicked.connect(lambda event, i=index: self.playlistBtnEvent(event, i))
        #     #enterevent, leaveevent 추가하기

        for index in range(0, len(self.ui.mainPageDeletePlaylistBtns)):
            # self.ui.mainPageDeletePlaylistBtns[index].clicked.connect(self.deletePlaylistBtnEvent)
            self.ui.mainPageDeletePlaylistBtns[index].enterEvent = lambda event, i=index: self.enterEvent5(event, i)
            self.ui.mainPageDeletePlaylistBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent5(event, i)
