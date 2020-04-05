import logging
import sys
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/var/www/html/expensesTracker/')
from app import app as application
application.secret_key = 'matteo00'
