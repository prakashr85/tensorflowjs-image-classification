from flask import Flask, render_template, url_for, request


app = Flask(__name__)

@app.route("/classify/")
def classify():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
