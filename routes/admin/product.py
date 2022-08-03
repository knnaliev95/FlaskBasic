from start import app,db,migrate,request,redirect,url_for,flash,render_template
from models import Product

@app.route('/admin/product/add',methods=['GET','POST'])
def add_product():
    if request.method=='POST':
        productName=request.form['productName']
        productPrice=request.form['productPrice']
        product=Product(productName=productName,productPrice=productPrice)
        db.session.add(product)
        db.session.commit()

    return render_template('/admin/product/add.html')

@app.route('/admin/product/list', methods=['GET','POST'])
def view_product():
    products=Product.query.all()
    return render_template('admin/product/list.html',products=products)

@app.route('/admin/products/update/<id>', methods=['GET','POST'])
def update_product(id):
    pass

app.route('/admin/product/delete/<id>', methods=['GET','POST'])
def delete_product(id):
    pass