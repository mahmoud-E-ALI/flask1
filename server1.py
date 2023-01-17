from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def page1(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('data.txt', 'a') as f:
        name = data['name']
        email = data['email']
        message = data['message']
        file = f.write(f'\n {name}, {email},{message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as f2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(f2)
        csv_writer.writerow([name, email, message])


def write_to_Mongo(data):
    with open('database.csv', 'a', newline='') as f2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(f2)
        csv_writer.writerow([name, email, message])

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            # write_to_csv(data)
            write_to_Mongo(data)
            return redirect('/thanks.html')
        except:
            return 'does not connect'
            
    else:
        return 'wrong'
