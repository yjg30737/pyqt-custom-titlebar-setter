# pyqt-custom-titlebar-setter
PyQt custom titlebar setter.

This is movable/resizable. 

When resizing, cursor shape will be automatically changed depends on the direction of edge where the cursor is hovering over.

For example, you want to resize the window horizontally, cursor shape will be changed like "⇿".

You can set the title, and icon which should be SVG type.

You can set the min/max/close buttons separately.

This package supports full-screen. If your app has full screen, this custom titlebar can perfectly deal with it. So there's no need to do another chore for full-screen.

## Requirements
* PyQt5 >= 5.15 - This package is using <a href="https://doc.qt.io/qt-5/qwindow.html#startSystemMove">startSystemMove</a>, <a href="https://doc.qt.io/qt-5/qwindow.html#startSystemResize">startSystemResize</a> which were both introduced in Qt 5.15.

## Setup
`python -m pip install pyqt-custom-titlebar-setter`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>

## Usage
* `CustomTitlebarSetter.getCustomTitleBarWindow(main_window: QWidget, title: str = '', icon_filename: str = '',
                                font: QFont = QFont('Arial', 12), hint: list = ['min', 'max', 'close'],
                                align=Qt.AlignCenter, bottom_separator: bool = False) -> CustomTitlebarWindow`
    * `main_window` is your widget.
    * `title` is windows title. If you set this by default (empty string), title is based of the title you set with <a href="https://doc.qt.io/qt-5/qwidget.html#windowTitle-prop">`setWindowTitle`</a>.
    * `icon_filename` is title bar's icon. Icon file should be svg file. If it is not set, then there is no icon.
    * `font` is font of the title.
    * `hint` is hint of the button on the title bar. For example, if you give the value such as ['min', 'close'], the title bar buttons will contain minimize and close buttons only.
    * `align` is alignment of the title. You can give Qt.AlignLeft, Qt.AlignCenter, Qt.AlignRight. Some of these are not recommended depending on the title bar button's position.
    * `bottom_separator` decides whether you want to put the separator(horizontal line) at the bottom of the title bar. If it is set to True, line will be shown between title bar and main widget.
## Example
### 1. Very basic text editor
Code Sample

```python
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
    window = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=widget, icon_filename='dark-notepad.svg')
    window.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/167746119-c3715693-d7f9-4cb5-8c1c-76b3de372c3c.png)

How about dark theme?

![image](https://user-images.githubusercontent.com/55078043/167748426-adcc8b70-2778-4ccb-9fcf-26448a254e9f.png)

If you want to set dark theme, install the <a href="https://github.com/yjg30737/pyqt-style-setter.git">pyqt-style-setter</a>, then write code like this.

```python
...
widget = TextEditor()
StyleSetter.setWindowStyle(widget, theme='dark') # write it at this spot, BEFORE calling getCustomTitleBarWindow.
window = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=widget, icon_filename='dark-notepad.svg')
...
```

By the way, you can clearly see the title label and min/max/close button color changed based on background's color <b>automatically</b>.


Now let's apply this to some of the applications.

※ From now on, examples below are using dark theme. Of course, you don't have to use this.
### 2. <a href="https://github.com/yjg30737/pyqt-dark-notepad.git">pyqt-dark-notepad</a> - `DarkNotepadApp` class
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
        StyleSetter.setWindowStyle(mainWindow, theme='dark')  # you don't need this. this is just for adding style.
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBarWindow(mainWindow,
                                                                             icon_filename='ico/dark-notepad.svg')
        self.__titleBarWindow.show()
```

Result

![image](https://user-images.githubusercontent.com/55078043/156855872-1f247914-0a51-4bf1-a28c-908c83ffeccd.png)

### 3. <a href="https://github.com/yjg30737/pyqt-dark-calculator.git">pyqt-dark-calculator</a> - `CalculatorApp` class
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
        StyleSetter.setWindowStyle(mainWindow, theme='dark', exclude_type_lst=[QAbstractButton])
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBarWindow(mainWindow,
                                                                             icon_filename='ico/calculator.svg')
        self.__titleBarWindow.show()
```

Result

![image](https://user-images.githubusercontent.com/55078043/156855894-b2565bbf-8e80-440b-bb47-182ba3a61f1c.png)

### 4. <a href="https://github.com/yjg30737/pyqt-comic-viewer.git">pyqt-comic-viewer</a> - `ComicBookViewerApp` class
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
        StyleSetter.setWindowStyle(mainWindow, theme='dark')
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBarWindow(mainWindow, icon_filename='ico/book.svg')
        self.__titleBarWindow.show()
```

Result

![image](https://user-images.githubusercontent.com/55078043/156855909-7bd2d5a6-f741-4b9a-85eb-6509fe9e6c68.png)
