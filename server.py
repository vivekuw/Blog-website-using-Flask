import smtplib
from flask import Flask, render_template, request
import requests

npoint = "https://api.npoint.io/1961aec4f5296d32b927"
res = requests.get(npoint)
data =res.json()
OWN_EMAIL = "wadhervivek6904@gmail.com"
OWN_PASSWORD = "bqrmjmcfvzinvzbb"

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',blog=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form-fill',methods=['POST'])
def form():
    name=request.form['username']
    email = request.form['email']
    phone= request.form['phone']
    message = request.form['message']
    send_email(name, email, phone, message)
    return render_template('contact.html',msg_sent=True)

def send_email(name,email,phone,message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, email, email_message)
    pass
@app.route('/post/<blog_id>')
def post(blog_id):
    req_data = blog_id
    return render_template('post.html',blog=data,data=req_data)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')