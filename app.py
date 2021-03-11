from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
 

@app.route("/")
def index():
	return render_template("index.html",title="Get Started")
@app.route("/home")
def home():
	return render_template("home.html",title="GS-Home")
@app.route("/register")
def register():
	return render_template("register.html",title="Join now")
@app.route("/login")
def login():
	return render_template("login.html",title="Login Now!!")

@app.route("/view")
def view():
	#flask requires data to be sent in form of dict only.
	return render_template("view.html",gifts=gifts)
@app.route("/contact-us")
def contactUs():
	return render_template("contact.html",title="Contact Us")

def about():
	return "About Us";
app.add_url_rule("/about","about",about)
	

'''
@app.route('/admin')
def hello_admin():
	return "Hello admin"
@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello %s as Guest' % guest
@app.route('/user/<name>')
def hello_run(name):
	if name=="admin":
		return redirect(url_for('Hello admin'))
	else:
		return redirect(url_for('hello_guest',guest=name))
@app.route('/muser/<uname>')
def give_message(uname):
	return render_template("message.html",name=uname)

@app.route('/table/<int:num>')
def table(num):
	return render_template('printTable.html',n=num)

@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name
@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':
		user=request.form['nm']
		return redirect(url_for('success',name=user))
	else:
		user=request.args.get('nm')
		return redirect(url_for('success',name=user))

'''
 
if __name__=='__main__':
	app.run(debug=True)