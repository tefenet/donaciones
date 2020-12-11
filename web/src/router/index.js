import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/components/Home'
import Estadisticas from '@/components/Estadisticas'
import Map from '@/components/Map'
import SolicitudCentro from '@/components/SolicitudCentro'
import Solicitudes from '@/components/Solicitudes'
import SolicitudesTurno from '@/components/SolicitudTurno'
import NotFound404 from '@/components/NotFound404'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {title: 'Inicio'}
    },
    {
        path: '/estadisticas',
        name: 'Estadisticas',
        component: Estadisticas,
        meta: {title: 'Estadísticas'}
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
        name: 'SolicitudTurno',
        component: SolicitudesTurno,
        meta: {title: 'Solicitud Turno'}
    },
    {
        path: "*",
        component: NotFound404,
        meta: {title: 'Error 404'}
    }
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