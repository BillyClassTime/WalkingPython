from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()