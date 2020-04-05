import logging
import sys
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/var/www/html/expensesTracker/')
from app import app as app
from werkzeug.debug import DebuggedApplication

app.secret_key = 'matteo00'
app.debug = True
application = DebuggedApplication(app, evalex=True)
