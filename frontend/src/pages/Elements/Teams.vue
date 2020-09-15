<template>
  <div class="dashboard-page">
    <h1 class="page-title">Timovi</h1>
    &nbsp;
    <b-button variant="primary" v-b-modal.createTeam>Dodaj tim</b-button>
     &nbsp;
    <b-button variant="primary" v-b-modal.createPlayer>Dodaj igrača</b-button>
    <b-row><p></p></b-row>
    <b-row>
      <b-col xs="12" lg="6" xl="12"> 
    <div>
    <b-card no-body>
    <b-tabs pills card>
      <b-tab disabled title="Odaberi tim:"></b-tab>
      <b-tab @click="getTeams3(team.id)" :title="team.name" v-for="team of teams" v-bind:key="team.id">
            <Widget class="h-100 mb-0" close>
            <div class="d-flex justify-content-between align-items-center mb-lg">
              <h2>{{team.name}}  &nbsp; &nbsp; &nbsp;
                <b-button class="p-1 px-3 btn-xs btn-default" @click="editTeam(team)" v-b-modal.updateTeam  >Ažuriraj</b-button>
                  &nbsp;
                <b-button class="p-1 px-3 btn-xs btn-default" @click="removeTeam(team.id)">Obriši</b-button>
              </h2>
              <i class="la la-arrow text-primary" />
            </div>
            <div class="d-flex flex-wrap justify-content-between">
              <div class="mt">
                <h6>{{team.location}}</h6><p class="text-muted mb-0 mr"><small>Lokacija</small></p>
              </div>
              <div class="mt">
                <h6>{{team.arena}}</h6><p class="text-muted mb-0"><small>Arena</small></p>
              </div>
              <div class="mt">
                <h6>{{team.head_coach}}</h6><p class="text-muted mb-0 mr"><small>Trener</small></p>
              </div>
              <div class="mt">
                <h6>{{team.president}}</h6><p class="text-muted mb-0 mr"><small>Predsjednik</small></p>
              </div>
              <div class="mt">
                
              </div>
            </div>
            <div class="w-600 py-3 pr-2">
          </div>
          </Widget>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
      <b-row xs="100" lg="100" xl="100">
      <b-card v-for="player of players" v-bind:key="player.id" class="position" :title="'# ' +  player.number_player" :footer="pozicija + player.position">
        <b-img class="avatar" center src="https://image.flaticon.com/icons/svg/1865/1865223.svg"></b-img>
        <b-card-text>Ime:&nbsp;{{player.fname}} {{player.lname}}</b-card-text>
        <b-card-text>Rođen:&nbsp;{{player.born}}</b-card-text>
        <b-card-text>Starost:&nbsp;{{player.years}}</b-card-text>
        <b-card-text>Zemlja:&nbsp;{{player.nationality}}</b-card-text>
        <b-card-text>Mjesto rođenja:&nbsp;{{player.place_of_birth}}</b-card-text>
        <b-card-text>Visina:&nbsp;{{player.height}} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
          <span class="buttonsDeleteAndUpdate2">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <b-button class="p-1 px-3 btn-xs btn-light" @click="removePlayer(player.id)">Obriši</b-button>
          </span>
        </b-card-text>
        
      </b-card>
      </b-row>
      </b-tab>
    </b-tabs>
  </b-card>
    </div>
      </b-col>
    </b-row>
      <b-modal id="createTeam" scrollable title="Dodaj tim" hide-footer ref="my-modal">
        <b-form @submit.prevent="createTeam(); addSuccessNotification1(); hideModal()" class="w-100">
        <!--  -->
        <b-form-group label="Naziv">
          <b-form-input type="text" v-model="name" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Lokacija">
          <b-form-input type="text" v-model="location" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Godina osnivanja">
          <b-form-input type="text" v-model="founded" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Dvorana">
          <b-form-input type="text" v-model="arena" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Trener">
          <b-form-input type="text" v-model="head_coach" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Predsjednik">
          <b-form-input type="text" v-model="president" required>
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="default">Dodaj tim</b-button>
        <b-button variant="default" style="float: right" @click="hideModal()">Odustani</b-button>
        </b-form>
      </b-modal>

      <b-modal id="updateTeam" scrollable title="Izmjeni tim" hide-footer ref="my-modal">
        <b-form class="w-100">
        <!--  -->
        <b-form-group label="Naziv">
          <b-form-input type="text" v-model="editForm.name" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Lokacija">
          <b-form-input type="text" v-model="editForm.location" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Godina osnivanja">
          <b-form-input type="text" v-model="editForm.founded" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Dvorana">
          <b-form-input type="text" v-model="editForm.arena" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Trener">
          <b-form-input type="text" v-model="editForm.head_coach" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Predsjednik">
          <b-form-input type="text" v-model="editForm.president" required>
          </b-form-input>
        </b-form-group>
        </b-form>
        <b-button type="submit" variant="primary" @click="hideModal(); addSuccessNotification2(); onSubmitUpdate()">Ažuriraj</b-button>
      </b-modal>

      <b-modal id="createPlayer" title="Dodaj igrača" hide-footer ref="my-modal" size="lg">
        <b-form @submit.prevent="createPlayer(v-bind); hideModal()" class="w-100">
        <!--  -->
        <b-row>
        <b-col>
        <b-form-group label="Odaberi tim">
          <b-form-select type="text" v-model="player.team_id" required >
            <option v-for="team of teams" v-bind:key="team.id" v-bind:value="team.id">
            {{ team.name }}
          </option>
          </b-form-select>
        </b-form-group>
        <!--  -->
        <b-form-group label="Broj">
          <b-form-input type="text" v-model="player.number_player" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Ime">
          <b-form-input type="text" v-model="player.fname" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Prezime">
          <b-form-input type="text" v-model="player.lname" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Pozicija">
          <b-form-input type="text" v-model="player.position" required>
          </b-form-input>
        </b-form-group>
        </b-col>
        <b-col>
        <!--  -->
        <b-form-group label="Datum rođenja">
          <b-form-input type="text" v-model="player.born" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Starost">
          <b-form-input type="text" v-model="player.years" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Drzava">
          <b-form-input type="text" v-model="player.nationality" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Visina">
          <b-form-input type="text" v-model="player.height" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Mjesto rođenja">
          <b-form-input type="text" v-model="player.place_of_birth" required>
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="default" style="float: right;">Dodaj igrača</b-button>
        </b-col>
        </b-row>
        </b-form>
      </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
  name: 'Teams',
  components: {
  },
  data() {
    return {
      pozicija: 'Pozicija: ',
      teams: [],
      players: [],
      player: {
        team_id: '',
        fname: '',
        lname: '',
        position: '',
        born: '',
        years: '',
        nationality: '',
        height: '',
        place_of_birth: '',
        number_player: '',

      },
      name: '',
      location: '',
      founded: '',
      arena: '',
      president: '',
      head_coach: '',
      editForm: {
        id: '',
        name: '',
        location: '',
        founded: '',
        arena: '',
        president: '',
        head_coach: '',
      },
    };
  },
  methods: {
    addSuccessNotification1() {
      this.$toasted.success('Tim uspješno dodan!', {
      })
    },
    addSuccessNotification2() {
      this.$toasted.success('Tim uspješno ažuriran!', {
      })
    },
    addSuccessNotification3() {
      this.$toasted.error('Ne možete obrisati tim ako sadrži igrače.', {
      })
    },
    getTeams() {
      axios.get('http://localhost:8000/teams').then((response) => {
        this.teams = response.data;
      })
    },
    getTeams3(team_id) {
      axios.get(`http://localhost:8000/players/${team_id}/team`).then((response) => {
        this.players = response.data;
      })
    },
    createTeam() {
      axios.post('http://localhost:8000/team', {
        name: this.name,
        location: this.location,
        founded: this.founded,
        arena: this.arena,
        president: this.president,
        head_coach: this.head_coach,
      }).then((res) => {
        this.getTeams();
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    createPlayer() {
      axios.post(`http://localhost:8000/player/team`, {
        fname: this.player.fname,
        lname: this.player.lname,
        position: this.player.position,
        born: this.player.born,
        years: this.player.years,
        nationality: this.player.nationality,
        height: this.player.height,
        place_of_birth: this.player.place_of_birth,
        number_player: this.player.number_player,
        id_team: this.player.team_id,

      }).then((res) => {
        this.getTeams3();
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    removeTeam(team_id) {
      const path = `http://localhost:8000/team/${team_id}`;
      axios.delete(path)
        .then(() => {
          this.getTeams();   
        })
        .catch((error) => {
          //this.errorMessage = 'Ne možete obrisati tim ako sadrži igrače.';
          this.addSuccessNotification3();
          console.error(error);
        });        
    },
    removePlayer(player_id) {
      const path = `http://localhost:8000/player/${player_id}`;
      axios.delete(path)
        .then(() => {
          this.getTeams3();   
        })
        .catch((error) => {
          console.error(error);
        });        
    },
    editTeam(team_id) {
      this.editForm = team_id;
    },
    onSubmitUpdate() {
      const payload = {
        name: this.editForm.name,
        location: this.editForm.location,
        founded: this.editForm.founded,
        arena: this.editForm.arena,
        president: this.editForm.president,
        head_coach: this.editForm.head_coach,
        wins: '',
        loses: '',
        games_played: '',
        points: '',

      };
      this.updateTeam(payload, this.editForm.id);
    },
    updateTeam(payload, team_id) {
      const path = `http://localhost:8000/team/${team_id}`;
      axios.put(path, payload)
        .then(() => {
          this.getTeams();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    hideModal() {
      this.$refs['my-modal'].hide();
    },
  },
  created() {
    this.getTeams();
    this.getTeams3();
  },
};
</script>

<style lang="scss">
.position {
   left : 35px;
   margin-right: 30px;
   margin-bottom: 30px;
   width: 300px;
   height: 405px;
}

.teampos {
   left : 480px;
   margin-top: 35px;
   margin-bottom: 30px;
   width: 350px;
   height: 200px;
}

.avatar {
   margin-top: 4px;
   margin-bottom: 10px;
   width: 90px;
   height: 90px;
}

.buttonsDeleteAndUpdate2 {
  left : 480px;
}
</style>
