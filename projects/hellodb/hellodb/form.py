from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class MemberForm(FlaskForm):
    name = StringField('Nama', validators=[DataRequired()],
                       render_kw={"placeholder": "Nama"})
    address = TextAreaField('Alamat',
                            render_kw={"placeholder": "Alamat"})
    phone = StringField('No. Telp', validators=[Length(max=20)],
                        render_kw={"placeholder": "No. Telp"})
    email = StringField('Email', validators=[Length(max=120)],
                        render_kw={"placeholder": "Email"})
