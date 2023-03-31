import pafy, sys, urllib.request, vlc, time
from PyQt5 import QtWidgets, QtGui


class Ui:
    def __init__(self):

        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1500, 900)

        self.centralWidget = QtWidgets.QWidget()
        self.mainWindow.setCentralWidget(self.centralWidget)

        self.urlLabel = QtWidgets.QLabel(self.centralWidget)
        self.urlLabel.setGeometry(100, 100, 100, 30)
        self.urlLabel.setText("URL")

        self.urlEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.urlEdit.setGeometry(200, 100, 710, 30)

        self.urlBtn = QtWidgets.QPushButton(self.centralWidget)
        self.urlBtn.setGeometry(950, 100, 50, 30)
        self.urlBtn.setText("add")
        self.urlBtn.clicked.connect(self.clickEvent)

        self.volumeBtn = QtWidgets.QPushButton(self.centralWidget)
        self.volumeBtn.setGeometry(950, 150, 50, 30)
        self.volumeBtn.setText("50")
        self.volumeBtn.clicked.connect(self.volume50BtnEvent)

        self.volumeBtn2 = QtWidgets.QPushButton(self.centralWidget)
        self.volumeBtn2.setGeometry(950, 200, 50, 30)
        self.volumeBtn2.setText("20")
        self.volumeBtn2.clicked.connect(self.volume20BtnEvent)

        self.volumeBtn3 = QtWidgets.QPushButton(self.centralWidget)
        self.volumeBtn3.setGeometry(950, 250, 50, 30)
        self.volumeBtn3.setText("100")
        self.volumeBtn3.clicked.connect(self.volume100BtnEvent)


        self.thumbLabel = QtWidgets.QLabel(self.centralWidget)
        self.thumbLabel.setGeometry(1000, 100, 400, 400)
    

        self.authorLabel = QtWidgets.QLabel(self.centralWidget)
        self.authorLabel.setGeometry(100, 150, 100, 30)
        self.authorLabel.setText("AUTHOR")

        self.authorEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.authorEdit.setGeometry(200, 150, 710, 30)

        self.titleLabel = QtWidgets.QLabel(self.centralWidget)
        self.titleLabel.setGeometry(100, 200, 100, 30)
        self.titleLabel.setText("TITLE")

        self.titleEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.titleEdit.setGeometry(200, 200, 710, 30)

        self.viewLabel = QtWidgets.QLabel(self.centralWidget)
        self.viewLabel.setGeometry(100, 250, 100, 30)
        self.viewLabel.setText("VIEW")

        self.viewEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.viewEdit.setGeometry(200, 250, 710, 30)

        self.streamingUrlLabel = QtWidgets.QLabel(self.centralWidget)
        self.streamingUrlLabel.setGeometry(100, 300, 100, 30)
        self.streamingUrlLabel.setText("STREAM URL")

        self.streamingUrlEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.streamingUrlEdit.setGeometry(200, 300, 710, 30)

        self.videoLabel = QtWidgets.QLabel(self.centralWidget)
        self.videoLabel.setGeometry(100, 350, 100, 30)
        self.videoLabel.setText("VIDEO")

        self.vlc = vlc.Instance()
        self.player = self.vlc.media_player_new()
        self.media = None
        # self.media = self.vlc.media_new("BTSDynamiteMV.mp4")
        # self.player.set_media(self.media)
        self.vlcWidget = QtWidgets.QFrame(self.centralWidget)
        self.vlcWidget.setGeometry(200, 350, 710, 400)

        self.player.set_nsobject(int(self.vlcWidget.winId()))
        # self.player.play()

        self.mainWindow.show()

    def clickEvent(self):
        try:
            info = pafy.new(self.urlEdit.text())
            self.authorEdit.setText(info.author)
            self.titleEdit.setText(info.title)
            self.viewEdit.setText(str(info.viewcount))
            self.streamingUrlEdit.setText(info.getbest().url)

            thumb = urllib.request.urlopen(info.bigthumb).read()
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(thumb)
            self.thumbLabel.setPixmap(pixmap)

            # 1.media로 영상재생컨텐츠 설정하는 법
            # self.media = self.vlc.media_new(info.getbest().url)
            # self.player.set_media(self.media)

            # 2.mrl로 영상재생컨텐츠 설정하는 법
            self.player.set_mrl(info.getbest().url)

            self.player.play()
            time.sleep(2)

            self.vlcWidget.show()
        except:
            self.authorEdit.setText("실패")

    def volume50BtnEvent(self):
        self.player.audio_set_volume(50)
        print(self.player.audio_get_volume())

    def volume20BtnEvent(self):
        self.player.audio_set_volume(20)
        print(self.player.audio_get_volume())

    def volume100BtnEvent(self):
        self.player.audio_set_volume(100)
        print(self.player.audio_get_volume())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui()

    sys.exit(app.exec_())

