# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HSIWebScraper(object):
    def setupUi(self, HSIWebScraper):
        HSIWebScraper.setObjectName("HSIWebScraper")
        HSIWebScraper.resize(965, 570)
        self.centralwidget = QtWidgets.QWidget(parent=HSIWebScraper)
        self.centralwidget.setObjectName("centralwidget")
        self.websiteSelectionDropdown = QtWidgets.QComboBox(parent=self.centralwidget)
        self.websiteSelectionDropdown.setGeometry(QtCore.QRect(120, 120, 161, 41))
        self.websiteSelectionDropdown.setCurrentText("")
        self.websiteSelectionDropdown.setObjectName("websiteSelectionDropdown")
        self.websiteSelectionDropdown.addItem("")
        self.websiteSelectionDropdown.setItemText(0, "")
        self.websiteSelectionDropdown.addItem("")
        self.websiteSelectionDropdown.addItem("")
        self.websiteSelectionDropdown.addItem("")
        self.setSelectionDropdown = QtWidgets.QComboBox(parent=self.centralwidget)
        self.setSelectionDropdown.setGeometry(QtCore.QRect(120, 300, 161, 41))
        self.setSelectionDropdown.setCurrentText("")
        self.setSelectionDropdown.setObjectName("setSelectionDropdown")
        self.setSelectionDropdown.addItem("")
        self.setSelectionDropdown.setItemText(0, "")
        self.setSelectionDropdown.addItem("")
        self.setSelectionDropdown.addItem("")
        self.setSelectionDropdown.addItem("")
        self.setSelectionDropdown.addItem("")
        self.setSelectionDropdown.addItem("")
        self.searchButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(430, 480, 80, 24))
        self.searchButton.setObjectName("searchButton")
        self.paymentMethodcheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.paymentMethodcheckBox.setGeometry(QtCore.QRect(120, 370, 181, 22))
        self.paymentMethodcheckBox.setObjectName("paymentMethodcheckBox")
        self.searchTextBox = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.searchTextBox.setGeometry(QtCore.QRect(120, 210, 161, 41))
        self.searchTextBox.setText("")
        self.searchTextBox.setObjectName("searchTextBox")
        self.websiteSelectionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.websiteSelectionLabel.setGeometry(QtCore.QRect(120, 100, 161, 16))
        self.websiteSelectionLabel.setObjectName("websiteSelectionLabel")
        self.textSearchLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.textSearchLabel.setGeometry(QtCore.QRect(120, 190, 161, 16))
        self.textSearchLabel.setObjectName("textSearchLabel")
        self.setSelectionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.setSelectionLabel.setGeometry(QtCore.QRect(120, 280, 161, 16))
        self.setSelectionLabel.setObjectName("setSelectionLabel")
        self.toolButton = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(820, 400, 22, 23))
        self.toolButton.setObjectName("toolButton")
        self.keywordListLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.keywordListLabel.setGeometry(QtCore.QRect(540, 100, 161, 16))
        self.keywordListLabel.setObjectName("keywordListLabel")
        self.keywordlistWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.keywordlistWidget.setGeometry(QtCore.QRect(540, 120, 301, 271))
        self.keywordlistWidget.setObjectName("keywordlistWidget")
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.keywordlistWidget.addItem(item)
        self.selectAllKeywordscheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.selectAllKeywordscheckBox.setGeometry(QtCore.QRect(540, 400, 181, 22))
        self.selectAllKeywordscheckBox.setObjectName("selectAllKeywordscheckBox")
        self.keywordInclusivecheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.keywordInclusivecheckBox.setGeometry(QtCore.QRect(120, 400, 201, 22))
        self.keywordInclusivecheckBox.setObjectName("keywordInclusivecheckBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        HSIWebScraper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=HSIWebScraper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(parent=self.menubar)
        self.menufile.setObjectName("menufile")
        HSIWebScraper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=HSIWebScraper)
        self.statusbar.setObjectName("statusbar")
        HSIWebScraper.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(parent=HSIWebScraper)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSelectStorageLocation = QtGui.QAction(parent=HSIWebScraper)
        self.actionSelectStorageLocation.setObjectName("actionSelectStorageLocation")
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionSelectStorageLocation)
        self.menufile.addAction(self.actionQuit)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(HSIWebScraper)
        QtCore.QMetaObject.connectSlotsByName(HSIWebScraper)

    def retranslateUi(self, HSIWebScraper):
        _translate = QtCore.QCoreApplication.translate
        HSIWebScraper.setWindowTitle(_translate("HSIWebScraper", "MainWindow"))
        self.websiteSelectionDropdown.setItemText(1, _translate("HSIWebScraper", "www.facebook.com"))
        self.websiteSelectionDropdown.setItemText(2, _translate("HSIWebScraper", "www.craigslist.com"))
        self.websiteSelectionDropdown.setItemText(3, _translate("HSIWebScraper", "www.skipthegames.com"))
        self.setSelectionDropdown.setItemText(1, _translate("HSIWebScraper", "Payment Methods"))
        self.setSelectionDropdown.setItemText(2, _translate("HSIWebScraper", "Trafficker"))
        self.setSelectionDropdown.setItemText(3, _translate("HSIWebScraper", "Phone Numbers"))
        self.setSelectionDropdown.setItemText(4, _translate("HSIWebScraper", "Female"))
        self.setSelectionDropdown.setItemText(5, _translate("HSIWebScraper", "Male"))
        self.searchButton.setText(_translate("HSIWebScraper", "Search"))
        self.paymentMethodcheckBox.setText(_translate("HSIWebScraper", "Include payment method"))
        self.websiteSelectionLabel.setText(_translate("HSIWebScraper", "Select website to scrape:"))
        self.textSearchLabel.setText(_translate("HSIWebScraper", "Type text to scrape (optional):"))
        self.setSelectionLabel.setText(_translate("HSIWebScraper", "Select set to scrape (optional):"))
        self.toolButton.setText(_translate("HSIWebScraper", "..."))
        self.keywordListLabel.setText(_translate("HSIWebScraper", "List of keywords:"))
        __sortingEnabled = self.keywordlistWidget.isSortingEnabled()
        self.keywordlistWidget.setSortingEnabled(False)
        item = self.keywordlistWidget.item(0)
        item.setText(_translate("HSIWebScraper", "cheese"))
        item = self.keywordlistWidget.item(1)
        item.setText(_translate("HSIWebScraper", "hotdog"))
        item = self.keywordlistWidget.item(2)
        item.setText(_translate("HSIWebScraper", "cheese pizza"))
        item = self.keywordlistWidget.item(3)
        item.setText(_translate("HSIWebScraper", "ice cream"))
        item = self.keywordlistWidget.item(4)
        item.setText(_translate("HSIWebScraper", "fashion show"))
        item = self.keywordlistWidget.item(5)
        item.setText(_translate("HSIWebScraper", "lola"))
        item = self.keywordlistWidget.item(6)
        item.setText(_translate("HSIWebScraper", "mac and cheese"))
        item = self.keywordlistWidget.item(7)
        item.setText(_translate("HSIWebScraper", "pos"))
        item = self.keywordlistWidget.item(8)
        item.setText(_translate("HSIWebScraper", "pal"))
        item = self.keywordlistWidget.item(9)
        item.setText(_translate("HSIWebScraper", "pir"))
        item = self.keywordlistWidget.item(10)
        item.setText(_translate("HSIWebScraper", "p911"))
        item = self.keywordlistWidget.item(11)
        item.setText(_translate("HSIWebScraper", "kpc"))
        item = self.keywordlistWidget.item(12)
        item.setText(_translate("HSIWebScraper", "paw"))
        item = self.keywordlistWidget.item(13)
        item.setText(_translate("HSIWebScraper", "lolita group"))
        item = self.keywordlistWidget.item(14)
        item.setText(_translate("HSIWebScraper", "magic kingdom"))
        item = self.keywordlistWidget.item(15)
        item.setText(_translate("HSIWebScraper", "outcall"))
        item = self.keywordlistWidget.item(16)
        item.setText(_translate("HSIWebScraper", "incall"))
        self.keywordlistWidget.setSortingEnabled(__sortingEnabled)
        self.selectAllKeywordscheckBox.setText(_translate("HSIWebScraper", "Select all keywords from list"))
        self.keywordInclusivecheckBox.setText(_translate("HSIWebScraper", "Keyword inclusive (AND)"))
        self.label.setText(_translate("HSIWebScraper", "HSI Web Scraper"))
        self.menufile.setTitle(_translate("HSIWebScraper", "file"))
        self.actionQuit.setText(_translate("HSIWebScraper", "Quit"))
        self.actionSelectStorageLocation.setText(_translate("HSIWebScraper", "Select storage location"))
