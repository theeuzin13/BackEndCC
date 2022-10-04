from flask import Flask, render_template, request
import os

app = Flask(__name__)

#route -> controlcar.com/  seria o endereço
#function -> o que quer exibir na tela

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/supply")
def supply():
    return render_template("supply.html")

@app.route("/about")
def about():
    return render_template("about.html")

#up site
if __name__ == "__main__":
    app.run(debug=True)