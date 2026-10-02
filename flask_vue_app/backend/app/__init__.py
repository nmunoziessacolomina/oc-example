from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    with app.app_context():
        db.create_all()  # Create tables
        from .models import Post
        # Seed initial data if table is empty
        if not Post.query.first():
            mock_posts = [
                Post(title='First Post', content='Content of the first post', author='Author 1'),
                Post(title='Second Post', content='Content of the second post', author='Author 2')
            ]
            db.session.bulk_save_objects(mock_posts)
            db.session.commit()

    return app
