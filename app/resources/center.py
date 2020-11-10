import io
from datetime import date

from flask import redirect, render_template, request, url_for, abort, flash, send_file
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequestKeyError

from app import dbSession
from app.helpers.auth import restricted
from app.helpers.handler import display_errors
from app.helpers.pagination import paginate
from app.models.center import Center, STATES
from app.models.sistema import Sistema
from app.resources.forms import CreateCenterForm
SYS_PAGE_COUNT = Sistema.page_count()


@restricted(perm='centro_index')
def index():
    try:
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError):
        page = 1
    try:
        res = paginate(Center.get_for_index(), page, SYS_PAGE_COUNT)
    except AttributeError:
        return redirect(url_for('center_index'))
    return render_template("center/index.html", pagination=res)


@restricted(perm='centro_new')
def new():
    form = CreateCenterForm()
    return render_template("center/new.html", form=form)


@restricted(perm='centro_new')
def create():
    """ Da de alta un centro en la base de datos."""
    form = CreateCenterForm()
    if form.validate():
        center = Center()
        form.populate_obj(center)
        center.protocol = request.files['protocol'].read()
        dbSession.add(center)
        dbSession.commit()
    if form.errors:
        display_errors(form.errors)
        return new()
    return redirect(url_for("center_index", page=1))


@restricted(perm='centro_destroy')
def delete_center():
    """Elimina un centro de manera definitiva"""
    try:
        center_id = request.args['object_id']
        center_name = Center.get_by_id(center_id).name
        if Center.delete_by_id(center_id):
            dbSession.commit()
            flash("el Centro {} ha sido borrado".format(center_name), "info")
    except BadRequestKeyError:
        flash("ERROR: id Centro no recibido", "danger")
    finally:
        return redirect(url_for('center_index'))


@restricted('centro_update')
def update_center_form(object_id):
    """ renderiza el formulario para editar un centro """
    center = Center.get_by_id(object_id)
    if center:
        form = CreateCenterForm(obj=center)
        return render_template('center/update.html', form=form, center_id=object_id)
    abort(500, "ERROR: Error al obtener centro id = {}".format(object_id))


@restricted('centro_update')
def update_center(object_id):
    """ edita los atributos del centro con los datos obtenidos del formulario """
    form = CreateCenterForm(request.form)
    if form.validate():
        center = Center.get_by_id(object_id)
        form.populate_obj(center)
        center.protocol = request.files['protocol'].read()
        dbSession.commit()
    elif form.errors:
        display_errors(form.errors)
        flash("Error al validar formulario", "danger")
        return update_center_form(object_id)
    flash("se guardaron los cambios", "info")
    return redirect(url_for("center_index"))


def search_by_name():
    """Busca centros por nombre.
        Recibe name, que es un string, devuelve una lista paginada de centros """
    try:
        name = request.args['name']
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('center_index'))
    query = Center.query_by_name(name)
    try:
        pagination = paginate(query, page, SYS_PAGE_COUNT)
    except AttributeError:  # raised when page < 1
        pagination = paginate(query, 1, SYS_PAGE_COUNT)
    return render_template("center/index.html", pagination=pagination)


def search_by_state():
    try:
        state = request.args['state']
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('center_index'))
    query = Center.query_by_state(state)
    try:
        pagination = paginate(query, page, SYS_PAGE_COUNT)
    except AttributeError:
        pagination = paginate(query, 1, SYS_PAGE_COUNT)
    return render_template("center/index.html", pagination=pagination)


def search_by_published():
    try:
        published = False if request.args['published'] == "False" else True
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('center_index'))
    query = Center.query_by_published(published)
    try:
        page = int(request.args['page'])
        pagination = paginate(query, page, SYS_PAGE_COUNT)
    except (BadRequestKeyError, ValueError):
        pagination = paginate(query, 1, SYS_PAGE_COUNT)
    except AttributeError:
        pagination = paginate(query, 1, SYS_PAGE_COUNT)
    return render_template("center/index.html", pagination=pagination)


def change_state(method, message):
    try:
        center_id = request.args['object_id']
    except BadRequestKeyError:
        flash("ERROR: id Centro no recibido", "danger")
        return redirect(url_for("center_index"))
    center = Center.get_by_id(center_id)
    try:
        getattr(center, method)()
    except IntegrityError:
        flash('hubo un problema en la transacción', 'danger')
        return redirect(url_for("center_index"))
    except AttributeError as e:
        flash(e, 'danger')
        return redirect(url_for("center_index"))
    flash(message.format(center.name), "info")
    return redirect(url_for("center_index"))


@restricted('centro_update')
def approve_center():
    return change_state('approve', "el centro {} fue aprobado")


@restricted('centro_update')
def reject_center():
    return change_state('reject', "el centro {} fue rechazado")


@restricted('centro_update')
def review_center():
    return change_state('review', "el centro {} está pendiente de revisión")


@restricted('centro_update')
def toogle_publish_center():
    """ edita los atributos del centro con los datos obtenidos del formulario """
    return change_state('toogle_published', "el centro {} cambio su estado")


def get_protocol(object_id):
    try:
        center = Center.get_by_id(object_id)
        return send_file(io.BytesIO(center.protocol), mimetype='pdf', as_attachment=True,
                         attachment_filename='{} protocol.pdf'.format(center.name))
    except BadRequestKeyError:
        flash("ERROR: id Centro no recibido", "danger")
    return redirect(url_for("center_index"))
