from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("encuesta.html")

@app.route("/resultados", methods=["POST"])
def resultados():
    lenguaje = request.form.get("lenguaje")
    experiencia = request.form.get("experiencia")
    editor = request.form.get("editor")
    return render_template("resultados.html",
                            lenguaje=lenguaje,
                            experiencia=experiencia,
                            editor=editor)

if __name__ == "__main__":
    app.run(debug=True)