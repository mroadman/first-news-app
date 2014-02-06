import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

#import CSV
csv_path = './static/la-riots-deaths.csv'
csv_obj = csv.DictReader(open(csv_path, 'r'))
csv_list = list(csv_obj)
#use Python to transform data into dictionary with id as key
csv_dict = dict([[o['id'], o] for o in csv_list])


@app.route("/")
def index():
    return render_template('index.html',
    		#adds CSV to index file
    		object_list = csv_list, 
    	)
#creating a unique detail page for each person
@app.route('/<number>/')
def detail(number):
	return render_template('detail.html',
		#connect number from URL with record in dictionary and pass through template
		object=csv_dict[number],
	)

#setting up server	
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000,
        use_reloader=True,
        debug=True,
    )