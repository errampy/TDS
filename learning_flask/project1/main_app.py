from flask import Flask, redirect
app = Flask(__name__) # Flask Constructor

@app.route('/') # this is decorator which use to tell the application which url is associated function
def home():
    my_text = '''
                <center>
                <h1>Welcome to flask learning....!!!</h1><hr>
                <h2>Learn until get success...!!!</h2>
                </center>
              '''
    return my_text

@app.route('/admin')
def admin():
    return 'Im admin'

@app.route('/redirect/<username>')
def redirect_user(username):
    if username == 'admin':
        return redirect(location='/admin')
    return 'Invalid user'

if __name__ == '__main__':
    app.run(debug=True)