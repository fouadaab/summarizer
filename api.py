from flask import Flask
import nltk
from autocorrect import spell
from views.routes import init_app 

app = Flask(__name__)
init_app(app)
nltk.download('punkt')

if __name__ == '__main__':
    app.run(debug=True)