from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Post
from . import db
import json

view = Blueprint('view', __name__)

@view.route('/', methods=['GET'])
def home():
    return render_template('home.html', user=current_user)

@view.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@view.route('/post', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'POST':
        post_title = request.form.get('title')
        post_text = request.form.get('text')
        new_post = Post(title=post_title, content=post_text, user_id=current_user.id, username=current_user.username)
        db.session.add(new_post)
        db.session.commit()

    return render_template('post.html', user=current_user)

@view.route('/forum', methods=['GET'])
def forum():
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    posts = Post.query.order_by(Post.date)
    users = User.query
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
        return jsonify({})