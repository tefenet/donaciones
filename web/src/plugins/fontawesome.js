import Vue from 'vue'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faFacebook, faInstagram, faTwitter} from '@fortawesome/free-brands-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

library.add(faFacebook, faInstagram, faTwitter)

Vue.component('font-awesome-icon', FontAwesomeIcon)
