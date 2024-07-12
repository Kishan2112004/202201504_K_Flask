from flask import Flask , render_template,jsonify

app = Flask(__name__)
positions = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Bengaluru, India',
        'salary' : 'Rs. 10,00,000'
    },
    {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Gurgaon, India',
    
    },
    {
        'id' : 3,
        'title' : 'Web developer',
        'location' : 'Gurgaon, India',
        'salary' : 'Rs. 15,00,00'
    },
    {
        'id' : 4,
        'title' : 'Product Manager',
        'location' : 'California',
        'salary' : '$. 150, 000'
    },
    {
        'id' : 5,
        'title' : 'Data Scientist',
        'location' : 'Seatel , USA',
        'salary' : '$. 150, 000'
    }
    
]
@app.route('/')
def hello_world():
    return render_template('home.html' , jobs = positions)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(positions)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)