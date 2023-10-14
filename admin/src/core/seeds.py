from src.core import institutions, configuration, auth

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
    create_institutions()
    create_users()


