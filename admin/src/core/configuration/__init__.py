from src.core.database import db
from src.core.configuration.configuration import Configuration

def create_configuration(rows_per_page, contact_information, is_maintenance, maintenance_message):
    """Crea la configuracion inicial del sitio

    Args:
        rows_per_page (_int_): Elementos por pagina
        contact_information (_str_): Informacion de contacto
        is_maintenance (_bool_): Determina si la pagina esta en mantenimiento o no
        maintenance_message (_str_): Mensaje para mostrar si la pagina esta en mantenmiento

    Returns:
        Configuration: Devuelve un objeto Configuration(rows_per_page, contact_information, is_maintenance, maintenance_message)
    """
    config = Configuration(
        rows_per_page=rows_per_page,
        contact_information=contact_information,
        is_maintenance=is_maintenance,
        maintenance_message=maintenance_message
    )
    db.session.add(config)
    db.session.commit()
    return config

def get_configuration():
    """Devuelve la configuracion actual del sitio

    Returns:
        Configuration: Devuelve un objeto Configuration(rows_per_page, contact_information, is_maintenance, maintenance_message)
    """
    return Configuration.query.first()

def is_in_maintenance():
    """Devuelve el estado actual del sitio

    Returns:
        bool: True si esta en mantenimiento, False si no.
    """

    return Configuration.query.first().is_maintenance

def maintenance_message():
    """Devuelve el mensaje de mantenimiento del sitio

    Returns:
        string: mensaje de mantenimiento del sitio
    """

    return Configuration.query.first().maintenance_message

def get_rows_per_page():
    """Devuelve la configuracion actual del sitio para cuantas filas mostrar por pagina

    Returns:
        int: Devuelve la cantidad de filas por pagina
    """
    return Configuration.query.first().rows_per_page

def update_configuration(rows_per_page=None, contact_information=None, is_maintenance=None, maintenance_message=None):
    """Actualiza la configuracion de la pagina

    Args:
        rows_per_page (_int_, optional): Elementos por pagina. Defaults to None.
        contact_information (_int_, optional): Informacion de contacto. Defaults to None.
        is_maintenance (_bool_, optional): Determina si la pagina esta en mantenimiento o no. Defaults to None.
        maintenance_message (_str_, optional): Mensaje para mostrar si la pagina esta en mantenmiento. Defaults to None.

    Returns:
        boolean: Devuelve true en caso de que se pudo actualizar, false en caso contrario
    """
    try:
         config = Configuration.query.first()
         if config:
              if rows_per_page is not None:
                  config.rows_per_page = rows_per_page
              if contact_information is not None:
                  config.contact_information = contact_information
              if is_maintenance is not None:
                  config.is_maintenance = is_maintenance
              if maintenance_message is not None:
                  config.maintenance_message = maintenance_message
              db.session.commit()
              return True
         return False
    except Exception as e:
         print(str(e))
         return False