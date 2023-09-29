from flask import Flask, render_template

app = Flask(__name__)

@main_bp.route('/')
def welcome():
    return render_template('welcome.html')


