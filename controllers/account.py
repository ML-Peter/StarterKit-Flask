from flask import render_template, request, redirect, url_for, session, flash
from models.account import Account, db
from models.user import User

def profile_logic():
    if 'user_id' not in session:
        flash("Vous devez être connecté pour accéder à votre profil.")
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    account = Account.query.filter_by(user_id=user.id).first()
    return render_template('account/profile.html', user=user, account=account, is_authenticated=True, username=user.username)

def edit_logic():
    if 'user_id' not in session:
        flash("Vous devez être connecté pour modifier votre profil.")
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    account = Account.query.filter_by(user_id=user.id).first()
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        bio = request.form['bio']
        if not account:
            account = Account(user_id=user.id, full_name=full_name, email=email, bio=bio)
            db.session.add(account)
        else:
            account.full_name = full_name
            account.email = email
            account.bio = bio
        db.session.commit()
        flash('Profil mis à jour !')
        return redirect(url_for('account.profile'))
    return render_template('account/edit.html', user=user, account=account, is_authenticated=True, username=user.username)

def delete_account_logic():
    if 'user_id' not in session:
        flash("Vous devez être connecté pour supprimer votre compte.")
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    account = Account.query.filter_by(user_id=user.id).first()
    if account:
        db.session.delete(account)
    db.session.delete(user)
    db.session.commit()
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Votre compte a été supprimé avec succès.')
    return redirect(url_for('main.index'))
