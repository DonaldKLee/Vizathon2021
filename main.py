"""
Criteria
- Challenge 2: 
- Min 
- US, Brazil, 
- Employment insurance/stimulus checks, vaccine rollouts
- Homelessness, evictions
"""
import random
from flask import Flask, render_template, url_for, request

#Sets up the flask app
app = Flask(
	__name__,
	template_folder='templates', #Name of folder containing html files
	static_folder='static'  #Name of folder containing static files
)


@app.route('/')
def index(): # Home page
    return render_template('index.html')

if __name__ == "__main__":  
	app.run( 
    debug=True,
    #Starts the website
		host='0.0.0.0',  #Sets the host, required for repl to detect the site
		port=random.randint(2000, 9000)  #Randomly select the port the machine hosts on.
	)