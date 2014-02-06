from flask_frozen import Freezer
from app import app, csv_list
freezer = Freezer(app)


#make a page for every record in the source CSV
@freezer.register_generator
def detail():
    for row in csv_list:
        yield {'number': row['id']}

if __name__ == '__main__':
    freezer.freeze()