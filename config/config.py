import os

class Config:
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000
    MAX_FILE_SIZE = '16MB'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'uploads')
    ANALYTICS_SCRIPTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')

    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

