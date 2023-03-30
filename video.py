import pafy, youtube_dl, sys, urllib.request, vlc

class Video:

    def __init__(self, ui, database):
        self.ui = ui
        self.database = database

        self.indexOfSelectedPlaylistBtn = None

        # self.ui.homeBtns[1].clicked.connect(self.homeBtnEvent)

        self.ui.videoPageAddUrlBtn.clicked.connect(self.addUrlBtnEvent)
        self.ui.videoPageAddUrlBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.videoPageAddUrlBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        for index in range(0, len(self.ui.videoPageVideoBtns)):
            self.ui.videoPageVideoBtns[index].clicked.connect(self.videoBtnEvent)

        for index in range (0, len(self.ui.videoPageDeleteVideoBtns)):
            self.ui.videoPageDeleteVideoBtns[index].clicked.connect(self.deleteVideoBtnEvent)
            self.ui.videoPageDeleteVideoBtns[index].enterEvent = lambda event, i=index: self.enterEvent2(event, i)
            self.ui.videoPageDeleteVideoBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent2(event, i)

    # def homeBtnEvent(self):
    #     self.ui.screen.setCurrentIndex(4)
    #     self.ui.clearVideoPage()

    #     self.database.readIndiceOfPlaylist()
    #     tmpList = []
    #     for index in range (0, len(self.database.indiceOfPlaylist)):
    #         tmpList.append(self.database.indiceOfPlaylist[index][0])

    #     print(tmpList)
    #     print(self.database.indexOfSelectedPlaylist)

    #     self.indexOfSelectedPlaylistBtn = tmpList.index(int(self.database.indexOfSelectedPlaylist))
        
    #     self.ui.mainPagePlaylistBtns[self.indexOfSelectedPlaylistBtn].clicked.disconnect()

    def addUrlBtnEvent(self):
        try:
            self.database.createVideo()

            self.database.readIndiceOfVideo()
            self.ui.indexOfNewVideo = self.database.indiceOfVideo[-1][0]
            self.ui.indexOfNewVideoBtn = len(self.database.indiceOfVideo)-1

            self.database.readNewVideoInfo()
            self.ui.addVideo()

            self.ui.videoPageVideoBtns[self.ui.indexOfNewVideoBtn].clicked.connect(self.videoBtnEvent)

            self.ui.videoPageDeleteVideoBtns[self.ui.indexOfNewVideoBtn].clicked.connect(self.deleteVideoBtnEvent)
            self.ui.videoPageDeleteVideoBtns[self.ui.indexOfNewVideoBtn].enterEvent = lambda event, i = self.ui.indexOfNewVideoBtn: self.enterEvent2(event, i)
            self.ui.videoPageDeleteVideoBtns[self.ui.indexOfNewVideoBtn].leaveEvent = lambda event, i = self.ui.indexOfNewVideoBtn: self.leaveEvent2(event, i)
            
            self.ui.videoPageUrlEdit.clear()
        except:
            self.ui.messageBoxPopUp(5)
            self.ui.videoPageUrlEdit.clear()


    def deleteVideoBtnEvent(self):
        self.ui.messageBoxPopUp(2)

        tmpIndex = self.ui.mainWindow.sender().objectName()
        self.database.readIndiceOfVideo()

        tmpList=[]
        for index in range(0, len(self.database.indiceOfVideo)):
            tmpList.append(self.database.indiceOfVideo[index][0])
        self.ui.deletedVideoBtnIndex = tmpList.index(int(tmpIndex))
        #여기까지 실행되면 몇번째 버튼의 playlist가 삭제됐는지 알 수 있음

        # self.ui.videoPageDeleteVideoBtns[self.ui.deletedVideoBtnIndex].clicked.disconnect()

        if self.ui.reply == 1:
            self.database.indexOfDeletedVideo = tmpIndex
            self.database.deleteVideo()

            self.ui.deleteVideo()
            self.resetEnterLeaveEvent2()
        else:
            pass
        
        self.ui.reply = None

    def videoBtnEvent(self):

        self.ui.videoPageEmptyLabel.hide()
        
        self.vlc = vlc.Instance()
        self.player = self.vlc.media_player_new()
        self.media = None
        # self.media = self.vlc.media_new("BTSDynamiteMV.mp4")
        # self.player.set_media(self.media)
        self.ui.makeVlcFrame()

        self.player.set_nsobject(int(self.ui.vlcFrame.winId()))

        tmpIndex = self.ui.mainWindow.sender().objectName()
        self.database.selectedVideoBtnIndex = tmpIndex
        self.database.readIndiceOfVideo()

        tmpList=[]
        for index in range(0, len(self.database.indiceOfVideo)):
            tmpList.append(self.database.indiceOfVideo[index][0])
        self.ui.selectedVideoBtnIndex = tmpList.index(int(tmpIndex))
        #여기까지 실행되면 몇번째 버튼의 video가 선택됐는지 알 수 있음

        self.database.readCurrentVideoInfo()


        self.media = self.vlc.media_new(self.database.currentVideoInfo[0][3])
        self.player.set_media(self.media)
        self.player.play()
        self.ui.vlcFrame.show()

        self.ui.videoPageCurrentVideoNameLabel.setText(self.database.currentVideoInfo[0][0])
        self.ui.videoPageCurrentVideoChannelLabel.setText(self.database.currentVideoInfo[0][1])
        self.ui.videoPageCurrentVideoViewLabel.setText("조회수 "+str(round((self.database.currentVideoInfo[0][2])/10000))+"만회")

    def enterEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnEnteredStyle)

    def leaveEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnStyle)

    def enterEvent2(self, event, index):
        self.ui.videoPageDeleteVideoBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtnBlue.png)")

    def leaveEvent2(self, event, index):
        self.ui.videoPageDeleteVideoBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png)")

    def resetEnterLeaveEvent2(self): #lambda 이벤트 해제하는 법: None으로 바꾸기
        for index in range(0, len(self.ui.videoPageDeleteVideoBtns)):
            self.ui.videoPageDeleteVideoBtns[index].enterEvent = lambda event, i=index: self.enterEvent2(event, i)
            self.ui.videoPageDeleteVideoBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent2(event, i)



# if __name__ == "__main__":
#     video = Video()

