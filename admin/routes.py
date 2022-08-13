from flask import render_template,redirect,request
from admin import admin_bp
from models import *
from admin.forms import ProductForm

@admin_bp.route('/add', methods=['GET','POST'])
def product_add():
    productForm=ProductForm()
    from models import Product
    from start import db
    if request.method=='POST':
        product=Product(productName=productForm.name.data, productPrice=productForm.price.data, add_date=productForm.date.data)
        db.session.add(product)
        db.session.commit()
        return redirect('/admin/list')
    return render_template('add.html', productForm=productForm)

@admin_bp.route('/list', methods=['GET','POST'])
def product_list():
    products=Product.query.all()
    return render_template('list.html', products=products)

@admin_bp.route('/update/<id>', methods=['GET','POST'])
def product_update(id):
    product=Product.query.get(id)
    if request.method=='POST':
        p_name=request.form['p_name']
        p_price=request.form['p_price']
        product.productName=p_name
        product.productPrice=p_price
        db.session.commit()
        return redirect('/admin/list')
    return render_template('update.html', product=product)

@admin_bp.route('/delete/<id>', methods=['GET','POST'])
def product_delete(id):
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect('/admin/list')
