import Vue from 'vue'
import App from './App.vue'
import router from '@/router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css' // importo los estilos de vbootstrap
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue) // Registro BootstrapVue
Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
