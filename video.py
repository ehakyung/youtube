import pafy, youtube_dl

class Video:

    def __init__(self, ui, database):
        self.ui = ui
        self.database = database

        self.ui.videoPageAddUrlBtn.clicked.connect(self.addUrlBtnEvent)
        self.ui.videoPageAddUrlBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.videoPageAddUrlBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        for index in range (0, len(self.ui.videoPageDeleteVideoBtns)):
            # self.ui.videoPageDeleteVideoBtns[index].clicked.connect(self.deleteVideoBtnEvent)
            self.ui.videoPageDeleteVideoBtns[index].enterEvent = lambda event, i=index: self.enterEvent2(event, i)
            self.ui.videoPageDeleteVideoBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent2(event, i)



    def addUrlBtnEvent(self):
        # try:
            self.database.createVideo()

            self.database.readIndiceOfVideo()
            self.ui.indexOfNewVideo = self.database.indiceOfVideo[-1][0]
            self.ui.indexOfNewVideoBtn = len(self.database.indiceOfVideo)-1

            self.ui.addVideo()
        # except:
        #     print("실패")

    def deleteVideoBtnEvent(self):
        print("성공")

    def enterEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnEnteredStyle)

    def leaveEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnStyle)

    def enterEvent2(self, event, index):
        self.ui.videoPageDeleteVideoBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtnBlue.png)")

    def leaveEvent2(self, event, index):
        self.ui.videoPageDeleteVideoBtns.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png)")

# if __name__ == "__main__":
#     video = Video()

