from setuptools import setup, find_packages

setup(
    name='pyqt-custom-titlebar-setter',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Custom Titlebar Setter',
    url='https://github.com/yjg30737/pyqt-custom-titlebar-setter.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-custom-titlebar-window @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-window.git@main'
    ]
)