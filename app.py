from flask import Flask
from helper import pets
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href="animals/dogs">Dogs</a></li>
    <li><a href="animals/cats">Cats</a></li>
    <li><a href="animals/rabbits">Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<path:pet_type>')
def animals(pet_type):
  html = f'''
  <h1>List of {pet_type}</h1>
  '''
  html += f'''<ul>'''
  for k,v in enumerate(pets[pet_type]):
    html += f'''<li><a href="/animals/{pet_type}/{k}"> { v["name"] } </a></li>'''
  html += f'''</ul>'''
  return html

@app.route('/animals/<path:pet_type>/<int:pet_id>')
def pet(pet_type,pet_id):
  pet = pets[pet_type][pet_id]
  html = f'''<h1>{pet['name']}</h1>'''
  html += f'''<img src="{pet['url']}"/>'''
  html += f'''<p>{pet['description']}</p>'''
  html += f'''<ul>'''
  html += f'''
  <li>{pet['age']}</li>
  <li>{pet['breed']}</li>
  '''
  html += f'''</ul>'''
  return html


if __name__ == '__main__':
    app.run(debug=True)