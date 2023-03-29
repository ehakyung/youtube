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


            self.media = self.vlc.media_new(info.getbest().url)
            self.player.set_media(self.media)
            self.player.play()
            time.sleep(2)

            self.vlcWidget.show()
        except:
            self.authorEdit.setText("실패")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui()

    sys.exit(app.exec_())

