from app import create_app
from flask import request, abort

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


allowed_routes = {
    "/":["GET"],
    "/NotificationEditor/": ["GET"],
    "/NotificationEditor/ChangeLog": ["GET"],
    "/NotificationEditor/DownloadDefaultTemplates": ["POST"],
    "/ModuleEditor/": ["GET"],
}
@app.before_request
def block_ip():
    ip = request.headers['X-Real-IP']

    route=request.path
    method = request.method

    if route in allowed_routes:
        if method not in allowed_routes[route]:
            abort(405)