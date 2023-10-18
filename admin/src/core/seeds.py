from src.core import institutions, configuration, auth, rol_permission

def run():
    def create_institutions():
        inst1 = institutions.create_institution(
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
        inst2 = institutions.create_institution(
            name="Instituto de Física",
            information="Instituto de Física",
            address="Rua do Matão, 1371 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://portal.if.usp.br/",
            keywords="Física",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-6149",
            is_active=True
        )
        inst3 = institutions.create_institution(
            name="Instituto de Química",
            information="Instituto de Química",
            address="Av. Prof. Lineu Prestes, 748 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://www.iq.usp.br/",
            keywords="Química",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-6149",
            is_active=True
        )
        inst4 = institutions.create_institution(
            name="Instituto de Biociências",
            information="Instituto de Biociências",
            address="Rua do Matão, 277 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://ib.usp.br/",
            keywords="Biologia",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-6149",
            is_active=True
        )
        inst5 = institutions.create_institution(
            name="Instituto de Psicologia",
            information="Instituto de Psicologia",
            address="Av. Prof. Mello Moraes, 1721 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://www.ip.usp.br/",
            keywords="Psicologia",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-6149",
            is_active=True
        )
        inst6 = institutions.create_institution(
            name="Instituto de Ciências Biomédicas",
            information="Instituto de Ciências Biomédicas",
            address="Av. Prof. Lineu Prestes, 1524 - Cidade Universitária - Butantã - São Paulo - SP",
            localization="São Paulo - SP",
            web="https://icb.usp.br/",
            keywords="Biologia, Medicina",
            attention_time="Segunda à Sexta das 8h às 17h",
            contact="11 3091-6149",
            is_active=True
        )
    def create_users():
        user1 = auth.create_user(
            email="mail1@gmail.com",
            name="Jane",
            lastname="Doe",
            username="jane",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        user2 = auth.create_user(
            email="mail2@gmail.com",
            name="John",
            lastname="Doe",
            username="john",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        user3 = auth.create_user(
            email="mail3@gmail.com",
            name="Alice",
            lastname="Doe",
            username="alice",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        user4 = auth.create_user(
            email="mail4@gmail.com",
            name="Bob",
            lastname="Doe",
            username="bob",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        user5 = auth.create_user(
            email="mail5@gmail.com",
            name="Eve",
            lastname="Doe",
            username="eve",
            password="123456",
            is_confirmed=True,
            is_active=True
        )
        user6 = auth.create_user(
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
        
    def create_roles():
        rol1 = rol_permission.create_rol(
            name = "Owner"
        )
        rol2 = rol_permission.create_rol(
            name = "Admin"
        )
        rol3 = rol_permission.create_rol(
            name = "SuperAdmin"
        )
        rol4 = rol_permission.create_rol(
            name = "Operator"
        )
    def create_permissions():
        user_index = rol_permission.create_permission(
            name="user_index"
        )
        user_show = rol_permission.create_permission(
            name="user_show"
        )
        user_update = rol_permission.create_permission(
            name="user_update"
        )
        user_create = rol_permission.create_permission(
            name="user_create"
        )
        user_destroy = rol_permission.create_permission(
            name="user_destroy"
        )
        user_active = rol_permission.create_permission(
            name="user_active"
        )
        user_deactive = rol_permission.create_permission(
            name="user_deactive"
        )
        
        institution1 = rol_permission.create_permission(
            name="institution_index"
        )
        
        institution2 = rol_permission.create_permission(
            name="institution_show"
        )
        
        institution3 = rol_permission.create_permission(
            name="institution_update"
        )
        
        institution4 = rol_permission.create_permission(
            name="institution_create"
        )
        
        institution5 = rol_permission.create_permission(
            name="institution_destroy"
        )
        
        institution6 = rol_permission.create_permission(
            name="institution_active"
        )
        
        institution7 = rol_permission.create_permission(
            name="institution_deactive"
        )
        
        service1 = rol_permission.create_permission(
            name="service_index"
        )
        service2 = rol_permission.create_permission(
            name="service_show"
        )
        service3 = rol_permission.create_permission(
            name="service_update"
        )
        service4 = rol_permission.create_permission(
            name="service_create"
        )
        service5 = rol_permission.create_permission(
            name="service_destroy"
        )
        request1 = rol_permission.create_permission(
            name="request_index"
        )
        request2 = rol_permission.create_permission(
            name="request_show"
        )
        request3 = rol_permission.create_permission(
            name="request_update"
            ###Este permiso es para que se cambie el estado de la solicitud o se comente,etc
        )
        request4 = rol_permission.create_permission(
            name="request_destroy"
        )
        config1 = rol_permission.create_permission(
            name="config_show"
        )
        config2 = rol_permission.create_permission(
            name="config_update"
        )
        
    def create_rol_has_these_permission():
        
        role_SuperAdmin1= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_index"
        )
        
        role_SuperAdmin2= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_show"
        )
        
        role_SuperAdmin3= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_update"
        )
        
        role_SuperAdmin4= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_create"
        )
        role_SuperAdmin5= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_destroy"
        )
        role_SuperAdmin6= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_active"
        )
        
        role_SuperAdmin7= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "user_deactive"
        )
        role_SuperAdmin8= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_index"
        )
        
        role_SuperAdmin9= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_show"
        )
        
        role_SuperAdmin10= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_update"
        )
        
        role_SuperAdmin11= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_create"
        )
        role_SuperAdmin12= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_destroy"
        )
        role_SuperAdmin13= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_active"
        )
        
        role_SuperAdmin14= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "institution_deactive"
        )
        role_SuperAdmin15= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_index"
        )
        
        role_SuperAdmin16= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_show"
        )
        
        role_SuperAdmin17= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_update"
        )
        
        role_SuperAdmin18= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_create"
        )
        role_SuperAdmin19= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "service_destroy"
        )
        role_SuperAdmin22= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_index"
        )
        role_SuperAdmin23= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_show"
        )
        role_SuperAdmin24= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_update"
        )
        role_SuperAdmin26= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "request_destroy"
        )
        role_SuperAdmin27= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "config_show"
        )    
        role_SuperAdmin28= rol_permission.create_rol_permission(
            role_id ="SuperAdmin",
            permission_id = "config_update"
        )
        ###permisos del Owner        
        role_Owner5 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_index"
        )
        role_Owner6 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_show"
        )
        role_Owner7 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_update"
        )
        role_Owner8 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_create"
        )
        role_Owner9 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="service_destroy"
        )
        role_Owner10 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_index"
        )
        role_Owner11 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_show"
        )
        role_Owner12 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_update"
        )
        role_Owner13 = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="request_destroy"
        )
        role_Owner_Show_Institution = rol_permission.create_rol_permission(
            role_id = "Owner",
            permission_id ="institution_show"
        )
        ###Aca van los permisos del admin de una institucion
        role_Admin1 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_index"
        )
        role_Admin2 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_show"
        )
        role_Admin3 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_update"
        )
        role_Admin4 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_create"
        )
        role_Admin5 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="service_destroy"
        )
        role_Admin6 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_index"
        )
        role_Admin7 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_show"
        )
        role_Admin8 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_update"
        )
        role_Admin9 = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="request_destroy"
        )
        role_Admin_Show_Institution = rol_permission.create_rol_permission(
            role_id = "Admin",
            permission_id ="institution_show"
        )
        
        ###Aca van los permisos del operator
        role_Operator1 = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_index"
        )
        role_Operator2 = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_show"
        )
        role_Operator3 = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_update"
        )
        role_Operator4 = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "service_create"
        )
        
        role_Operator5 = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "request_index"
        )
        role_Operator6 = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "request_show"
        )
        role_Operator7 = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id = "request_update"
        )
        role_Operator_Show_Institution = rol_permission.create_rol_permission(
            role_id = "Operator",
            permission_id ="institution_show"
        )
        
    create_configurations()
    create_institutions()
    create_users()
    create_roles()
    create_permissions()
    create_rol_has_these_permission()


