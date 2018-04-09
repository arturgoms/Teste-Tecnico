""" Settings File

    Arquivo onde se concentra as configurações do servidor

Todo:

    None

"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = 'src/static/'
PORT = 4000
DATABASE = {
  'user': 'root',
  'password': 'pwarturgomes',
  'host': '127.0.0.1',
  'database': 'user',
  'raise_on_warnings': True,
  'use_pure': False,
}

