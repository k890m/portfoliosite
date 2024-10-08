import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                         user=os.getenv("MYSQL_USER"),
                         password=os.getenv("MYSQL_PASSWORD"),
                         host=os.getenv("MYSQL_HOST"),
                         port=3306
    )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email =  CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

# ---------- DATA ----------
user_data = {"name": "Kanmani Murugesan", "about" : "Software Engineer, MLH Production Engineering Fellow, CodePath Tech Fellow", "profilepic": "./static/img/Kanmani.jpg", "github": "link", "linkedin": "link"}

hobbies_data = [
    {"name": "Baking", "image": "static/img/placeholder.png"},
    {"name": "Digital Art", "image": "static/img/placeholder.png"},
    {"name": "Painting", "image": "static/img/placeholder.png"}
]

education_data = [
    {
        "school": "University of Maryland",
        "img": "/static/img/placeholder.png",
        "degree": "B.S in Computer Science",
        "year": 2025
    },
   
]

experiences_data = [
    {
        "company_name": "XYZ",
        "position": "Software Engineer",
        "dates": "2023 - 2024",
        "location": "US",
        "description": [
            "bullet point 1",
            "bullet point 2",
        ]
    },
    {
        "company_name": "XYZ2",
        "position": "Software Engineer",
        "dates": "2020 - 2021",
        "location": "US",
        "description": [
            "bullet point 1",
            "bullet point 2",
        ]
    },
]

locations_data = [
    {"country": "Boston, MA, USA", "lat": 42.3601, "long": -71.0589},
    {"country": "Fairfax County, VA, USA", "lat": 38.8462, "long": -77.3064},
    {"country": "Fresno, California, USA", "lat": 36.7378, "long": -119.7871},
    {"country": "Toronto, Ontario, Canada", "lat": 43.651070, "long": -79.347015}
]

# ---------- ROUTES ----------

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), user=user_data)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=hobbies_data)

@app.route('/education')
def education():
    return render_template('education.html', title="Education", education=education_data)

@app.route('/experiences')
def experiences():
    return render_template('experiences.html', title="Experiences", experiences=experiences_data)

@app.route('/locations')
def map_view():
    return render_template('map.html', title="Map", locationData=locations_data)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name=request.form['name']
    email=request.form['email']
    content=request.form['content']
    timeline_post=TimelinePost.create(name=name, email=email, content=content)

    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
    
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in 
TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

