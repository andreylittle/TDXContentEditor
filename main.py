from app import create_app
from flask import request, abort

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

