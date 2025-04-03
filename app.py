from flask import Flask, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = 'Secret'

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

    # check if any input is empty
    if fname == '' or sname == '' or email == '' or phone == '' or addrline == '' or towncity == '' or county == '' or postcode == '':
        flash('All inputs are required', 'error')
    
    # check fname is between 3-30 char
    if len(fname) < 3 or len(fname) > 30:
        flash('Firstname must be between 3-30 characters long', 'error')

    # check sname is between 3-50 char
    if len(sname) < 3 or len(sname) > 50:
        flash('Surname must be between 3-50 characters long', 'error')
    
    # check email is less than 60 char
    if len(email) > 60:
        flash('Email must be less than 60 characters long', 'error')
    
    # check phone is equal to 11 char
    if len(phone) != 11:
        flash('Phone number must be 11 characters long', 'error')

    # check addrline is less than 255 char
    if len(addrline) > 255:
        flash('Address line must be less than 255 characters long', 'error')

    # check towncity is less than 255 char
    if len(towncity) > 255:
        flash('Town/City must be less than 255 characters', 'error')

    # check county is less than 50 char
    if len(county) > 50:
        flash('County must be less than 50 characters', 'error')

    # check postcode is 6-8 char
    if len(postcode) < 6 or len(postcode) > 8:
        flash('Postcode must be between 6-8 characters long', 'error')

    # check phone starts with 0
    if len(phone) != 0 and phone[0] != '0':
        flash('Phone number must start with a \'0\'', 'error')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)