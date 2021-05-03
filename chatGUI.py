from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QListWidget,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
    QListWidgetItem,
    QGridLayout
)
from chat import get_reply

class ChatGUI(QMainWindow):
    """ MAIN WINDOW """
    def __init__(self, parent=None):
        # INITIALIZER
        super().__init__(parent)
        self.setWindowTitle("Chatbot")
        self.resize(343, 319)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.gridLayout = QGridLayout()
        self.centralWidget.setLayout(self.gridLayout)

        self.setupUI()

    def setupUI(self):

        self.chatBox = QListWidget()
        self.gridLayout.addWidget(self.chatBox, 0, 0, 1, 2)

        self.newSenEdit = QLineEdit()
        self.gridLayout.addWidget(self.newSenEdit, 1, 0, 1, 1)
        self.newSenEdit.returnPressed.connect(self.sendChat)

        self.sendBtn = QPushButton("Send")
        self.gridLayout.addWidget(self.sendBtn, 1, 1, 1, 1)
        self.sendBtn.clicked.connect(self.sendChat)

    def sendChat(self):
        sentence = self.newSenEdit.text()
        self.newSenEdit.clear()

        self.chatBox.addItem(QListWidgetItem(f"Me: {sentence}"))

        reply = get_reply(sentence=sentence)
        if not reply:
            win.close()
            return
        self.chatBox.addItem(QListWidgetItem(reply))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = ChatGUI()
    # win.setupUI()
    win.show()
    sys.exit(app.exec_())
