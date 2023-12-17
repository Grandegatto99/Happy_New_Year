from datetime import *
from flask import *

app = Flask(__name__)

@app.route('/')
def new_year():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    delta = new_year - now
    return render_template('base.html', days=delta.days, hours=delta.seconds // 60//60, minutes=delta.seconds//60)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)