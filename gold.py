from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = "Secret"
import random
import datetime

def odds():
    number = random.randint(1,2)
    if number ==1:
        return True
    if number == 2:
        return False 

def log_activity(amount,result, place):
    if place == 'casino':
        if result == 'lost':
            return("Entered a casino and " + result +" "+ amount + " golds...Ouch "+ str(datetime.datetime.now()))
        else:
            return("Entered a casino and " + result +" "+ amount + " golds " + str(datetime.datetime.now()))
    else:
        return(result + " " + amount + " golds from the "+ place + " "+ str(datetime.datetime.now()))

@app.route('/')
def index():
    if 'activity' in session:
        pass
    else:
        session['activity']= []
    if 'amount' in session:
        pass
    else:
        session['amount']=0
    return render_template('index.html', amount = session['amount'], list = session['activity'])

@app.route('/process_money', methods = ['POST'])
def process():
    if request.form['place']== "farm":
        firstnum = random.randint(10,20)
        session['amount']+= firstnum
        log_activity(str(firstnum),"Earned","farm!")
        session['activity'].append(log_activity(str(firstnum),"Earned","farm!"))
    elif request.form['place']=="cave":
        secondnum= random.randint(5,10)
        session['amount']+= secondnum
        session['activity'].append(log_activity(str(secondnum),"Earned","cave!"))
    elif request.form['place'] == "house":
        thirdnum= random.randint(2,5)
        session['amount']+= thirdnum
        session['activity'].append(log_activity(str(thirdnum),"Earned","house!"))
    elif request.form['place'] == "casino" :
        odds()
        fourthnum= random.randint(0,50)
        if odds() == True:
            session['amount']+= fourthnum
            session['activity'].append(log_activity(str(fourthnum),"earned","casino"))
        else:
            session['amount']-= fourthnum
            session['activity'].append(log_activity(str(fourthnum),"lost","casino"))
    return redirect('/')




if __name__ == "__main__":
    app.run(debug = True)