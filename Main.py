from PyQt6.QtWidgets import QApplication
from main_app_window import MainAppWindow

def run_app():
    app = QApplication([])
    window = MainAppWindow()   
    window.show()
    app.exec()

if __name__ == '__main__':
    run_app()