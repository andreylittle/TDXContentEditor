from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'DifferentSecret'




    from app.home import home
    from app.NotificationTemplateEditor import NotificationTemplateEditor
    from app.HtmlModuleEditor import HtmlModuleEditor
    from app.feedback import feedback

    app.register_blueprint(home.home, url_prefix="/")
    app.register_blueprint(NotificationTemplateEditor.NotificationEditor, url_prefix="/NotificationEditor")
    app.register_blueprint(HtmlModuleEditor.HTMLModuleEditor, url_prefix="/HtmlModuleEditor")
    app.register_blueprint(feedback.feedback, url_prefix="/Feedback")




    return app
