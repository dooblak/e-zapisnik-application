<template>
  <div class="posts-page">
    <h1 class="page-title">Raspored</h1>
    <b-button variant="primary" v-b-modal.createPost>Dodaj utakmicu</b-button>
    <b-row><p></p></b-row>
    <b-row>
      <b-col xs="12" lg="6" xl="4" v-for="match of matches" v-bind:key="match.id">
    <div class="mb-xlg">
    <Widget class="h-100 mb-0" close>
            <div>
              <div class="w-600 py-3 pr-2" style="float: right">
              <b-dropdown variant="primary" class="ml-xs" size="sm" text="Uredi" right>
                <b-dropdown-item-btn v-b-modal.updateMatch @click.native="editMatch(match)">
                <i class="la la-refresh" />
                  Ažuriraj
                </b-dropdown-item-btn>
                <b-dropdown-divider />
                <b-dropdown-item @click="removeMatch(match.id); addSuccessNotification3();">
                 <i class="la la-trash" />
                  Obriši
                </b-dropdown-item>
              </b-dropdown>
              </div>
              <h2>{{match.arena}}</h2>
              <h5>{{match.date}}&nbsp;{{match.hours}}h</h5>
            </div>
            <div class="d-flex flex-wrap justify-content-between">
              <div class="mt">
                <h6>{{match.home}}</h6><p class="text-muted mb-0 mr"><small>Domaci</small></p>
              </div>
              <div class="mt">
                <h6>{{match.away}}</h6><p class="text-muted mb-0"><small>Gosti</small></p>
              </div>
              <div class="mt">
             
              </div>
            </div>
          </Widget>
    </div>
      </b-col>
    </b-row>
    <b-modal id="createPost" scrollable title="Dodaj utakmicu" hide-footer ref="my-modal">
        <b-form @submit.prevent="createMatch(); addSuccessNotification1(); hideModal()" class="w-100" >
        <!--  -->
        <b-form-group label="Domaci">
          <b-form-input type="text" v-model="home" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Gosti">
          <b-form-input type="text" v-model="away" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Arena">
          <b-form-input type="text" v-model="arena" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Datum">
          <b-form-input type="text" v-model="date" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Sati">
          <b-form-input type="text" v-model="hours" required>
          </b-form-input>
        </b-form-group>
         <b-button type="submit" variant="default">Dodaj utakmicu</b-button>
        <b-button variant="default" style="float: right" @click="hideModal()">Odustani</b-button>
        </b-form>
      </b-modal>

      <b-modal id="updateMatch" scrollable title="Izmjeni utakmicu" hide-footer ref="my-modal">
        <b-form class="w-100">
        <!--  -->
        <b-form-group label="Domaci">
          <b-form-input type="text" v-model="editForm.home" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Gosti">
          <b-form-input type="text" v-model="editForm.away" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Arena">
          <b-form-input type="text" v-model="editForm.arena" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Datum">
          <b-form-input type="text" v-model="editForm.date" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Sati">
          <b-form-input type="text" v-model="editForm.hours" required>
          </b-form-input>
        </b-form-group>
        </b-form>
          <b-button type="submit" variant="primary" @click="hideModal(); addSuccessNotification2(); onSubmitUpdate()">Ažuriraj</b-button>
      </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import Widget from '@/components/Widget/Widget';

export default {
  name: 'Schedule',
  components: {
    Widget,
  },
  data() {
    return {
      matches: [],
      home: '',
      away: '',
      date: '',
      hours: '',
      arena: '',
      editForm: {
        id: '',
        away: '',
        date: '',
        hours: '',
        arena: '',

      }
    };
  },
  methods: {
    addSuccessNotification1() {
      this.$toasted.success('Utakmica uspješno dodana!', {
      })
    },
    addSuccessNotification2() {
      this.$toasted.success('Utakmica uspješno ažurirana!', {
      })
    },
    addSuccessNotification3() {
      this.$toasted.success('Utakmica uspješno obrisana!', {
      })
    },
    getMatches() {
      axios.get('http://localhost:8000/matches').then((response) => {
        this.matches = response.data;
      })
    },
  createMatch() {
      axios.post('http://localhost:8000/match', {
        home: this.home,
        away: this.away,
        arena: this.arena,
        date: this.date,
        hours: this.hours,
      }).then((res) => {
        this.getMatches();
        this.home = '',
        this.away = '',
        this.arena = '',
        this.date = '',
        this.hours = '',
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    removeMatch(match_id) {
      const path = `http://localhost:8000/match/${match_id}`;
      axios.delete(path)
        .then(() => {
          this.getMatches();   
        })
        .catch((error) => {
          console.error(error);
        });         
    },
    editMatch(match_id) {
      this.editForm = match_id;
    },
    onSubmitUpdate() {
      const payload = {
        home: this.editForm.home,
        away: this.editForm.away,
        date: this.editForm.date,
        arena: this.editForm.arena,
        hours: this.editForm.hours,
      };
      this.updateMatch(payload, this.editForm.id);
    },
    updateMatch(payload, match_id) {
      const path = `http://localhost:8000/match/${match_id}`;
      axios.put(path, payload)
        .then(() => {
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
      this.getMatches();
    },
};
</script>
