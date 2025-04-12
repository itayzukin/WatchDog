from PyQt6.QtWidgets import QApplication
from user_main_window import UserMainWindow

def main():
    app = QApplication([])
    window = UserMainWindow('WatchDog')
    app.exec()


if __name__ == '__main__':
    main()