<template>
  <div class="auth-page"> 
    <b-container>
      <b-card
      header="Prijava"
      header-tag="header"
      title="E-zapisnik"
    >
      <Widget class="widget-auth mx-auto" title="<h3 class='mt-0'>Dobrodošli</h3>" customHeader >
        <p class="widget-auth-info">
            Prijavi se kao korisnik
        </p>
        <div class="widget-auth-info">
          <b-img class="avatar3" src="https://image.flaticon.com/icons/svg/174/174848.svg"></b-img>
          <b-img class="avatar3" src="https://image.flaticon.com/icons/svg/2111/2111463.svg" ></b-img>
          <b-img class="avatar3" src="https://image.flaticon.com/icons/svg/174/174857.svg"></b-img>
        </div>
        <form class="mt" @submit.prevent="login">
          <b-alert class="alert-sm" variant="warning" :show="!!errorMessage">
            {{errorMessage}}
          </b-alert>
          <div class="form-group">
            <label>E-mail</label>
            <input class="form-control no-border" ref="email" type="email" name="email" v-model="email" />
          </div>
          <div class="form-group">
            <label>Lozinka</label>
            <input class="form-control no-border" ref="password" type="password" name="password" v-model="password" />
          </div>
          <b-button type="submit" size="sm" class="auth-btn mb-3" variant="inverse">Prijavi se</b-button>
        </form>
        <p class="widget-auth-info">
          Nemaš korisnički račun? Registriraj se!
        </p>
        <router-link class="d-block text-center" to="register">Napravi račun</router-link>
      </Widget>
      </b-card>
    </b-container>
  </div>
</template>

<script>
/* eslint-disable */
import Widget from '@/components/Widget/Widget';
import EventBus from '@/pages/Elements/EventBus';
import axios from 'axios';

export default {
  name: 'LoginPage',
  components: { Widget },
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    login() {
      axios.post('http://localhost:8000/user/login', {
        email: this.email,
        password: this.password,
      }).then((res) => {
        if(res.status === 200){
        localStorage.setItem('usertoken', res.data);
        this.email = '';
        this.password = '';
        this.$router.push({ name: 'Posts' });
        }
      }).catch((err) => {
        this.errorMessage = 'Unesena e-pošta ili lozinka ne odgovaraju nijednom računu.';
        console.log(err);
      });
      this.emitMethod();
    },
    emitMethod() {
      EventBus.$emit('logged-in', 'loggedin');
    },
  },
 
};
</script>
<style>
.avatar3 {
   margin-top: 14px;
   margin-bottom: 7px;
   margin-right: 17px;
   margin-left: 14px;
   width: 35px;
   height: 35px;
   align-items: center;
}
</style>
