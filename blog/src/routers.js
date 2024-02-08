import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import Signup from './components/signup.vue';
import Login from './components/Login.vue';
import Add from './components/add.vue';
import UpdateShowComponent from './components/Update.vue';
import addshow from './components/addshow.vue';
import mainhome from './components/mainhome.vue';
import mainlogin from './components/mainlogin.vue';
import mainsignup from './components/mainsignup.vue';
import UserDashboard from './components/UserDashboard.vue';
import venuelist from './components/venuelist.vue';
import VenueDetail from './components/VenueDetail.vue';
import showvenue from './components/showvenue.vue';
import mytickets from './components/mytickets.vue';

const routes = [
  {
    name: 'mainhome',
    component: mainhome,
    path: '/',
  },
  {
    name: 'Signup',
    component: Signup,
    path: '/signup',
  },
  {
    name: 'Login',
    component: Login,
    path: '/login',
  },
  {
    name: 'Add',
    component: Add,
    path: '/add',
  },
  {
    
      path: '/update/:showId',
      name: 'UpdateShow',
      component: UpdateShowComponent,
    
    
  },
  {
    name: 'addshow',
    component: addshow,
    path: '/addshow',
  },
  {
      name: 'home',
      component: Home,
      path: '/home',
  },
  {
    name: 'mainlogin',
    component: mainlogin,
    path: '/mainlogin',
  },
  {
    name: 'mainsignup',
    component: mainsignup,
    path: '/mainsignup',
  },
  {
    name: 'UserDashboard',
    component: UserDashboard,
    path: '/UserDashboard',
  },
  {
    name: 'venuelist',
    component: venuelist,
    path: '/venuelist',
  },
  {
    name: 'VenueDetail', // Use the correct name for the route
    component: VenueDetail, // Use the imported component
    path: '/venues/:id', // Add the dynamic segment to the path
  },
  {
    name: 'showvenue',
    component: showvenue,
    path: '/showvenue',
  },
  {
    name: 'mytickets',
    component: mytickets,
    path: '/mytickets',
  },
  {
    name:'TheaterCSVExport',
    path:'/TheaterCSVExport',
    component: () => import('./components/TheaterCSVExport.vue')
  },
];


const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
