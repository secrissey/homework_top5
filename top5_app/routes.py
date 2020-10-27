from chicodes_blog_app import app
from flask import render_template

# Default Home Route
@app.route('/')
def home():
    name = 'My Top 5 Artists'
    return render_template('home.html',name=name)
# Artists Route
@app.route('/top5')
def top5():
    names = ['Tina Turner','Diana Ross', 'Bette Midler', 'Prince', 'Chaka Khan']
    return render_template('top5.html',list_names = names)