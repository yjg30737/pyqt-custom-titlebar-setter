from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from pyqt_custom_titlebar_window.customTitlebarWindow import CustomTitlebarWindow


class CustomTitlebarSetter:
    @staticmethod
    def getCustomTitleBarWindow(main_window: QWidget, title: str = '', icon_filename: str = '',
                                font: QFont = QFont('Arial', 14), hint: list = ['min', 'max', 'close'],
                                align=Qt.AlignCenter, bottom_separator: bool = False) -> CustomTitlebarWindow:
        titleBarWindow = CustomTitlebarWindow(main_window)
        titleBarWindow.setTopTitleBar(title=title, icon_filename=icon_filename, font=font, align=align,
                                      bottom_separator=bottom_separator)
        titleBarWindow.setButtonHint(hint)
        titleBarWindow.setButtons()

        return titleBarWindow