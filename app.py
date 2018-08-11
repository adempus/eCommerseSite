from flask import Flask, render_template, request
# from data import ShopDAO, LocationDAO
from data import LocationDAO
from models import Model

app = Flask(__name__)
shopDAO = object
locationDAO = LocationDAO()

@app.route('/', methods=['GET', 'POST'])
def index():
    signIn()
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # data to post from registration form
    signUp()
    countries = locationDAO.countriesList()
    countrySelect = request.form.get('country_select')
    print(countrySelect)
    return render_template('register.html', country_select=countries)


def signUp():
    userModel = Model()
    userModel.setData(from_request=True,
                      first_name='first_name', last_name='last_name', email='email',
                      password='password', street='street', city='city', state='state',
                      country_select='country_select', zip='zip', apt='apt')
    print(userModel)


def signIn():
    userEmail = request.form.get('login-email')
    userPass = request.form.get('login-pass')
    print(f'email: {userEmail} \npasswd: {userPass}')


def initDAO():
    #shopDAO = ShopDAO()
    locationDAO = LocationDAO()

if __name__ == '__main__':
    app.run()
    initDAO()
