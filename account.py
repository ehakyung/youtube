import database, re

class Account:
    def __init__(self, ui):
        self.ui = ui
        self.database = database.Database()
        self.nameCheck = None
        self.idCheck = None
        self.pwCheck = None
        self.phoneCheck = None
        self.mailCheck = None

        for index in range (0, len(self.ui.loginPageBtns)):
            self.ui.loginPageBtns[index].clicked.connect(lambda event, i=index: self.clickEvent(event, i))
            self.ui.loginPageBtns[index].enterEvent = lambda event, i=index: self.enterEvent1(event, i)
            self.ui.loginPageBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent1(event, i)

        for index in range (0, len(self.ui.backBtns)):
            self.ui.backBtns[index].clicked.connect(self.backBtnEvent)
            self.ui.backBtns[index].enterEvent = lambda event, i=index: self.enterEvent3(event, i)
            self.ui.backBtns[index].leaveEvent = lambda event, i=index: self.leaveEvent3(event, i)
            
        self.ui.loginPageLoginBtn.clicked.connect(self.loginBtnEvent)
        # self.ui.loginPageLoginBtn.enterEvent = self.enterEvent2
        # self.ui.loginPageLoginBtn.leaveEvent = self.leaveEvent2
        self.ui.loginPageLoginBtn.enterEvent = lambda event: self.enterEvent2(self.ui.loginPageLoginBtn, event)
        self.ui.loginPageLoginBtn.leaveEvent = lambda event: self.leaveEvent2(self.ui.loginPageLoginBtn, event)

        self.ui.findIdPageFindBtn.clicked.connect(self.findIdPageFindBtnEvent)
        self.ui.findIdPageFindBtn.enterEvent = lambda event: self.enterEvent2(self.ui.findIdPageFindBtn, event)
        self.ui.findIdPageFindBtn.leaveEvent = lambda event: self.leaveEvent2(self.ui.findIdPageFindBtn, event)

        self.ui.findPwPageFindBtn.clicked.connect(self.findPwPageFindBtnEvent)
        self.ui.findPwPageFindBtn.enterEvent = lambda event: self.enterEvent2(self.ui.findPwPageFindBtn, event)
        self.ui.findPwPageFindBtn.leaveEvent = lambda event: self.leaveEvent2(self.ui.findPwPageFindBtn, event)



        self.ui.joinPageEdits[0].textChanged.connect(self.nameCheckEvent)
        self.ui.joinPageEdits[1].textChanged.connect(self.idCheckEvent)
        self.ui.joinPageEdits[2].textChanged.connect(self.pwCheckEvent)
        self.ui.joinPageEdits[3].textChanged.connect(self.phoneCheckEvent)
        self.ui.joinPageEdits[4].textChanged.connect(self.mailCheckEvent)

        self.ui.joinPageJoinBtn.clicked.connect(self.joinBtnEvent)
        self.ui.joinPageJoinBtn.enterEvent = lambda event: self.enterEvent2(self.ui.joinPageJoinBtn, event)
        self.ui.joinPageJoinBtn.leaveEvent = lambda event: self.leaveEvent2(self.ui.joinPageJoinBtn, event)

        
#-------------------------------------------------------------------------------------[ 페이지 전환 함수 ]

    def clickEvent(self, event, index):
        self.ui.screen.setCurrentIndex(index+1)
        if index == 0:
            self.ui.findIdPageNoticeLabel.setText("가입시 입력한 메일주소를 입력하세요")
            self.ui.findIdPageEdit.clear()
        elif index == 1:
            self.ui.findPwPageNoticeLabel.setText("가입시 입력한 아이디와 메일주소를 입력하세요")
            for index in range(0, len(self.ui.findPwPageEdits)):
                self.ui.findPwPageEdits[index].clear()
        elif index == 2:
            self.ui.joinPageNoticeLabel.clear()
            for index in range(0, len(self.ui.joinPageEdits)):
                self.ui.joinPageEdits[index].clear()


    def backBtnEvent(self):
        self.ui.screen.setCurrentIndex(0)
        self.ui.loginPageNoticeLabel.clear()
        for index in range(0, len(self.ui.loginPageEdits)):
            self.ui.loginPageEdits[index].clear()

#-------------------------------------------------------------------------------------[ 마우스커서 함수 ]

    def enterEvent1(self, event, index):
        self.ui.loginPageBtns[index].setStyleSheet(self.ui.backgroundTransparent + self.ui.borderNone + self.ui.fontBlue)

    def leaveEvent1(self, event, index):
        self.ui.loginPageBtns[index].setStyleSheet(self.ui.backgroundTransparent + self.ui.borderNone + self.ui.fontWhite)

    # def enterEvent2(self, event):
    #     self.ui.loginPageLoginBtn.setStyleSheet(self.ui.btnEnteredStyle)

    # def leaveEvent2(self, event):
    #     self.ui.loginPageLoginBtn.setStyleSheet(self.ui.btnStyle)

    def enterEvent2(self, btn, event):
        btn.setStyleSheet(self.ui.btnEnteredStyle)

    def leaveEvent2(self, btn, event):
        btn.setStyleSheet(self.ui.btnStyle)

    def enterEvent3(self, event, index):
        self.ui.backBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/backBtnBlue.png)")

    def leaveEvent3(self, event, index):
        self.ui.backBtns[index].setStyleSheet("background-image: url(/Users/ehakyung/Desktop/Youtube/image/backBtn.png)")

#-------------------------------------------------------------------------------------[ 로그인 함수 ]

    def loginBtnEvent(self):
        info = []
        for index in range (0, len(self.ui.loginPageEdits)):
            info.append(self.ui.loginPageEdits[index].text())

        if "" in info:
            self.ui.loginPageNoticeLabel.setText("아이디와 비밀번호를 모두 입력해주세요")
        else:
            self.database.cursor.execute("SELECT id, pw FROM account WHERE id=? AND pw=?", info)
            result=self.database.cursor.fetchall()
            if len(result) == 0:
                self.ui.loginPageNoticeLabel.setText("아이디와 비밀번호가 일치하지 않습니다")
            else:
                self.database.loggedId = info[0]
                # self.game=Game.Game(self.ui, self) #game 버튼 이벤트를 AtterLogin에 포함시키기
                # self.afterLogin=AfterLogin.AfterLogin(self.ui, self)

                self.ui.screen.setCurrentIndex(4)

                for index in range(0, len(self.ui.loginPageEdits)):
                    self.ui.loginPageEdits[index].clear()
#-------------------------------------------------------------------------------------[ 아이디 찾기 함수 ]

    def findIdPageFindBtnEvent(self):
        mail=self.ui.findIdPageEdit.text()
        self.database.cursor.execute("SELECT id FROM account WHERE mail=?", [mail])
        result=self.database.cursor.fetchall()
        if len(result) == 0:
            self.ui.findIdPageNoticeLabel.setText("메일주소를 잘못 입력하셨습니다")
        else:
            self.ui.findIdPageNoticeLabel.setText("귀하의 아이디는 " + result[0][0] + "입니다")

#-------------------------------------------------------------------------------------[ 비밀번호 찾기 함수 ]

    def findPwPageFindBtnEvent(self):
        info=[]
        for index in range (0, len(self.ui.findPwPageEdits)):
            info.append(self.ui.findPwPageEdits[index].text())

        if "" in info:
            self.ui.findPwPageNoticeLabel.setText("모든 정보를 입력해주세요")
        else:
            self.database.cursor.execute("SELECT pw FROM account WHERE id=? AND mail=?", info)
            result=self.database.cursor.fetchall()

            if len(result) == 0:
                self.ui.findPwPageNoticeLabel.setText("아이디 또는 메일주소를 잘못 입력하셨습니다")
            else:
                self.ui.findPwPageNoticeLabel.setText("귀하의 비밀번호는 " + result[0][0] + "입니다")

#-------------------------------------------------------------------------------------[ 이름 유효성 검사 함수 ]

    def nameCheckEvent(self):
        name = self.ui.joinPageEdits[0].text()
        if len(name) == 0:
            self.ui.joinPageNoticeLabel.setText("")
            self.nameCheck = False
        elif len(name) > 10:
            self.ui.joinPageNoticeLabel.setText("공백 포함 10자 이하로 입력하세요")
            self.nameCheck = False
        else:
            self.ui.joinPageNoticeLabel.setText(name +"님 안녕하세요")
            self.nameCheck = True

#-------------------------------------------------------------------------------------[ 아이디 중복확인 / 유효성 검사 함수 ]

    def idCheckEvent(self):
        id = self.ui.joinPageEdits[1].text()
        if len(id) == 0:
            self.ui.joinPageNoticeLabel.setText("")
            self.idCheck = False
        elif len(id) < 4 or len(id) > 20:
            self.ui.joinPageNoticeLabel.setText("4자 이상 20자 이하로 입력하세요")
            self.idCheck = False
        else:
            self.database.cursor.execute("SELECT id FROM account WHERE id=?", [id]) 
            result=self.database.cursor.fetchall()

            if len(result) == 0:
                if id.isalnum() == True:
                    self.ui.joinPageNoticeLabel.setText("사용 가능한 아이디입니다")
                    self.idCheck = True
                elif id.isalnum() == False:
                    self.ui.joinPageNoticeLabel.setText("특수문자를 제외한 문자 또는 숫자만 사용하세요")
                    self.idCheck = False
            else:
                self.ui.joinPageNoticeLabel.setText("이미 사용 중인 아이디입니다")
                self.idCheck = False

#-------------------------------------------------------------------------------------[ 비밀번호 유효성 검사 함수 ]

    def pwCheckEvent(self):
        pw = self.ui.joinPageEdits[2].text()
        if len(pw) == 0:
            self.ui.joinPageNoticeLabel.setText("")
            self.pwCheck = False
        elif len(pw) < 8 or len(pw) > 20:
            self.ui.joinPageNoticeLabel.setText("8자 이상 20자 이하로 입력하세요")
            self.pwCheck = False
        else:
            self.ui.joinPageNoticeLabel.setText("")
            self.pwCheck = True

#-------------------------------------------------------------------------------------[ 휴대전화번호 유효성 검사 함수 ]

    def phoneCheckEvent(self):
        phone = self.ui.joinPageEdits[3].text()
        regexPhone = re.compile("^(01)\d{1}-\d{3,4}-\d{4}$")
        validation = regexPhone.search(phone.replace(" ", ""))
        if validation:
            self.ui.joinPageNoticeLabel.setText("")
            self.phoneCheck = True
        else:
            self.ui.joinPageNoticeLabel.setText("01X-XXX-XXXX 또는 01X-XXXX-XXXX로 입력하세요")
            self.phoneCheck = False

#-------------------------------------------------------------------------------------[ 메일주소 중복확인 / 유효성 검사 함수 ]

    def mailCheckEvent(self):
        mail = self.ui.joinPageEdits[4].text()
        REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if not re.fullmatch(REGEX_EMAIL, mail):
            self.ui.joinPageNoticeLabel.setText("유효하지 않은 메일주소입니다")
            self.mailCheck = False
        else:
            self.database.cursor.execute("SELECT mail FROM account WHERE mail=?", [mail])
            result=self.database.cursor.fetchall() 
            if len(result) == 0:
                self.ui.joinPageNoticeLabel.setText("사용 가능한 메일주소입니다")
                self.mailCheck = True
            else:
                self.ui.joinPageNoticeLabel.setText("이미 사용 중인 메일주소입니다")
                self.mailCheck = False

#-------------------------------------------------------------------------------------[ 회원가입 함수 ]

    def joinBtnEvent(self):
        checks = [self.nameCheck, self.idCheck, self.pwCheck, self.phoneCheck, self.mailCheck]
        if None in checks:
            self.ui.joinPageNoticeLabel.setText("모든 정보를 입력해주세요")
        else:
            if self.nameCheck == False:
                self.ui.joinPageNoticeLabel.setText("이름을 올바르게 입력해주세요")
            else:
                if self.idCheck == False:
                    self.ui.joinPageNoticeLabel.setText("아이디를 올바르게 입력해주세요")
                else:
                    if self.pwCheck == False:
                        self.ui.joinPageNoticeLabel.setText("비밀번호를 올바르게 입력해주세요")
                    else:
                        if self.phoneCheck == False:
                            self.ui.joinPageNoticeLabel.setText("휴대전화번호를 올바르게 입력해주세요")
                        else:
                            if self.mailCheck == False:
                                self.ui.joinPageNoticeLabel.setText("메일주소를 올바르게 입력해주세요")
                            else:
                                self.ui.joinPageNoticeLabel.setText("가입을 축하합니다. 로그인 후 이용해주세요")
                                info=[]
                                for index in range (0, len(self.ui.joinPageEdits)):
                                    info.append(self.ui.joinPageEdits[index].text())
                                    print(info)
                                self.database.cursor.execute("INSERT INTO account VALUES (?, ?, ?, ?, ?, datetime('now','localtime'))", [info[0], info[1], info[2], info[3], info[4]])
                                self.database.connect.commit()
