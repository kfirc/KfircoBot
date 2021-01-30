from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    TELEGRAM_TOKEN = environ['TELEGRAM_TOKEN']
    LOGGER_PATH = environ['LOGGER_PATH']
    GITHUB_REPO_URL = 'https://github.com/kfirc/KfircoBot'
    DOWNLOAD_CV_URL = 'https://drive.google.com/uc?export=download&id=14PUObXjl7NRqlRRVL1C4hPvy6y6LU4fB'
    OWNER_WEBSITE = 'https://www.linkedin.com/in/kfirco/'
    BOT_NAME = 'KfircoBot'
