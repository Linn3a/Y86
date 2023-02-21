from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class UploadForm(FlaskForm):
    file = FileField('Upload file', validators=[FileRequired(), FileAllowed(['yo'])])
    submit = SubmitField()
