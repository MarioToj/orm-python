from flask import Blueprint, render_template, request, flash, redirect, get_flashed_messages
from services.contact_service import ContactService;


contacts = Blueprint("contacts", __name__)


@contacts.route("/", methods=["GET"])
def home():
    all_contacts = ContactService.findAll()
    return render_template("index.html", contac = all_contacts)


@contacts.route("/new", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        
        data = {
            "fullname": request.form.get("fullname"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone")
        }

        try:
            # Usar el servicio para crear un contacto
            ContactService.create(data)
            flash("Contacto creado exitosamente.")
            return redirect("/")  # Redirigir a la lista de contactos después de agregar uno
        except ValueError as ve:
            if isinstance(ve.args[0], dict):
                errors = ve.args[0]
                for field, messages in errors.items():
                    for message in messages:
                        flash(f"{message}", category=field)
        except Exception as e:
            flash(f"Error al agregar contacto: {str(e)}")  
    
    errors = get_flashed_messages(with_categories=True)
    return render_template('register.html', errors=errors)


# @contacts.route('/update')
# def update_contact():
#     return "actualizar contacto"

# @contacts.route('/delete')
# def delete_contact():
#     return "eliminar contacto"

# @contacts.route('/about')
# def about_contact():
#     return "about"
