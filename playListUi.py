import sys, account, database, urllib.request
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
        self.backgroundWhite = "background-color: white;"

        self.borderLightGray = "border: 1px solid rgba(255, 255, 255, 0.14);"
        self.borderNone = "border: 0px;"

        self.radius10 = "border-radius: 10px;"
        self.radius15 = "border-radius: 15px;"
        self.radius20 = "border-radius: 20px;"
        self.leftRadius20 = "border-top-left-radius: 20px;" + "border-bottom-left-radius: 20px;"
        self.rightRadius20 = "border-top-right-radius: 20px;" + "border-bottom-right-radius: 20px;"

        self.padding10 = "padding-left: 10px;" + "padding-right: 10px;"

        self.alignLeft=QtCore.Qt.AlignLeft
        self.alignRight=QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
        self.alignCenter = QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter

        self.leftLabelStyle = self.backgroundGray + self.borderLightGray + self.leftRadius20 + self.fontWhite 
        self.rightLabelStyle = self.backgroundGray + self.borderLightGray + self.rightRadius20 + self.fontWhite 
        self.transparentLabelStyle = self.backgroundTransparent + self.fontWhite
        self.videoPagePlayOptionLabelStyle = self.backgroundGray + self.radius10

        self.leftEditStyle = self.backgroundBlack + self.borderLightGray + self.leftRadius20 + self.fontBlue + self.padding10
        self.rightEditStyle = self.backgroundBlack + self.borderLightGray + self.rightRadius20 + self.fontBlue + self.padding10
        self.profilePageEditStyle = self.backgroundTransparent + self.borderNone + self.fontBlue

        self.btnStyle = self.backgroundGray + self.borderLightGray + self.leftRadius20 + self.rightRadius20 + self.fontWhite
        self.btnEnteredStyle = self.backgroundBlue + self.borderLightGray + self.leftRadius20 + self.rightRadius20 + self.fontWhite
        self.rightBtnStyle = self.backgroundGray + self.borderLightGray + self.rightRadius20 + self.fontWhite
        self.rightBtnEnteredStyle = self.backgroundBlue + self.borderLightGray + self.rightRadius20 + self.fontWhite
        self.transparentBtnStyle = self.backgroundTransparent + self.borderNone + self.fontWhite
        self.profileBtnStyle = self.backgroundWhite + self.fontBlack + self.fontSemibold + self.radius20
        self.profileBtnEnteredStyle = self.backgroundBlue + self.fontBlack + self.fontSemibold + self.radius20

        self.emptyPlaylistBtnStyle = self.backgroundGray + self.radius15 + "background-image: url(/Users/ehakyung/Desktop/Youtube/image/emptyPlaylistBtn.png);" + "background-repeat: no-repeat;" + "background-position: center;"
        
        self.logoutSetting()

#=====================================================================================[ UI ]

        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1200, 900)

        self.centralWidget = QtWidgets.QWidget()
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

        self.screen.setCurrentIndex(0)

        # Back Button(아이디찾기 페이지, 비밀번호찾기 페이지, 회원가입 페이지)
        self.backBtns = []
        for index in range (1, 4):
            tmpBtn = QtWidgets.QPushButton(self.pagesOfScreen[index])
            tmpBtn.setGeometry(40, 28, 24, 24)
            tmpBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/backBtn.png)")
            self.backBtns.append(tmpBtn)

        # Button(프로필 페이지, 동영상 페이지)
        self.homeBtns = []
        for index in range (5, 7):
            tmpBtn = QtWidgets.QPushButton(self.pagesOfScreen[index])
            tmpBtn.setGeometry(20, 20, 40, 40)
            tmpBtn.setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/homeBtn.png)")
            self.homeBtns.append(tmpBtn)

#-------------------------------------------------------------------------------------[ 로그인 페이지 ]

        # Notice Label
        self.loginPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[0])
        self.loginPageNoticeLabel.setGeometry(420, 297, 360, 20)
        self.loginPageNoticeLabel.setStyleSheet(self.transparentLabelStyle)
        self.loginPageNoticeLabel.setFont(self.font16)
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
        self.loginPageBtns = []
        self.nameOfLoginPageBtns = ["아이디 찾기", "비밀번호 찾기", "회원가입"]
        for index in range (0, 3):
            tmpBtn = QtWidgets.QPushButton(self.pagesOfScreen[0])
            tmpBtn.setGeometry(445+(index*110), 533, 90, 20)
            tmpBtn.setStyleSheet(self.transparentBtnStyle)
            tmpBtn.setFont(self.font14)
            tmpBtn.setText(self.nameOfLoginPageBtns[index])
            self.loginPageBtns.append(tmpBtn)

#-------------------------------------------------------------------------------------[ 아이디찾기 페이지 ]

        # Notice Label
        self.findIdPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[1])
        self.findIdPageNoticeLabel.setGeometry(420, 390, 360, 20)
        self.findIdPageNoticeLabel.setStyleSheet(self.transparentLabelStyle)
        self.findIdPageNoticeLabel.setFont(self.font16)
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

        # Notice Label
        self.findPwPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[2])
        self.findPwPageNoticeLabel.setGeometry(420, 380, 360, 20)
        self.findPwPageNoticeLabel.setStyleSheet(self.transparentLabelStyle)
        self.findPwPageNoticeLabel.setFont(self.font16)
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

        # Notice Label
        self.joinPageNoticeLabel = QtWidgets.QLabel(self.pagesOfScreen[3])
        self.joinPageNoticeLabel.setGeometry(420, 294, 360, 20)
        self.joinPageNoticeLabel.setStyleSheet(self.transparentLabelStyle)
        self.joinPageNoticeLabel.setFont(self.font16)
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
        self.hintForJoinPageEdits = ["공백 포함 10자 이내", "문자(특수문자 불가), 숫자 사용 4~20자", "문자(특수문자 가능), 숫자 사용 8~20자", "예: 01X-XXX(또는 XXXX)-XXXX", "예: id@domain.com"]
        for index in range (0, 5):
            tmpEdit = QtWidgets.QLineEdit(self.pagesOfScreen[3])
            tmpEdit.setGeometry(480, 334+(index*60), 300, 40)
            tmpEdit.setStyleSheet(self.rightEditStyle)
            tmpEdit.setFont(self.font16)
            tmpEdit.setPlaceholderText(self.hintForJoinPageEdits[index])
            self.joinPageEdits.append(tmpEdit)

        self.joinPageEdits[2].setEchoMode(QtWidgets.QLineEdit.Password)

        # Button(Join)
        self.joinPageJoinBtn = QtWidgets.QPushButton(self.pagesOfScreen[3])
        self.joinPageJoinBtn.setGeometry(540, 634, 120, 40)
        self.joinPageJoinBtn.setStyleSheet(self.btnStyle)
        self.joinPageJoinBtn.setFont(self.font16)
        self.joinPageJoinBtn.setText("Join")

#-------------------------------------------------------------------------------------[ 메인 페이지 ]

        self.mainPageWidgetForScoll=QtWidgets.QWidget(self.pagesOfScreen[4])

        self.mainPageEmptyLabel = QtWidgets.QLabel(self.mainPageWidgetForScoll)
        self.mainPageEmptyLabel.setGeometry(420, 320, 360, 20)
        self.mainPageEmptyLabel.setStyleSheet(self.transparentLabelStyle)
        self.mainPageEmptyLabel.setFont(self.font16)
        self.mainPageEmptyLabel.setText("재생목록이 없습니다")
        self.mainPageEmptyLabel.setAlignment(self.alignCenter)

        # Profile Button
        self.mainPageProfileBtn = QtWidgets.QPushButton(self.pagesOfScreen[4])
        self.mainPageProfileBtn.setGeometry(20, 20, 40, 40)
        self.mainPageProfileBtn.setStyleSheet(self.profileBtnStyle)
        self.mainPageProfileBtn.setFont(self.font16)
        
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
        self.mainPageAddPlaylistLabel.setStyleSheet(self.transparentLabelStyle)
        self.mainPageAddPlaylistLabel.setFont(self.font16)
        self.mainPageAddPlaylistLabel.setText("재생목록 추가")

#-------------------------------------------------------------------------------------[ 프로필 페이지 ]

        # Widget
        self.profilePageBoxWidget = QtWidgets.QWidget(self.pagesOfScreen[5])
        self.profilePageBoxWidget.setGeometry(200, 200, 800, 500)
        self.profilePageBoxWidget.setStyleSheet(self.backgroundGray + self.radius20)

        # Label(NAME, ID, 가입일, PHONE, MAIL, 재생목록수)
        self.myInfoPageLabels = []
        self.myInfoPageEdits = []
        self.nameOfMyInfoPageLabels = ["NAME", "ID", "가입일", "PHONE", "MAIL", "재생목록수"]
        for index in range (0, 6):
            tmpLabel = QtWidgets.QLabel(self.pagesOfScreen[5])
            tmpLabel.setGeometry(278, 290+(index*60), 80, 20)
            tmpLabel.setStyleSheet(self.transparentLabelStyle)
            tmpLabel.setFont(self.font16)
            tmpLabel.setAlignment(self.alignRight)
            tmpLabel.setText(self.nameOfMyInfoPageLabels[index])
            self.myInfoPageLabels.append(tmpLabel)

            tmpEdit = QtWidgets.QLineEdit(self.pagesOfScreen[5])
            tmpEdit.setGeometry(388, 290+(index*60), 400, 20)
            tmpEdit.setStyleSheet(self.profilePageEditStyle)
            tmpEdit.setFont(self.font16)
            tmpEdit.setText(self.nameOfMyInfoPageLabels[index])
            tmpEdit.setEnabled(False)
            self.myInfoPageEdits.append(tmpEdit)

#-------------------------------------------------------------------------------------[ 동영상 페이지 ]
        
        self.videoPageWidgetForScoll=QtWidgets.QWidget(self.pagesOfScreen[6])
        self.videoPageWidgetForScoll.setGeometry(760, 80, 423, 2000)

        self.videoPageScrollArea=QtWidgets.QScrollArea(self.pagesOfScreen[6])
        self.videoPageScrollArea.setGeometry(760, 80, 440, 900)
        self.videoPageScrollArea.setWidget(self.videoPageWidgetForScoll)

        # Widget
        self.videoPageCurrentVideoSectionWidget = QtWidgets.QWidget(self.pagesOfScreen[6])
        self.videoPageCurrentVideoSectionWidget.setGeometry(0, 80, 750, 820)
        self.videoPageCurrentVideoSectionWidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.977273, x2:0.0199005, y2:0.0227273, stop:0 rgba(17, 17, 17, 1), stop:1 rgba(255, 255, 255, 15));")

        # Edit(url 입력창)
        self.videoPageUrlEdit = QtWidgets.QLineEdit(self.pagesOfScreen[6])
        self.videoPageUrlEdit.setGeometry(100, 20, 900, 40)
        self.videoPageUrlEdit.setStyleSheet(self.leftEditStyle)
        self.videoPageUrlEdit.setFont(self.font16)

        # Button(Add)
        self.videoPageAddUrlBtn = QtWidgets.QPushButton(self.pagesOfScreen[6])
        self.videoPageAddUrlBtn.setGeometry(1000, 20, 100, 40)
        self.videoPageAddUrlBtn.setStyleSheet(self.rightBtnStyle)
        self.videoPageAddUrlBtn.setText("Add")
        self.videoPageAddUrlBtn.setFont(self.font16)

        # Notice Label
        self.videoPageEmptyLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        self.videoPageEmptyLabel.setGeometry(195,390, 360, 20)
        self.videoPageEmptyLabel.setStyleSheet(self.transparentLabelStyle)
        self.videoPageEmptyLabel.setFont(self.font16)
        self.videoPageEmptyLabel.setText("재생 중인 영상이 없습니다")
        self.videoPageEmptyLabel.setAlignment(self.alignCenter)

        # Label(재생목록 아이콘)
        self.videoPagePlaylistIconLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        self.videoPagePlaylistIconLabel.setGeometry(20, 120, 40, 40)
        self.videoPagePlaylistIconLabel.setPixmap(QtGui.QPixmap("/Users/ehakyung/Desktop/Youtube/image/addPlaylistBtn.png"))
        self.videoPagePlaylistIconLabel.setAlignment(self.alignCenter)
#------------------>
        # Label(재생목록명)
        self.videoPagePlaylistNameLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        self.videoPagePlaylistNameLabel.setGeometry(83, 124, 400, 30)
        self.videoPagePlaylistNameLabel.setStyleSheet(self.transparentLabelStyle + self.fontSemibold)
        self.videoPagePlaylistNameLabel.setFont(self.font24)

        # Label(재생중인 영상)
        # self.videoPagePlaylistCurrentVideoLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        # self.videoPagePlaylistCurrentVideoLabel.setGeometry(20, 200, 710, 400)
        # self.videoPagePlaylistCurrentVideoLabel.setPixmap(QtGui.QPixmap("/Users/ehakyung/homework9/image/thumbnail/thumb_1.webp"))

        # Label(재생옵션버튼 상자)
        self.videoPagePlayOptionLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        self.videoPagePlayOptionLabel.setGeometry(20, 620, 110, 34)
        self.videoPagePlayOptionLabel.setStyleSheet(self.videoPagePlayOptionLabelStyle)

        # Option Button
        self.videoPagePlayOptionBtns = []
        self.iconOfVideoPagePlayOptionBtns = ["background-image: url(/Users/ehakyung/Desktop/Youtube/image/playBtn.png);", "background-image: url(/Users/ehakyung/Desktop/Youtube/image/pauseBtn.png);", "background-image: url(/Users/ehakyung/Desktop/Youtube/image/stopBtn.png);"]
        for index in range (0, 3):
            tmpBtn = QtWidgets.QPushButton(self.pagesOfScreen[6])
            if index==2:
                tmpBtn.setGeometry(100, 628, 20, 22)
            else:    
                tmpBtn.setGeometry(32.5+(index*32.5), 627, 20, 22)
            tmpBtn.setStyleSheet(self.iconOfVideoPagePlayOptionBtns[index] + self.backgroundTransparent + "background-repeat: no-repeat;")
            self.videoPagePlayOptionBtns.append(tmpBtn)

        # # Label(재생 중인 영상 제목)
        self.videoPageCurrentVideoNameLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        self.videoPageCurrentVideoNameLabel.setGeometry(20, 670, 710, 63)
        self.videoPageCurrentVideoNameLabel.setStyleSheet(self.transparentLabelStyle + self.fontSemibold)
        self.videoPageCurrentVideoNameLabel.setFont(self.font20)
        self.videoPageCurrentVideoNameLabel.setAlignment(self.alignLeft)
        self.videoPageCurrentVideoNameLabel.setWordWrap(True)

        # # Label(재생 중인 영상 채널명)
        self.videoPageCurrentVideoChannelLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        self.videoPageCurrentVideoChannelLabel.setGeometry(20, 735, 700, 30)
        self.videoPageCurrentVideoChannelLabel.setStyleSheet(self.transparentLabelStyle)
        self.videoPageCurrentVideoChannelLabel.setFont(self.font16)

        # # Label(재생 중인 영상 조회수)
        self.videoPageCurrentVideoViewLabel = QtWidgets.QLabel(self.pagesOfScreen[6])
        self.videoPageCurrentVideoViewLabel.setGeometry(20, 765, 700, 30)
        self.videoPageCurrentVideoViewLabel.setStyleSheet(self.transparentLabelStyle)
        self.videoPageCurrentVideoViewLabel.setFont(self.font16)

        # # Videolist Button
        # self.videoPageVideolistBtn = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
        # self.videoPageVideolistBtn.setGeometry(0, 0, 168, 94)
        # self.videoPageVideolistBtn.setStyleSheet(self.radius10)
        # self.videolistThumbnailPixmap=QtGui.QPixmap("/Users/ehakyung/homework9/image/thumbnail/thumb_1.webp")
        # self.videolistThumbnailPixmap.scaled(168, 94)
        # self.videolistThumbnailIcon=QtGui.QIcon()
        # self.videolistThumbnailIcon.addPixmap(self.videolistThumbnailPixmap)
        # self.videoPageVideolistBtn.setIcon(self.videolistThumbnailIcon)
        # self.videoPageVideolistBtn.setIconSize(QtCore.QSize(168, 94))

        # # Label(영상목록 제목)
        # self.videoPageVideolistNameLabel = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        # self.videoPageVideolistNameLabel.setGeometry(170, 3, 220, 42)
        # self.videoPageVideolistNameLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite + self.fontSemibold)
        # self.videoPageVideolistNameLabel.setFont(self.font14)
        # self.videoPageVideolistNameLabel.setAlignment(self.alignLeft)
        # self.videoPageVideolistNameLabel.setWordWrap(True)
        # self.videoPageVideolistNameLabel.setText("Playlist 따사로운 봄을 기다리며 spring pop 🌱🌼")

        # # Label(영상목록 채널명)
        # self.videoPageVideolistChannelLabel = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        # self.videoPageVideolistChannelLabel.setGeometry(170, 50, 220, 15)
        # self.videoPageVideolistChannelLabel.setStyleSheet(self.transparentLabelStyle)
        # self.videoPageVideolistChannelLabel.setFont(self.font12)
        # self.videoPageVideolistChannelLabel.setText("때껄룩 TAKE A LOOK")

        # # Label(영상목록 조회수)
        # self.videoPageVideolistViewLabel = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        # self.videoPageVideolistViewLabel.setGeometry(170, 65, 220, 15)
        # self.videoPageVideolistViewLabel.setStyleSheet(self.transparentLabelStyle)
        # self.videoPageVideolistViewLabel.setFont(self.font12)
        # self.videoPageVideolistViewLabel.setText("조회수 68만")

        # # Delete Videolist Button
        # self.videoPageDeleteVideoBtn = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
        # self.videoPageDeleteVideoBtn.setGeometry(390, 3, 20, 20)
        # self.videoPageDeleteVideoBtn.setStyleSheet( 
        #     "background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png);" +
        #     "background-repeat: no-repeat;" +
        #     "background-position: center;")

#-------------------------------------------------------------------------------------[  ]
        self.mainWindow.show()
#=====================================================================================[ 위젯 생성/삭제/재배열 함수 ]

    def displayPlaylist(self):
        if len(database.playlistOfLoggedId) == 0:
            self.mainPageWidgetForScoll.setGeometry(0, 120, 1183, 770)
        elif len(database.playlistOfLoggedId) != 0:
            self.mainPageEmptyLabel.hide()
            self.mainPageWidgetForScoll.setGeometry(0, 120, 1183, (((len(database.playlistOfLoggedId)-1)//4)+1)*212)

        for index in range(0, len(database.playlistOfLoggedId)):
            tmpBtn1 = QtWidgets.QPushButton(self.mainPageWidgetForScoll)
            tmpBtn1.setGeometry(68+(index%4)*270, (index//4)*212, 254, 142)
            tmpBtn1.setStyleSheet(self.emptyPlaylistBtnStyle)
            tmpBtn1.setObjectName(str(database.playlistOfLoggedId[index][1]))
            self.mainPagePlaylistBtns.append(tmpBtn1)

            tmpLabel = QtWidgets.QLabel(self.mainPageWidgetForScoll)
            tmpLabel.setGeometry(68+(index%4)*270, 152+(index//4)*212, 234, 20)
            tmpLabel.setStyleSheet(self.transparentLabelStyle + self.fontBold)
            tmpLabel.setFont(self.font16)
            tmpLabel.setText(database.playlistOfLoggedId[index][0])
            self.mainPagePlaylistNameLabels.append(tmpLabel)

            tmpBtn2 = QtWidgets.QPushButton(self.mainPageWidgetForScoll)
            tmpBtn2.setGeometry(302+(index%4)*270, 152+(index//4)*212, 20, 20)
            tmpBtn2.setStyleSheet( 
            "background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png);" +
            "background-repeat: no-repeat;" +
            "background-position: center;" +
            "color: transparent;")
            tmpBtn2.setObjectName(str(database.playlistOfLoggedId[index][1]))
            self.mainPageDeletePlaylistBtns.append(tmpBtn2)

        self.mainPageScrollArea=QtWidgets.QScrollArea(self.pagesOfScreen[4])
        self.mainPageScrollArea.setGeometry(0, 120, 1200, 780)
        self.mainPageScrollArea.setWidget(self.mainPageWidgetForScoll)
        self.mainPageScrollArea.setWidgetResizable(False)

    def clearMainPage(self):
        for index in range(0, len(self.mainPagePlaylistBtns)):
            self.mainPagePlaylistBtns[index].deleteLater()
            self.mainPagePlaylistNameLabels[index].deleteLater()
            self.mainPageDeletePlaylistBtns[index].deleteLater()

    def addPlaylist(self):
        if self.indexOfNewPlaylistBtn < 12:  
            self.mainPageWidgetForScoll.setGeometry(0, 120, 1183, 770)
            self.mainPageScrollArea.setWidgetResizable(False)
        else:
            print(self.indexOfNewPlaylistBtn)
            self.mainPageWidgetForScoll.setGeometry(0, 120, 1183, ((self.indexOfNewPlaylistBtn//4)+1)*212)
            self.mainPageScrollArea.setWidgetResizable(False)

        tmpBtn1 = QtWidgets.QPushButton(self.mainPageWidgetForScoll)
        tmpBtn1.setGeometry(68+(self.indexOfNewPlaylistBtn%4)*270, (self.indexOfNewPlaylistBtn//4)*212, 254, 142)
        tmpBtn1.setStyleSheet(self.emptyPlaylistBtnStyle)
        tmpBtn1.setObjectName(str(self.indexOfNewList))
        self.mainPagePlaylistBtns.append(tmpBtn1)
        self.mainPagePlaylistBtns[self.indexOfNewPlaylistBtn].show()

        tmpLabel = QtWidgets.QLabel(self.mainPageWidgetForScoll)
        tmpLabel.setGeometry(68+(self.indexOfNewPlaylistBtn%4)*270, 152+(self.indexOfNewPlaylistBtn//4)*212, 234, 20)
        tmpLabel.setStyleSheet(self.transparentLabelStyle + self.fontBold)
        tmpLabel.setFont(self.font16)
        tmpLabel.setText(self.tmpPlaylistName)
        self.mainPagePlaylistNameLabels.append(tmpLabel)
        self.mainPagePlaylistNameLabels[self.indexOfNewPlaylistBtn].show()

        tmpBtn2 = QtWidgets.QPushButton(self.mainPageWidgetForScoll)
        tmpBtn2.setGeometry(302+(self.indexOfNewPlaylistBtn%4)*270, 152+(self.indexOfNewPlaylistBtn//4)*212, 20, 20)
        tmpBtn2.setStyleSheet( 
        "background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png);" +
        "background-repeat: no-repeat;" +
        "background-position: center;")
        tmpBtn2.setObjectName(str(self.indexOfNewList))
        self.mainPageDeletePlaylistBtns.append(tmpBtn2)
        self.mainPageDeletePlaylistBtns[self.indexOfNewPlaylistBtn].show()

        self.mainPageEmptyLabel.hide()

    def deletePlaylist(self):

        self.mainPagePlaylistBtns[int(self.deletedPlaylistBtnIndex)].deleteLater()
        self.mainPagePlaylistNameLabels[int(self.deletedPlaylistBtnIndex)].deleteLater()
        self.mainPageDeletePlaylistBtns[int(self.deletedPlaylistBtnIndex)].deleteLater()

        del self.mainPagePlaylistBtns[int(self.deletedPlaylistBtnIndex)]
        del self.mainPagePlaylistNameLabels[int(self.deletedPlaylistBtnIndex)]
        del self.mainPageDeletePlaylistBtns[int(self.deletedPlaylistBtnIndex)]

        self.resetPlaylistGeometry()
        if self.mainPagePlaylistBtns == [] :
            self.mainPageEmptyLabel.show()
        # self.mainWindow.update()

    def resetPlaylistGeometry(self):
        if len(self.mainPageDeletePlaylistBtns) <= 12 :
            self.mainPageWidgetForScoll.setGeometry(0, 120, 1183, 770)
            self.mainPageScrollArea.setWidgetResizable(False)
        else:
            print(len(self.mainPageDeletePlaylistBtns))
            self.mainPageWidgetForScoll.setGeometry(0, 120, 1183, (((len(self.mainPageDeletePlaylistBtns)-1)//4)+1)*212)
            self.mainPageScrollArea.setWidgetResizable(False)

        if int(self.deletedPlaylistBtnIndex) < len(self.mainPageDeletePlaylistBtns):
            for index in range(int(self.deletedPlaylistBtnIndex), len(self.mainPageDeletePlaylistBtns)):
                self.mainPagePlaylistBtns[index].setGeometry(68+(index%4)*270, (index//4)*212, 254, 142)
                self.mainPagePlaylistNameLabels[index].setGeometry(68+(index%4)*270, 152+(index//4)*212, 234, 20)
                self.mainPageDeletePlaylistBtns[index].setGeometry(302+(index%4)*270, 152+(index//4)*212, 20, 20)
        else:
            pass

    def displayVideo(self):
        if len(database.videosOfSelectedPlaylist) == 0:
            self.videoPageWidgetForScoll.setGeometry(760, 80, 423, 890)
        elif len(database.videosOfSelectedPlaylist) != 0:
            # self.videoPageEmptyLabel.hide()
            self.videoPageWidgetForScoll.setGeometry(760, 80, 423, len(database.videosOfSelectedPlaylist)*104)

        for index in range(0, len(database.videosOfSelectedPlaylist)):

            tmpBtn1 = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
            tmpBtn1.setGeometry(0, index*104, 168, 94)

            thumb = urllib.request.urlopen(database.videosOfSelectedPlaylist[index][3]).read()

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(thumb)
            pixmap = pixmap.scaled(168, 94)

            icon = QtGui.QIcon()
            icon.addPixmap(pixmap)
            tmpBtn1.setIcon(icon)
            tmpBtn1.setIconSize(QtCore.QSize(168, 94))
            
            # tmpBtn1.setStyleSheet("background-image: url ({database.videosOfSelectedPlaylist[index][3]});")

            tmpBtn1.setStyleSheet(self.radius10)
            tmpBtn1.setObjectName(str(database.videosOfSelectedPlaylist[index][4]))
            self.videoPageVideoBtns.append(tmpBtn1)

            tmpLabel1 = QtWidgets.QLabel(self.videoPageWidgetForScoll)
            tmpLabel1.setGeometry(170, 3+index*104, 220, 42)
            tmpLabel1.setStyleSheet(self.backgroundTransparent + self.fontWhite + self.fontSemibold)
            tmpLabel1.setFont(self.font14)
            tmpLabel1.setAlignment(self.alignLeft)
            tmpLabel1.setWordWrap(True)
            tmpLabel1.setText(database.videosOfSelectedPlaylist[index][0])
            self.videoPageVideoNameLabels.append(tmpLabel1)

            tmpLabel2 = QtWidgets.QLabel(self.videoPageWidgetForScoll)
            tmpLabel2.setGeometry(170, 50+index*104, 220, 15)
            tmpLabel2.setStyleSheet(self.transparentLabelStyle)
            tmpLabel2.setFont(self.font12)
            tmpLabel2.setText(database.videosOfSelectedPlaylist[index][1])
            self.videoPageVideoAuthorLabels.append(tmpLabel2)

            tmpLabel3 = QtWidgets.QLabel(self.videoPageWidgetForScoll)
            tmpLabel3.setGeometry(170, 65+index*104, 220, 15)
            tmpLabel3.setStyleSheet(self.transparentLabelStyle)
            tmpLabel3.setFont(self.font12)
            tmpLabel3.setText(str(database.videosOfSelectedPlaylist[index][2]))
            tmpLabel3.setText("조회수 "+str(round(database.videosOfSelectedPlaylist[index][2]/10000))+"만회")
            self.videoPageVideoViewLabels.append(tmpLabel3)

            tmpBtn2 = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
            tmpBtn2.setGeometry(390, 3+index*104, 20, 20)
            tmpBtn2.setStyleSheet( 
                "background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png);" +
                "background-repeat: no-repeat;" +
                "background-position: center;")
            tmpBtn2.setObjectName(str(database.videosOfSelectedPlaylist[index][4]))
            self.videoPageDeleteVideoBtns.append(tmpBtn2)

        self.videoPageScrollArea=QtWidgets.QScrollArea(self.pagesOfScreen[6])
        self.videoPageScrollArea.setGeometry(760, 80, 440, 900)
        self.videoPageScrollArea.setWidget(self.videoPageWidgetForScoll)
        self.videoPageScrollArea.setWidgetResizable(False)

    def clearVideoPage(self):
        for index in range(0, len(self.videoPageVideoBtns)):
            self.videoPageVideoBtns[index].deleteLater()
            self.videoPageVideoNameLabels[index].deleteLater()
            self.videoPageVideoAuthorLabels[index].deleteLater()
            self.videoPageVideoViewLabels[index].deleteLater()
            self.videoPageDeleteVideoBtns[index].deleteLater()
        
        self.vlcFrame.deleteLater()
        self.videoPageVideoBtns = []
        self.videoPageVideoNameLabels = []
        self.videoPageVideoAuthorLabels = []
        self.videoPageVideoViewLabels = []
        self.videoPageDeleteVideoBtns = []


        self.ui.videoPageCurrentVideoNameLabel.clear()
        self.ui.videoPageCurrentVideoChannelLabel.clear()
        self.ui.videoPageCurrentVideoViewLabel.clear()

    def addVideo(self):
        if self.indexOfNewVideoBtn < 7:  
            self.videoPageWidgetForScoll.setGeometry(760, 80, 423, 890)
            self.videoPageScrollArea.setWidgetResizable(False)
        else:
            print(self.indexOfNewVideoBtn)
            self.videoPageWidgetForScoll.setGeometry(760, 80, 423, len(database.videosOfSelectedPlaylist)*104)
            self.videoPageScrollArea.setWidgetResizable(False)

        tmpBtn1 = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
        tmpBtn1.setGeometry(0, self.indexOfNewVideoBtn*104, 168, 94)

        thumb = urllib.request.urlopen(database.newThumb).read()

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(thumb)
        pixmap = pixmap.scaled(168, 94)

        icon = QtGui.QIcon()
        icon.addPixmap(pixmap)
        tmpBtn1.setIcon(icon)
        tmpBtn1.setIconSize(QtCore.QSize(168, 94))

        tmpBtn1.setStyleSheet("border: 1px solid white;")
        tmpBtn1.setObjectName(str(self.indexOfNewVideo))
        self.videoPageVideoBtns.append(tmpBtn1)
        self.videoPageVideoBtns[self.indexOfNewVideoBtn].show()

        # Videolist Button
        # self.videoPageVideolistBtn = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
        # self.videoPageVideolistBtn.setGeometry(0, 0, 168, 94)
        # self.videoPageVideolistBtn.setStyleSheet(self.radius10)
        # self.videolistThumbnailPixmap=QtGui.QPixmap("/Users/ehakyung/homework9/image/thumbnail/thumb_1.webp")
        # self.videolistThumbnailPixmap.scaled(168, 94)
        # self.videolistThumbnailIcon=QtGui.QIcon()
        # self.videolistThumbnailIcon.addPixmap(self.videolistThumbnailPixmap)
        # self.videoPageVideolistBtn.setIcon(self.videolistThumbnailIcon)
        # self.videoPageVideolistBtn.setIconSize(QtCore.QSize(168, 94))

        tmpLabel1 = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        tmpLabel1.setGeometry(170, 3+self.indexOfNewVideoBtn*104, 220, 42)
        tmpLabel1.setStyleSheet(self.backgroundTransparent + self.fontWhite + self.fontSemibold)
        tmpLabel1.setFont(self.font14)
        tmpLabel1.setAlignment(self.alignLeft)
        tmpLabel1.setWordWrap(True)
        tmpLabel1.setText(database.newTitle)
        self.videoPageVideoNameLabels.append(tmpLabel1)
        self.videoPageVideoNameLabels[self.indexOfNewVideoBtn].show()

        # Label(영상목록 제목)
        # self.videoPageVideolistNameLabel = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        # self.videoPageVideolistNameLabel.setGeometry(170, 3, 220, 42)
        # self.videoPageVideolistNameLabel.setStyleSheet(self.backgroundTransparent + self.fontWhite + self.fontSemibold)
        # self.videoPageVideolistNameLabel.setFont(self.font14)
        # self.videoPageVideolistNameLabel.setAlignment(self.alignLeft)
        # self.videoPageVideolistNameLabel.setWordWrap(True)
        # self.videoPageVideolistNameLabel.setText("Playlist 따사로운 봄을 기다리며 spring pop 🌱🌼")

        tmpLabel2 = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        tmpLabel2.setGeometry(170, 50+self.indexOfNewVideoBtn*104, 220, 15)
        tmpLabel2.setStyleSheet(self.transparentLabelStyle)
        tmpLabel2.setFont(self.font12)
        tmpLabel2.setText(database.newAuthor)
        self.videoPageVideoAuthorLabels.append(tmpLabel2)
        self.videoPageVideoAuthorLabels[self.indexOfNewVideoBtn].show()

        # Label(영상목록 채널명)
        # self.videoPageVideolistChannelLabel = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        # self.videoPageVideolistChannelLabel.setGeometry(170, 50, 220, 15)
        # self.videoPageVideolistChannelLabel.setStyleSheet(self.transparentLabelStyle)
        # self.videoPageVideolistChannelLabel.setFont(self.font12)
        # self.videoPageVideolistChannelLabel.setText("때껄룩 TAKE A LOOK")

        tmpLabel3 = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        tmpLabel3.setGeometry(170, 65+self.indexOfNewVideoBtn*104, 220, 15)
        tmpLabel3.setStyleSheet(self.transparentLabelStyle)
        tmpLabel3.setFont(self.font12)
        tmpLabel3.setText("조회수 "+str(round(database.newView/10000))+"만회")
        self.videoPageVideoViewLabels.append(tmpLabel3)
        self.videoPageVideoViewLabels[self.indexOfNewVideoBtn].show()

        # # Label(영상목록 조회수)
        # self.videoPageVideolistViewLabel = QtWidgets.QLabel(self.videoPageWidgetForScoll)
        # self.videoPageVideolistViewLabel.setGeometry(170, 65, 220, 15)
        # self.videoPageVideolistViewLabel.setStyleSheet(self.transparentLabelStyle)
        # self.videoPageVideolistViewLabel.setFont(self.font12)
        # self.videoPageVideolistViewLabel.setText("조회수 68만")

        tmpBtn2 = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
        tmpBtn2.setGeometry(390, 3+self.indexOfNewVideoBtn*104, 20, 20)
        tmpBtn2.setStyleSheet( 
            "background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png);" +
            "background-repeat: no-repeat;" +
            "background-position: center;")
        tmpBtn2.setObjectName(str(self.indexOfNewVideo))
        self.videoPageDeleteVideoBtns.append(tmpBtn2)
        self.videoPageDeleteVideoBtns[self.indexOfNewVideoBtn].show()

        # Delete Videolist Button
        # self.videoPageDeleteVideoBtn = QtWidgets.QPushButton(self.videoPageWidgetForScoll)
        # self.videoPageDeleteVideoBtn.setGeometry(390, 3, 20, 20)
        # self.videoPageDeleteVideoBtn.setStyleSheet( 
        #     "background-image: url(/Users/ehakyung/Desktop/Youtube/image/deletePlaylistBtn.png);" +
        #     "background-repeat: no-repeat;" +
        #     "background-position: center;")

        # self.videoPageEmptyLabel.hide()


    def deleteVideo(self):
        self.videoPageVideoBtns[int(self.deletedVideoBtnIndex)].deleteLater()
        self.videoPageVideoNameLabels[int(self.deletedVideoBtnIndex)].deleteLater()
        self.videoPageVideoAuthorLabels[int(self.deletedVideoBtnIndex)].deleteLater()
        self.videoPageVideoViewLabels[int(self.deletedVideoBtnIndex)].deleteLater()
        self.videoPageDeleteVideoBtns[int(self.deletedVideoBtnIndex)].deleteLater()

        del self.videoPageVideoBtns[int(self.deletedVideoBtnIndex)]
        del self.videoPageVideoNameLabels[int(self.deletedVideoBtnIndex)]
        del self.videoPageVideoAuthorLabels[int(self.deletedVideoBtnIndex)]
        del self.videoPageVideoViewLabels[int(self.deletedVideoBtnIndex)]
        del self.videoPageDeleteVideoBtns[int(self.deletedVideoBtnIndex)]

        self.resetVideoGeometry()
        # if self.mainPagePlaylistBtns == [] :
        #     self.mainPageEmptyLabel.show()
        # self.mainWindow.update()

    def resetVideoGeometry(self):
        if len(self.videoPageDeleteVideoBtns) <= 7 :
            self.videoPageWidgetForScoll.setGeometry(760, 80, 423, 890)
            self.videoPageScrollArea.setWidgetResizable(False)
        else:
            print(len(self.videoPageDeleteVideoBtns))
            self.videoPageWidgetForScoll.setGeometry(760, 80, 423, len(self.videoPageDeleteVideoBtns)*104)
            self.videoPageScrollArea.setWidgetResizable(False)

        if int(self.deletedVideoBtnIndex) < len(self.videoPageDeleteVideoBtns):
            for index in range(int(self.deletedVideoBtnIndex), len(self.videoPageDeleteVideoBtns)):
                self.videoPageVideoBtns[index].setGeometry(0, index*104, 168, 94)
                self.videoPageVideoNameLabels[index].setGeometry(170, 3+index*104, 220, 42)
                self.videoPageVideoAuthorLabels[index].setGeometry(170, 50+index*104, 220, 15)
                self.videoPageVideoViewLabels[index].setGeometry(170, 65+index*104, 220, 15)
                self.videoPageDeleteVideoBtns[index].setGeometry(390, 3+index*104, 20, 20)
        else:
            pass


    def makeVlcFrame(self):
        self.vlcFrame = QtWidgets.QFrame(self.centralWidget)
        self.vlcFrame.setGeometry(20, 200, 710, 400)

    def messageBoxPopUp(self, index):
        self.textOfDialog = ["로그아웃 하시겠습니까?", "재생목록을 삭제하시겠습니까?", "영상을 재생목록에서 삭제하시겠습니까?", "이름을 20자 이내로 입력해주세요", "동일한 이름의 재생목록이 있습니다", "URL이 잘못되었거나 영상을 불러올 수 없습니다"]
        self.msgBox = QtWidgets.QMessageBox(self.mainWindow)
        self.msgBox.setText(self.textOfDialog[index])
        if index < 3:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Question)
            self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            tmpReply = self.msgBox.exec_()
        
            if tmpReply == QtWidgets.QMessageBox.Yes:
                self.reply = 1
            elif tmpReply == QtWidgets.QMessageBox.No:
                self.reply ==0
                
        elif index >= 3:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            tmpReply = self.msgBox.exec_()
        
            if tmpReply == QtWidgets.QMessageBox.Ok:
                self.reply = 1
            elif tmpReply == QtWidgets.QMessageBox.No:
                self.reply ==0

    def inputDialogPopUp(self):
        text, ok = QtWidgets.QInputDialog.getText(self.mainWindow, "", "재생목록의 이름을 입력하세요(20자 이내)")
        self.tmpPlaylistName = text
        if ok:
            self.reply = 1
        else:
            self.reply = 0

    def logoutSetting(self):
        self.reply = None
        self.playlistOfLoggedId = []    
        self.indexOfNewList = None 
        self.indexOfNewPlaylistBtn = None
        self.mainPagePlaylistBtns = []
        self.mainPagePlaylistNameLabels = []
        self.mainPageDeletePlaylistBtns = []

        self.deletedPlaylistBtnIndex = None
        self.selectedPlaylistName = None

        self.indexOfNewVideo = None
        self.indexOfNewVideoBtn = None
        self.indexOfNewVideoBtn = []
        self.videoPageVideoBtns = []
        self.videoPageVideoNameLabels = []
        self.videoPageVideoAuthorLabels = []
        self.videoPageVideoViewLabels = []
        self.videoPageDeleteVideoBtns = []

        self.deletedVideoBtnIndex = None
        # self.selectedVideoBtnIndex = None

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui()
    database = database.Database(ui)
    account = account.Account(ui, database)

    sys.exit(app.exec_())