from PyQt6.QtWidgets import QApplication
from main_app_window import MainAppWindow
import os.path as op
import configparser

def run_app():
    if not op.isfile('config.ini'):
        create_config()

    app = QApplication([])
    window = MainAppWindow()   
    window.show()
    app.exec()

def create_config():
    config = configparser.ConfigParser()

    config['Initialisation'] = {'setup': False, 'account_type': 'None'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    run_app()