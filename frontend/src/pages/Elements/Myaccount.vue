<template>
  <div class="dashboard-page">
    <h1 class="page-title">Moj račun</h1>
  <div><p></p></div>
    <div>
      <Widget title="Podaci">
          <b-row>
            <b-col></b-col>
            <b-col>
              <b-img class="avatar2" center src="https://cdn0.iconfinder.com/data/icons/social-media-network-4/48/male_avatar-512.png"></b-img>
              <b-form class="w-100">
                <div class="form-group">
                  <label>Ime:</label>
                  <h2>{{fname}}</h2>
                </div>
                <div class="form-group">
                  <label>Prezime:</label>
                  <h2>{{lname}}</h2>
                </div>
                <div class="form-group">
                  <label>Email:</label>
                  <h2>{{email}}</h2>
                </div>
              </b-form>
            </b-col>
            <b-col></b-col>
          </b-row>
      </Widget>
    </div>
        </div>
</template>

<script>
/* eslint-disable */
import Widget from '@/components/Widget/Widget';
import jwtDecode from 'jwt-decode';
import EventBus from '@/pages/Elements/EventBus';

EventBus.$on('logged-in', test => {
  console.log(test)
})


export default {
  name: 'Zapisnik',
  components: {
    Widget,
  },
  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return {
      id: decoded.identity.id,
      fname: decoded.identity.fname,
      lname: decoded.identity.lname,  
      email: decoded.identity.email,
    };
  },
  methods: {
  },
};
</script>

<style lang="scss">
.zapisnik-team-1 {
   height: 1200px;
}
.zapisnik-team-2 {
   height: 1200px;
}
.zapisnikpdf {
   height: 700px;
   width: 600px;
}
.dsad {
   margin-bottom: 30px;
}
.foulsAndTimeouts {
   margin-bottom: 30px;
}
.form-control {
    width: 303px;
}

.avatar2 {
   margin-top: 4px;
   margin-bottom: 7px;
   width: 150px;
   height: 150px;
}
</style>
