from flask import Flask, render_template

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

# Required for Vercel handler
def handler(environ, start_response):
    return app(environ, start_response)

app.run()