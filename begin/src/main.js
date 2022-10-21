import Vue from 'vue';
import App from './App.vue';
import VCharts from 'v-charts';
import VueECharts from 'vue-echarts' 
import ElementUI from 'element-ui';
import VueRouter from 'vue-router';
import 'element-ui/lib/theme-chalk/index.css';
import "echarts";


Vue.config.productionTip = false

Vue.use(VCharts);
Vue.use(ElementUI);
Vue.use(VueRouter);
Vue.component('v-chart',  VueECharts);

// 引入组件
import MyHome from './components/MyHome.vue';
import BasicData from './components/BasicData.vue';
import CorrelationAnalysis from './components/CorrelationAnalysis.vue';
import BoxOffice from './components/BoxOffice.vue';
import PopularWel from './components/PopularWel.vue';
import SummaryAn from './components/SummaryAn.vue';

// 配置路由
const routes = [
  { path: '/', component: MyHome },
  { path: '/home', component: MyHome },
  { path: '/basicData', component: BasicData },
  { path: '/correlationAnalysis', component: CorrelationAnalysis },
  { path: '/boxOffice', component: BoxOffice },
  { path: '/popularWel', component: PopularWel },
  { path: '/summaryAn', component: SummaryAn },
]
// 实例化VueRouter
const router = new VueRouter({
  routes
})

new Vue({
  // 挂载路由
  router,
  render: h => h(App),
}).$mount('#app')
