<template>
  <div class="tables-basic">
    <h2 class="page-title">Tablica - <span class="fw-semi-bold">Sezona 2019/2020</span></h2>
    <b-row>
      <b-col>
        <Widget customHeader settings close>
          <div class="table-resposive">
            <table class="table">
              <thead>
                <tr>
                  <th class="hidden-sm-down">#</th>
                  <th></th>
                  <th>Tim</th>
                  <th class="hidden-sm-down">P</th>
                  <th class="hidden-sm-down">I</th>
                  <th class="hidden-sm-down">OS</th>
                  <th class="hidden-sm-down">Info</th>
                  <th class="hidden-sm-down">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="team in teams" :key="team.id">
                  <td>{{team.id}}</td>
                  <td>
                    <img class="img-rounded" :src="picture" alt="" height="60" />
                  </td>
                  <td>
                    {{team.name}}
                    <div>
                    </div>
                  </td>
                  <td class="text-semi-muted">
                    {{team.wins}}
                  </td>
                  <td class="text-semi-muted">
                    {{team.loses}}
                  </td>
                  <td>
                    {{team.games_played}}
                  </td>
                  <td>
                    <p class="mb-0">
                      <small>
                        <span class="fw-semi-bold">Bodovi:</span>
                        <span class="text-muted">&nbsp; {{team.points}}</span>
                      </small>
                    </p>
                    <p>
                      <small>
                        <span class="fw-semi-bold">Ukupno koševa:</span>
                        <span class="text-muted">&nbsp; 1500-1332</span>
                      </small>
                    </p>
                  </td>
                  <td >
                      <b-button v-if="team.id <8" type="submit" :variant="colorClass1"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b-button>
                      <b-button v-if="team.id == 8" type="submit" :variant="colorClass2"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b-button>
                      <b-button v-if="team.id == 9" type="submit" :variant="colorClass3"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b-button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="clearfix">
            <b-button type="submit" variant="primary"></b-button>
            <p>Sljedeća faza - Premijer liga (Playoff)</p>
            <b-button type="submit" variant="warning"></b-button>
            <p>Premijer liga (Relegacija - doigravanje)</p> 
            <b-button type="submit" variant="danger"></b-button>
            <p>Relegacija</p> 
          </div>
        </Widget>
      </b-col>
    </b-row>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import Widget from '@/components/Widget/Widget';

export default {
  name: 'Table',
  components: {
    Widget,
  },
  data() {
    return {
      colorClass1: 'primary',
      colorClass2: 'warning',
      colorClass3: 'danger',
      teams: [],
      picture: require('../../assets/tables/6.jpg')
    };
  },
  methods: {
    getTeams() {
      axios.get('http://localhost:8000/teams').then((response) => {
        this.teams = response.data;
      })
    },
  },
  created() {
    this.getTeams();
  },
};
</script>

<style>
.mb-0{
  width: -150px;
}
</style>
