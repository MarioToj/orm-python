from utils.db import db

class Contact(db.Model):
    __tablename__ = 'contact'
    
    id = db.Column(db.Integer, primary_key=True) 
    fullname = db.Column(db.String(96), nullable=False)
    email = db.Column(db.String(96), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True)
    
    # Definimos el constructor del modelo
    def __init__(self, fullname: str, email: str, phone: str = None):
        self.fullname = fullname
        self.email = email
        self.phone = phone
