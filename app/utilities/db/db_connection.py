import sqlite3
from ..config import BaseConfig

connection = sqlite3.connect(BaseConfig.SQLITE_DB)
