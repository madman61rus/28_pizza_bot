from werkzeug.exceptions import HTTPException
from flask import Flask, Response, request, session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from models import db, Choice, Pizza
from flask_babelex import Babel
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI, ADMIN_CREDENTIALS
from sqlalchemy.orm import scoped_session, sessionmaker


class LoginModelView(ModelView):
    def is_accessible(self):
        auth = request.authorization
        if not auth or (auth.username, auth.password) != ADMIN_CREDENTIALS:
            raise HTTPException('', Response("Пожалуйста введите логин и пароль", 401,
                                             {'WWW-Authenticate': 'Basic realm="Login Required"'}
                                             ))
        else:
            return True


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
babel = Babel(app)
migrate = Migrate(app, db)
admin = Admin(app, name='pizza', template_mode='bootstrap3')
admin.add_view(LoginModelView(Pizza, db.session))
admin.add_view(LoginModelView(Choice, db.session))
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'rus')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run()
