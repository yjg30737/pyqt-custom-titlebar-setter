import os, inspect, sys

from PyQt5.QtWidgets import QWidget
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class CustomTitlebarSetter:
    @staticmethod
    def setCustomTitleBar(main_window: QWidget, icon_filename: str):
        titleBarWindow = CustomTitlebarWindow(main_window)
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
        titleBarWindow.setTopTitleBar(icon_filename=os.path.join(caller_path, icon_filename))
        titleBarWindow.setButtons()
        titleBarWindow.show()