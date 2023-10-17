import re
def is_valid_email(email):
    """valida si el email es valido o no

    Args:
        email (string): email a validar
    Returns:
        boolean: True si es valido, False en caso contrario
    """
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

def is_valid_length(string, max_characters):
    """Validates if given string surpass or not the max characters

    Args:
        string (string): The string to validate
        max_characters (integer): The max number of characters

    Returns:
        boolean: False if is invalid, true if string length is less or equal than max characters
    """
    if len(string) > max_characters:
        return False
    else:
        return True

def current_selected_institution(request):
    selectedInstitution = request.cookies.get('selectedInstitution')
    if selectedInstitution:
        return int(request.cookies.get('selectedInstitution'))
    else:
        return None

