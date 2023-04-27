from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <body style="background-color:powderblue;">

    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()