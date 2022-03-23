from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class CustomTitlebarSetter:
    @staticmethod
    def getCustomTitleBar(main_window: QWidget, icon_filename: str = '', style='windows',
                          hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint) -> CustomTitlebarWindow:
        titleBarWindow = CustomTitlebarWindow(main_window)
        titleBarWindow.setTopTitleBar(icon_filename=icon_filename)
        titleBarWindow.setButtonStyle(style)
        titleBarWindow.setButtonHint(hint)
        titleBarWindow.setButtons()
        return titleBarWindow