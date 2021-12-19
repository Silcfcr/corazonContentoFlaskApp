from flask import flash
from todos_app.config.MySQLConnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db = "corazon_lleno_2"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user_type = data['user_type']
        self.type = data['type']
        self.population = data['population']
        self.state = data['state']
        self.city = data['city']
        self.address = data['address']
        self.contact_first_name = data['contact_first_name']
        self.contact_last_name = data['contact_last_name']
        self.contact_phone = data['contact_phone']
        self.contact_email = data['contact_email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register_new_user(cls, data):
        query = "INSERT INTO users (name, type,user_type, population,state,city,address,contact_first_name, contact_last_name, contact_phone, contact_email, password) VALUES (%(name)s,%(type)s,%(user_type)s,%(population)s, %(state)s,%(city)s,%(address)s,%(contact_first_name)s,%(contact_last_name)s,%(contact_phone)s,%(contact_email)s,%(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_one_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
        print(cls(results[0]))

    @classmethod
    def get_one_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE contact_email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
        print(cls(results[0]))

    @classmethod
    def get_all_donators(cls):
        query = "SELECT * FROM users WHERE user_type = 'donator';"
        results = connectToMySQL(cls.db).query_db(query)
        if not results:
            return False
        return results

    @classmethod
    def get_all_receivers(cls):
        query = "SELECT * FROM users WHERE user_type = 'receiver';"
        results = connectToMySQL(cls.db).query_db(query)
        if not results:
            return False
        return results

    @staticmethod
    def validate_user(data):
        is_valid = True
        query = "SELECT * from users WHERE contact_email = %(contact_email)s;"
        results = connectToMySQL("corazon_lleno_2").query_db(query, data)
        print(results)
        # for name
        if len(data['name']) < 3:
            flash(
                "Nombre de la institución debe tener mínimo 3 letras, favor no utilizar acrónimos", "register")
            is_valid = False
        if data['user_type'] == 'receiver':
            if int(data['population']) < 1:
                flash("La población debe ser mayor a 1", "register")
                is_valid = False
        # for city
        if len(data['city']) < 3:
            flash("El nombre del cantón debe tener mínimo 3 letras", "register")
            is_valid = False
        if len(data['address']) < 3:
            flash("La dirección debe ser mas detallada", "register")
            is_valid = False

        # for contact person info
        if len(data['contact_first_name']) < 3:
            flash("Nombre debe tener mínimo 3 letras", "contact_info")
            is_valid = False
        if len(data['contact_last_name']) < 3:
            flash("Apellidos deben tener mínimo 3 letras", "contact_info")
            is_valid = False
         # for phone
        if len(data['contact_phone']) != 8:
            flash("Número de teléfono debe contener 8 dígitos", "contact_info")
            is_valid = False
        # for email
        if results != False:
            if len(results) >= 1:
                flash("Este email ya fue registrado", "contact_info")
                is_valid = False
        # for email
        if not EMAIL_REGEX.match(data['contact_email']):
            flash("El email proporcionado es inválido", "contact_info")
            is_valid = False
        # for password
            is_valid = False
        if len(data['password']) < 5:
            flash("La contraseña debe contener mínimo 5 caracteres", "contact_info")
            is_valid = False
        if (data['password'] != data['cpassword']):
            flash("Las contraseñas no coinciden", "contact_info")
            is_valid = False
        return is_valid
