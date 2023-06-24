from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DifferentSecret'


    from app.home import home
    from app.NotificationTemplateEditor import NotificationTemplateEditor
    from app.HtmlModuleEditor import HTMLModuleEditor

    app.register_blueprint(home.home, url_prefix="/")
    app.register_blueprint(NotificationTemplateEditor.NotificationEditor, url_prefix="/NotificationEditor")
    app.register_blueprint(HTMLModuleEditor.HTMLModuleEditor, url_prefix="/ModuleEditor")




    return app
