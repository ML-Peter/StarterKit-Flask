
from flask import render_template, session, flash, redirect, url_for

def index_logic():
    is_authenticated = 'user_id' in session
    username = session.get('username')
    return render_template("index.html", is_authenticated=is_authenticated, username=username)

def accueil_logic():
    if 'user_id' not in session:
        flash("Vous devez être connecté pour accéder à l'accueil.")
        return redirect(url_for('auth.login'))
    username = session.get('username')
    return render_template("accueil.html", is_authenticated=True, username=username)
