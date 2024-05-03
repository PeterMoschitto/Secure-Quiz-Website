import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():	
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
	error = None
	if 'firstName' in session and 'lastName' in session and 'birthday' in session:
		error = "You have been caught trying to change your answer!"
	else: 
		session["firstName"]=request.form['firstName']
		session["lastName"]=request.form['lastName']
		session["birthday"]=request.form['birthday']
		return render_template('page2.html')
	session.clear() #clears variable values and creates a new session
	return render_template('home.html', error=error) # url_for('renderMain') could be replaced with '/' 


@app.route('/page3',methods=['GET','POST'])
def renderPage3():
	error = None
	if 'Question 1' in session:
		error = "You have been caught trying to change your answer!"
	else:
		session["Question 1"]=request.form['Question 1']
		return render_template('page3.html')
	session.clear() #clears variable values and creates a new session
	return render_template('home.html', error=error) # url_for('renderMain') could be replaced with '/' 


@app.route('/page4',methods=['GET','POST'])
def renderPage4():
	error = None
	if 'Question 2' in session:
		error = "You have been caught trying to change your answer!"
	else:
		session["Question 2"]=request.form['Question 2']
		return render_template('page4.html')
	session.clear() #clears variable values and creates a new session
	return render_template('home.html', error=error) # url_for('renderMain') could be replaced with '/' 


@app.route('/page5',methods=['GET','POST'])
def renderPage5():
	error = None
	if 'Question 3' in session:
		error = "You have been caught trying to change your answer!"
	else:
		session["Question 3"]=request.form['Question 3']
		return render_template('page5.html')
	session.clear() #clears variable values and creates a new session
	return render_template('home.html', error=error) # url_for('renderMain') could be replaced with '/' 

    
@app.route('/page6',methods=['GET','POST'])
def renderPage6():
	scores = score()
	q1 = correct1()
	q2 = correct2()
	q3 = correct3()
	session["favAnimal"]=request.form['favAnimal']
	return render_template('page6.html', score = scores, correct1 = q1, correct2 = q2, correct3 = q3)
	
	
@app.route('/page7',methods=['GET','POST'])
def renderPage7():
	return render_template('page7.html') 
	
@app.route('/page8',methods=['GET','POST'])
def renderPage8():
    if 'ExtraCredit' in session:
        error = "You have been caught trying to change your answer!"
    else:
        session["ExtraCredit"]=request.form['ExtraCredit']
        scores = score()
        q1 = correct1()
        q2 = correct2()
        q3 = correct3()
        q4 = correct4()
        if session['ExtraCredit'] == "Mr. Stewart":
            scores+=1
        return render_template('page8.html', score = scores, correct1 = q1, correct2 = q2, correct3 = q3, correct4 = q4)
    session.clear() #clears variable values and creates a new session
    return render_template('home.html', error=error) # url_for('renderMain') could be replaced with '/' 
   
   
	

def score():
    score = 0
    if session['Question 1'] == "Rhinoceros beetle":
        score += 1
        
    if session['Question 2'] == "Whale Shark":
        score += 1
        
    if session['Question 3'] == "Capybara":
        score += 1
    return score
	
def correct1():
	correct1 = None
	if session['Question 1'] == "Rhinoceros beetle":
		correct1 = "Correct"
	else: 
		correct1 = "Incorrect"
	return correct1
	
def correct2():
	correct2 = None
	if session['Question 2'] == "Whale Shark":
		correct2 = "Correct"
	else: 
		correct2 = "Incorrect"
	return correct2
	
def correct3():
	correct3 = None
	if session['Question 3'] == "Capybara":
		correct3 = "Correct"
	else: 
		correct3 = "Incorrect"
	return correct3
	
	
def correct4():
	correct4 = None
	if session['ExtraCredit'] == "Mr. Stewart":
		correct4 = "Correct"
	else: 
		correct4 = "Incorrect"
	return correct4

    
if __name__=="__main__":
    app.run(debug=True)
