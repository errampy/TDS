from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Contact
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY']='ASDF4423ed--34082394jweksn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' # Database ULR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Avoid unnecessary warnings
db.init_app(app) # Initialize SQLAlchemy with the Flask app


@app.route('/')
def home():
    template_name = 'index.html'
    return render_template(template_name)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        form = ContactForm(request.form)
        if form.validate_on_submit():
            data = form.data # get all data into dict
            name = form.name.data # get name only
            email = form.email.data # get email only
            print('name ', name)
            print('email ', email)
            print('data ',data)

    form = ContactForm()
    context = {
        'form' : form,
    }
    template_name = 'contact.html'
    return render_template(template_name,**context)


if __name__ == '__main__':
    with app.app_context():  # Required for context in some environments
        db.create_all()  # Creates all tables
    app.run()