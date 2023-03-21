class Main:
    def __init__(self, ui, database, account):
        self.ui = ui
        self.database = database
        self.account = account

        self.loggedId = self.database.loggedId

        self.playlist=[]

        self.ui.mainPageProfileBtn.clicked.connect(self.profileBtnEvent)
        self.ui.mainPageProfileBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.mainPageProfileBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        self.ui.mainPageLogoutBtn.clicked.connect(self.logoutBtnEvent)
        self.ui.mainPageLogoutBtn.enterEvent = lambda event: self.enterEvent2(event)
        self.ui.mainPageLogoutBtn.leaveEvent = lambda event: self.leaveEvent2(event)

        self.ui.mainPageAddPlaylistBtn.clicked.connect(self.addPlaylistBtnEvent)
        self.ui.mainPageAddPlaylistBtn.enterEvent = lambda event: self.enterEvent3(event)
        self.ui.mainPageAddPlaylistBtn.leaveEvent = lambda event: self.leaveEvent3(event)


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
                print(self.ui.tmpPlaylistName)
        elif self.ui.reply == 0:
            self.ui.reply = None


    def enterEvent1(self, event):
        self.ui.mainPageProfileBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/profileBtnBlue.png)")

    def leaveEvent1(self, event):
        self.ui.mainPageProfileBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/profileBtn.png)")

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
