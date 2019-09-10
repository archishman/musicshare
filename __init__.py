from flask import Flask
from login_page import login_page
from user_profile import user_profile
from config import PORT
app = Flask(__name__)
app.register_blueprint(login_page)
app.register_blueprint(user_profile)

if __name__ == "__main__":
    app.run(debug=True, port=PORT)