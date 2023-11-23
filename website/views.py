from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy import desc
from .models import User, Post
from . import db
import json

view = Blueprint('view', __name__)

@view.route('/', methods=['GET'])
def home():
    return render_template('home.html', user=current_user)

@view.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        credits = request.form.get('credits')
        if credits.isdigit() == False:
            flash('Please give a valid input.', "error")
        else:
            credits = int(credits)
            current_user.credit = current_user.credit + credits
            db.session.commit()
    return render_template('profile.html', user=current_user)

@view.route('/post', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'POST':
        post_title = request.form.get('title')
        post_text = request.form.get('text')
        new_post = Post(title=post_title, content=post_text, user_id=current_user.id, username=current_user.username, credit=0)
        db.session.add(new_post)
        db.session.commit()

    return render_template('post.html', user=current_user)

@view.route('/forum', methods=['GET'])
def forum():
    username = request.form.get('username')
    posts = Post.query.order_by(desc(Post.credit)).all()
    return render_template('forum.html', user=current_user, posts=posts)

@view.route('/delete-post', methods=['POST'])
def delete_post():
    post = json.loads(request.data)
    postId = post['postId']
    #data = request.get_json()
    #noteId = data.get('noteId')
    post = Post.query.get(postId)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()
            flash('Post deleted!', category='success')
        return jsonify({})
    
@view.route('/donate', methods=['POST'])
def donate():
    post = json.loads(request.data)
    postId = post['postId']
    post = Post.query.get(postId)
    credits_sender = current_user.credit
    receiver = User.query.filter_by(id=post.user_id).first()
    if post:
        if post.user_id == current_user.id:
            flash('You cannot gift yourself credits.', category='error')
        elif credits_sender < 10:
            flash('Not enough credits!', category='error')
        else:
            receiver.credit = receiver.credit + 10
            current_user.credit = current_user.credit - 10
            post.credit = post.credit + 5
            db.session.commit()
            flash('Credits have been gifted!', 'success')
        return jsonify({})
    
@view.route("/gift", methods=['GET', 'POST'])
def gift():
    if request.method == 'POST':
        username = request.form.get('username')
        credits = request.form.get('credits')
        user = User.query.filter_by(username=username).first()
        if user:
            if username == current_user.username:
                flash('You cannot gift yourself', 'error')
            elif credits.isdigit() == False:
                flash('Please give a valid input', 'error')
            else:
                credits = int(credits)
                if current_user.credit < credits:
                    flash('You do not have enough credits.', 'error')
                else:
                    user.credit = user.credit + credits
                    current_user.credit = current_user.credit - credits
                    db.session.commit()
                    flash('Your gift has been sent!', 'success')
        else:
            flash('This user does not exist.', 'error')
    return render_template('gift.html', user=current_user)
    