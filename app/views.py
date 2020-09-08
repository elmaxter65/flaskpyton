#Se importa render_template, flash y redirect
from flask import render_template, flash, redirect
#Se importa la aplicacion app
from app import app
#De forms.py se importa LoginForm
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
  user = {'usuario': 'Ernesto'}
  posts = [
      {
          'autor': {'usuario': 'John'},
          'asunto': 'Un gran dia en Edimburgo!'
      },
      {
          'autor': {'usuario': 'Jane'},
          'asunto': 'Civil War, una gran pelicula!'
      }
  ]
  return render_template('index.html',
                         title='Inicio',
                         user=user,
                         posts=posts)


#Se define login con url /login con metodos GET y POST
@app.route('/login', methods=['GET', 'POST'])
def login():
  #Se crea una instancia de LoginForm
  form = LoginForm()
  #Se consulta si validate existe
  if form.validate_on_submit():
    flash('Solicitud de login por OpenID="%s", recuerdame=%s' %
          (form.openid.data, str(form.recuerdame.data)))
    return redirect('/index')
  return render_template('login.html',
                         title='Inicio sesion',
                         form=form,
                         providers=app.config['PROVEEDORES_OPENID'])
