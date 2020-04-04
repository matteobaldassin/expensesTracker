#! /usr/bin/python3.8

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/username/expensesTracker/')
from app import app as application
application.secret_key = 'matteo00'