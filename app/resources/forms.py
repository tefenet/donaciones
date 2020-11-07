from flask_wtf import FlaskForm
from flask_wtf.file import FileField

from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, \
    RadioField, widgets, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length, length, Email, EqualTo, Optional

from wtforms.fields.html5 import EmailField, TimeField, URLField

from pymysql import escape_string as thwart  # escape_string para prevenir sql injections

from app.models.center import CENTER_TYPES_ENUM, CENTER_TYPES
from app.models.city import City
from app.models.role import Role
from app.models.user import User


class LoginForm(FlaskForm):
    """Formulario para inicio de sesión del usuario"""

    username = StringField('Usuario: ', [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Contraseña: ', [DataRequired()])
    submit = SubmitField('Iniciar Sesión')

    # Formulario para registro de usuarios


def select_role():
    return Role.query.all()


def select_city():
    return City.query


def select_type():
    return CENTER_TYPES_ENUM


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
                             [Length(message="El nombre debe tener entre 2 y 20 caracteres", min=2, max=20),
                              DataRequired()], render_kw={"placeholder": "bob"})
    last_name = StringField('Apellido',
                            [Length(message="El apellido  debe tener entre 2 y 20 caracteres", min=2, max=20),
                             DataRequired()], render_kw={"placeholder": "perez"})
    active = BooleanField('Estado(Activo/Inactivo)')
    role = QuerySelectMultipleField('Rol', query_factory=select_role, get_label='name',
                                    widget=widgets.ListWidget(prefix_label=False),
                                    option_widget=widgets.CheckboxInput())

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
                                                   max=20), ],
                             render_kw={"placeholder": "entre 6 y 20 caracteres"})
    first_name = StringField('Nombre',
                             [Length(message="El nombre  debe tener entre 2 y 20 caracteres", min=2, max=20),
                              DataRequired()])
    last_name = StringField('Apellido',
                            [Length(message="El apellido  debe tener entre 2 y 20 caracteres", min=2, max=20),
                             DataRequired()])
    active = BooleanField('Estado(Activo/Inactivo)')
    user_roles = QuerySelectMultipleField('Rol', query_factory=select_role, get_label='name',
                                          widget=widgets.ListWidget(prefix_label=False),
                                          option_widget=widgets.CheckboxInput())


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


class CreateCenterForm(FlaskForm):
    name = StringField('nombre', validators=[DataRequired(), Length(max=55)])
    address = StringField('direccion')
    phone = StringField('telefono', validators=[])
    email = StringField('email', validators=[DataRequired(), Length(max=60)])
    opening = TimeField('apertura')
    closing = TimeField('cierre')
    city = QuerySelectField('ciudad', query_factory=select_city, get_label='name')
    type = SelectField(label='tipo', choices=[(g, g) for g in CENTER_TYPES])
    web_site = URLField('sitio web', render_kw={"placeholder": "https://www.site.com"})
    geo_location = StringField('coordenadas')
    protocol = FileField('protocolo')