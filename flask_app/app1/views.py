from flask import render_template, flash, redirect


from . import app
from .form import LoginForm

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'name': 'cong'}
    return render_template('index.html', user=user, title='Home')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                            provider=app.config['OPENID_PROVIDER']
                            )

