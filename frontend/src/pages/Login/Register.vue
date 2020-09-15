<template>
  <div class="auth-page">
    <b-container>
      <b-card
      header="Registracija"
      header-tag="header"
      title="E-zapisnik"
    >
      <Widget class="widget-auth mx-auto" title="<h3 class='mt-0'>Dobrodošli</h3>" customHeader>
        <p class="widget-auth-info">
            Registriraj se
        </p>
        <form v-on:submit.prevent="register">
          <div class="form-group">
            <label>Ime</label>
            <input class="form-control no-border" required type="text" v-model="fname" />
          </div>

          <div class="form-group">
            <label>Prezime</label>
            <input class="form-control no-border" required type="text"  v-model="lname" />
          </div>

          <div class="form-group">
            <label>E-mail</label>
            <input class="form-control no-border" required type="email" v-model="email" />
          </div>

          <div class="form-group" >
            <label>Lozinka</label>
            <input class="form-control no-border" type="password" required v-model="password"  /> 
          </div>

          <div class="form-group">
            <b-button type="submit" size="sm" class="auth-btn mb-3" variant="inverse">Registriraj se</b-button>
          </div> 

        </form>
        <p class="widget-auth-info">
          Imaš korisnički račun?
        </p>
        <router-link class="d-block text-center" to="login">Prijavi se</router-link>
      </Widget>
       </b-card>
    </b-container>
  </div>
</template>

<script>
/* eslint-disable */
import Widget from '@/components/Widget/Widget';
import axios from 'axios';

export default {
  name: 'Register',
  components: { Widget },
  data() {
    return {     
        fname: '',
        lname: '',
        email: '',
        password: '',
    }
  },
  methods: {
    register() {
      axios.post('http://localhost:8000/user/register', {
        fname: this.fname,
        lname: this.lname,
        email: this.email,
        password: this.password,
        is_admin: false,
      }).then((res) => {
        this.$router.push({ name: 'Login' });
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
  },
};
</script>
