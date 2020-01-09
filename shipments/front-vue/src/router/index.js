import Vue from 'vue'
import Router from 'vue-router'
import ShipmentList from '@/components/ShipmentList'
import ShipmentDetail from '@/components/ShipmentDetail'
import ShipmentCreate from '@/components/ShipmentCreate'
import Home from '@/components/Home'
import NotFound from '@/components/404.vue';

Vue.use(Router)
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default new Router({
  mode: 'history',
  routes: [
  {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/shipments/',
      name: 'shipment_list',
      component: ShipmentList,
      meta: {title: 'Shipments list'}
    },
    {
      path: '/shipments/create',
      name: 'shipment_create',
      component: ShipmentCreate
    },
    {
      path: '/shipments/:id',
      name: 'shipment_detail',
      component: ShipmentDetail
    },
    { path: '*', component: NotFound }
  ]
})
