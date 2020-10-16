from flask import flash
from flask_wtf import FlaskForm, RecaptchaField
from datetime import date
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, FileField, \
    TextAreaField, RadioField, DateField
from wtforms.validators import ValidationError, DataRequired, Length, length, Email, EqualTo, required, Optional
from wtforms.fields.html5 import EmailField
from pymysql import escape_string as thwart  # escape_string para prevenir sql injections
from datetime import date
from app.models.user import User


class LoginForm(FlaskForm):
    """Formulario para inicio de sesión del usuario"""

    username = StringField('Usuario: ', [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Contraseña: ', [DataRequired()])
    submit = SubmitField('Iniciar Sesión')

    # Formulario para registro de usuarios


class CreateUserForm(FlaskForm):
    email = EmailField('Dirección de correo',
                       [DataRequired(), Email(message="Ingresá un correo electronico válido")],render_kw={"placeholder": "my.email@mail.com"})
    username = StringField('Nombre de usuario',
                           [Length(message="El nombre de usuario debe tener entre 4 y 20 caracteres", min=4, max=20),
                            DataRequired()],render_kw={"placeholder": "bob_username"})
    password = PasswordField('Contraseña', [DataRequired(),
                                            length(message="La contraseña debe tener entre 6 y 20 caracteres", min=6,
                                                   max=20),
                                            EqualTo('confirm', message='Las contraseñas deben ser iguales')],render_kw={"placeholder": "entre 6 y 20 caracteres"})
    confirm = PasswordField('Confirmar Contraseña')
    first_name = StringField('Nombre',
                             [Length(message="El nombre  debe tener entre 4 y 20 caracteres", min=4, max=20),
                              DataRequired()], render_kw={"placeholder": "bob"})
    last_name = StringField('Apellido',
                            [Length(message="El apellido  debe tener entre 2 y 20 caracteres", min=2, max=20),
                             DataRequired()], render_kw={"placeholder": "perez"})
    active = BooleanField('Estado(Activo/Inactivo)')

    def validate_username(self, username):
        """Compruebo que el nombre de usuario no exista en el sistema"""
        if ' ' in username.data:
            raise ValidationError("El nombre de usuario no puede contener espacios")
        user = User.query.filter(User.username == username.data).first()
        if user is not None:
            raise ValidationError('Ya existe una cuenta registrada con ese nombre de usuario.')

    def validate_email(self, email):
        """Compruebo que el correo no exista en el sistema, si existe levanta una excepción de tipo ValidationError"""
        user = User.query.filter(User.email == email.data).first()
        if user is not None:
            raise ValidationError('Ya existe una cuenta registrada con ese correo.')