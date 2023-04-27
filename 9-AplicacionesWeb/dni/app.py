from flask import Flask, request, render_template
from valida import validaDNI

app = Flask(__name__,template_folder='html')

def home2():
    return render_template('DNIval.html')

@app.route("/")
def home():
    return f"""
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

@app.route("/validar", methods=['POST'])
def validacionDN():
    dniPaginaWeb = request.form["dni"]
    letraPaginaWeb = request.form["letra"]
    resultado = validaDNI(dniPaginaWeb,letraPaginaWeb)
    return render_template('DNIvalr.html',dni=dniPaginaWeb,letra=letraPaginaWeb,resultado=resultado)


if __name__ == '__main__':
   app.run(debug=True)