from todos_app.config.MySQLConnection import connectToMySQL
from flask import flash


class Donation:
    db = "corazon_lleno_2"

    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']
        self.transport = data['transport']
        self.portions = data['portions']
        self.expiration = data['expiration']
        self.description = data['description']
        self.donator_id = data['donator_id']
        self.status = data['status']
        self.receiver_id = data['receiver_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register_new_donation(cls, data):
        query = "INSERT INTO donations (type,transport, portions,expiration,description,status, donator_id,receiver_id) VALUES (%(type)s,%(transport)s,%(portions)s,%(expiration)s,%(description)s,%(status)s,%(donator_id)s,%(receiver_id)s);"
        print("change made")
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def change_donation_status(cls, data):
        query = "UPDATE donations SET status=%(status)s, receiver_id=%(receiver_id)s WHERE id= %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_donation(cls, data):
        query = "DELETE FROM donations WHERE id=%(id)s AND status = 'disponible';"
        print(query)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def edit_donation(cls, data):
        query = "UPDATE donations SET type=%(type)s, transport=%(transport)s, portions=%(portions)s, expiration=%(expiration)s, description=%(description)s WHERE id= %(id)s;"
        print('query completed', query)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_one_donation_by_id(cls, data):
        query = "SELECT * FROM donations WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
        print(cls(results[0]))

    @classmethod
    def get_one_donation_by_id_with_details(cls, data):
        query = "SELECT * FROM donations JOIN users as donators on donations.donator_id = donators.id WHERE donations.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        print(results[0])
        return (results[0])

    @classmethod
    def get_all_donations(cls):
        query = "SELECT * FROM donations;"
        results = connectToMySQL(cls.db).query_db(query)
        if not results:
            return False
        return results

    @classmethod
    def get_all_available_donations(cls):
        query = "SELECT * FROM donations WHERE status ='disponible';"
        results = connectToMySQL(cls.db).query_db(query)
        if not results:
            return False
        return results

    @classmethod
    def get_all_claimed_donations(cls, data):
        query = "SELECT * FROM donations WHERE (status ='solicitada'  AND receiver_id = %(id)s) OR (status ='entregada'  AND receiver_id = %(id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return results

    @classmethod
    def get_donator_donations(cls, data):
        query = "SELECT * FROM donations WHERE donator_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return results

    @staticmethod
    def validate_donation(data):
        is_valid = True
        # for name
        if len(data['description']) < 3:
            flash("Porfavor provea una descripción detallada de su donación", "donation")
            is_valid = False
        if int(data['portions']) < 10:
            flash("La donación debe ser mayor a 10 porciones", "donation")
            is_valid = False
        return is_valid
