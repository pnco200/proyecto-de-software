from src.core import institutions, configuration, auth, rol_permission, services, service_requests

def run():
    def create_institutions():
        institutions.create_institution(
            name="Instituto de Matematica",
            information="Instituto de Matematica e Estatistica",
            address="Buenos Aires",
            localization= [
                "-34.6118", 
                "-58.4173"
            ],
            web="https://www.ime.usp.br/",
            keywords="Matematica, Estatistica, Computacao",
            attention_time="Segunda a Sexta das 8h as 17h",
            contact="11 3091-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Fisica",
            information="Instituto de Fisica",
            address="Cordoba",
            localization= [
                "-31.4201",
                "-64.1888"
            ],
            web="https://portal.if.usp.br/",
            keywords="Fisica",
            attention_time="Segunda a Sexta das 8h as 17h",
            contact="11 309-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Quimica",
            information="Instituto de Quimica",
            address="Mendoza",
            localization= [
                "-32.8908",
                "-68.8272"
            ],
            web="https://www.iq.usp.br/",
            keywords="Quimica",
            attention_time="Segunda a Sexta das 8h as 17h",
            contact="11 091-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Biociencias",
            information="Instituto de Biociencias",
            address="Resistencia",
            localization= [
                "-27.4661",
                "-58.8300"
            ],
            web="https://ib.usp.br/",
            keywords="Biologia",
            attention_time="Segunda a Sexta das 8h as 17h",
            contact="11 91-6149",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Psicologia",
            information="Instituto de Psicologia",
            address="Salta",
            localization= [
                "-24.7821",
                "-65.4125"
            ],
            web="https://www.ip.usp.br/",
            keywords="Psicologia",
            attention_time="Segunda a Sexta das 8h as 17h",
            contact="11 3091-49",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Ciencias Biomedicas",
            information="Instituto de Ciencias Biomedicas",
            address="La Rioja",
            localization= [
                "-29.4689",
                "-66.8509"
            ],
            web="https://icb.usp.br/",
            keywords="Biologia, Medicina",
            attention_time="Segunda a Sexta das 8h as 17h",
            contact="11 3091-9",
            is_active=True
        )
        institutions.create_institution(
            name="Instituto de Computação",
            information="Instituto de Ciências Matemáticas e de Computação",
            address="San Carlos de Bariloche",
            localization= [
                "-41.1335",
                "-71.3107"
            ],
            web="https://www.icmc.usp.br/",
            keywords="Matemática, Computação",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="16 3373-9",
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
            maintenance_message="El sitio se encuentra en mantenimiento",
        )
    def create_services():
        service1 = services.create_service(
            name="Matematica",
            type="ANALISIS",
            centers="IME",
            description="Matematica",
            key_words=["Matematica", "Calculo", "Algebra", "Geometria", "Analisis"],
            enabled=True,
            institution_id=1
        )
        service2 = services.create_service(
            name="Fisica",
            type="ANALISIS",
            centers="IF",
            description="Fisica",
            key_words=["Fisica", "Mecanica", "Optica", "Termodinamica", "Electricidad", "Magnetismo", "Ondas", "Fisica Moderna", "Fisica Cuantica", "Relatividad"],
            enabled=True,
            institution_id=2
        )
        service3 = services.create_service(
            name="Quimica",
            type="ANALISIS",
            centers="IQ",
            description="Quimica",
            key_words=["Quimica"],
            enabled=True,
            institution_id=3
        )
        service4 = services.create_service(
            name="Biologia",
            type="ANALISIS",
            centers="IB",
            description="Biologia",
            key_words=["Quimica", "Biologia", "Biologia", "Biologia Celular", "Biologia Molecular", "Genetica", "Bioquimica", "Microbiologia", "Botanica", "Zoologia", "Ecologia", "Fisiologia", "Anatomia", "Embriologia", "Biologia Evolutiva", "Biologia del Desarrollo", "Bi"],
            enabled=True,
            institution_id=3
        )
        service5 = services.create_service(
            name="Psicologia",
            type="CONSULTORIA",
            centers="IP",
            description="Psicologia",
            key_words=["Quimica", "psico"],
            enabled=True,
            institution_id=5
        )
        service6 = services.create_service(
            name="biociencia",
            type="CONSULTORIA",
            centers="IP",
            description="biocientifico",
            key_words=["Quimica"],
            enabled=True,
            institution_id=4
        )
        service7 = services.create_service(
            name="Biomedicina aplicada",
            type="CONSULTORIA",
            centers="IP",
            description="Bio",
            key_words=["Quimica","Bio"],
            enabled=True,
            institution_id=6
        )        
        service8 = services.create_service(
            name="Computo",
            type="CONSULTORIA",
            centers="IP",
            description="Computos terrenales",
            key_words=["Computacion"],
            enabled=True,
            institution_id=7
        )
        return service1,service2,service3, service4, service5, service6, service7, service8
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
    def create_state_finalizada():
        return service_requests.create_state_request(
            name="finalizada",
            state_message = "Fin"
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
        user = auth.get_random_user()
        
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

        service_requests.set_new_state_seeds(create_state_finalizada(), solicitude.id)

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
        user = auth.get_random_user()
        
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
        user = auth.get_random_user()
       
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
    service1,service2,service3, service4, service5, service6, service7, service8 = create_services()
    create_roles()
    create_permissions()
    create_rol_has_these_permission()
    create_solcitudes_Example_1(service1)
    create_solcitudes_Example_2(service2)
    create_solcitudes_Example_3(service3)
    create_solcitudes_Example_1(service4)
    create_solcitudes_Example_1(service5)
    create_solcitudes_Example_1(service5)
    create_solcitudes_Example_1(service5)
    create_solcitudes_Example_1(service1)
    create_solcitudes_Example_1(service1)
    create_solcitudes_Example_1(service2)
    create_solcitudes_Example_1(service2)
    create_solcitudes_Example_1(service6)
    create_solcitudes_Example_1(service6)
    create_solcitudes_Example_1(service7)
    create_solcitudes_Example_1(service7)
    create_solcitudes_Example_1(service8)







