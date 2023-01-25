import datetime
from flask import request
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
ckeditor = CKEditor()
ckeditor.init_app(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'standard'

Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Python/100-Days-of-Code/RESTful-blog/posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __init__(self, title, subtitle, body, author, img_url):
        self.title = title
        self.subtitle = subtitle
        self.date = datetime.date.today()
        self.body = body
        self.author = author
        self.img_url = img_url


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


#
@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


#
#

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    new_posts = db.session.query(BlogPost).get(post_id)
    edit_form = CreatePostForm(title=new_posts.title, subtitle=new_posts.subtitle, img_url=new_posts.img_url,
                               author=new_posts.author,
                               body=new_posts.body)
    if request.method == "POST":
        new_posts.title = request.form.get('title')
        new_posts.subtitle = request.form.get('subtitle')
        new_posts.img_url = request.form.get('img_url')
        new_posts.author = request.form.get('author')
        new_posts.body = request.form.get('body')
        db.session.commit()
        return render_template("post.html", post=new_posts)

    return render_template("make-post.html", pid=post_id, form=edit_form, is_edit=True)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/new_post', methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if request.method == "POST":
        title = request.form.get('title')
        subtitle = request.form.get('subtitle')
        author = request.form.get('author')
        img_url = request.form.get('img_url')
        body = Markup(request.form.get('body'))
        blg_post = BlogPost(title=title, subtitle=subtitle, author=author, img_url=img_url, body=body)
        db.session.add(blg_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=form, edit_post=False)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    data = db.session.query(BlogPost).get(post_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
