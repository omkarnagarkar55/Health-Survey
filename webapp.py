from flask import Flask,render_template,request
import psyco as p
import socket

app=Flask(__name__)
from send_email import send_email

def BMI(w,h):
    h=h/100
    bmi=w/(h*h)
    bmi=round(bmi,1)
    return bmi
    
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/success/",methods=['POST'])

def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=int(request.form["height_name"])
        weight=int(request.form["weight_name"])
        print(email)
        print(height)
        print(weight)
        bmi=BMI(weight,height)
        db=p.Data(email,height,weight,bmi)
        db.create()
        db.create2()
        if((db.count(email)[0])[0]==0):
            db.insert(email,height,weight)
            db.insert2(bmi)
            avg=(db.average()[0])[0]
            avg=round(avg,1)
            cnt=(db.countAll()[0])[0]
            ana=db.Analysis()
            print("Analysis",ana)
            try:
                send_email(email,height,avg,cnt,bmi)
            except socket.gaierror:
                db.delete(email)
                return render_template('index.html',
                text="Unable to reach the server please try again")
            return render_template('success.html')    
        return render_template('index.html',
        text="Seems like we got something from that email once!")
        
if __name__=='__main__':
    app.debug=True
    app.run()