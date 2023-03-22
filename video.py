class Video:

    def __init__(self, ui):
        self.ui = ui

        self.ui.videoPageAddBtn.clicked.connect(self.videoPageAddBtnEvent)
        self.ui.videoPageAddBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.videoPageAddBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        self.ui.videoPageDeleteVideoBtn.clicked.connect(self.videoPageDeleteBtnEvent)
        self.ui.videoPageDeleteVideoBtn.enterEvent = lambda event: self.enterEvent2(event)
        self.ui.videoPageDeleteVideoBtn.leaveEvent = lambda event: self.leaveEvent2(event)



    def videoPageAddBtnEvent(self):
        print("성공")

    def videoPageDeleteBtnEvent(self):
        print("성공")

    def enterEvent1(self, event):
        self.ui.videoPageAddBtn.setStyleSheet(self.ui.rightBtnEnteredStyle)

    def leaveEvent1(self, event):
        self.ui.videoPageAddBtn.setStyleSheet(self.ui.rightBtnStyle)

    def enterEvent2(self, event):
        self.ui.videoPageDeleteVideoBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtnBlue.png)")

    def leaveEvent2(self, event):
        self.ui.videoPageDeleteVideoBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png)")
