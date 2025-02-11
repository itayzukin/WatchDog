from PyQt6.QtWidgets import QApplication
from initial_setup_window import InitialSetupWindow

def main():
    app = QApplication([])
    window = InitialSetupWindow('WatchDog')
    app.exec()


if __name__ == '__main__':
    main()