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
        return redirect('/admin/product/list')
    return render_template('/admin/product/add.html')

@app.route('/admin/product/list', methods=['GET','POST'])
def view_product():
    products=Product.query.all()
    return render_template('admin/product/list.html',products=products)

@app.route('/admin/product/update/<id>', methods=['GET','POST'])
def update_product(id):
    product=Product.query.get(id)
    if request.method=='POST':
        p_name=request.form['p_name']
        p_price=request.form['p_price']
        product.productName=p_name
        product.productPrice=p_price
        db.session.commit()
        return redirect('/admin/product/list')
    return render_template('/admin/product/update.html',product=product)

app.route('/admin/product/delete/<id>', methods=['GET','POST'])
def delete_product(id):
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect('/admin/product/list')