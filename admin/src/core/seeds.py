from src.core import institutions, configuration, auth, rol_permission, services, service_requests

def run():
    def create_institutions():
        institutions.create_institution(
            name="Instituto de Matemática e Estatística",
            information="Instituto de Matemática e Estatística",
            address="Rua do Matão, 1010 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://www.ime.usp.br/",
            keywords="Matemática, Estatística, Computação",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Física",
            information="Instituto de Física",
            address="Rua do Matão, 1371 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://portal.if.usp.br/",
            keywords="Física",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 309-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Química",
            information="Instituto de Química",
            address="Av. Prof. Lineu Prestes, 748 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://www.iq.usp.br/",
            keywords="Química",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 091-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Biociências",
            information="Instituto de Biociências",
            address="Rua do Matão, 277 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://ib.usp.br/",
            keywords="Biologia",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 91-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Psicologia",
            information="Instituto de Psicologia",
            address="Av. Prof. Mello Moraes, 1721 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://www.ip.usp.br/",
            keywords="Psicologia",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-49",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Ciências Biomédicas",
            information="Instituto de Ciências Biomédicas",
            address="Av. Prof. Lineu Prestes, 1524 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://icb.usp.br/",
            keywords="Biologia, Medicina",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-9",
            is_active=True
        )
    def create_users():
        auth.create_user(
            email="mail1@gmail.com",
            name="Jane",
            lastname="Doe",
            username="jane",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        auth.create_user(
            email="mail2@gmail.com",
            name="John",
            lastname="Doe",
            username="john",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        auth.create_user(
            email="mail3@gmail.com",
            name="Alice",
            lastname="Doe",
            username="alice",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        auth.create_user(
            email="mail4@gmail.com",
            name="Bob",
            lastname="Doe",
            username="bob",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        auth.create_user(
            email="mail5@gmail.com",
            name="Eve",
            lastname="Doe",
            username="eve",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        auth.create_user(
            email="mail6@gmail.com",
            name="Carol",
            lastname="Doe",
            username="carol",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
    def create_configurations():
        configuration.create_configuration(
            rows_per_page=5,
            contact_information="11 3091-6149",
            is_maintenance=False,
            maintenance_message="",
        )
    def create_services():
        service1= services.create_service(
            name="Matemática",
            type="ANALISIS",
            centers="IME",
            description="Matemática",
            key_words=["Matemática", "Cálculo", "Álgebra", "Geometría", "Análisis"],
            enabled=True,
            institution_id=1
        )
        service2 = services.create_service(
            name="Física",
            type="ANALISIS",
            centers="IF",
            description="Física",
            key_words=["Física", "Mecánica", "Óptica", "Termodinámica", "Electricidad", "Magnetismo", "Ondas", "Física Moderna", "Física Cuántica", "Relatividad"],
            enabled=True,
            institution_id=1
        )
        service3 = services.create_service(
            name="Química",
            type="ANALISIS",
            centers="IQ",
            description="Química",
            key_words=["Quimica"],
            enabled=True,
            institution_id=1
        )
        services.create_service(
            name="Biologia",
            type="ANALISIS",
            centers="IB",
            description="Biologia",
            key_words=["Quimica","Biologia", "Biología", "Biología Celular", "Biología Molecular", "Genética", "Bioquímica", "Microbiología", "Botánica", "Zoología", "Ecología", "Fisiología", "Anatomía", "Embriología", "Biología Evolutiva", "Biología del Desarrollo", "Bi"],
            enabled=True,
            institution_id=1
        )
        services.create_service(
            name="Psicologia",
            type="CONSULTORIA",
            centers="IP",
            description="Psicologia",
            key_words=["Quimica","psico"],
            enabled=True,
            institution_id=5
        )
        return service1,service2,service3
    def create_roles():
        rol_permission.create_rol(
            name = "Owner"
        )
        rol_permission.create_rol(
            name = "Admin"
        )
        rol_permission.create_rol(
            name = "SuperAdmin"
        )
        rol_permission.create_rol(
            name = "Operator"
        )
    
    def create_permissions():
        rol_permission.create_permission(
            name="user_index"
        )
        rol_permission.create_permission(
            name="user_show"
        )
        rol_permission.create_permission(
            name="user_update"
        )
        rol_permission.create_permission(
            name="user_create"
        )
        rol_permission.create_permission(
            name="user_destroy"
        )
        rol_permission.create_permission(
            name="user_active"
        )
        rol_permission.create_permission(
            name="user_deactive"
        )

        rol_permission.create_permission(
            name="institution_index"
        )
        
        rol_permission.create_permission(
            name="institution_show"
        )
        
        rol_permission.create_permission(
            name="institution_update"
        )
        
        rol_permission.create_permission(
            name="institution_create"
        )
        
        rol_permission.create_permission(
            name="institution_destroy"
        )
        
        rol_permission.create_permission(
            name="institution_active"
        )
        
        rol_permission.create_permission(
            name="institution_deactive"
        )
        rol_permission.create_permission(
            name="institution_add_owner"
        )
        rol_permission.create_permission(
            name="institution_add_member"
        )
        rol_permission.create_permission(
            name="institution_delete_owner"
        )
        rol_permission.create_permission(
            name="institution_delete_member"
        )

        rol_permission.create_permission(
            name="service_index"
        )
        rol_permission.create_permission(
            name="service_show"
        )
        rol_permission.create_permission(
            name="service_update"
        )
        rol_permission.create_permission(
            name="service_create"
        )
        rol_permission.create_permission(
            name="service_destroy"
        )
        rol_permission.create_permission(
            name="request_index"
        )
        rol_permission.create_permission(
            name="request_show"
        )
        rol_permission.create_permission(
            name="request_update"
            ###Este permiso es para que se cambie el estado de la solicitud o se comente,etc
        )
        rol_permission.create_permission(
            name="request_destroy"
        )
        rol_permission.create_permission(
            name="config_show"
        )
        rol_permission.create_permission(
            name="config_update"
        )      
    
    def create_rol_has_these_permission():
        
        # Permisos del SuperAdmin
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_index"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_show"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_update"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_create"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_destroy"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_active"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_deactive"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_index"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_show"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_update"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_create"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_destroy"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_active"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_deactive"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_index"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_show"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_update"
        )
        
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_create"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_destroy"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_index"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_show"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_update"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_destroy"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "config_show"
        )    
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "config_update"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_add_owner"
        )
        rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_delete_owner"
        )
        
        # Permiso del Owner
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_index"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_update"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_create"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_destroy"
        )
        
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_index"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_show"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_update"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_create"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_destroy"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_index"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_show"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_update"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_destroy"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_add_member"
        )
        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_delete_member"
        )

        rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_show"
        )
        # Permiso del Admin de una institucion
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_index"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_show"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_update"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_create"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_destroy"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_index"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_show"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_update"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_destroy"
        )
        rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="institution_show"
        )
        
        # Permiso del Operador de una institucion
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_index"
        )
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_show"
        )
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_update"
        )
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_create"
        )
        
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "request_index"
        )
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "request_show"
        )
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "request_update"
        )
        rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id ="institution_show"
        )

        # Usuario con mail1@gmail = SuperAdmin
        rol_permission.create_rol_usuario(
            user_id = 1,
            role_id = "SuperAdmin"
        )
        
    def   create_solcitudes_Example_1(service):
        user = auth.create_user(
            email="mail30@gmail.com",
            name="Jay",
            lastname="Dem",
            username="jaye",
            password="1453",
            is_confirmed=True,
            is_active=True
        )
        
        state = service_requests.create_state_request(
            name="inicial",
            state_message = "estado inicial"
        )
        solicitude = service_requests.create_service_request(
            user_id = user.id,
            service_id = service.id,
            state_id = state.id,
            observations ="quiero que se le mida correctamente las dimensiones de los aspectos mas importantes",
            archive = None
        )
        message = service_requests.create_user_message(
            user_id = solicitude.user_id,
            service_request_id = solicitude.id,
            msg_content = "Quisiera saber si se encuentra algun tipo de proporcion en la pintura"            
        )
        message = service_requests.create_user_message(
            user_id = solicitude.user_id,
            service_request_id = solicitude.id,
            msg_content = "En lo posible quisiera conocer un costo estimado"            
        )
    def   create_solcitudes_Example_2(service):
        user = auth.create_user(
            email="mail10@gmail.com",
            name="Juanito",
            lastname="guay",
            username="juan2",
            password="2009",
            is_confirmed=True,
            is_active=True
        )
        
        state = service_requests.create_state_request(
            name="inicial",
            state_message = "estado inicial"
        )
        solicitude = service_requests.create_service_request(
            user_id = user.id,
            service_id = service.id,
            state_id = state.id,
            observations ="aplicar un tratamiento para conocer la edad de la pintura",
            archive = None
        )
        message = service_requests.create_user_message(
            user_id = solicitude.user_id,
            service_request_id = solicitude.id,
            msg_content = "conocer que tipo de pintura se utilizo"            
        )
        message = service_requests.create_user_message(
            user_id = solicitude.user_id,
            service_request_id = solicitude.id,
            msg_content = "En lo posible quisiera conocer un costo estimado"            
        )
    def   create_solcitudes_Example_3(service):
        user = auth.create_user(
            email="mail20@gmail.com",
            name="roman",
            lastname="tamar",
            username="je",
            password="13456",
            is_confirmed=True,
            is_active=True
        )
       
        state = service_requests.create_state_request(
            name="inicial",
            state_message = "estado inicial"
        )
        solicitude = service_requests.create_service_request(
            user_id = user.id,
            service_id = service.id,
            state_id = state.id,
            observations ="conocer el datos de edad de la pintura",
            archive = None
        )
        message = service_requests.create_user_message(
            user_id = solicitude.user_id,
            service_request_id = solicitude.id,
            msg_content = "tener conocimiento sobre la edad de la pintura, que aspecto se puede saber del tipo de pintura utilizada"            
        )
        message = service_requests.create_user_message(
            user_id = solicitude.user_id,
            service_request_id = solicitude.id,
            msg_content = "En lo posible quisiera conocer un costo estimado"            
        )
        
        
        
    create_configurations()
    create_institutions()
    create_users()
    service1,service2,service3 = create_services()
    create_roles()
    create_permissions()
    create_rol_has_these_permission()
    create_solcitudes_Example_1(service1)##De instituto de fmatematica 
    create_solcitudes_Example_2(service2)##De instituto de fisica
    create_solcitudes_Example_3(service3)##De instuto de quimica


