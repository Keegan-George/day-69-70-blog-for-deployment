from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")


# WTForm for new user registration
class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[InputRequired(), Email()])
    password = StringField(label="Password", validators=[InputRequired()])
    name = StringField(label="Name", validators=[InputRequired()])
    submit = SubmitField(label="Sign Me Up!")


# WTForm for logging in
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[InputRequired(), Email()])
    password = StringField(label="Password", validators=[InputRequired()])
    submit = SubmitField(label="Let Me In!")


# WTForm for users to leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField(label="Comment", validators=[InputRequired()])
    submit = SubmitField(label="Submit Comment")
