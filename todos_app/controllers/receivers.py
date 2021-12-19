from todos_app.models.User import User
from todos_app.models.donation import Donation
from todos_app import app
from flask import render_template, request, redirect, session, flash


@app.route("/list_of_receivers")
def list_of_receivers():
    receivers = User.get_all_receivers()
    print(receivers)
    if "user_id" in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one_user_by_id(data)
        return render_template("list_of_receivers.html", receivers=receivers, user=user)
    user = False
    return render_template("list_of_receivers.html", receivers=receivers, user=user)


@app.route("/register_as_receiver")
def register_as_receiver():
    return render_template("receiver_registry.html")


@app.route("/show_receiver/<int:id>")
def show_receiver(id):
    print("i GOT HERE")
    data = {
        "id": id
    }
    receiver = User.get_one_user_by_id(data)
    print(receiver)
    return render_template("show_receiver.html", receiver=receiver)


@app.route("/claim_donation/<int:id>")
def claim_donation(id):
    data = {
        'id': id,
        'status': "solicitada",
        'receiver_id': session['user_id']
    }
    donation = Donation.change_donation_status(data)
    print(donation)
    print("Yes!")
    return redirect('/dashboard')


@app.route("/delivered_donation/<int:id>")
def delivered_donation(id):
    data = {
        'id': id,
        'status': "entregada",
        'receiver_id': session['user_id']
    }
    donation = Donation.change_donation_status(data)
    print(donation)
    print("Yes!")
    return redirect('/dashboard')
