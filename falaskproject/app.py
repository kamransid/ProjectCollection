from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt




app=Flask(__name__)

Articles = Articles()


# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=id)



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=1,max=50)])
    username = StringField('Username', [validators.length(min=4,max=25)])
    email = StringField('Email', [validators.length(min=6,max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET','POST'])
def resgister():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
       name = form.name.data
       email = form.email.data
       username = form.username.data
       password = sha256_crypt.encrypt(str(form.password.data))

       #creat cursor
       cur = mysql.connection.cursor();
       cur.execute("insert into users(name, email, username, password) values(%s,%s,%s,%s)",(name,email,username,password))
       
       #Commit to db
       mysql.connection.commit()

       #Close connection
       cur.close()
       
       #Flash Message
       flash('You are now registered','success')
       return  redirect(url_for('index'))
       
       return render_template('register.html',form=form)
    return render_template('register.html',form=form)


if __name__ == '__main__':
    app.secret_key='LAK:cncandv ldsjhfqUD'
    app.run(debug=True)
