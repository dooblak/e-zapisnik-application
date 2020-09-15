<template>
  <div class="dashboard-page">
    <h1 class="page-title">Rezultati</h1>
    <b-button variant="primary" v-b-modal.createResult>Dodaj rezultat</b-button>
    <b-row><p></p></b-row> 
    <b-row>
      <b-col lg="3" sm="6" xs="12" v-for="result of results" v-bind:key="result.id">
        <div class="pb-xlg h-100">
          <Widget class="h-100 mb-0" close>
            <p class="text-muted d-flex flex-wrap">
              <small class="mr-lg d-flex align-items-center">
                <span class="circle bg-primary text-danger mr-xs" style="font-size: 4px;">
                  .
                </span>
                  Domaci
              </small>
              <small class="mr-lg d-flex align-items-center">
                <span class="circle bg-success text-primary mr-xs" style="font-size: 4px;">
                  .
                </span>
                Gosti
              </small>
            </p>
            <h5>{{result.home}}
            <i class="la la-arrow-right text-primary la-sm" />
            {{result.home_points}}
            </h5>
            <b-progress class="mb-xs" style="height: 6px"
              variant="primary" :value="result.home_points" :max="100" />
              <b-row><p></p></b-row> 
            <h5>{{result.away}}
            <i class="la la-arrow-right text-primary la-sm" />
            {{result.away_points}}
            </h5>
            <b-progress class="mb" style="height: 5px"
              variant="success" :value="result.away_points" :max="100" />

            <h6>Datum: {{result.date}}</h6>
          <div class="w-600 py-3 pr-2">
            <div class="d-flex align-items-start">
              <b-dropdown id="dropdown-dropup" variant="primary" class="ml-xs" size="sm" text="Uredi" right>
                <b-dropdown-item-btn @click.native="editResult(result)" v-b-modal.updateResult>
                    <i class="la la-refresh" />
                  Ažuriraj</b-dropdown-item-btn>
                <b-dropdown-divider />
                <b-dropdown-item @click="removeResult(result.id); addSuccessNotification3()">
                        <i class="la la-trash" />
                  Obriši</b-dropdown-item>
              </b-dropdown>
            </div>
          </div>
          </Widget>
        </div>
      </b-col>
    </b-row>
    <b-modal id="createResult" scrollable title="Dodaj rezultat" hide-footer ref="my-modal">
        <b-form @submit.prevent="createResult(); addSuccessNotification1(); hideModal()" class="w-100">
        <!--  -->
        <b-form-group label="Domaci">
          <b-form-input type="text" v-model="home" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Gosti">
          <b-form-input type="text" v-model="away">
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Datum">
          <b-form-input type="text" v-model="date">
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Domaci koševa">
          <b-form-input type="text" v-model="home_points">
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Gosti koševa">
          <b-form-input type="text" v-model="away_points">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="default">Dodaj rezultat</b-button>
        <b-button variant="default" style="float: right" @click="hideModal()">Odustani</b-button>
        </b-form>
      </b-modal>

      <b-modal id="updateResult" scrollable title="Izmjeni rezultat" hide-footer ref="my-modal">
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
        <b-form-group label="Datum">
          <b-form-input type="text" v-model="editForm.date" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Domaci koševa">
          <b-form-input type="text" v-model="editForm.home_points" required>
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Gosti koševa">
          <b-form-input type="text" v-model="editForm.away_points" required>
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

import { Chart } from 'highcharts-vue';

export default {
  name: 'Results',
  components: {
    Widget, highcharts: Chart
  },
  data() {
    return {
      results: [],
      home: '',
      away: '',
      date: '',
      home_points: '',
      away_points: '',
      editForm: {
        id: '',
        home: '',
        away: '',
        date: '',
        home_points: '',
        away_points: '',
      },
    };
  },
  methods: {
    addSuccessNotification1() {
      this.$toasted.success('Rezultat uspješno dodan!', {
      })
    },
    addSuccessNotification2() {
      this.$toasted.success('Rezultat uspješno ažuriran!', {
      })
    },
    addSuccessNotification3() {
      this.$toasted.success('Rezultat uspješno obrisan!', {
      })
    },
    getResults() {
      axios.get('http://localhost:8000/results').then((response) => {
        this.results = response.data;
      })
    },
    createResult() {
      axios.post('http://localhost:8000/result', {
        home: this.home,
        away: this.away,
        date: this.date,
        home_points: this.home_points,
        away_points: this.away_points,
      }).then((res) => {
        this.getResults();
        this.home= '',
        this.away= '',
        this.date= '',
        this.home_points= '',
        this.away_points= '',
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    removeResult(result_id) {
      const path = `http://localhost:8000/result/${result_id}`;
      axios.delete(path)
        .then(() => {
          this.getResults();   
        })
        .catch((error) => {
          console.error(error);
        });        
    },
    editResult(result_id) {
      this.editForm = result_id;
    },
    onSubmitUpdate() {
      const payload = {
        home: this.editForm.home,
        away: this.editForm.away,
        date: this.editForm.date,
        home_points: this.editForm.home_points,
        away_points: this.editForm.away_points,
      };
      this.updateResult(payload, this.editForm.id);
    },
    updateResult(payload, result_id) {
      const path = `http://localhost:8000/result/${result_id}`;
      axios.put(path, payload)
        .then(() => {
          this.getResults(); 
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
    this.getResults();
  },
};
</script>