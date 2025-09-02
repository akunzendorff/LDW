from flask import render_template, request, redirect, url_for

def init(app):
    
    @app.route('/')
    def home():
        return render_template('index.html')