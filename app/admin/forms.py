from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class DepartmentForm(FlaskForm):
	"""Form for admin to add or edit department"""
	name = StringField('Name',validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Submit')

class RoleForm(FlaskForm):
	"""Form for admin to add or edit a role"""
	name = StringField('Name', validators= [DataRequired()])
	description = StringField('Description', validators = [DataRequired()])
	submit = SubmitField('Submit')