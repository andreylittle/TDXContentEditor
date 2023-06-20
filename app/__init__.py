from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DifferentSecret'

    from app.NotificationTemplateEditor import NotificationTemplateEditor

    app.register_blueprint(NotificationTemplateEditor.NotificationEditor, url_prefix="/NotificationEditor")




    return app