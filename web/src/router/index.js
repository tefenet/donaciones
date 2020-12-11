import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/components/Home'
import Estadisticas from '@/components/Estadisticas'
import Map from '@/components/Map'
import SolicitudCentro from '@/components/SolicitudCentro'
import Solicitudes from '@/components/Solicitudes'
import SolicitudesTurno from '@/components/SolicitudTurno'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/estadisticas',
        name: 'Estadisticas',
        component: Estadisticas
    },
    {
        path: '/Mapa',
        name: 'Mapa',
        component: Map
    },
    {
        path: '/solicitudes',
        name: 'Solicitudes',
        component: Solicitudes
    },
    {
        path: '/solicitudCentro',
        name: 'SolicitudCentro',
        component: SolicitudCentro
    },
    {
        path: '/solicitudTurno',
        name: 'SolicitudTurno',
        component: SolicitudesTurno
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router;