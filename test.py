from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Text Editor')
        lay = QGridLayout()
        lay.addWidget(QTextEdit())
        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = TextEditor()
    window = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=widget, icon_filename='icon.svg')
    window.show()
    sys.exit(app.exec_())