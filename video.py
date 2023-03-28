import pafy, youtube_dl

class Video:

    def __init__(self, ui):
        self.ui = ui

        self.ui.videoPageAddUrlBtn.clicked.connect(self.addUrlBtnEvent)
        self.ui.videoPageAddUrlBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.videoPageAddUrlBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        self.ui.videoPageDeleteVideoBtn.clicked.connect(self.deleteVideoBtnEvent)
        self.ui.videoPageDeleteVideoBtn.enterEvent = lambda event: self.enterEvent2(event)
        self.ui.videoPageDeleteVideoBtn.leaveEvent = lambda event: self.leaveEvent2(event)



    def addUrlBtnEvent(self):
        print("성공")

    def deleteVideoBtnEvent(self):
        print("성공")

    def enterEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnEnteredStyle)

    def leaveEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnStyle)

    def enterEvent2(self, event):
        self.ui.videoPageDeleteVideoBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtnBlue.png)")

    def leaveEvent2(self, event):
        self.ui.videoPageDeleteVideoBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png)")

# if __name__ == "__main__":
#     video = Video()

