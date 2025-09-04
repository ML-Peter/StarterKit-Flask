from flask import render_template, request, redirect, url_for, session, flash
from models.user import User, db

def register_logic():
    is_authenticated = 'user_id' in session
    username = ''
    password = ''
    confirm_password = ''
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        confirm_password = request.form.get('confirm_password', '')
        if not username or not password or not confirm_password:
            flash("Veuillez remplir tous les champs.", 'error')
            return render_template('auth/register.html', is_authenticated=is_authenticated, username=username, password=password, confirm_password=confirm_password)
        if password != confirm_password:
            flash("Les mots de passe ne correspondent pas.", 'error')
            return render_template('auth/register.html', is_authenticated=is_authenticated, username=username, password='', confirm_password='')
        if len(username) < 2 or len(password) < 6:
            flash("Nom d'utilisateur ou mot de passe trop court.", 'error')
            return render_template('auth/register.html', is_authenticated=is_authenticated, username=username, password='', confirm_password='')
        if User.query.filter_by(username=username).first():
            flash('Ce nom d\'utilisateur est déjà utilisé.', 'error')
            return render_template('auth/register.html', is_authenticated=is_authenticated, username='', password='', confirm_password='')
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Compte créé avec succès ! Connectez-vous.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', is_authenticated=is_authenticated, username=username, password=password, confirm_password=confirm_password)

def login_logic():
    is_authenticated = 'user_id' in session
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not username or not password:
            flash("Veuillez remplir tous les champs.", 'error')
            return render_template('auth/login.html', is_authenticated=is_authenticated, username=username, password=password)
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Connexion réussie !', 'success')
            return redirect(url_for('main.accueil'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect.', 'error')
            return render_template('auth/login.html', is_authenticated=is_authenticated, username=username, password='')
    return render_template('auth/login.html', is_authenticated=is_authenticated, username=username, password=password)

def logout_logic():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Déconnecté avec succès.')
    return redirect(url_for('main.index'))
