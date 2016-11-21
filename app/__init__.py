from flask import Flask, request, render_template

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY=''
)

from app import views
