from flask import redirect, render_template, request, url_for, abort, flash
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequestKeyError
from app import dbSession
from app.helpers.auth import restricted
from app.helpers.handler import display_errors
from app.helpers.pagination import paginate
from app.models.center import Center, STATES
from app.models.sistema import Sistema
from app.resources.forms import CreateCenterForm


@restricted(perm='centro_index')
def index():
    sys = Sistema.get_sistema()
    try:
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError):
        page = 1
    try:
        res = paginate(Center.query, page, sys.cant_por_pagina)
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
    form = CreateCenterForm(request.form)
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
def toogle_publish_center():
    """ edita los atributos del centro con los datos obtenidos del formulario """
    try:
        center_id = request.args['object_id']
    except BadRequestKeyError:
        flash("ERROR: id Centro no recibido", "danger")
    center = Center.get_by_id(center_id)
    try:
        center.toogle_published()
    except AttributeError as e:
        flash(e, 'danger')
        return redirect(url_for("center_index"))
    flash("el centro {} ha sido {}".format(center.name, "publicado" if center.published else "despublicado"), "info")
    return redirect(url_for("center_index"))


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
    sys = Sistema.get_sistema()
    query = Center.query_by_name(name)
    try:
        pagination = paginate(query, page, sys.cant_por_pagina)
    except AttributeError:  # raised when page < 1
        pagination = paginate(query, 1, sys.cant_por_pagina)
    return render_template("center/index.html", pagination=pagination)


def search_by_state():
    try:
        state = request.args['state']
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('center_index'))
    sys = Sistema.get_sistema()
    query = Center.query_by_state(state)
    try:
        pagination = paginate(query, page, sys.cant_por_pagina)
    except AttributeError:
        pagination = paginate(query, 1, sys.cant_por_pagina)
    return render_template("center/index.html", pagination=pagination)


def search_by_published():
    try:
        published = False if request.args['published'] == "False" else True
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('center_index'))
    sys = Sistema.get_sistema()
    query = Center.query_by_published(published)
    try:
        page = int(request.args['page'])
        pagination = paginate(query, page, sys.cant_por_pagina)
    except (BadRequestKeyError, ValueError):
        pagination = paginate(query, 1, sys.cant_por_pagina)
    except AttributeError:
        pagination = paginate(query, 1, sys.cant_por_pagina)
    return render_template("center/index.html", pagination=pagination)


@restricted('centro_update')
def approve_center():
    center_id = request.args['center_id']
    center = Center.get_by_id(center_id)
    center.state = STATES[1]
    center.published = True
    try:
        dbSession.commit()
    except IntegrityError:
        return redirect(url_for("center_index"))
    flash("el centro {} fue aprobado".format(center.name), "info")
    return redirect(url_for("center_index"))


@restricted('centro_update')
def reject_center():
    center_id = request.args['center_id']
    center = Center.get_by_id(center_id)
    center.state = STATES[2]
    center.published = False
    try:
        dbSession.commit()
    except IntegrityError:
        return redirect(url_for("center_index"))
    flash("el centro {} fue rechazado".format(center.name), "info")
    return redirect(url_for("center_index"))
