from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    hash_result = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        hash_result = hashlib.md5(text.encode()).hexdigest()
    return render_template("index.html", hash_result=hash_result)


if __name__ == "__main__":
    app.run(debug=True)