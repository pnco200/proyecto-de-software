from src.core.database import db
from src.core.configuration.configuration import Configuration
def get_configuration():
    """Devuelve la configuracion actual del sitio

    Returns:
        Configuration: Devuelve un objeto Configuration(rows_per_page, contact_information, is_maintenance, maintenance_message)
    """
    return Configuration.query.first()

def update_configuration(rows_per_page=None, contact_information=None, is_maintenance=None, maintenance_message=None):
    """Actualiza la configuracion de la pagina

    Args:
        rows_per_page (integer, optional): Elementos por pagina. Defaults to None.
        contact_information (string, optional): Informacion de contacto. Defaults to None.
        is_maintenance (boolean, optional): Determina si la pagina esta en mantenimiento o no. Defaults to None.
        maintenance_message (string, optional): Mensaje para mostrar si la pagina esta en mantenmiento. Defaults to None.

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