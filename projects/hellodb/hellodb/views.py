from flask import render_template, request, flash, redirect, url_for
from hellodb import app, db
from hellodb.models import Member
from hellodb.form import MemberForm


@app.route('/')
def home():
    members = Member.query.limit(10).all()
    return render_template('home.html', members=members)


@app.route('/add', methods=['GET', 'POST'])
def add_member():
    form = MemberForm(request.form)
    if form.validate_on_submit():
        member = Member()
        member.name = form.name.data,
        member.address = form.address.data,
        member.phone = form.phone.data,
        member.email = form.email.data

        db.session.add(member)
        db.session.commit()
        flash('Data berhasil disimpan.', 'success')
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_member(id):
    member = Member.query.filter_by(id=id).first_or_404()
    form = MemberForm(request.form, obj=member)
    if form.validate_on_submit():
        form.populate_obj(member)
        db.session.commit()
        flash('Data berhasil diperbarui.', 'success')
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, member=member)


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_member(id):
    member = Member.query.filter_by(id=id).first_or_404()
    if request.method == 'POST':
        db.session.delete(member)
        db.session.commit()
        flash('Data berhasil dihapus.', 'success')
        return redirect(url_for('home'))

    return render_template("delete.html", member=member)
