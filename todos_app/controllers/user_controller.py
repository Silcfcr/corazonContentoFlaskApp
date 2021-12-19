from todos_app.models.User import User
from todos_app.models.donation import Donation
from todos_app import app
from flask import render_template, request, redirect, session, flash

# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


@app.route("/")
def landing_page():
    if 'user_id' in session:
        return redirect("/dashboard")
    return render_template("landing_page.html")


@app.route("/register")
def register_new_user():
    return render_template("choose_register.html")


@app.route("/register_user", methods=['POST'])
def register_receiver():
    datatoValidate = {
        'name': request.form['name'],
        'type': request.form['type'],
        'user_type': request.form['user_type'],
        'population': request.form['population'],
        'state': request.form['state'],
        'city': request.form['city'],
        'address': request.form['address'],
        'contact_first_name': request.form['contact_first_name'],
        'contact_last_name': request.form['contact_last_name'],
        'contact_phone': request.form['contact_phone'],
        'contact_email': request.form['contact_email'],
        'password': request.form['password'],
        'cpassword': request.form['cpassword']
    }

    print(datatoValidate)
    # pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'name': request.form['name'],
        'type': request.form['type'],
        'user_type': request.form['user_type'],
        'population': request.form['population'],
        'state': request.form['state'],
        'city': request.form['city'],
        'address': request.form['address'],
        'contact_first_name': request.form['contact_first_name'],
        'contact_last_name': request.form['contact_last_name'],
        'contact_phone': request.form['contact_phone'],
        'contact_email': request.form['contact_email'],
        'password': request.form['password']
    }

    if User.validate_user(datatoValidate):
        id = User.register_new_user(data)
        session['user_id'] = id
        session['user_type'] = request.form['user_type']
        data = {
            "id": id
        }
        return redirect("/dashboard")
    else:
        print('Error with registration!')
        return redirect("/register")


@app.route("/login")
def display_login():
    return render_template("login.html")


@app.route("/login_user", methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    user = User.get_one_user_by_email(data)
    print(user)
    if not user:
        flash("El email no se encuentra registrado", "login")
        return redirect('/login')
    # if not bcrypt.check_password_hash(user.password, data['password']):
    #     flash("La contraseña es incorrecta","login")
    #     return redirect('/login')

    session['user_id'] = user.id
    session['user_type'] = user.user_type
    print(session)

    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    data = {
        'id': session['user_id']
    }
    user = User.get_one_user_by_id(data)
    if session['user_type'] == 'receiver':
        donations = Donation.get_all_available_donations()
        claimed_donations = Donation.get_all_claimed_donations(data)
        print(donations)
        return render_template("receiver_dashboard.html", receiver=user, donations=donations, claimed_donations=claimed_donations)
    else:
        return render_template("donator_dashboard.html", donator=user)


@app.route("/logout")
def logout():
    session.clear()
    return render_template("landing_page.html")
