import os
import sys
import configparser
from PyQt6.QtWidgets import QApplication
from windows.main_app_window import MainAppWindow

def run_app():
    """Initialize config if needed and start the Qt application."""
    if not os.path.isfile('config.ini'):
        create_config()

    app = QApplication(sys.argv)
    window = MainAppWindow()
    window.show()
    sys.exit(app.exec())

def create_config():
    """Create default config file with initial setup flags."""
    config = configparser.ConfigParser()
    config['Initialisation'] = {
        'setup': 'False',
        'account_type': 'None'
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    run_app()
