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
                       [DataRequired(), Email(message="Ingresá un correo electronico válido")],
                       render_kw={"placeholder": "my.email@mail.com"})
    username = StringField('Nombre de usuario',
                           [Length(message="El nombre de usuario debe tener entre 4 y 20 caracteres", min=4, max=20),
                            DataRequired()], render_kw={"placeholder": "bob_username"})
    password = PasswordField('Contraseña', [DataRequired(),
                                            length(message="La contraseña debe tener entre 6 y 20 caracteres", min=6,
                                                   max=20),
                                            EqualTo('confirm', message='Las contraseñas deben ser iguales')],
                             render_kw={"placeholder": "entre 6 y 20 caracteres"})
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
            raise ValidationError('Ya existe una cuenta registrada con ese correoo.')


class EditUserForm(FlaskForm):
    email = EmailField('Dirección de correo',
                       [DataRequired(), Email(message="Ingresá un correo electronico válido")])
    username = StringField('Nombre de usuario',
                           [Length(message="El nombre de usuario debe tener entre 4 y 20 caracteres", min=4, max=20),
                            DataRequired()])
    password = PasswordField('Contraseña', [Optional(),
                                            length(message="La contraseña debe tener entre 6 y 20 caracteres", min=6,
                                                   max=20),],
                             render_kw={"placeholder": "entre 6 y 20 caracteres"})
    first_name = StringField('Nombre',
                             [Length(message="El nombre  debe tener entre 4 y 20 caracteres", min=4, max=20),
                              DataRequired()])
    last_name = StringField('Apellido',
                            [Length(message="El apellido  debe tener entre 2 y 20 caracteres", min=2, max=20),
                             DataRequired()])
    active = BooleanField('Estado(Activo/Inactivo)')


# Formulario de configuración del sistema
class SistemaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=55)])
    descripcion = StringField('Descripción', validators=[DataRequired(), Length(
        message="La descripción no puede superar más de 255 caracteres", max=255)])
    bienvenida = StringField('Bienvenida', validators=[DataRequired(), Length(
        message="El texto de la bienvenida no puede superar más de 255 caracteres", max=255)])
    email = StringField('Email', validators=[DataRequired(), Length(
        message="El email no puede superar más de 25 caracteres", max=25)])
    cant_por_pagina = IntegerField('Cantidad de elementos por página', validators=[DataRequired()])
    habilitado = RadioField('Estado de la página', coerce=int, choices=[(0, "Deshabilitado."),
                                                                        (1, "Habilitado")], default=1)
    # habilitado = BooleanField('Estado de la página')
