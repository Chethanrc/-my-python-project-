from flask import *
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin',methods=['POST'])
def signin():
    name=request.form['name']
    password=request.form['password']
    if name ==  'admin' and password == 'admin123':
        return render_template('index.html',msg=f'hii{name},welcome to the chatbot')
    else:
        return render_template('index.html',msg='Invalid username or password')
if __name__ == '__main__':
    app.run(debug=True)