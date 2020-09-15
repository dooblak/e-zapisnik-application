<template>
  <div class="sidebar-wrapper">
    <nav
        :class="{sidebar: true, sidebarStatic, sidebarOpened}"
        @mouseenter="sidebarMouseEnter"
        @mouseleave="sidebarMouseLeave"
    >
      <header class="logo">
        <router-link to="/app/posts"><span class="primary-word">E-zapisnik</span></router-link>
      </header>
      <ul class="nav">
        <NavLink
            :activeItem="activeItem"
            header="Novosti"
            link="/app/posts"
            iconName="flaticon-edit"
            index="posts"
            isHeader
        />
        <NavLink
            :activeItem="activeItem"
            header="Raspored"
            link="/app/schedule"
            iconName="flaticon-calendar"
            index="schedule"
            isHeader
        />
        <NavLink
            :activeItem="activeItem"
            header="Rezultati"
            link="/app/results"
            iconName="flaticon-bookmark"
            index="results"
            isHeader
        />
        <NavLink
            :activeItem="activeItem"
            header="Tablica"
            link="/app/table"
            iconName="flaticon-list"
            index="table"
            isHeader
        />
        <NavLink
            :activeItem="activeItem"
            header="Timovi"
            link="/app/teams"
            iconName="flaticon-file"
            index="teams"
            isHeader
        />
         <NavLink
            :activeItem="activeItem"
            header="Zapisnik"
            link="/app/zapisnik"
            iconName="flaticon-document"
            index="zapisnik"
            isHeader
        />
      </ul>
    </nav>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import isScreen from '@/core/screenHelper';
import NavLink from './NavLink/NavLink';

export default {
  name: 'Sidebar',
  components: { NavLink },
  data() {
    return {
    };
  },
  methods: {
    ...mapActions('layout', ['changeSidebarActive', 'switchSidebar']),
    setActiveByRoute() {
      const paths = this.$route.fullPath.split('/');
      paths.pop();
      this.changeSidebarActive(paths.join('/'));
    },
    sidebarMouseEnter() {
      if (!this.sidebarStatic && (isScreen('lg') || isScreen('xl'))) {
        this.switchSidebar(false);
        this.setActiveByRoute();
      }
    },
    sidebarMouseLeave() {
      if (!this.sidebarStatic && (isScreen('lg') || isScreen('xl'))) {
        this.switchSidebar(true);
        this.changeSidebarActive(null);
      }
    },
  },
  created() {
    this.setActiveByRoute();
  },
  computed: {
    ...mapState('layout', {
      sidebarStatic: state => state.sidebarStatic,
      sidebarOpened: state => !state.sidebarClose,
      activeItem: state => state.sidebarActiveElement,
    }),
  },
};
</script>

<!-- Sidebar styles should be scoped -->
<style src="./Sidebar.scss" lang="scss" scoped/>
