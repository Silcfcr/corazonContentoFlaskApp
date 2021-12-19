from flask import Flask, render_template, request, redirect, session
from todos_app import app
from todos_app.controllers import donators_controller, user_controller, receivers

if __name__ == "__main__":
    app.run(debug=True)
