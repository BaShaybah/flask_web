from flask import Flask,render_template
app = Flask(__name__)

posts = [
	{
		"name":"khalid", 
		"age" : 23,
		"job" : "engineer"
	},
	{
		"name":"Ahmed", 
		"age" : 39,
		"job" : "programmer"
	}
	]
@app.route("/")
def home():
	return render_template("home.html", posts=posts)
	
	
	
if __name__ == "__main__":
	app.run(debug=True)