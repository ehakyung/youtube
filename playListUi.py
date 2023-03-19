from ctypes.wintypes import RGB
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Ui:
    def __init__(self):
        # super().__init__()
#=====================================================================================[ STYLE ]

        #font 크기를 vw vh로 설정하는 법 생각해보기
        self.font12 = QtGui.QFont("Inter", 12)
        self.font14 = QtGui.QFont("Inter", 14)
        self.font16 = QtGui.QFont("Inter", 16)
        self.font20 = QtGui.QFont("Inter", 20)
        self.font24 = QtGui.QFont("Inter", 24)

        self.fontWhite = "color: white;"
        self.fontBlue = "color: rgba(135, 162, 233, 1);"
        self.fontBlack = "color: rgba(17, 17, 17, 1);"

        self.fontSemibold = "font-weight: 500;"
        self.fontBold = "font-weight: 700;"

        self.backgroundGray = "background-color: rgba(255, 255, 255, 0.20);"
        self.backgroundBlack= "background-color: rgba(17, 17, 17, 1);"
        self.backgroundBlue = "background-color: rgba(135, 162, 233, 1);"
        self.backgroundTransparent = "background-color: transparent;"

        self.borderStyle = "border: 1px solid rgba(255, 255, 255, 0.14);"
        self.borderNone = "border: 0px;"

        self.radius15 = "border-radius: 15px;"
        self.radius20 = "border-radius: 20px;"
        self.leftRadius20 = "border-top-left-radius: 20px;" + "border-bottom-left-radius: 20px;"
        self.rightRadius20 = "border-top-right-radius: 20px;" + "border-bottom-right-radius: 20px;"

        self.padding = "padding-left: 10px;" + "padding-right: 10px;"

        self.alignRight=QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
        self.alignCenter = QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter

        self.leftLabelStyle = self.backgroundGray + self.borderStyle + self.leftRadius20 + self.fontWhite 
        self.rightLabelStyle = self.backgroundGray + self.borderStyle + self.rightRadius20 + self.fontWhite 
        self.leftEditStyle = self.backgroundBlack + self.borderStyle + self.leftRadius20 + self.fontBlue + self.padding
        self.rightEditStyle = self.backgroundBlack + self.borderStyle + self.rightRadius20 + self.fontBlue + self.padding
        self.btnStyle = self.backgroundGray + self.borderStyle + self.leftRadius20 + self.rightRadius20 + self.fontWhite

#=====================================================================================[ UI ]

        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1200, 900)

        self.centralWidget = QtWidgets.QWidget()
        # self.centralWidget.setStyleSheet(self.pageEditMainColor)
        self.mainWindow.setCentralWidget(self.centralWidget)

        self.screen = QtWidgets.QStackedWidget(self.centralWidget)
        self.screen.setGeometry(0, 0, 1200, 900)

        # 0: 로그인 페이지 / 1: 아이디찾기 페이지 / 2: 비밀번호찾기 페이지 / 3: 회원가입 페이지 / 4: 메인 페이지 / 5: 프로필 페이지 / 6: 동영상 페이지
        self.pagesOfScreen = []
        for index in range (0, 7):
            tmpPage = QtWidgets.QWidget()
            tmpPage.setStyleSheet(self.backgroundBlack)

            self.screen.addWidget(tmpPage)
            self.pagesOfScreen.append(tmpPage)

        self.screen.setCurrentIndex(6)

        # Back Button(아이디찾기 페이지, 비밀번호찾기 페이지, 회원가입 페이지)
        # self.backBtns = []
        for index in range (1, 4):
            tmpBtn = QtWidgets.QPushButton(self.pagesOfScreen[index])
            tmpBtn.setGeometry(40, 28, 24, 24)
            tmpBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/backBtn.png)")

        # Button(프로필 페이지, 동영상 페이지)
        # self.homeBtns = []
        for index in range (5, 7):
            tmpBtn = QtWidgets.QPushButton(self.pagesOfScreen[index])
            tmpBtn.setGeometry(20, 20, 40, 40)
            tmpBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/homeBtn.png)")

#=====================================================================================[ UI ]
#-------------------------------------------------------------------------------------[ 로그인 페이지 ]

        # Label(아이디와 비밀번호가 일치하지 않습니다)
        self.loginPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[0])
        self.loginPageNoticeLabel.setGeometry(420, 297, 360, 20)
        self.loginPageNoticeLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite)
        self.loginPageNoticeLabel.setFont(self.font16)
        self.loginPageNoticeLabel.setText("아이디와 비밀번호가 일치하지 않습니다")
        self.loginPageNoticeLabel.setAlignment(self.alignCenter)

        #  Label(ID, PW)
        self.loginPagelabels = []
        self.nameOfLoginPageLabels = ["ID", "PW"]
        for index in range (0, 2):
            tmpLabel = QtWidgets.QLabel(self.pagesOfScreen[0])
            tmpLabel.setGeometry(420, 346+(index*60), 60, 40)
            tmpLabel.setStyleSheet(self.leftLabelStyle)
            tmpLabel.setFont(self.font14)
            tmpLabel.setAlignment(self.alignCenter)
            tmpLabel.setText(self.nameOfLoginPageLabels[index])
            self.loginPagelabels.append(tmpLabel)

        # Edit(ID, PW)
        self.loginPageEdits = []
        for index in range (0, 2):
            tmpEdit = QtWidgets.QLineEdit(self.pagesOfScreen[0])
            tmpEdit.setGeometry(480, 346+(index*60), 300, 40)
            tmpEdit.setStyleSheet(self.rightEditStyle)
            tmpEdit.setFont(self.font16)
            self.loginPageEdits.append(tmpEdit)

        self.loginPageEdits[1].setEchoMode(QtWidgets.QLineEdit.Password)

        # Button(Login)
        self.loginPageLoginBtn = QtWidgets.QPushButton(self.pagesOfScreen[0])
        self.loginPageLoginBtn.setGeometry(540, 466, 120, 40)
        self.loginPageLoginBtn.setStyleSheet(self.btnStyle)
        self.loginPageLoginBtn.setFont(self.font16)
        self.loginPageLoginBtn.setText("Login")

        # Button(아이디 찾기, 비밀번호 찾기, 회원가입)
        self.loginPagebtns = []
        self.nameOfLoginPageBtns = ["아이디 찾기", "비밀번호 찾기", "회원가입"]
        for index in range (0, 3):
            tmpBtn = QtWidgets.QPushButton(self.pagesOfScreen[0])
            tmpBtn.setGeometry(445+(index*110), 533, 90, 20)
            tmpBtn.setStyleSheet(self.backgroundTransparent + self.borderNone + self.fontWhite)
            tmpBtn.setFont(self.font14)
            tmpBtn.setText(self.nameOfLoginPageBtns[index])
            self.loginPagebtns.append(tmpBtn)

#-------------------------------------------------------------------------------------[ 아이디찾기 페이지 ]

        # Label(가입시 입력한 메일주소를 입력하세요)
        self.findIdPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[1])
        self.findIdPageNoticeLabel.setGeometry(420, 390, 360, 20)
        self.findIdPageNoticeLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite)
        self.findIdPageNoticeLabel.setFont(self.font16)
        self.findIdPageNoticeLabel.setText("가입시 입력한 메일주소를 입력하세요")
        self.findIdPageNoticeLabel.setAlignment(self.alignCenter)

        # Label(MAIL)
        self.findIdPageLabel = QtWidgets.QLabel(self.pagesOfScreen[1])
        self.findIdPageLabel.setGeometry(420, 430, 60, 40)
        self.findIdPageLabel.setStyleSheet(self.leftLabelStyle)
        self.findIdPageLabel.setFont(self.font14)
        self.findIdPageLabel.setAlignment(self.alignCenter)
        self.findIdPageLabel.setText("MAIL")

        # Edit(MAIL)
        self.findIdPageEdit = QtWidgets.QLineEdit(self.pagesOfScreen[1])
        self.findIdPageEdit.setGeometry(480, 430, 300, 40)
        self.findIdPageEdit.setStyleSheet(self.rightEditStyle)
        self.findIdPageEdit.setFont(self.font16)
        
        # Button(Find)
        self.findIdPageFindBtn = QtWidgets.QPushButton(self.pagesOfScreen[1])
        self.findIdPageFindBtn.setGeometry(540, 490, 120, 40)
        self.findIdPageFindBtn.setStyleSheet(self.btnStyle)
        self.findIdPageFindBtn.setFont(self.font16)
        self.findIdPageFindBtn.setText("Find")

#-------------------------------------------------------------------------------------[ 비밀번호찾기 페이지 ]

        # Label(가입시 입력한 아이디와 메일주소를 입력하세요)
        self.findPwPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[2])
        self.findPwPageNoticeLabel.setGeometry(420, 380, 360, 20)
        self.findPwPageNoticeLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite)
        self.findPwPageNoticeLabel.setFont(self.font16)
        self.findPwPageNoticeLabel.setText("가입시 입력한 아이디와 메일주소를 입력하세요")
        self.findPwPageNoticeLabel.setAlignment(self.alignCenter)

        #  Label(ID, MAIL)
        self.findPwPageLabels = []
        self.nameOfFindPwPageLabels = ["ID", "MAIL"]
        for index in range (0, 2):
            tmpLabel = QtWidgets.QLabel(self.pagesOfScreen[2])
            tmpLabel.setGeometry(420, 420+(index*60), 60, 40)
            tmpLabel.setStyleSheet(self.leftLabelStyle)
            tmpLabel.setFont(self.font14)
            tmpLabel.setAlignment(self.alignCenter)
            tmpLabel.setText(self.nameOfFindPwPageLabels[index])
            self.findPwPageLabels.append(tmpLabel)

        # Edit(ID, MAIL)
        self.findPwPageEdits = []
        for index in range (0, 2):
            tmpEdit = QtWidgets.QLineEdit(self.pagesOfScreen[2])
            tmpEdit.setGeometry(480, 420+(index*60), 300, 40)
            tmpEdit.setStyleSheet(self.rightEditStyle)
            tmpEdit.setFont(self.font16)
            self.findPwPageEdits.append(tmpEdit)

        # Button(Find)
        self.findPwPageFindBtn = QtWidgets.QPushButton(self.pagesOfScreen[2])
        self.findPwPageFindBtn.setGeometry(540, 540, 120, 40)
        self.findPwPageFindBtn.setStyleSheet(self.btnStyle)
        self.findPwPageFindBtn.setFont(self.font16)
        self.findPwPageFindBtn.setText("Find")

#-------------------------------------------------------------------------------------[ 회원가입 페이지 ]

        # Label(이미 사용 중인 아이디입니다)
        self.joinPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[3])
        self.joinPageNoticeLabel.setGeometry(420, 294, 360, 20)
        self.joinPageNoticeLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite)
        self.joinPageNoticeLabel.setFont(self.font16)
        self.joinPageNoticeLabel.setText("이미 사용 중인 아이디입니다")
        self.joinPageNoticeLabel.setAlignment(self.alignCenter)

        #  Label(NAME, ID, PW, PHONE, MAIL)
        self.myInfoPageLabels = []
        self.nameOfMyInfoPageLabels = ["NAME", "ID", "PW", "PHONE", "MAIL"]
        for index in range (0, 5):
            tmpLabel = QtWidgets.QLabel(self.pagesOfScreen[3])
            tmpLabel.setGeometry(420, 334+(index*60), 60, 40)
            tmpLabel.setStyleSheet(self.leftLabelStyle)
            tmpLabel.setFont(self.font14)
            tmpLabel.setAlignment(self.alignCenter)
            tmpLabel.setText(self.nameOfMyInfoPageLabels[index])
            self.myInfoPageLabels.append(tmpLabel)

        # Edit(NAME, ID, PW, PHONE, MAIL)
        self.joinPageEdits = []
        for index in range (0, 5):
            tmpEdit = QtWidgets.QLineEdit(self.pagesOfScreen[3])
            tmpEdit.setGeometry(480, 334+(index*60), 300, 40)
            tmpEdit.setStyleSheet(self.rightEditStyle)
            tmpEdit.setFont(self.font16)
            self.joinPageEdits.append(tmpEdit)

        self.joinPageEdits[2].setEchoMode(QtWidgets.QLineEdit.Password)

        # Button(Join)
        self.joinPageJoinBtn = QtWidgets.QPushButton(self.pagesOfScreen[3])
        self.joinPageJoinBtn.setGeometry(540, 634, 120, 40)
        self.joinPageJoinBtn.setStyleSheet(self.btnStyle)
        self.joinPageJoinBtn.setFont(self.font16)
        self.joinPageJoinBtn.setText("Join")

#-------------------------------------------------------------------------------------[ 메인 페이지 ]

        # Profile Button
        # self.mainPageProfileBtn = QtWidgets.QPushButton(self.pagesOfScreen[4])
        # self.mainPageProfileBtn.setGeometry(20, 20, 40, 40)
        # self.mainPageProfileBtn.setStyleSheet(
        #     "background-image: url(/Users/ehakyung/Desktop/Youtube/image/profileBtn.png);" +
        #     self.fontBlack +
        #     self.fontSemibold)
        # self.mainPageProfileBtn.setFont(self.font16)
        # self.mainPageProfileBtn.setText("하경")

        # Profile Button
        self.mainPageProfileBtn = QtWidgets.QPushButton(self.pagesOfScreen[4])
        self.mainPageProfileBtn.setGeometry(20, 20, 40, 40)
        self.mainPageProfileBtn.setStyleSheet(
            "background-color: white;" +
            self.fontBlack +
            self.fontSemibold +
            "border-radius: 20px;")
        self.mainPageProfileBtn.setFont(self.font16)
        self.mainPageProfileBtn.setText("하경")
        

        # Logout Button
        self.mainPageLogoutBtn = QtWidgets.QPushButton(self.pagesOfScreen[4])
        self.mainPageLogoutBtn.setGeometry(80, 20, 40, 40)
        self.mainPageLogoutBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/logoutBtn.png);")

        # Add Playlist Button
        self.mainPageAddPlaylistBtn = QtWidgets.QPushButton(self.pagesOfScreen[4])
        self.mainPageAddPlaylistBtn.setGeometry(1035, 20, 40, 40)
        self.mainPageAddPlaylistBtn.setStyleSheet(
            "background-image: url(/Users/ehakyung/Desktop/Youtube/image/addPlaylistBtn.png);" +
            "background-repeat: no-repeat;")
        
        # Label(재생목록 추가)
        self.mainPageAddPlaylistLabel = QtWidgets.QLabel(self.pagesOfScreen[4])
        self.mainPageAddPlaylistLabel.setGeometry(1085, 30, 100, 20)
        self.mainPageAddPlaylistLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite)
        self.mainPageAddPlaylistLabel.setFont(self.font16)
        self.mainPageAddPlaylistLabel.setText("재생목록 추가")

        # Playlist Button
        self.mainPagePlaylistBtn = QtWidgets.QPushButton(self.pagesOfScreen[4])
        self.mainPagePlaylistBtn.setGeometry(68, 120, 254, 142)
        self.mainPagePlaylistBtn.setStyleSheet(
            self.backgroundGray +
            self.radius15 + 
            "background-image: url(/Users/ehakyung/Desktop/Youtube/image/emptyPlaylistBtn.png);" +
            "background-repeat: no-repeat;" +
            "background-position: center;")


        self.mainPagePlaylistBtn2 = QtWidgets.QPushButton(self.pagesOfScreen[4])
        self.mainPagePlaylistBtn2.setGeometry(338, 120, 254, 142)
        self.mainPagePlaylistBtn2.setIcon(QtGui.QIcon("/Users/ehakyung/homework9/image/thumbnail/thumb_1.webp"))
        self.mainPagePlaylistBtn2.setIconSize(QtCore.QSize(254, 142))


        # Playlist Name Label
        self.mainPagePlaylistNameLabel = QtWidgets.QLabel(self.pagesOfScreen[4])
        self.mainPagePlaylistNameLabel.setGeometry(68, 272, 234, 20)
        self.mainPagePlaylistNameLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite + self.fontBold)
        self.mainPagePlaylistNameLabel.setFont(self.font16)
        self.mainPagePlaylistNameLabel.setText("봄 느낌 팝송")

        # Delete Playlist Button
        self.mainPageDeletePlaylistBtn = QtWidgets.QPushButton(self.pagesOfScreen[4])
        self.mainPageDeletePlaylistBtn.setGeometry(302, 272, 20, 20)
        self.mainPageDeletePlaylistBtn.setStyleSheet( 
            "background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png);" +
            "background-repeat: no-repeat;" +
            "background-position: center;")

#-------------------------------------------------------------------------------------[ 프로필 페이지 ]

        # Widget
        self.profilePageSectionWidget = QtWidgets.QWidget(self.pagesOfScreen[5])
        self.profilePageSectionWidget.setGeometry(200, 200, 800, 500)
        self.profilePageSectionWidget.setStyleSheet(self.backgroundGray + self.radius20)

        # Label(NAME, ID, 가입일, PHONE, MAIL, 재생목록수)
        self.myInfoPageLabels = []
        self.nameOfMyInfoPageLabels = ["NAME", "ID", "가입일", "PHONE", "MAIL", "재생목록수"]
        for index in range (0, 6):
            tmpLabel1 = QtWidgets.QLabel(self.pagesOfScreen[5])
            tmpLabel1.setGeometry(278, 290+(index*60), 80, 20)
            tmpLabel1.setStyleSheet(self.backgroundTransparent + self.fontWhite)
            tmpLabel1.setFont(self.font16)
            tmpLabel1.setAlignment(self.alignRight)
            tmpLabel1.setText(self.nameOfMyInfoPageLabels[index])
            self.myInfoPageLabels.append(tmpLabel1)

            tmpLabel2 = QtWidgets.QLabel(self.pagesOfScreen[5])
            tmpLabel2.setGeometry(388, 290+(index*60), 400, 20)
            tmpLabel2.setStyleSheet(self.backgroundTransparent + self.fontBlue)
            tmpLabel2.setFont(self.font16)
            tmpLabel2.setText(self.nameOfMyInfoPageLabels[index])

#-------------------------------------------------------------------------------------[ 동영상 페이지 ]

        # Widget
        self.videoPageSectionWidget = QtWidgets.QWidget(self.pagesOfScreen[6])
        self.videoPageSectionWidget.setGeometry(0, 80, 750, 820)
        self.videoPageSectionWidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.977273, x2:0.0199005, y2:0.0227273, stop:0 rgba(17, 17, 17, 1), stop:1 rgba(255, 255, 255, 255));")
#-------------------------------------------------------------------------------------[  ]
#-------------------------------------------------------------------------------------[  ]
#-------------------------------------------------------------------------------------[  ]
#-------------------------------------------------------------------------------------[  ]
#-------------------------------------------------------------------------------------[  ]
#-------------------------------------------------------------------------------------[  ]
#=====================================================================================[  ]

        self.mainWindow.show()

if __name__=="__main__":

    
    app=QtWidgets.QApplication(sys.argv)

    ui=Ui()
    
    sys.exit(app.exec_())