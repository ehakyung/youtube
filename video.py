import pafy, youtube_dl, sys, urllib.request, vlc, time

class Video:

    def __init__(self, ui, database):
        self.ui = ui
        self.database = database

        self.logoutSetting()

        self.ui.videoPageAddUrlBtn.clicked.connect(self.addUrlBtnEvent)
        self.ui.videoPageAddUrlBtn.enterEvent = lambda event: self.enterEvent1(event)
        self.ui.videoPageAddUrlBtn.leaveEvent = lambda event: self.leaveEvent1(event)

        self.ui.videoPagePlayOptionBtns[0].clicked.connect(self.playBtnEvent)
        self.ui.videoPagePlayOptionBtns[0].enterEvent = lambda event: self.enterEvent3(event)
        self.ui.videoPagePlayOptionBtns[0].leaveEvent = lambda event: self.leaveEvent3(event)

        self.ui.videoPagePlayOptionBtns[1].clicked.connect(self.pauseBtnEvent)
        self.ui.videoPagePlayOptionBtns[1].enterEvent = lambda event: self.enterEvent4(event)
        self.ui.videoPagePlayOptionBtns[1].leaveEvent = lambda event: self.leaveEvent4(event)

        self.ui.videoPagePlayOptionBtns[2].clicked.connect(self.stopBtnEvent)
        self.ui.videoPagePlayOptionBtns[2].enterEvent = lambda event: self.enterEvent5(event)
        self.ui.videoPagePlayOptionBtns[2].leaveEvent = lambda event: self.leaveEvent5(event)
        
        self.ui.slider.valueChanged[int].connect(self.changeVolume)


        for index in range(0, len(self.ui.videoPageVideoBtns)):
            self.ui.videoPageVideoBtns[index].clicked.connect(self.videoBtnEvent)

        for index in range (0, len(self.ui.videoPageDeleteVideoBtns)):
            self.ui.videoPageDeleteVideoBtns[index].clicked.connect(self.deleteVideoBtnEvent)
            self.ui.videoPageDeleteVideoBtns[index].enterEvent = lambda event, i=index: self.enterEvent2(event, i)
            self.ui.videoPageDeleteVideoBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent2(event, i)

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

    def initPlayer(self):
        self.vlc = vlc.Instance("--network-caching=20000")
        self.player = self.vlc.media_player_new()
        self.player.set_nsobject(int(self.ui.vlcFrame.winId()))

        self.eventManager = self.player.event_manager()
        self.eventManager.event_attach(vlc.EventType.MediaPlayerEndReached, lambda event: self.playNextVideo(event))

    def videoBtnEvent(self):
        self.ui.videoPageEmptyLabel.hide()
        
        tmpIndex = self.ui.mainWindow.sender().objectName()
        self.database.selectedVideoIndex = tmpIndex
        self.database.readIndiceOfVideo()

        print(self.selectedVideoBtnIndex)

        tmpList=[]
        for index in range(0, len(self.database.indiceOfVideo)):
            tmpList.append(self.database.indiceOfVideo[index][0])
        self.selectedVideoBtnIndex = tmpList.index(int(tmpIndex))
        self.database.readCurrentVideoInfo()

        self.player.set_mrl(self.database.currentVideoInfo[0][3])
        self.player.audio_set_volume(70)
        self.player.play()
        # self.ui.vlcFrame.show()

        self.ui.videoPageCurrentVideoNameLabel.setText(self.database.currentVideoInfo[0][0])
        self.ui.videoPageCurrentVideoChannelLabel.setText(self.database.currentVideoInfo[0][1])
        self.ui.videoPageCurrentVideoViewLabel.setText("조회수 "+str(round((self.database.currentVideoInfo[0][2])/10000))+"만회")

    def playCurrentVideo(self):
        self.database.readCurrentVideoInfo()

        self.ui.videoPageCurrentVideoNameLabel.setText(self.database.currentVideoInfo[0][0])
        self.ui.videoPageCurrentVideoChannelLabel.setText(self.database.currentVideoInfo[0][1])
        self.ui.videoPageCurrentVideoViewLabel.setText("조회수 "+str(round((self.database.currentVideoInfo[0][2])/10000))+"만회")

        self.player = self.vlc.media_player_new()
        self.player.set_nsobject(int(self.ui.vlcFrame.winId()))
        self.player.set_mrl(self.database.currentVideoInfo[0][3])
        self.player.stop()
        self.player.audio_set_volume(70)
        self.player.play()

        self.eventManager = self.player.event_manager()
        self.eventManager.event_attach(vlc.EventType.MediaPlayerEndReached, lambda event: self.playNextVideo(event))

    def playNextVideo(self, event):

        self.database.readIndiceOfVideo()

        tmpList = []
        for index in range(0, len(self.database.indiceOfVideo)):
            tmpList.append(self.database.indiceOfVideo[index][0])
        tmpList.sort()

        print(tmpList)
        print(self.selectedVideoBtnIndex, type(self.selectedVideoBtnIndex))

        if self.selectedVideoBtnIndex == len(tmpList)-1:
            tmpIndex = tmpList[0]
            self.database.selectedVideoIndex = tmpIndex
            self.selectedVideoBtnIndex = 0
            self.playCurrentVideo()

        else:
            self.selectedVideoBtnIndex += 1
            print(self.selectedVideoBtnIndex)
            tmpIndex = tmpList[self.selectedVideoBtnIndex]
            self.database.selectedVideoIndex = tmpIndex

            print(self.database.selectedVideoIndex)

            self.playCurrentVideo()

    def playBtnEvent(self):
        if self.player.is_playing() == 0:
            self.player.play()
        else:
            pass

    def pauseBtnEvent(self):
        if self.player.is_playing() == 1:
            self.player.pause()
        else:
            pass

    def stopBtnEvent(self):
        self.ui.videoPageCurrentVideoNameLabel.clear()
        self.ui.videoPageCurrentVideoChannelLabel.clear()
        self.ui.videoPageCurrentVideoViewLabel.clear()
        self.ui.videoPageEmptyLabel.show()
        self.ui.vlcFrame.hide()
        self.player.stop()

    def enterEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnEnteredStyle)

    def leaveEvent1(self, event):
        self.ui.videoPageAddUrlBtn.setStyleSheet(self.ui.rightBtnStyle)

    def enterEvent2(self, event, index):
        self.ui.videoPageDeleteVideoBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtnBlue.png)")

    def leaveEvent2(self, event, index):
        self.ui.videoPageDeleteVideoBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png)")

    def enterEvent3(self, event):
        self.ui.videoPagePlayOptionBtns[0].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/playBtnBlue.png);" + self.ui.backgroundTransparent + "background-repeat: no-repeat;")

    def leaveEvent3(self, event):
        self.ui.videoPagePlayOptionBtns[0].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/playBtn.png);" + self.ui.backgroundTransparent + "background-repeat: no-repeat;")

    def enterEvent4(self, event):
        self.ui.videoPagePlayOptionBtns[1].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/pauseBtnBlue.png);" + self.ui.backgroundTransparent + "background-repeat: no-repeat;")

    def leaveEvent4(self, event):
        self.ui.videoPagePlayOptionBtns[1].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/pauseBtn.png);" + self.ui.backgroundTransparent + "background-repeat: no-repeat;")

    def enterEvent5(self, event):
        self.ui.videoPagePlayOptionBtns[2].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/stopBtnBlue.png);" + self.ui.backgroundTransparent + "background-repeat: no-repeat;")

    def leaveEvent5(self, event):
        self.ui.videoPagePlayOptionBtns[2].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/stopBtn.png);" + self.ui.backgroundTransparent + "background-repeat: no-repeat;")

    def resetEnterLeaveEvent2(self): #lambda 이벤트 해제하는 법: None으로 바꾸기
        for index in range(0, len(self.ui.videoPageDeleteVideoBtns)):
            self.ui.videoPageDeleteVideoBtns[index].enterEvent = lambda event, i=index: self.enterEvent2(event, i)
            self.ui.videoPageDeleteVideoBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent2(event, i)

    def changeVolume(self, value):
        self.player.audio_set_volume(value)

    def logoutSetting(self):
        self.selectedVideoBtnIndex = None
        self.vlc = None
        self.player = None
        self.eventManager = None

