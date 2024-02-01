from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from site_forms import AddCafeForm
from dotenv import load_dotenv
import os
import csv
load_dotenv()


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
Bootstrap5(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        # Remove the 'submit' and 'csrf' values.
        form_data = list(form.data.values())[:-2]

        with open('cafe-data.csv', 'a', encoding='utf-8', newline='') as csv_file:

            csv_file.write("\n")

            # lineterminator = '' fixes a Windows specific issue where an extra \n will be added
            # to the row written which causes empty lines in the csv file.
            writer = csv.writer(csv_file, lineterminator='')
            writer.writerow(form_data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
