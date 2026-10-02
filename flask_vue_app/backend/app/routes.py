from flask import Blueprint, jsonify, request
from .models import Post, db
from datetime import datetime
import traceback

print("Routes module loaded")

api = Blueprint('api', __name__)

@api.route('/posts', methods=['GET'])
def get_posts():
    try:
        print("Received GET request for /posts")
        posts = Post.query.all()
        return jsonify([{
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author,
            'created_at': post.created_at.isoformat() if post.created_at else None,
            'updated_at': post.updated_at.isoformat() if post.updated_at else None
        } for post in posts])
    except Exception as e:
        print(f"Error in get_posts: {e}")
        traceback.print_exc()
        return jsonify({"error": "Internal server error"}), 500

@api.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(
        title=data['title'],
        content=data['content'],
        author=data['author']
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({
        'id': new_post.id,
        'title': new_post.title,
        'content': new_post.content,
        'author': new_post.author,
        'created_at': new_post.created_at.isoformat() if new_post.created_at else None,
        'updated_at': new_post.updated_at.isoformat() if new_post.updated_at else None
    }), 201

@api.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    print(f"GET request for post {post_id}")
    post = Post.query.get_or_404(post_id)
    print(f"Found post: {post}")
    return jsonify({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author,
        'created_at': post.created_at.isoformat() if post.created_at else None,
        'updated_at': post.updated_at.isoformat() if post.updated_at else None
    })

@api.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    post.author = data.get('author', post.author)
    post.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author,
        'created_at': post.created_at.isoformat() if post.created_at else None,
        'updated_at': post.updated_at.isoformat() if post.updated_at else None
    })

@api.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return '', 204

# More routes can be added here
