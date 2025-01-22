from PyQt6.QtWidgets import QApplication
from IinitialSetupWindow import IinitialSetupWindow

def main():
    app = QApplication([])
    window = IinitialSetupWindow('WatchDog')
    app.exec()


if __name__ == '__main__':
    main()