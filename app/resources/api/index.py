from flask import jsonify


def index():
    json = {
        'info': 'referencia rutas principales de la api',
        'centros':
            {
                'api/v1.0/centros/': [
                    {
                        'METHOD': 'GET',
                        'PARAMS': [],
                        'DESCRP': 'listado de centros paginados',
                        'RESPON': [200, 400],

                    },
                    {
                        'METHOD': 'POST',
                        'PARAMS': ['centro'],
                        'DESCRP': 'da de alta un centro en el sistema',
                        'RESPON': [200, 400, 500],
                    }
                ],
                'api/v1.0/centrosAll/':
                    {
                        'METHOD': 'GET',
                        'PARAMS': [],
                        'DESCRP': 'listado de centros sin paginar',
                        'RESPON': [200, 400, 500],
                    },
                'api/v1.0/centros/:id':
                    {
                        'METHOD': 'GET',
                        'PARAMS': ['id'],
                        'DESCRP': 'devuelve un centro id',
                        'RESPON': [200, 400],
                    },
                'api/v1.0/centros/:id/turnos_disponibles':
                    {
                        'METHOD': 'GET',
                        'PARAMS': ['id', 'date'],
                        'DESCRP': 'devuelve una lista de turnos disponibles para el centro id en una fecha dada',
                        'RESPON': [200, 400],
                    },
                'api/v1.0/centros/:id/reserva':
                    {
                        'METHOD': 'POST',
                        'PARAMS': ['id', 'turno'],
                        'DESCRP': 'reserva un turno para el centro id en el sistema',
                        'RESPON': [200, 400],
                    },

            },
        'stats':
            {
                'api/v1.0/stats/byMonth/:month>':
                    {
                        'METHOD': 'GET',
                        'PARAMS': ['month_id'],
                        'DESCRP': 'Devuelve los turnos por ciudad para el mes indicado',
                        'RESPON': [200, 400, 500],
                    },
                'api/v1.0/stats/byCity/:city_id':
                    {
                        'METHOD': 'GET',
                        'PARAMS': ['city_id'],
                        'DESCRP': 'dada una ciudad Devuelve los turnos totales por tipo de centro de la'
                                  ' ciudad indicada, recibe el id de la ciudad',
                        'RESPON': [200, 400, 500],
                    },
                'api/v1.0/stats/byCity/topSixCity':
                    {
                        'METHOD': 'GET',
                        'PARAMS': ['city_id'],
                        'DESCRP': 'Devuelve las 6 ciudaes con mas turnos para centros de alimentos en este mes, '
                                  'y sus cantidades respectivas.no recibe parametros',
                        'RESPON': [200, 400, 500],
                    },
            },
        'consultas':
            {
                'api/v1.0/consultas/':
                    {
                        'METHOD': 'GET',
                        'PARAMS': [],
                        'DESCRP': 'devuelve una lista de issues',
                        'RESPON': [200, 400],
                    },
            },
    }
    return jsonify(json), 200
