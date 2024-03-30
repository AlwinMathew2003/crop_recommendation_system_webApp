from flask import Flask,render_template,request
from sklearn import *
import joblib
# app = Flask(__name__,static_url_path='/static') #This tells Flask to serve static files from the /static URL path.
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    list1=[]
    if request.method== 'POST':
        list1=[
            request.form['N'],
            request.form['P'],
            request.form['K'],
            request.form['temperature'],
            request.form['humidity'],
            request.form['ph'],
            request.form['rainfall']
        ]
    arr=[list1]
    app=joblib.load('crop_app')
    crop=app.predict(arr)        
    return render_template('index.html',prediction=crop[0],form=request.form)

if __name__=='__main__':
    app.run(debug=True)

# In the context of a Flask web application, `request.form` is a special dictionary-like object provided by Flask that contains the data submitted in an HTML form using the POST method.

# When you iterate over `request.form` using a loop like `for key in request.form:`, `key` represents the name attribute of each form field submitted in the HTML form. In HTML forms, each input field typically has a name attribute which identifies the data when it's submitted to the server.

# For example, if you have an HTML form with fields like this:

# ```html
# <form method="POST">
#     <input type="text" name="username">
#     <input type="password" name="password">
#     <input type="submit" value="Submit">
# </form>
# ```

# When this form is submitted, Flask collects the data and makes it available in the `request.form` object. In this case, `request.form` would contain key-value pairs like:

# - `'username': 'value_entered_by_user'`
# - `'password': 'password_entered_by_user'`

# So, when you iterate over `request.form` with `for key in request.form:`, `key` will take on the values `'username'` and `'password'` in each iteration, allowing you to access the corresponding values entered by the user in the form fields.

#if we want to input field to be filled after sumbit:
#<input type="number" id="N" name="N" step="0.01" min="0" max="300" required {% if form and form.N %}value="{{ form.N }}"{% endif %}>
#return render_template('index.html',prediction=crop[0],form=request.form)