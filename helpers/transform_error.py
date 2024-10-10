def handle_errors(error):
    error_messages = []

    # Manejar el error de duplicado
    if str(error) == "duplicate_email":
        error_messages.append(("duplicate_email", "El correo electrónico ya está en uso. Por favor, usa otro."))
        return error_messages

    # Manejar otros errores de validación
    if isinstance(error.args[0], dict):
        errors = error.args[0]
        for field, messages in errors.items():
            for message in messages:
                error_messages.append((field, message))
    
    return error_messages
