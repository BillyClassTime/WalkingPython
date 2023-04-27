from flask import Flask,request
import LetraDNI
app = Flask(__name__)

@app.route('/')
def index():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Validar DNI</title>
    </head>
    <body>
        <h1>Validar DNI</h1>
        <form method="post" action="/validar">
            <label for="numero">Número:</label>
            <input type="number" name="dni" id="dni">
            <br>
            <label for="letra">Letra:</label>
            <input type="text" name="letra" id="letra" maxlength="1">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     letraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
     dniPagWeb= request.form["dni"]
     letPagWeb= request.form["letra"]
     resultado=LetraDNI.LetraDNI(dniPagWeb,letPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Validar DNI</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """
if __name__ == "__main__":
    app.run()