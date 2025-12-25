from flask import Flask, render_template, request

app = Flask(__name__)

# Database (simple)
restaurants = {
    "pizza": "Pizza Hut",
    "burger": "McDonalds",
    "shawarma": "Abu Ahmad",
    "pasta": "Italiano Restaurant"
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        meal = request.form["meal"].lower()
        result = restaurants.get(meal, "No restaurant found")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
