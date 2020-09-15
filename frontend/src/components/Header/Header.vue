<template>
  <b-navbar class="header d-print-none app-header">
    <b-nav>
      <b-nav-item>
        <a class="d-md-down-none px-2" href="#" @click="toggleSidebarMethod" id="barsTooltip">
          <i class='la la-bars la-lg' />
        </a>
        <a class="fs-lg d-lg-none" href="#" @click="switchSidebarMethod">
          <i class="la la-bars la-lg" />
        </a>
      </b-nav-item>
    </b-nav>
    <a  class="navbarBrand d-md-none">
      <i class="fa fa-circle text-primary mr-n-sm" />
      <i class="fa fa-circle text-danger" />
      &nbsp;
      sing
      &nbsp;
      <i class="fa fa-circle text-danger mr-n-sm" />
      <i class="fa fa-circle text-primary" />
    </a>
    <b-nav class="ml-auto">
      <b-nav-item-dropdown
        class="notificationsMenu d-md-down-none mr-2"
        menu-class="notificationsWrapper py-0 animated animated-fast fadeIn"
        right>
        <template slot="button-content">
          <span>{{fname}} {{lname}}</span>
        </template>
        <b-dropdown-item-button @click="myacc"><i class="la la-user"/>Račun </b-dropdown-item-button>
        <b-dropdown-divider />
        <b-dropdown-item-button @click="logout2">
          <i class="la la-sign-out" /> Log Out
        </b-dropdown-item-button>
      </b-nav-item-dropdown>
    </b-nav>
  </b-navbar>
</template>

<script>
/* eslint-disable */
import { mapState, mapActions } from 'vuex';

import jwtDecode from 'jwt-decode';
import EventBus from '@/pages/Elements/EventBus';

EventBus.$on('logged-in', test => {
  console.log(test)
})

export default {
  name: 'Header',
  components: {},
  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return {
      fname: decoded.identity.fname,
      lname: decoded.identity.lname,
      auth: '',
      user: ''
    };
  },
  computed: {
    ...mapState('layout', ['sidebarClose', 'sidebarStatic']),
  },
  methods: {
    logout2 () {
      localStorage.removeItem('usertoken');
      this.$router.push({ name: 'Login' });
    },
    myacc(){
      this.$router.push({ name: 'Myaccount' });
    },
    ...mapActions('layout', ['toggleSidebar', 'switchSidebar', 'changeSidebarActive']),
    switchSidebarMethod() {
      if (!this.sidebarClose) {
        this.switchSidebar(true);
        this.changeSidebarActive(null);
      } else {
        this.switchSidebar(false);
        const paths = this.$route.fullPath.split('/');
        paths.pop();
        this.changeSidebarActive(paths.join('/'));
      }
    },
    toggleSidebarMethod() {
      if (this.sidebarStatic) {
        this.toggleSidebar();
        this.changeSidebarActive(null);
      } else {
        this.toggleSidebar();
        const paths = this.$route.fullPath.split('/');
        paths.pop();
        this.changeSidebarActive(paths.join('/'));
      }
    },
    logout() {
      window.localStorage.setItem('authenticated', false);
      this.$router.push('/login');
    },
  },
  mounted () {
    EventBus.$on('logged-in', status => {
      this.auth = status
    })
  }
};
</script>

<style src="./Header.scss" lang="scss"></style>
