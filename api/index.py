from flask import Flask, render_template

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

# ✅ Required for Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
