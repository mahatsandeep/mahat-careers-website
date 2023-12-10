from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS = [

{
'id': 1,
'title': 'Data Analyst',
  'Location': 'Los Angeles, CA',
  'Salary':'$76,000'  
},
  {'id': 2,
  'title': 'Data Scientist',
   'Location': 'Los Angeles, CA',
    'Salary':'$100,000'  
  },

{'id': 3,
'title': 'Data Engineer',
 'Location': 'Los Angeles, CA',
  'Salary':'$110,000'  
},
{'id': 4,
'title': 'Data Manager',
 'Location': 'Remote',
 
}
]

@app.route('/')
def hello_world():
    return render_template('index.html',
                           jobs=JOBS,
                           company_name= 'M2'
                          ) 

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
   app.run(host= '0.0.0.0',debug=True)


