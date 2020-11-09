from flask import Flask ,redirect,render_template ,url_for







app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iwobashop.db'




@app.route('/index')
def index():
	return render_template('index.html')



@app.route('/myaccount')
def myaccount():
	return render_template('myaccount.html')



@app.route('/cart')
def cart():
	return render_template('cart.html')



@app.route('/checkout')
def checkout():
	return render_template('checkout.html')



@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/service')
def service():
	return render_template('service.html')


@app.route('/detail')
def shopdetail():
	return render_template('shop-detail.html')



@app.route('/login')
def login():
	return render_template('login.html')




@app.route('/register')
def register():
	return render_template('register.html')


@app.route('/')
def base():
	return render_template('base.html')



@app.route('/wishlist')
def wishlist():
	return render_template('wishlist.html')


@app.route('/shop')
def shop():
	return render_template('shop.html')













if __name__ == '__main__':
	app.run(debug=True)