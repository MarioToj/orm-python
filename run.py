from flask import Flask
from routes.contacts import contacts
from config import Config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'tu-clave-secreta-única-y-difícil-de-adivinar'
# Configuramos la base de datos desde el archivo Config
app.config.from_object(Config)

app.register_blueprint(contacts)
