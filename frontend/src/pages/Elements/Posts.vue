<template>
  <div class="posts-page">
    <h1 class="page-title">Novosti</h1>

      
        <b-button variant="primary" v-b-modal.createPost>Dodaj novost</b-button>
        <input type="text" class="asd" placeholder="Traži" v-model="search" style="float: right"> 
     
    <b-row><p></p></b-row> 
    <b-row>
      <b-col xs="12" lg="6" xl="12" v-for="post of filterNews" v-bind:key="post.id"> 
    <div class="mb-xlg">
    <Widget class="h-100" bodyClass="p-0 mt-0">
      <div class="d-flex justify-content-between flex-wrap px-4">
        <h4 class='d-flex align-items-center pb-1 bigStatTitle'>
            {{post.title}}
        </h4>
      </div>
      <div class="px-5">
        <p>{{post.content}}</p>
        <p><small>Datum objave: {{post.created_at | moment("from", "now", true)}}</small></p>
      
          <div class="w-600 py-3 pr-2">
            <div class="d-flex align-items-start">
              <b-dropdown id="dropdown-dropup" variant="primary" class="ml-xs" size="sm" text="Uredi" right>
                <b-dropdown-item-btn @click.native="editPost(post)" v-b-modal.updatePost>
                  <i class="la la-refresh" />
                  Ažuriraj</b-dropdown-item-btn>
                <b-dropdown-divider />
                <b-dropdown-item @click="removePost(post.id); addSuccessNotification3()">
                  <i class="la la-trash" />
                  Obriši
                  </b-dropdown-item>
              </b-dropdown>
                             &nbsp;&nbsp;&nbsp;
               <b-button v-b-toggle="post.id" @click="getComments(post.id)" variant="primary" class="ml-xs" size="sm">Komentar</b-button>
            </div>
          </div>
      </div>
               <b-collapse v-bind="post">
            <b-card border-variant="light">
              <form @submit.prevent="createComment(post.id)">
 
              <b-card id="a" v-for="commentr  of comments" v-bind:key="commentr.id" style="margin-bottom: 15px;">
                <p><small>{{commentr.ime}} {{commentr.prezime}}</small></p>
                {{commentr.comment}}
              </b-card>
                 
               <b-input-group prepend="Komentiraj" class="mt-3">
                <b-form-input required v-model="comment"></b-form-input>
                <b-input-group-append>
                  <b-button type="submit" variant="primary">Objavi</b-button>
                </b-input-group-append>
              </b-input-group>
              </form>
            </b-card>
          </b-collapse>
    </Widget>
    </div>
      </b-col>
    </b-row>
    <b-modal id="createPost" scrollable title="Dodaj obavijest" hide-footer ref="my-modal">
        <b-form @submit.prevent="createPost(); addSuccessNotification1(); hideModal()" class="w-100">
        <!--  -->
        <b-form-group label="Naslov">
          <b-form-input type="text" v-model="title" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Sadržaj">
          <b-form-textarea type="text" v-model="content" required rows="15">
          </b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="default">Dodaj novost</b-button>
        <b-button variant="default" style="float: right" @click="hideModal()">Odustani</b-button>
        </b-form>
      </b-modal>

      <b-modal id="updatePost" scrollable title="Izmjeni projekt" hide-footer ref="my-modal">
        <b-form @submit.prevent="onSubmitUpdate()" class="w-100">
        <!--  -->
        <b-form-group label="Naslov">
          <b-form-input type="text" v-model="editForm.title" required >
          </b-form-input>
        </b-form-group>
        <!--  -->
        <b-form-group label="Sadržaj">
          <b-form-textarea type="text" v-model="editForm.content" required rows="15">
          </b-form-textarea>
        </b-form-group>

        <b-button type="submit" variant="primary" @click="hideModal(); addSuccessNotification2()">Ažuriraj</b-button>
        </b-form>
      </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import Widget from '@/components/Widget/Widget';
import moment from 'moment';
import jwtDecode from 'jwt-decode';

export default {
  name: 'Posts',
  components: {
    Widget
  },
  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return {
      fname: decoded.identity.fname,
      lname: decoded.identity.lname, 
      posts: [],
      comments: [],
      comment: '',
      search: '',
      title: '',
      content: '',
      editForm: {
        id: '',
        title: '',
        content: '',
      },
    };
  },
  methods: {
    addSuccessNotification1() {
      this.$toasted.success('Novost uspješno dodana!', {
      })
    },
    addSuccessNotification2() {
      this.$toasted.success('Novost uspješno ažurirana!', {
      })
    },
    addSuccessNotification3() {
      this.$toasted.success('Novost uspješno obrisana!', {
      })
    },
    getPosts() {
      axios.get('http://localhost:8000/posts').then((response) => {
        this.posts = response.data;
      })
    },
    getComments(post_id) {
      axios.get(`http://localhost:8000/comments/${post_id}`).then((response) => {
        this.comments = response.data;
      })
    },
    createComment(id_post) {
      axios.post('http://localhost:8000/comment', {
        id_post: id_post,
        ime: this.fname,
        prezime: this.lname,
        comment: this.comment,
      }).then((res) => {
        this.getComments(id_post);
        this.comment = '',
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    createPost() {
      axios.post('http://localhost:8000/post', {
        title: this.title,
        content: this.content,
        created_at: new Date(),
      }).then((res) => {
        this.getPosts();
        this.title = '',
        this.content = '',
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    removePost(post_id) {
      const path = `http://localhost:8000/post/${post_id}`;
      axios.delete(path)
        .then(() => {
          this.getPosts();  
        })
        .catch((error) => {
          console.error(error);
        });         
    },
    editPost(post_id) {
      this.editForm = post_id;
    },
    onSubmitUpdate() {
      const payload = {
        title: this.editForm.title,
        content: this.editForm.content,
        created_at: new Date(),
      };
      this.updatePost(payload, this.editForm.id);
    },
    updatePost(payload, post_id) {
      const path = `http://localhost:8000/post/${post_id}`;
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
  computed: {
      filterNews(){
        return this.posts.filter((post) => {
          return post.title.toLowerCase().match(this.search.toLowerCase());
        });
      },
  },
  created() {
    this.getPosts();
  },
};
</script>
<style>
.asd{
  width: 210px;
  height: 30px;
  padding: 0px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  box-shadow: 3px 3px 3px 3px #ccc;
}
</style>
