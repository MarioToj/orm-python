from flask import Blueprint, render_template, request, flash, redirect, get_flashed_messages
from services.contact_service import ContactService;
from helpers.transform_error import handle_errors

contacts = Blueprint("contacts", __name__)


@contacts.route("/", methods=["GET"])
def home():
    all_contacts = ContactService.findAll()
    return render_template("index.html", contact = all_contacts)


@contacts.route("/new", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        
        data = {
            "fullname": request.form.get("fullname"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone")
        }

        try:
            ContactService.create(data)
            flash("Contacto creado exitosamente.")
            return redirect("/")
        except ValueError as ve:
            errors = handle_errors(ve)
            for category, message in errors:
                flash(message, category=category)
        except Exception as e:
            flash(f"Error al agregar contacto: {str(e)}") 
    
    errors = get_flashed_messages(with_categories=True)
    return render_template('register.html', errors=errors)


@contacts.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    if request.method == 'GET':
        contact = ContactService.findOneById(id)
        if not contact:
            return "Contacto no encontrado", 404
        return render_template('update.html', data = contact)
    
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email'],
        phone = request.form['phone']
        
        updated_contact = ContactService.update_contact(id, fullname, email, phone)
        if updated_contact:
            return redirect('/')
        else:
            return "Error al actualizar el contacto", 400
        
@contacts.route('/delete/<int:id>', methods=['GET'])
def delete_contact(id):
        ContactService.delete_contact(id)
        return redirect('/')

@contacts.route('/about<int:id>', methods=['GET'])
def about_contact(id):
    contact = ContactService.findOneById(id)
    
    return render_template('about.html', data = contact)
