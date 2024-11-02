from flask import Flask, render_template
import random

app = Flask(__name__)

welcome_msgs = ["Welcome to My Profile",
                "Hello to My Portfoloio"
                "This is My Portfolio"]

my_name = 'Khadheeja zoya mohamed'
my_description = 'welcome to our project.we are maldivians and we like to do and learn new stuff'


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/about')
def about():
    return render_template('about.html', my_name=my_name, my_description=my_description)

@app.route('/project')
def project_list():
    return render_template('projects.html', projects=projects)

@app.route('/contacts')
def contact():
    return render_template('contact.html',contact=my_contact, email=my_email)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    random_welcome_msg =  random.choice(welcome_msgs)
    return render_template( 'index html', welcome_msg=random_welcome_msg)

projects = [
{"name": "smile", "description": "this is our first project and we hope you like our project there will be more coming."},
{"name": "rose", "description": "we hope you like the project we made. hope you like the projects we make in the future."}
]

my_contact = "9998677"
my_email = "zoya143@gmail.com"