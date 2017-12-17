from flask import Flask, request, render_template, make_response,jsonify
import requests,json

app = Flask(__name__)
#Task 1
#A simple hello-world at http://localhost:5000/ that displays a simple string like "Hello World - Nageswara reddy"
 
@app.route("/")
def hello():
    return "Hello World-Nageswara Reddy"
# Task 2 fetches a list of authors, fetches a list of posts and Respond with only a list of authors and the count of their posts
@app.route('/authors')
def authors():
    Request1 = requests.get('https://jsonplaceholder.typicode.com/users')
    Request2 = requests.get('https://jsonplaceholder.typicode.com/posts')
    parsed1 = Request1.json()
    parsed2 = Request2.json()
    return render_template('auth.html', parsed1=parsed1, parsed2=parsed2)

# Task 3 Create cookies
@app.route('/cookie')
def cookie():
    return render_template("index.html")

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
   if request.method =='POST':
       user = request.form['Name']
       old=request.form['Age']
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('Name',user)
   resp.set_cookie('Age',old)
   
   return resp
# Task 4 Display the cookies  
@app.route('/getcookie')
def getcookie():
    name=request.cookies.get('Name')
    age=request.cookies.get('Age')
    return '<h1>Name:'+name+'<br>Age:'+age+'</h1>'
 # Task 5 Deny requests to your http://localhost:5000/robots.txt page. 
@app.route('/robot.txt')
def error():
    return render_template("error.html")
# Task 6 Render the simple htmlpage and image
@app.route('/html')
def image():
    return render_template("propilelink.html")
@app.route('/image')
def img():
    return render_template("image.html")
# Task 7 A text box at http://localhost:5000/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.

@app.route('/input')
def input():
    return render_template("sample.html")
@app.route('/result',methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        user=request.form['Name']
        print(user,file=sys.stdout)
    return "Output is Dsplay on terminal"

    
if __name__ == "__main__":
    app.debug= True
    app.run()
