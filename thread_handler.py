from user.auth_server_thread import AuthServerThread

def enable_user_threads():
    auth_server = AuthServerThread().start()
    
    auth_server.start()

def enable_admin_threads():
    pass