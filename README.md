# pyqt-custom-titlebar-setter
PyQt Custom Titlebar(<a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>) Setter.

## Requirements
* PyQt5 >= 5.15

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-custom-titlebar-setter.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>

## Usage
* ```CustomTitlebarSetter.getCustomTitleBar(main_window: QWidget, icon_filename: str) -> CustomTitlebarWindow``` - Icon file should be svg file.

## Example
### 1. <a href="https://github.com/yjg30737/pyqt-dark-notepad.git">pyqt-dark-notepad</a> - ```DarkNotepadApp``` class
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_dark_notepad import DarkNotepad

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = DarkNotepad()
        StyleSetter.setWindowStyle(mainWindow)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/dark-notepad.svg')
        self.__titleBarWindow.show()
```

Result

![image](https://user-images.githubusercontent.com/55078043/156855872-1f247914-0a51-4bf1-a28c-908c83ffeccd.png)

### 2. <a href="https://github.com/yjg30737/pyqt-dark-calculator.git">pyqt-dark-calculator</a> - ```CalculatorApp``` class
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QAbstractButton
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_dark_calculator.calculator import Calculator

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class CalculatorApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = Calculator()
        StyleSetter.setWindowStyle(mainWindow, exclude_type_lst=[QAbstractButton])
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/calculator.svg')
        self.__titleBarWindow.show()
```

Result

![image](https://user-images.githubusercontent.com/55078043/156855894-b2565bbf-8e80-440b-bb47-182ba3a61f1c.png)

### 3. <a href="https://github.com/yjg30737/pyqt-comic-viewer.git">pyqt-comic-viewer</a> - ```ComicBookViewerApp``` class
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_comic_viewer.comicBookViewer import ComicBookViewer

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class ComicBookViewerApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = ComicBookViewer()
        StyleSetter.setWindowStyle(mainWindow)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/book.svg')
        self.__titleBarWindow.show()
```

Result

![image](https://user-images.githubusercontent.com/55078043/156855909-7bd2d5a6-f741-4b9a-85eb-6509fe9e6c68.png)
