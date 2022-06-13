from flask import Flask, render_template
app = Flask(__name__)

# some code for the routes andd endpoints
list_todos = [{
    "todo":"learn Templates in flask",
    "status":"in progres",
},
{
    "todo":"learn Objests Orientation Programing",
    "status":"complete"
},
{
    "todo":"learn Deployment",
    "status": "cancel"
}]

app.route("/")
@app.route("/Home")
def home():
    return render_template("index.html", first_name = "Lenddy",list_todos = list_todos)
#this is how we can we connect this python file to the html but to run it we need to use jinja


if __name__ == "__main__":
    app.run(debug=True)
"http://127.0.0.1:5000/hello"
'''@app.route("/hello")
def hello_from_flask():
    return "hello this message is coming from your first server in flask "


@app.route("/bye")
def bye_from_flask():
    return "<h1> bye classssss <h1/> "


@app.route("/number/<int:num>")
def print_number(num):
    print("number sent from URL:", num)
    return "your number is " + str(num)'''
