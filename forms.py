from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, TimeField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL, Email, EqualTo
from flask_ckeditor import CKEditorField

class AddTask(FlaskForm):
   add_task = StringField("Add a New Task", validators=[DataRequired()])
   category = StringField("Category", validators=[DataRequired()])
   task_priority = SelectField("Task Priority", validators=[DataRequired()], choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
   deadline = DateField("Due Date", validators=[DataRequired()])
   submit = SubmitField("Add Task")


