from flask import Flask, render_template, url_for, request, redirect  # type: ignore
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def homePage():
    print(url_for('static', filename='smile.ico'))
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subj = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subj}, {message}')

def write_to_CSV(data):
    with open('database.csv', newline='', mode='a') as db:
        email = data["email"]
        subj = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subj,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_CSV(data)
        return redirect('/thankyou.html')
    return 'Something went wrong..'

"""
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/thankyou.html')
def final():
    return render_template('thankyou.html')
"""
