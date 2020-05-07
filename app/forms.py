from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import *
from wtforms.validators import DataRequired, Email


class UploadForm(FlaskForm):
    """docstring for UploadForm."""

    description = TextAreaField('Description: ', validators=[DataRequired()])
    photofile = FileField('photofile', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','jpeg','Images only'])
    ])
