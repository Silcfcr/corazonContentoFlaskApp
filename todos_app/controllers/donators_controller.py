from todos_app.models.User import User
from todos_app.models.donation import Donation
from todos_app import app
from flask import render_template, request, redirect, session, flash

# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


@app.route("/list_of_donators")
def list_of_donators():
    donators = User.get_all_donators()
    if "user_id" in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one_user_by_id(data)
        return render_template("list_of_donators.html", donators=donators, user=user)
    user = False
    print("Hello", user)
    return render_template("list_of_donators.html", donators=donators, user=user)


@app.route("/register_as_donator")
def register_as_donator():
    return render_template("donator_registry.html")


@app.route("/make_donation")
def make_donation():
    data = {
        "id": session['user_id']
    }
    user = User.get_one_user_by_id(data)
    print(user)
    return render_template("donation_registry.html", user=user)


@app.route("/register_donation", methods=['POST'])
def register_donation():
    print(request.form)
    data = {
        'type': request.form['type'],
        'transport': request.form['transport'],
        'portions': request.form['portions'],
        'expiration': request.form['expiration'],
        'description': request.form['description'],
        'status': request.form['status'],
        'donator_id': request.form['donator_id'],
        'receiver_id': request.form['receiver_id']
    }
    if Donation.validate_donation(data):
        id = Donation.register_new_donation(data)
        return redirect('/dashboard')
    else:
        return redirect('/make_donation')


@app.route("/list_of_donations")
def list_of_available_donations():
    data = {
        "id": session['user_id']
    }
    donations = Donation.get_donator_donations(data)
    return render_template("list_of_donations.html", donations=donations)


@app.route("/see_donation/<int:id>")
def show_donation(id):
    data = {
        'id': id
    }
    donation = Donation.get_one_donation_by_id_with_details(data)
    print(donation)
    return render_template("show_donation.html", donation=donation)


@app.route("/delete_donation/<int:id>")
def delete_donation(id):
    data = {
        'id': id
    }
    deleted = Donation.delete_donation(data)
    print(deleted)
    if deleted != None:
        print(deleted)
        return redirect("/dashboard")
    else:
        print("I wasn't deleted")
        return redirect("/list_of_donations")


@app.route("/show_edit_donation/<int:id>")
def show_edit_donation(id):
    data = {
        'id': int(id)
    }
    donation = Donation.get_one_donation_by_id(data)
    return render_template('edit_donation.html', donation=donation)


@app.route("/edit_donation/<int:id>", methods=['POST'])
def edit_donation(id):
    data = {
        'type': request.form['type'],
        'transport': request.form['transport'],
        'portions': request.form['portions'],
        'expiration': request.form['expiration'],
        'description': request.form['description'],
        'id': id
    }
    donation = Donation.edit_donation(data)
    print(donation)
    print("i've edited")
    return redirect(f'/list_of_donations')
