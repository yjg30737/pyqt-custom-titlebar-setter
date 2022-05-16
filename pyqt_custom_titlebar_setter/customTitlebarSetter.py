from PyQt5.QtWidgets import QWidget
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class CustomTitlebarSetter:
    @staticmethod
    def getCustomTitleBarWindow(main_window: QWidget, icon_filename: str = '',
                                hint: list = ['min', 'max', 'close']) -> CustomTitlebarWindow:
        titleBarWindow = CustomTitlebarWindow(main_window)
        titleBarWindow.setTopTitleBar(icon_filename=icon_filename)
        titleBarWindow.setButtonHint(hint)
        titleBarWindow.setButtons()
        return titleBarWindow