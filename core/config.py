import os

class Config:
    BASE_DIR = os.getcwd()
    DATA_DIR = os.path.join(BASE_DIR, "data")
    TEMP_DIR = os.path.join(BASE_DIR, "temp")
