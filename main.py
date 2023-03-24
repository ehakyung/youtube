import video

class Main:
    def __init__(self, ui, database, account):
        self.ui = ui
        self.database = database
        self.account = account
        self.video = None

        # self.loggedId = self.database.loggedId

        # self.playlist=[]

        self.ui.mainPageProfileBtn.clicked.connect(self.profileBtnEvent)
        self.ui.mainPageProfileBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.mainPageProfileBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        self.ui.mainPageLogoutBtn.clicked.connect(self.logoutBtnEvent)
        self.ui.mainPageLogoutBtn.enterEvent = lambda event: self.enterEvent2(event)
        self.ui.mainPageLogoutBtn.leaveEvent = lambda event: self.leaveEvent2(event)

        self.ui.mainPageAddPlaylistBtn.clicked.connect(self.addPlaylistBtnEvent)
        self.ui.mainPageAddPlaylistBtn.enterEvent = lambda event: self.enterEvent3(event)
        self.ui.mainPageAddPlaylistBtn.leaveEvent = lambda event: self.leaveEvent3(event)

        for index in range (0, len(self.ui.mainPagePlaylistBtns)):
            self.ui.mainPagePlaylistBtns[index].clicked.connect(lambda event, i=index: self.playlistBtnEvent(event, i))
            #enterevent, leaveevent 추가하기



        # for index in range (0, len(self.ui.mainPagePlaylistIconBtns)):
        #     self.ui.mainPagePlaylistIconBtns[index].clicked.connect(lambda event, i=index: self.playlistIconBtnEvent(event, i))
        #     #enterevent, leaveevent 추가하기

        for index in range(0, len(self.ui.mainPageDeletePlaylistBtns)):
            self.ui.mainPageDeletePlaylistBtns[index].clicked.connect(self.deletePlaylistBtnEvent)
            self.ui.mainPageDeletePlaylistBtns[index].enterEvent = lambda event, i=index: self.enterEvent5(event, i)
            self.ui.mainPageDeletePlaylistBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent5(event, i)

        for index in range (0, len(self.ui.homeBtns)):
            self.ui.homeBtns[index].clicked.connect(self.homeBtnEvent)
            self.ui.homeBtns[index].enterEvent = lambda event, i=index: self.enterEvent4(event, i)
            self.ui.homeBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent4(event, i)

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

            # self.database.cursor.execute("SELECT indexOflist FROM playlist WHERE id=?", [self.database.loggedId]) 
            # result=self.database.cursor.fetchall()

            self.ui.clearMainPage()
            self.database.loggedId = None
            self.ui.reply = None
        elif self.ui.reply == 0:
            self.ui.reply = None
            

    def addPlaylistBtnEvent(self):
        self.ui.inputDialogPopUp()

        if self.ui.reply == 1:
            self.ui.reply = None
            if len(self.ui.tmpPlaylistName) > 20:
                self.ui.messageBoxPopUp(3)
            else: #중복방지기능 추가하기
                # self.playlist.append(self.ui.tmpPlaylistName)
                # print(self.playlist)
                self.database.cursor.execute("INSERT INTO playlist (id, nameOfList) VALUES (?, ?)", [self.database.loggedId, self.ui.tmpPlaylistName])
                self.database.connect.commit()

                self.database.cursor.execute("SELECT indexOfList FROM playlist WHERE id=?", [self.database.loggedId]) 
                result=self.database.cursor.fetchall()
                self.ui.indexOfNewList = result[len(result)-1][0]
                print(self.ui.indexOfNewList)
                self.ui.indexOfNewBtn = len(result)-1

                self.ui.addPlaylist()

                self.ui.mainPagePlaylistBtns[len(self.ui.mainPagePlaylistBtns)-1].clicked.connect(lambda event, i=len(self.ui.mainPagePlaylistBtns)-1: self.playlistBtnEvent(event, i))
                self.ui.mainPageDeletePlaylistBtns[len(self.ui.mainPageDeletePlaylistBtns)-1].clicked.connect(self.deletePlaylistBtnEvent)
                self.ui.mainPageDeletePlaylistBtns[len(self.ui.mainPageDeletePlaylistBtns)-1].enterEvent = lambda event, i=len(self.ui.mainPageDeletePlaylistBtns)-1: self.enterEvent5(event, i)
                self.ui.mainPageDeletePlaylistBtns[len(self.ui.mainPageDeletePlaylistBtns)-1].leaveEvent = lambda event, i=len(self.ui.mainPageDeletePlaylistBtns)-1: self.leaveEvent5(event, i)


        elif self.ui.reply == 0:
            self.ui.reply = None


    def playlistBtnEvent(self, event, index):
        self.ui.screen.setCurrentIndex(6)
        self.video = video.Video(self.ui)

    def deletePlaylistBtnEvent(self):
        self.ui.messageBoxPopUp(1)
        if self.ui.reply == 1:
            
            tmpIndex =self.ui.mainWindow.sender().objectName()
            self.ui.deletedPlaylistIndex = tmpIndex
            print("tmpIndex(sender's objectname):", tmpIndex)

            self.database.cursor.execute("SELECT indexOflist, nameOfList FROM playlist WHERE id=?", [self.database.loggedId]) 
            result=self.database.cursor.fetchall()
            print("로그인한 계정의 플레이리스트 리스트:", result)

            tmpList=[]
            for index in range(0, len(result)):
                tmpList.append(result[index][0])
            print("로그인한 계정의 플레이리스트 인덱스의 리스트:", tmpList)

            self.ui.deletedPlaylistBtnIndex = tmpList.index(int(tmpIndex))


            # tmpName = self.ui.mainPagePlaylistNameLabels[tmpIndex].text()
            self.database.cursor.execute("DELETE FROM playlist WHERE indexOfList =?", [tmpIndex])
            self.database.connect.commit()

            print(self.ui.mainWindow.sender().objectName())
            print(tmpIndex)
            print(type(tmpIndex))

            self.ui.deletePlaylist()
            print("재생목록 삭제")
            # self.ui.displayPlaylist()
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
