from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index_post():
    fname = request.form.get('fname')
    sname = request.form.get('sname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    addrline = request.form.get('addrline')
    towncity = request.form.get('towncity')
    county = request.form.get('county')
    postcode = request.form.get('postcode')

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)