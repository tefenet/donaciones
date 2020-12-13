import Vue from 'vue'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faFacebook, faInstagram, faTwitter} from '@fortawesome/free-brands-svg-icons'
import {
    faPhone,
    faMapMarkerAlt,
    faClock,
    faDoorOpen,
    faDoorClosed,
    faCalendar,
    faCalendarAlt,
    faCalendarWeek,
    faCity,
    faBuilding,
    faInfoCircle
} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

library.add(faFacebook, faInstagram, faTwitter, faPhone, faMapMarkerAlt, faClock, faDoorClosed, faDoorOpen, faCalendar,
    faCalendarAlt, faInfoCircle, faCalendarWeek, faCity, faBuilding)

Vue.component('font-awesome-icon', FontAwesomeIcon)
