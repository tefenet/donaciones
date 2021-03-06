import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/components/Home'
import Map from '@/components/Map'
import SolicitudCentro from '@/components/SolicitudCentro'
import Solicitudes from '@/components/Solicitudes'
import SolicitudTurno from '@/components/SolicitudTurno'
import SolicitudesTurno from '@/components/SolicitudesTurno'
import NotFound404 from '@/components/NotFound404'
import EstadisticasPrincipal from '@/components/stats/main'
import TurnosPorMes from '@/components/stats/turnosPorMes'
import EstadisticasTipoDonacionesPorCiudad from '@/components/stats/tipoDonacionesPorCiudad'
import EstadisticasTopCiudades from '@/components/stats/topCiudades'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {title: 'Inicio'}
    },
    {
        path: '/Mapa',
        name: 'Mapa',
        component: Map,
        meta: {title: 'Mapa'}
    },
    {
        path: '/solicitudes',
        name: 'Solicitudes',
        component: Solicitudes,
        meta: {title: 'Solicitudes'}
    },
    {
        path: '/solicitudCentro',
        name: 'SolicitudCentro',
        component: SolicitudCentro,
        meta: {title: 'Solicitud Centro'}
    },
    {
        path: '/solicitudTurno',
        name: 'SolicitudesTurno',
        component: SolicitudesTurno,
        meta: {title: 'Solicitudes Turno'}
    },
    {
        path: '/reservaTurno/:centro_id',
        name: 'ReservaTurno',
        component: SolicitudTurno,
        meta: {title: 'Reservar Turno'}
    },
    {
        path: "*",
        component: NotFound404,
        meta: {title: 'Error 404'}
    },
    {
        path: '/estadisticas',
        name: 'EstadisticasPrincipal',
        component: EstadisticasPrincipal,
        meta: {title: 'Estadísticas de donaciones'}
    },
    {
        path: '/estadisticas/turnosByMonth',
        name: 'TurnosPorMes',
        component: TurnosPorMes,
        meta: {title: 'Estadisticas: Turnos por mes'}
    },
    {
        path: '/estadisticas/tipodonacionesporciudad',
        name: 'EstadisticasTipoDonacionesPorCiudad',
        component: EstadisticasTipoDonacionesPorCiudad,
        meta: {title: 'Estadisticas: Tipo donaciones por ciudad'}
    },
    {
        path: '/estadisticas/topciudades',
        name: 'EstadisticasTopCiudades',
        component: EstadisticasTopCiudades,
        meta: {title: 'Estadisticas: Top 6 ciudades con mas donaciones'}
    },

]

const router = new VueRouter({
    mode: 'history',
    routes
})

const DEFAULT_TITLE = 'Centros de Ayuda BA';
router.afterEach((to) => {
    // Use next tick to handle router history correctly
    // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
    Vue.nextTick(() => {
        document.title = to.meta.title + ' | ' + DEFAULT_TITLE || DEFAULT_TITLE;
    });
});

export default router;