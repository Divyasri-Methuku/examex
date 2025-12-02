from Flask import flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route('\',method=['GET','POST'])
def home():
	if request.form=='POST':
		print("Successfull")
		return "successfull registration"
	return render_template('register.html')
if __name__='__main__':
	app.run(debug=True)