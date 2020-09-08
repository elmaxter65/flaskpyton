#Se importa Form
#from flask.ext.wtf import Form
from flask_wtf import Form
#De form se importa StringField y BooleanField
from wtforms import StringField, BooleanField
#De validadores se importa DataRequired
from wtforms.validators import DataRequired


#Se Crea la clase LoginForm que hereda de Form
class LoginForm(Form):
	#Se define el ID como StringField
    openid = StringField('openid', validators=[DataRequired()])
    #Se define un campo de check para definir si se recuerda el id o no,
    #por defecto no.
    recuerdame = BooleanField('recuerdame', default=False)
