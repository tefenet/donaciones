from datetime import date, time, datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, \
    RadioField, widgets, SelectField, HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length, length, Email, EqualTo, Optional
from wtforms.fields.html5 import EmailField, TimeField, URLField, DateField

from app.models.center import CENTER_TYPES_ENUM, CENTER_TYPES

from app.models.role import Role
from app.models.user import User
from app.models.shifts import Shifts


class LoginForm(FlaskForm):
    """Formulario para inicio de sesión del usuario"""

    username = StringField('Usuario: ', [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Contraseña: ', [DataRequired()])
    submit = SubmitField('Iniciar Sesión')

    # Formulario para registro de usuarios


def select_role():
    return Role.query.all()


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
    active = BooleanField('Estado (Activo/Inactivo)', default="checked")
    role = QuerySelectMultipleField('Rol', query_factory=select_role, get_label='name',
                                    widget=widgets.ListWidget(prefix_label=False),
                                    option_widget=widgets.CheckboxInput())
    user_roles = QuerySelectMultipleField('Rol', query_factory=select_role, get_label='name',
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


class CreateCenterForm(FlaskForm):
    name = StringField('nombre', validators=[DataRequired(), Length(max=55)])
    address = StringField('direccion', validators=[Length(max=99)])
    phone = StringField('telefono',
                        validators=[Length(min=8, max=20, message='el telefono debe tener entre 8 y 20 digitos')])
    email = EmailField('email', validators=[DataRequired(), Email('el email ingresado no es válido'),
                                            Length(max=60, message='se permite hasta 60 caracteres')])
    opening = TimeField('apertura', validators=[DataRequired()])
    closing = TimeField('cierre', validators=[DataRequired()])
    city_id = SelectField('ciudad', choices=[])
    center_type = SelectField(label='tipo', choices=[(g, g) for g in CENTER_TYPES])
    web_site = URLField('sitio web', render_kw={"placeholder": "https://www.site.com"})
    protocol = FileField('protocolo', widget=widgets.FileInput(),
                         validators=[FileAllowed(['pdf'], 'protocolo en pdf unicamente')])
    gl_lat = HiddenField()
    gl_long = HiddenField()

    @classmethod
    def validate_phone(cls, form, phone):
        for ch in phone.data:
            if not ch.isdigit():
                raise ValidationError('al ingresar el telefono, utilice dígitos únicamente, sin espacios ni guiones')

    @classmethod
    def validate_opening(cls, form, opening):
        if form.closing.data <= opening.data:
            raise ValidationError('el horario de apertura y cierre no son correctos')


shifts_blocks = [time(9), time(9, 30), time(10), time(10, 30), time(11), time(11, 30), time(12), time(12, 30),
                 time(13), time(13, 30), time(14), time(14, 30), time(15), time(15, 30)]


class CreateShiftForm(FlaskForm):
    donor_email = EmailField('Email Donante', validators=[DataRequired("El email es obligatorio"), Length(max=55),
                                                          Email(message="Ingresá un correo electronico válido")])
    donor_phone = StringField('Telefono Donante',
                              validators=[DataRequired("El telefono es obligatorio"), Length(max=55)])
    date = DateField("Día", validators=[DataRequired("El día es obligatorio")])
    start_time = SelectField("Horario", choices=shifts_blocks)

    def validate_start_time(self, start_time):
        try:
            start = datetime.strptime(start_time.data, '%H:%M:%S').time()
        except ValueError as e:
            raise ValidationError(e, ' seleccione un horario válido')
        if self.date.data == date.today() and start < datetime.now().time():
            raise ValidationError('seleccione un horario válido')
        self.start_time.data = start

    @classmethod
    def validate_date(cls, form, dat):
        if dat.data < date.today():
            raise ValidationError('seleccione una fecha válida')

    @classmethod
    def validate_donor_phone(cls, form, phone):
        for ch in phone.data:
            if not ch.isdigit():
                raise ValidationError(
                    'al ingresar el numero de telefono, utilice solo con digitos, sin espacios ni guiones')


class SearchDonorEmailForm(FlaskForm):
    donor_email = SelectField(choices=Shifts.get_donor_email_set(), render_kw={'style': 'width: auto;'})
