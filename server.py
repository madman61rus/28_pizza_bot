from flask import Flask, render_template , Response,request,session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from models import db,Choice,Pizza
from flask_babelex import Babel

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
babel = Babel(app)
migrate = Migrate(app, db)

admin = Admin(app, name='pizza', template_mode='bootstrap3')
admin.add_view(ModelView(Pizza,db.session))
admin.add_view(ModelView(Choice,db.session))

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'rus')

class AuthException():

    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

class ModelView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    def check_auth(self, username, password):
        return username == 'admin' and password == 'password'

    def is_accessible(self):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True



if __name__ == "__main__":
    app.run()