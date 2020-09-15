<template>
    <div :class="{ 'theme-helper': true, 'theme-helper-opened': opened }">
        <div class="theme-helper-toggler" @click="toggle">
            <div class="theme-helper-spinner bg-primary text-white">
                <i class="la la-envelope"></i>
                <i class="la la-envelope"></i>
            </div>
        </div>
      <section class="widget theme-helper-content">
            <div class="widget-body mt-3">
              <h6>Trebate pomoć? Kontaktirajte nas.</h6>
              <form class="contact-form" @submit.prevent="sendEmail">
                <div class="mt-4">
                    <div class="form-group">
                        <input class="form-control no-border" required type="text"  placeholder="Ime i prezime" name="user_name" />
                    </div>
                </div>  
                <div class="mt-4">
                    <div class="form-group">
                        <input class="form-control no-border" required type="email" placeholder="Email" name="email" />
                    </div>
                </div>
                <div class="mt-4">
                    <div class="form-group">
                        <input class="form-control no-border" required type="text" placeholder="Naslov" name="naslov" />
                    </div>
                </div>
                <div class="mt-4">
                    <div class="form-group">
                        <textarea rows=5 class="form-control no-border" required type="text"  placeholder="Upit" name="poruka" />
                    </div>
                </div>
                <div class="mt-4">
                 <div class="form-group">
                 <b-button type="submit" size="sm" class="auth-btn mb-3" variant="primary" @click="tyers()">Pošalji upit</b-button>
                 </div>
                </div>
                </form>
            </div>
        </section>
    </div>
</template>

<script>
/* eslint-disable */
import emailjs from 'emailjs-com';

export default {
    name: 'Helper',
    data() {
        return {
            opened: false,
        }
    },
    methods: {
        toggle() {
            this.opened = !this.opened;
        },
        sendEmail: (e) => {
      emailjs.sendForm('gmail', 'template_O5XT80GQ', e.target, 'user_DIMbGS19CbTQT4YosMAWO')
        .then((result) => {
            console.log('SUCCESS!', result.status, result.text);
        }, (error) => {
            console.log('FAILED...', error);
        });
    },
    tyers(){
        this.opened = !this.opened;
    },
    }
};
</script>

<style src="./Helper.scss" lang="scss"></style>
