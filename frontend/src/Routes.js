import Vue from 'vue';
import Router from 'vue-router';

import Layout from '@/components/Layout/Layout';
import Login from '@/pages/Login/Login';
import Register from '@/pages/Login/Register';
import AnalyticsPage from '@/pages/Elements/Dashboard';
import Posts from '@/pages/Elements/Posts';
import Schedule from '@/pages/Elements/Schedule';
import Results from '@/pages/Elements/Results';
import Table from '@/pages/Elements/Table';
import Teams from '@/pages/Elements/Teams';
import Zapisnik from '@/pages/Elements/Zapisnik';
import Myaccount from '@/pages/Elements/Myaccount';



Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
    },
    {
      path: '/app',
      name: 'Layout',
      component: Layout,
      children: [
        {
          path: 'myaccount',
          name: 'Myaccount',
          component: Myaccount,
        },
        {
          path: 'posts',
          name: 'Posts',
          component: Posts,
        },
        {
          path: 'schedule',
          name: 'Schedule',
          component: Schedule,
        },
        {
          path: 'results',
          name: 'Results',
          component: Results,
        },
        {
          path: 'table',
          name: 'Table',
          component: Table,
        },
        {
          path: 'teams',
          name: 'Teams',
          component: Teams,
        },
        {
          path: 'dashboard',
          name: 'AnalyticsPage',
          component: AnalyticsPage,
        },
        {
          path: 'zapisnik',
          name: 'Zapisnik',
          component: Zapisnik,
        },
      ],
    },
  ],
});
