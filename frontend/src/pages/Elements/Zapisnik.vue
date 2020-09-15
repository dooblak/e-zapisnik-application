<template>
  <div class="dashboard-page">
    <h1 class="page-title">Službeni zapisnik</h1>
    
  <div><p></p></div>
    <div v-if="tryer2==''">
      <Widget title="Unesite podatke">
          <b-row>
            <b-col></b-col>
            <b-col>
              <b-form @submit.prevent="createUtakmica(); getAwayTeam(); getHomeTeam(); getAwayTeamName(); getHomeTeamName();" class="w-100" >
                <div class="form-group">
                  <label>Timovi:</label>
                  <b-input-group>
                    <b-select v-model="id_home" required class="form-control no-border" > 
                      <option v-for="team of teams" v-bind:key="team.id" v-bind:value="team.id" >
                      {{ team.name }}
                      </option>
                    </b-select>
                    &nbsp;&nbsp;
                    <b-select v-model="id_away" required class="form-control no-border" > 
                      <option v-for="team of teams" v-bind:key="team.id" v-bind:value="team.id" >
                      {{ team.name }}
                      </option>
                    </b-select>
                  </b-input-group>
                </div>
                <div class="form-group">
                  <label>Natjecanje:</label>
                  <input class="form-control no-border" required v-model="natjecanje" />
                </div>
                <div class="form-group">
                  <label>Datum:</label>
                  <input class="form-control no-border" required v-model="date" />
                </div>
                <div class="form-group">
                  <label>Mjesto:</label>
                  <input class="form-control no-border" required v-model="mjesto" />
                </div>
                <div class="form-group">
                  <label>Prvi sudac:</label>
                  <input class="form-control no-border" required v-model="prvi_sudac" />
                </div>
                <div class="form-group">
                  <label>Sudac:</label>
                  <input class="form-control no-border" required v-model="drugi_sudac" />
                </div>
                <div class="form-group">
                  <label>Sudac:</label>
                  <input class="form-control no-border" required v-model="treci_sudac" />
                </div>
                <div class="form-group">
                  <label>Zapisničar:</label>
                  <input class="form-control no-border" required v-model="zapisnicar" />
                </div>
                <b-button  type="submit" size="sm" class="auth-btn mb-3" variant="inverse">Potvrdi</b-button>
              </b-form>
            </b-col>
            <b-col></b-col>
          </b-row>
      </Widget>
    </div>

    <div v-if="tryer==''">
    <b-row lg="3" sm="6" xs="12">
      <b-col lg="12" sm="6" xs="12">
    <Widget class="h-100 mb-0" close>
              <h3>Natjecanje: {{natjecanje}}</h3>
              <h5>Datum: {{date}}</h5>
              <h5>Mjesto: {{mjesto}}</h5>
              <p></p>
              <h6>Prvi sudac: {{prvi_sudac}}</h6>
              <h6>Sudac: {{drugi_sudac}}</h6>
              <h6>Sudac: {{treci_sudac}}</h6>
            <div class="d-flex flex-wrap justify-content-between">
              <div class="mt">
                <b-button pill variant="light" v-b-popover.hover.right="'Koristite jedan klik na gumb za dodavanje vrijednosti, dva klika na gumb za smanjivanje vrijednosti.'" title="Korisne upute">
                  Upute
                </b-button>
              </div>
              <div>
                <h1>{{team1Player1.points + team1Player2.points + team1Player3.points + team1Player4.points + team1Player5.points + team1Player6.points + team1Player7.points + team1Player8.points + team1Player9.points + team1Player10.points + team1Player11.points + team1Player12.points}}:{{team2Player1.points + team2Player2.points + team2Player3.points + team2Player4.points + team2Player5.points + team2Player6.points + team2Player7.points + team2Player8.points + team2Player9.points + team2Player10.points + team2Player11.points + team2Player12.points}}</h1>
              </div>
              <div class="mt">
              </div>
            </div>
          </Widget>
        </b-col>
      </b-row>
    <b-row><p></p></b-row> 



    <b-row lg="3" sm="6" xs="12">
      <b-col lg="6" sm="6" xs="12">
        <div class="zapisnik-team-1">
          <Widget class="h-100 mb-0" close>
            <p></p>
             <div style="margin-bottom:10px;" class="d-flex flex-wrap justify-content-between">
              <div class="mt">
              </div>
              <div>
                <h2>Domaci - {{ homeName }}</h2>
              </div>
              <div class="mt">
              </div>
            </div>

            <div class="foulsAndTimeouts">
              <b-row>
                <b-col>
                  <h6>Minute odmora:</h6>
                  <span> 1. Pol&nbsp;&nbsp; </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="primary" @click="minuteOdmoraPrvoPolMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="primary">{{minuteOdmoraPrvoPol}}</b-button> &nbsp;
                  <b-button size="sm" variant="primary" @click="minuteOdmoraPrvoPolPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  &nbsp;
                </b-col>
                <b-col>                  
                  <h6>Ekipne pogreške (1,2,3,4 razodbolje):</h6>
                  <span> 1)&nbsp; </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="primary" @click="ekipnePogreskePrvaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="primary">{{ekipnePogreskePrvaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="primary" @click="ekipnePogreskePrvaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  &nbsp;
                  <span> 2) </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="primary" @click="ekipnePogreskeDrugaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="primary">{{ekipnePogreskeDrugaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="primary" @click="ekipnePogreskeDrugaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                   <b-row><p></p></b-row> 
                  </b-col>
              </b-row>
              <b-row>
                <b-col>
                  <span> 2. Pol&nbsp; </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="primary" @click="minuteOdmoraDrugoPolMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="primary">{{minuteOdmoraDrugoPol}}</b-button> &nbsp;
                  <b-button size="sm" variant="primary" @click="minuteOdmoraDrugoPolPlus()">+</b-button> &nbsp;
                  </b-button-group>
                </b-col>
                <b-col>
                  <span> 3) </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="primary" @click="ekipnePogreskeTrecaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="primary">{{ekipnePogreskeTrecaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="primary" @click="ekipnePogreskeTrecaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  &nbsp;
                  <span> 4) </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="primary" @click="ekipnePogreskeCetvrtaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="primary">{{ekipnePogreskeCetvrtaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="primary" @click="ekipnePogreskeCetvrtaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  </b-col>
              </b-row>
            </div>

          
          <b-row>
              <b-col cols="4">
              <b-list-group>
                <b-list-group-item v-for="player of players" v-bind:key="player.id">
                  <h4># {{player.number_player}}</h4>
                  <div>{{player.fname}} {{player.lname}}</div>
                </b-list-group-item>
              </b-list-group>
              </b-col>


              <b-col>
                <b-row class="rowIgrac1">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player1Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player1PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player1TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player1Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player1Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player1Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player1Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player1Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player1.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player1.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player1.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player1.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player1.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player1.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player1.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player1.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac2">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player2Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player2PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player2TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player2Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player2Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player2Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player2Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player2Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player2.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player2.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player2.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player2.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player2.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player2.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player2.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player2.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac3">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player3Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player3PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player3TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player3Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player3Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player3Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player3Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player3Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player3.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player3.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player3.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player3.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player3.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player3.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player3.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player3.to}}</small></p>
                </b-row>

                <b-row class="rowIgrac4">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player4Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player4PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player4TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player4Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player4Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player4Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player4Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player4Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player4.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player4.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player4.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player4.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player4.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player4.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player4.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player4.to}}</small></p>
                </b-row>


                  <b-row class="rowIgrac5">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player5Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player5PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player5TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player5Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player5Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player5Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player5Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player5Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player5.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player5.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player5.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player5.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player5.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player5.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player5.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player5.to}}</small></p>
                </b-row>

                <b-row class="rowIgrac6">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player6Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player6PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player6TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player6Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player6Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player6Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player6Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player6Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player6.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player6.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player6.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player6.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player6.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player6.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player6.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player6.to}}</small></p>
                </b-row>


                
                <b-row class="rowIgrac7">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player7Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player7PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player7TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player7Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player7Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player7Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player7Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player7Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player7.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player7.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player7.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player7.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player7.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player7.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player7.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player7.to}}</small></p>
                </b-row>


                
                
                <b-row class="rowIgrac8">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player8Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player8PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player8TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player8Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player8Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player8Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player8Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player8Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player8.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player8.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player8.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player8.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player8.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player8.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player8.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player8.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac9">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player9Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player9PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player9TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player9Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player9Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player9Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player9Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player9Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player9.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player9.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player9.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player9.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player9.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player9.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player9.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player9.to}}</small></p>
                </b-row>

                

                <b-row class="rowIgrac10">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player10Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player10PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player10TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player10Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player10Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player10Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player10Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player10Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player10.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player10.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player10.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player10.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player10.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player10.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player10.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player10.to}}</small></p>
                </b-row>
                
                 <b-row class="rowIgrac11">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player11Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player11PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player11TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player11Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player11Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player11Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player11Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player11Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player11.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player11.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player11.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player11.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player11.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player11.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player11.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player11.to}}</small></p>
                </b-row>


                         
                 <b-row class="rowIgrac12">
                <b-button-group size="sm">
                <b-button size="sm" variant="primary" v-click-helper="team1Player12Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player12PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player12TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player12Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player12Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player12Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player12Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="primary" v-click-helper="team1Player12Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team1Player12.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team1Player12.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team1Player12.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team1Player12.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team1Player12.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team1Player12.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team1Player12.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team1Player12.to}}</small></p>
                </b-row>








              </b-col>


          </b-row>

          </Widget>
        </div>
      </b-col>




      <b-col lg="6" sm="6" xs="12">
            <div class="zapisnik-team-2">
          <Widget class="h-100 mb-0" close>
            <p></p>
             <div style="margin-bottom:10px;" class="d-flex flex-wrap justify-content-between">
              <div class="mt">
              </div>
              <div>
                <h2>Gosti - {{ awayName }}</h2>
              </div>
              <div class="mt">
              </div>
            </div>

             <div class="foulsAndTimeouts">
              <b-row>
                <b-col>
                  <h6>Minute odmora:</h6>
                  <span> 1. Pol&nbsp;&nbsp; </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="success" @click="team2minuteOdmoraPrvoPolMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="success">{{team2minuteOdmoraPrvoPol}}</b-button> &nbsp;
                  <b-button size="sm" variant="success" @click="team2minuteOdmoraPrvoPolPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  &nbsp;
                </b-col>
                <b-col>                  
                  <h6>Ekipne pogreške (1,2,3,4 razodbolje):</h6>
                  <span> 1)&nbsp; </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskePrvaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="success">{{team2ekipnePogreskePrvaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskePrvaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  &nbsp;
                  <span> 2) </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskeDrugaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="success">{{team2ekipnePogreskeDrugaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskeDrugaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                   <b-row><p></p></b-row> 
                  </b-col>
              </b-row>
              <b-row>
                <b-col>
                  <span> 2. Pol&nbsp; </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="success" @click="team2minuteOdmoraDrugoPolMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="success">{{team2minuteOdmoraDrugoPol}}</b-button> &nbsp;
                  <b-button size="sm" variant="success" @click="team2minuteOdmoraDrugoPolPlus()">+</b-button> &nbsp;
                  </b-button-group>
                </b-col>
                <b-col>
                  <span> 3) </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskeTrecaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="success">{{team2ekipnePogreskeTrecaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskeTrecaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  &nbsp;
                  <span> 4) </span>
                  <b-button-group size="sm">
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskeCetvrtaCetMinus()">-</b-button> &nbsp;
                  <b-button disabled size="sm" variant="success">{{team2ekipnePogreskeCetvrtaCet}}</b-button> &nbsp;
                  <b-button size="sm" variant="success" @click="team2ekipnePogreskeCetvrtaCetPlus()">+</b-button> &nbsp;
                  </b-button-group>
                  </b-col>
              </b-row>
            </div>



          <b-row>
              <b-col cols="4">
              <b-list-group>
                <b-list-group-item v-for="player2 of players2" v-bind:key="player2.id">
                  <h4># {{player2.number_player}}</h4>
                  <div>{{player2.fname}} {{player2.lname}}</div>
                </b-list-group-item>
              </b-list-group>
              </b-col>

              <b-col>
                <b-row class="rowIgrac1">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player1Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player1PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player1TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player1Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player1Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player1Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player1Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player1Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player1.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player1.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player1.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player1.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player1.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player1.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player1.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player1.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac2">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player2Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player2PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player2TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player2Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player2Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player2Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player2Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player2Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player2.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player2.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player2.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player2.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player2.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player2.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player2.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player2.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac3">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player3Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player3PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player3TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player3Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player3Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player3Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player3Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player3Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player3.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player3.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player3.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player3.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player3.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player3.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player3.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player3.to}}</small></p>
                </b-row>

                
                <b-row class="rowIgrac4">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player4Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player4PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player4TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player4Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player4Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player4Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player4Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player4Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player4.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player4.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player4.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player4.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player4.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player4.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player4.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player4.to}}</small></p>
                </b-row>


                
                <b-row class="rowIgrac5">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player5Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player5PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player5TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player5Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player5Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player5Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player5Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player5Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player5.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player5.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player5.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player5.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player5.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player5.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player5.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player5.to}}</small></p>
                </b-row>

                <b-row class="rowIgrac6">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player6Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player6PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player6TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player6Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player6Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player6Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player6Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player6Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player6.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player6.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player6.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player6.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player6.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player6.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player6.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player6.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac7">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player7Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player7PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player7TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player7Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player7Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player7Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player7Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player7Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player7.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player7.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player7.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player7.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player7.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player7.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player7.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player7.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac8">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player8Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player8PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player8TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player8Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player8Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player8Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player8Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player8Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player8.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player8.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player8.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player8.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player8.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player8.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player8.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player8.to}}</small></p>
                </b-row>

                <b-row class="rowIgrac9">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player9Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player9PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player9TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player9Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player9Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player9Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player9Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player9Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player9.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player9.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF:{{ team2Player9.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player9.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player9.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player9.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player9.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player9.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac10">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player10Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player10PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player10TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player10Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player10Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player10Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player10Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player10Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player10.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player10.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF: {{ team2Player10.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player10.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player10.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player10.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player10.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player10.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac11">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player11Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player11PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player11TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player11Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player11Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player11Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player11Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player11Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player11.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player11.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF: {{ team2Player11.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player11.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player11.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player11.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player11.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player11.to}}</small></p>
                </b-row>


                <b-row class="rowIgrac12">
                <b-button-group size="sm">
                <b-button size="sm" variant="success" v-click-helper="team2Player12Points">1 PT</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player12PersonalFouls">PF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player12TehnicalFouls">TF</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player12Rebounds">REB</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player12Assists">AST</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player12Steals">STL</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player12Blocks">BLK</b-button> &nbsp;
                <b-button size="sm" variant="success" v-click-helper="team2Player12Turnovers">TO</b-button> &nbsp;
                </b-button-group>
                </b-row>
                <b-row class="statistika1">
                  <p class="mb-0 mr"><small>Pts: {{team2Player12.points}} </small></p>
                  <p class="mb-0 mr"><small>PF: {{team2Player12.pf}} </small></p>
                  <p class="mb-0 mr"><small>TF: {{ team2Player12.tf}} </small></p>
                  <p class="mb-0 mr"><small>Reb: {{ team2Player12.reb}} </small></p>
                  <p class="mb-0 mr"><small>Ast: {{ team2Player12.ast}} </small></p>
                  <p class="mb-0 mr"><small>Stl: {{ team2Player12.stl}} </small></p>
                  <p class="mb-0 mr"><small>Blk: {{ team2Player12.blk}} </small></p>
                  <p class="mb-0 mr"><small>TO: {{ team2Player12.to}}</small></p>
                </b-row>

        </b-col>
          </b-row>
          </Widget>
        </div>
      </b-col>
    </b-row>
    
    <div><p></p></div>
    <div class="float-right">
        <b-button variant="dark" class="mr-xs" size="md" @click="generatePDF(); createResult()">Završi utakmicu</b-button>
    </div>
    </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import jspdf from 'jspdf';
import autoTable from 'jspdf-autotable';
import Widget from '@/components/Widget/Widget';
import vueClickHelper from 'vue-click-helper';
import moment from 'moment';

export default {
  name: 'Zapisnik',
  components: {
    Widget,
  },
  data() {
    return {
      show: false,
      teams: [],
      players: [],
      players2: [],
      //--
      tryer: 's',
      tryer2: '',
      homeName: '',
      awayName: '',
      //--
      team1Player1:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player2:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player3:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player4:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player5:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player6:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },  
      team1Player7:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player8:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player9:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player10:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player11:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team1Player12:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
  
  //--

      team2Player1:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player2:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player3:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player4:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player5:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player6:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player7:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player8:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player9:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player10:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player11:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      team2Player12:{
        points: 0,
        pf: 0,
        tf: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        to: 0,
        },
      //--
      home_name: '',
      away_name: '',
      id_home: '',
      id_away: '',
      name_home: '',
      name_away: '',
      natjecanje: '',
      date: '',
      mjesto: '',
      prvi_sudac: '',
      drugi_sudac: '',
      treci_sudac: '',
      zapisnicar: '',
      //--
      minuteOdmoraPrvoPol: 2,
      minuteOdmoraDrugoPol: 2,
      team2minuteOdmoraPrvoPol: 2,
      team2minuteOdmoraDrugoPol: 2,
      //--
      ekipnePogreskePrvaCet: 4,
      ekipnePogreskeDrugaCet: 4,
      ekipnePogreskeTrecaCet: 4,
      ekipnePogreskeCetvrtaCet: 4,
      team2ekipnePogreskePrvaCet: 4,
      team2ekipnePogreskeDrugaCet: 4,
      team2ekipnePogreskeTrecaCet: 4,
      team2ekipnePogreskeCetvrtaCet: 4,
      //--
    };
  },
  directives: {
        'click-helper': vueClickHelper
    },
  methods: {
    generatePDF(){
      //this.tryer = 's';
      this.$router.push('Posts'); 
      let columns = [
        {title: "Broj", dataKey: "number_player"},
        {title: "Prezime", dataKey: "lname"},
        {title: "Ime", dataKey: "fname"},
        {title: "Poeni", dataKey: "team1Player2.points"},
      ];
      let doc = new jspdf();
      doc.autoTable({})
      doc.autoTable({})
      doc.text('Natjecanje: ' + this.natjecanje, 10, 20);
      doc.text('Datum: ' + this.date, 110, 20);
      doc.text('Mjesto: ' + this.mjesto, 170, 20);
      doc.text('Ekipa A: ' + this.homeName, 15, 35);
      doc.autoTable({})
      doc.autoTable({})
      doc.autoTable({
        columnStyles: {}, 
        body: [
          { broj: this.players[0].number_player, prezime: this.players[0].lname, ime: this.players[0].fname, poeni: this.team1Player1.points, oPrekrsaji: this.team1Player1.pf, tPrekrsaji: this.team1Player1.tf, skokovi: this.team1Player1.reb, asistencije: this.team1Player1.ast, uLopte: this.team1Player1.stl, blokade: this.team1Player1.blk, preokreti: this.team1Player1.to },
          { broj: this.players[1].number_player, prezime: this.players[1].lname, ime: this.players[1].fname, poeni: this.team1Player2.points, oPrekrsaji: this.team1Player2.pf, tPrekrsaji: this.team1Player2.tf, skokovi: this.team1Player2.reb, asistencije: this.team1Player2.ast, uLopte: this.team1Player2.stl, blokade: this.team1Player2.blk, preokreti: this.team1Player2.to },
          { broj: this.players[2].number_player, prezime: this.players[2].lname, ime: this.players[2].fname, poeni: this.team1Player3.points, oPrekrsaji: this.team1Player3.pf, tPrekrsaji: this.team1Player3.tf, skokovi: this.team1Player3.reb, asistencije: this.team1Player3.ast, uLopte: this.team1Player3.stl, blokade: this.team1Player3.blk, preokreti: this.team1Player3.to },
          { broj: this.players[3].number_player, prezime: this.players[3].lname, ime: this.players[3].fname, poeni: this.team1Player4.points, oPrekrsaji: this.team1Player4.pf, tPrekrsaji: this.team1Player4.tf, skokovi: this.team1Player4.reb, asistencije: this.team1Player4.ast, uLopte: this.team1Player4.stl, blokade: this.team1Player4.blk, preokreti: this.team1Player4.to },
          { broj: this.players[4].number_player, prezime: this.players[4].lname, ime: this.players[4].fname, poeni: this.team1Player5.points, oPrekrsaji: this.team1Player5.pf, tPrekrsaji: this.team1Player5.tf, skokovi: this.team1Player5.reb, asistencije: this.team1Player5.ast, uLopte: this.team1Player5.stl, blokade: this.team1Player5.blk, preokreti: this.team1Player5.to },
          { broj: this.players[5].number_player, prezime: this.players[5].lname, ime: this.players[5].fname, poeni: this.team1Player6.points, oPrekrsaji: this.team1Player6.pf, tPrekrsaji: this.team1Player6.tf, skokovi: this.team1Player6.reb, asistencije: this.team1Player6.ast, uLopte: this.team1Player6.stl, blokade: this.team1Player6.blk, preokreti: this.team1Player6.to },
          { broj: this.players[6].number_player, prezime: this.players[6].lname, ime: this.players[6].fname, poeni: this.team1Player7.points, oPrekrsaji: this.team1Player7.pf, tPrekrsaji: this.team1Player7.tf, skokovi: this.team1Player7.reb, asistencije: this.team1Player7.ast, uLopte: this.team1Player7.stl, blokade: this.team1Player7.blk, preokreti: this.team1Player7.to },
          { broj: this.players[7].number_player, prezime: this.players[7].lname, ime: this.players[7].fname, poeni: this.team1Player8.points, oPrekrsaji: this.team1Player8.pf, tPrekrsaji: this.team1Player8.tf, skokovi: this.team1Player8.reb, asistencije: this.team1Player8.ast, uLopte: this.team1Player8.stl, blokade: this.team1Player8.blk, preokreti: this.team1Player8.to },
          { broj: this.players[8].number_player, prezime: this.players[8].lname, ime: this.players[8].fname, poeni: this.team1Player9.points, oPrekrsaji: this.team1Player9.pf, tPrekrsaji: this.team1Player9.tf, skokovi: this.team1Player9.reb, asistencije: this.team1Player9.ast, uLopte: this.team1Player9.stl, blokade: this.team1Player9.blk, preokreti: this.team1Player9.to },
          { broj: this.players[9].number_player, prezime: this.players[9].lname, ime: this.players[9].fname, poeni: this.team1Player10.points, oPrekrsaji: this.team1Player10.pf, tPrekrsaji: this.team1Player10.tf, skokovi: this.team1Player10.reb, asistencije: this.team1Player10.ast, uLopte: this.team1Player10.stl, blokade: this.team1Player10.blk, preokreti: this.team1Player10.to },
          { broj: this.players[10].number_player, prezime: this.players[10].lname, ime: this.players[10].fname, poeni: this.team1Player11.points, oPrekrsaji: this.team1Player11.pf, tPrekrsaji: this.team1Player11.tf, skokovi: this.team1Player11.reb, asistencije: this.team1Player11.ast, uLopte: this.team1Player11.stl, blokade: this.team1Player11.blk, preokreti: this.team1Player11.to },
          { broj: this.players[11].number_player, prezime: this.players[11].lname, ime: this.players[11].fname, poeni: this.team1Player12.points, oPrekrsaji: this.team1Player12.pf, tPrekrsaji: this.team1Player12.tf, skokovi: this.team1Player12.reb, asistencije: this.team1Player12.ast, uLopte: this.team1Player12.stl, blokade: this.team1Player12.blk, preokreti: this.team1Player12.to },
        ],
        columns: [
          { header: 'Broj', dataKey: 'broj' },
          { header: 'Prezime', dataKey: 'prezime' },
          { header: 'Ime', dataKey: 'ime' },
          { header: 'Poeni', dataKey: 'poeni' },
          { header: 'O.P.', dataKey: 'oPrekrsaji' },
          { header: 'T.P.', dataKey: 'tPrekrsaji' },
          { header: 'Skok.', dataKey: 'skokovi' },
          { header: 'Asist.', dataKey: 'asistencije' },
          { header: 'U.lopte', dataKey: 'uLopte' },
          { header: 'Blok.', dataKey: 'blokade' },
          { header: 'Preok.', dataKey: 'preokreti' },

        ],
        theme:'grid',
      })
      doc.autoTable({})
      doc.text('Ekipa B: ' + this.awayName, 15, 150);
      doc.autoTable({
        columnStyles: {}, 
        body: [
          { broj: this.players2[0].number_player, prezime: this.players2[0].lname, ime: this.players2[0].fname, poeni: this.team2Player1.points, oPrekrsaji: this.team2Player1.pf, tPrekrsaji: this.team2Player1.tf, skokovi: this.team2Player1.reb, asistencije: this.team2Player1.ast, uLopte: this.team2Player1.stl, blokade: this.team2Player1.blk, preokreti: this.team2Player1.to },
          { broj: this.players2[1].number_player, prezime: this.players2[1].lname, ime: this.players2[1].fname, poeni: this.team2Player2.points, oPrekrsaji: this.team2Player2.pf, tPrekrsaji: this.team2Player2.tf, skokovi: this.team2Player2.reb, asistencije: this.team2Player2.ast, uLopte: this.team2Player2.stl, blokade: this.team2Player2.blk, preokreti: this.team2Player2.to },
          { broj: this.players2[2].number_player, prezime: this.players2[2].lname, ime: this.players2[2].fname, poeni: this.team2Player3.points, oPrekrsaji: this.team2Player3.pf, tPrekrsaji: this.team2Player3.tf, skokovi: this.team2Player3.reb, asistencije: this.team2Player3.ast, uLopte: this.team2Player3.stl, blokade: this.team2Player3.blk, preokreti: this.team2Player3.to },
          { broj: this.players2[3].number_player, prezime: this.players2[3].lname, ime: this.players2[3].fname, poeni: this.team2Player4.points, oPrekrsaji: this.team2Player4.pf, tPrekrsaji: this.team2Player4.tf, skokovi: this.team2Player4.reb, asistencije: this.team2Player4.ast, uLopte: this.team2Player4.stl, blokade: this.team2Player4.blk, preokreti: this.team2Player4.to },
          { broj: this.players2[4].number_player, prezime: this.players2[4].lname, ime: this.players2[4].fname, poeni: this.team2Player5.points, oPrekrsaji: this.team2Player5.pf, tPrekrsaji: this.team2Player5.tf, skokovi: this.team2Player5.reb, asistencije: this.team2Player5.ast, uLopte: this.team2Player5.stl, blokade: this.team2Player5.blk, preokreti: this.team2Player5.to },
          { broj: this.players2[5].number_player, prezime: this.players2[5].lname, ime: this.players2[5].fname, poeni: this.team2Player6.points, oPrekrsaji: this.team2Player6.pf, tPrekrsaji: this.team2Player6.tf, skokovi: this.team2Player6.reb, asistencije: this.team2Player6.ast, uLopte: this.team2Player6.stl, blokade: this.team2Player6.blk, preokreti: this.team2Player6.to },
          { broj: this.players2[6].number_player, prezime: this.players2[6].lname, ime: this.players2[6].fname, poeni: this.team2Player7.points, oPrekrsaji: this.team2Player7.pf, tPrekrsaji: this.team2Player7.tf, skokovi: this.team2Player7.reb, asistencije: this.team2Player7.ast, uLopte: this.team2Player7.stl, blokade: this.team2Player7.blk, preokreti: this.team2Player7.to },
          { broj: this.players2[7].number_player, prezime: this.players2[7].lname, ime: this.players2[7].fname, poeni: this.team2Player8.points, oPrekrsaji: this.team2Player8.pf, tPrekrsaji: this.team2Player8.tf, skokovi: this.team2Player8.reb, asistencije: this.team2Player8.ast, uLopte: this.team2Player8.stl, blokade: this.team2Player8.blk, preokreti: this.team2Player8.to },
          { broj: this.players2[8].number_player, prezime: this.players2[8].lname, ime: this.players2[8].fname, poeni: this.team2Player9.points, oPrekrsaji: this.team2Player9.pf, tPrekrsaji: this.team2Player9.tf, skokovi: this.team2Player9.reb, asistencije: this.team2Player9.ast, uLopte: this.team2Player9.stl, blokade: this.team2Player9.blk, preokreti: this.team2Player9.to },
          { broj: this.players2[9].number_player, prezime: this.players2[9].lname, ime: this.players2[9].fname, poeni: this.team2Player10.points, oPrekrsaji: this.team2Player10.pf, tPrekrsaji: this.team2Player10.tf, skokovi: this.team2Player10.reb, asistencije: this.team2Player10.ast, uLopte: this.team2Player10.stl, blokade: this.team2Player10.blk, preokreti: this.team2Player10.to },
          { broj: this.players2[10].number_player, prezime: this.players2[10].lname, ime: this.players2[10].fname, poeni: this.team2Player11.points, oPrekrsaji: this.team2Player11.pf, tPrekrsaji: this.team2Player11.tf, skokovi: this.team2Player11.reb, asistencije: this.team2Player11.ast, uLopte: this.team2Player11.stl, blokade: this.team2Player11.blk, preokreti: this.team2Player11.to },
          { broj: this.players2[11].number_player, prezime: this.players2[11].lname, ime: this.players2[11].fname, poeni: this.team2Player12.points, oPrekrsaji: this.team2Player12.pf, tPrekrsaji: this.team2Player12.tf, skokovi: this.team2Player12.reb, asistencije: this.team2Player12.ast, uLopte: this.team2Player12.stl, blokade: this.team2Player12.blk, preokreti: this.team2Player12.to },
        ],
        columns: [
          { header: 'Broj', dataKey: 'broj' },
          { header: 'Prezime', dataKey: 'prezime' },
          { header: 'Ime', dataKey: 'ime' },
          { header: 'Poeni', dataKey: 'poeni' },
          { header: 'O.P.', dataKey: 'oPrekrsaji' },
          { header: 'T.P.', dataKey: 'tPrekrsaji' },
          { header: 'Skok.', dataKey: 'skokovi' },
          { header: 'Asist.', dataKey: 'asistencije' },
          { header: 'U.lopte', dataKey: 'uLopte' },
          { header: 'Blok.', dataKey: 'blokade' },
          { header: 'Preok.', dataKey: 'preokreti' },

        ],
        theme:'grid',
      })
      doc.text('Sudac: ' + this.prvi_sudac, 10, 270);
      doc.text('Sudac: ' + this.drugi_sudac, 75, 270);
      doc.text('Sudac: ' + this.treci_sudac, 150, 270);
      doc.text('Zapisnicar: ' + this.zapisnicar, 10, 280);
      doc.text('Rezultat: ' + (this.team1Player1.points + this.team1Player2.points + this.team1Player3.points + this.team1Player4.points + this.team1Player5.points + this.team1Player6.points + this.team1Player7.points + this.team1Player8.points + this.team1Player9.points + this.team1Player10.points + this.team1Player11.points + this.team1Player12.points) + ':' + (this.team2Player1.points + this.team2Player2.points + this.team2Player3.points + this.team2Player4.points + this.team2Player5.points + this.team2Player6.points + this.team2Player7.points + this.team2Player8.points + this.team2Player9.points + this.team2Player10.points + this.team2Player11.points + this.team2Player12.points), 75, 280);
      doc.save("export.pdf");
    },
    //-
    team1Player1Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.points--;
        }else{
          this.team1Player1.points++;
        }
    },
    team1Player1PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.pf--;
        }else{
          this.team1Player1.pf++;
        }
    },
    team1Player1TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.tf--;
        }else{
          this.team1Player1.tf++;
        }
    },
    team1Player1Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.reb--;
        }else{
          this.team1Player1.reb++;
        }
    },
    team1Player1Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.ast--;
        }else{
          this.team1Player1.ast++;
        }
    },
    team1Player1Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.stl--;
        }else{
          this.team1Player1.stl++;
        }
    },
    team1Player1Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.blk--;
        }else{
          this.team1Player1.blk++;
        }
    },
    team1Player1Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player1.to--;
        }else{
          this.team1Player1.to++;
        }
    },
    //-
    //-
    team1Player2Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.points--;
        }else{
          this.team1Player2.points++;
        }
    },
    team1Player2PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.pf--;
        }else{
          this.team1Player2.pf++;
        }
    },
    team1Player2TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.tf--;
        }else{
          this.team1Player2.tf++;
        }
    },
    team1Player2Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.reb--;
        }else{
          this.team1Player2.reb++;
        }
    },
    team1Player2Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.ast--;
        }else{
          this.team1Player2.ast++;
        }
    },
    team1Player2Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.stl--;
        }else{
          this.team1Player2.stl++;
        }
    },
    team1Player2Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.blk--;
        }else{
          this.team1Player2.blk++;
        }
    },
    team1Player2Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player2.to--;
        }else{
          this.team1Player2.to++;
        }
    },
    //-
    //-
    team1Player3Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.points--;
        }else{
          this.team1Player3.points++;
        }
    },
    team1Player3PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.pf--;
        }else{
          this.team1Player3.pf++;
        }
    },
    team1Player3TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.tf--;
        }else{
          this.team1Player3.tf++;
        }
    },
    team1Player3Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.reb--;
        }else{
          this.team1Player3.reb++;
        }
    },
    team1Player3Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.ast--;
        }else{
          this.team1Player3.ast++;
        }
    },
    team1Player3Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.stl--;
        }else{
          this.team1Player3.stl++;
        }
    },
    team1Player3Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.blk--;
        }else{
          this.team1Player3.blk++;
        }
    },
    team1Player3Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player3.to--;
        }else{
          this.team1Player3.to++;
        }
    },
    //-
    //-
    team1Player4Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.points--;
        }else{
          this.team1Player4.points++;
        }
    },
    team1Player4PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.pf--;
        }else{
          this.team1Player4.pf++;
        }
    },
    team1Player4TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.tf--;
        }else{
          this.team1Player4.tf++;
        }
    },
    team1Player4Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.reb--;
        }else{
          this.team1Player4.reb++;
        }
    },
    team1Player4Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.ast--;
        }else{
          this.team1Player4.ast++;
        }
    },
    team1Player4Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.stl--;
        }else{
          this.team1Player4.stl++;
        }
    },
    team1Player4Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.blk--;
        }else{
          this.team1Player4.blk++;
        }
    },
    team1Player4Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player4.to--;
        }else{
          this.team1Player4.to++;
        }
    },
    //-
    //-
    team1Player5Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.points--;
        }else{
          this.team1Player5.points++;
        }
    },
    team1Player5PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.pf--;
        }else{
          this.team1Player5.pf++;
        }
    },
    team1Player5TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.tf--;
        }else{
          this.team1Player5.tf++;
        }
    },
    team1Player5Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.reb--;
        }else{
          this.team1Player5.reb++;
        }
    },
    team1Player5Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.ast--;
        }else{
          this.team1Player5.ast++;
        }
    },
    team1Player5Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.stl--;
        }else{
          this.team1Player5.stl++;
        }
    },
    team1Player5Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.blk--;
        }else{
          this.team1Player5.blk++;
        }
    },
    team1Player5Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player5.to--;
        }else{
          this.team1Player5.to++;
        }
    },
    //-
    //-
    team1Player6Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.points--;
        }else{
          this.team1Player6.points++;
        }
    },
    team1Player6PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.pf--;
        }else{
          this.team1Player6.pf++;
        }
    },
    team1Player6TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.tf--;
        }else{
          this.team1Player6.tf++;
        }
    },
    team1Player6Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.reb--;
        }else{
          this.team1Player6.reb++;
        }
    },
    team1Player6Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.ast--;
        }else{
          this.team1Player6.ast++;
        }
    },
    team1Player6Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.stl--;
        }else{
          this.team1Player6.stl++;
        }
    },
    team1Player6Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.blk--;
        }else{
          this.team1Player6.blk++;
        }
    },
    team1Player6Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player6.to--;
        }else{
          this.team1Player6.to++;
        }
    },
    //-
    //-
    team1Player7Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.points--;
        }else{
          this.team1Player7.points++;
        }
    },
    team1Player7PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.pf--;
        }else{
          this.team1Player7.pf++;
        }
    },
    team1Player7TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.tf--;
        }else{
          this.team1Player7.tf++;
        }
    },
    team1Player7Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.reb--;
        }else{
          this.team1Player7.reb++;
        }
    },
    team1Player7Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.ast--;
        }else{
          this.team1Player7.ast++;
        }
    },
    team1Player7Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.stl--;
        }else{
          this.team1Player7.stl++;
        }
    },
    team1Player7Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.blk--;
        }else{
          this.team1Player7.blk++;
        }
    },
    team1Player7Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player7.to--;
        }else{
          this.team1Player7.to++;
        }
    },
    //-
    //-
    team1Player8Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.points--;
        }else{
          this.team1Player8.points++;
        }
    },
    team1Player8PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.pf--;
        }else{
          this.team1Player8.pf++;
        }
    },
    team1Player8TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.tf--;
        }else{
          this.team1Player8.tf++;
        }
    },
    team1Player8Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.reb--;
        }else{
          this.team1Player8.reb++;
        }
    },
    team1Player8Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.ast--;
        }else{
          this.team1Player8.ast++;
        }
    },
    team1Player8Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.stl--;
        }else{
          this.team1Player8.stl++;
        }
    },
    team1Player8Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.blk--;
        }else{
          this.team1Player8.blk++;
        }
    },
    team1Player8Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player8.to--;
        }else{
          this.team1Player8.to++;
        }
    },
    //-
    //-
    team1Player9Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.points--;
        }else{
          this.team1Player9.points++;
        }
    },
    team1Player9PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.pf--;
        }else{
          this.team1Player9.pf++;
        }
    },
    team1Player9TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.tf--;
        }else{
          this.team1Player9.tf++;
        }
    },
    team1Player9Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.reb--;
        }else{
          this.team1Player9.reb++;
        }
    },
    team1Player9Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.ast--;
        }else{
          this.team1Player9.ast++;
        }
    },
    team1Player9Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.stl--;
        }else{
          this.team1Player9.stl++;
        }
    },
    team1Player9Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.blk--;
        }else{
          this.team1Player9.blk++;
        }
    },
    team1Player9Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player9.to--;
        }else{
          this.team1Player9.to++;
        }
    },
     //-
    //-
    team1Player10Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.points--;
        }else{
          this.team1Player10.points++;
        }
    },
    team1Player10PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.pf--;
        }else{
          this.team1Player10.pf++;
        }
    },
    team1Player10TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.tf--;
        }else{
          this.team1Player10.tf++;
        }
    },
    team1Player10Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.reb--;
        }else{
          this.team1Player10.reb++;
        }
    },
    team1Player10Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.ast--;
        }else{
          this.team1Player10.ast++;
        }
    },
    team1Player10Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.stl--;
        }else{
          this.team1Player10.stl++;
        }
    },
    team1Player10Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.blk--;
        }else{
          this.team1Player10.blk++;
        }
    },
    team1Player10Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player10.to--;
        }else{
          this.team1Player10.to++;
        }
    },
    //-
    //-
    team1Player11Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.points--;
        }else{
          this.team1Player11.points++;
        }
    },
    team1Player11PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.pf--;
        }else{
          this.team1Player11.pf++;
        }
    },
    team1Player11TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.tf--;
        }else{
          this.team1Player11.tf++;
        }
    },
    team1Player11Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.reb--;
        }else{
          this.team1Player11.reb++;
        }
    },
    team1Player11Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.ast--;
        }else{
          this.team1Player11.ast++;
        }
    },
    team1Player11Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.stl--;
        }else{
          this.team1Player11.stl++;
        }
    },
    team1Player11Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.blk--;
        }else{
          this.team1Player11.blk++;
        }
    },
    team1Player11Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player11.to--;
        }else{
          this.team1Player11.to++;
        }
    },
    //-
    //-
    team1Player12Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.points--;
        }else{
          this.team1Player12.points++;
        }
    },
    team1Player12PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.pf--;
        }else{
          this.team1Player12.pf++;
        }
    },
    team1Player12TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.tf--;
        }else{
          this.team1Player12.tf++;
        }
    },
    team1Player12Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.reb--;
        }else{
          this.team1Player12.reb++;
        }
    },
    team1Player12Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.ast--;
        }else{
          this.team1Player12.ast++;
        }
    },
    team1Player12Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.stl--;
        }else{
          this.team1Player12.stl++;
        }
    },
    team1Player12Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.blk--;
        }else{
          this.team1Player12.blk++;
        }
    },
    team1Player12Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team1Player12.to--;
        }else{
          this.team1Player12.to++;
        }
    },
    //-
    //-
    team2Player1Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.points--;
        }else{
          this.team2Player1.points++;
        }
    },
    team2Player1PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.pf--;
        }else{
          this.team2Player1.pf++;
        }
    },
    team2Player1TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.tf--;
        }else{
          this.team2Player1.tf++;
        }
    },
    team2Player1Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.reb--;
        }else{
          this.team2Player1.reb++;
        }
    },
    team2Player1Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.ast--;
        }else{
          this.team2Player1.ast++;
        }
    },
    team2Player1Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.stl--;
        }else{
          this.team2Player1.stl++;
        }
    },
    team2Player1Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.blk--;
        }else{
          this.team2Player1.blk++;
        }
    },
    team2Player1Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player1.to--;
        }else{
          this.team2Player1.to++;
        }
    },
    //-
    //-
    team2Player2Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.points--;
        }else{
          this.team2Player2.points++;
        }
    },
    team2Player2PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.pf--;
        }else{
          this.team2Player2.pf++;
        }
    },
    team2Player2TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.tf--;
        }else{
          this.team2Player2.tf++;
        }
    },
    team2Player2Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.reb--;
        }else{
          this.team2Player2.reb++;
        }
    },
    team2Player2Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.ast--;
        }else{
          this.team2Player2.ast++;
        }
    },
    team2Player2Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.stl--;
        }else{
          this.team2Player2.stl++;
        }
    },
    team2Player2Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.blk--;
        }else{
          this.team2Player2.blk++;
        }
    },
    team2Player2Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player2.to--;
        }else{
          this.team2Player2.to++;
        }
    },
    //-
    //-
    team2Player3Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.points--;
        }else{
          this.team2Player3.points++;
        }
    },
    team2Player3PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.pf--;
        }else{
          this.team2Player3.pf++;
        }
    },
    team2Player3TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.tf--;
        }else{
          this.team2Player3.tf++;
        }
    },
    team2Player3Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.reb--;
        }else{
          this.team2Player3.reb++;
        }
    },
    team2Player3Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.ast--;
        }else{
          this.team2Player3.ast++;
        }
    },
    team2Player3Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.stl--;
        }else{
          this.team2Player3.stl++;
        }
    },
    team2Player3Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.blk--;
        }else{
          this.team2Player3.blk++;
        }
    },
    team2Player3Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player3.to--;
        }else{
          this.team2Player3.to++;
        }
    },
    //-
    //-
    team2Player4Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.points--;
        }else{
          this.team2Player4.points++;
        }
    },
    team2Player4PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.pf--;
        }else{
          this.team2Player4.pf++;
        }
    },
    team2Player4TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.tf--;
        }else{
          this.team2Player4.tf++;
        }
    },
    team2Player4Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.reb--;
        }else{
          this.team2Player4.reb++;
        }
    },
    team2Player4Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.ast--;
        }else{
          this.team2Player4.ast++;
        }
    },
    team2Player4Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.stl--;
        }else{
          this.team2Player4.stl++;
        }
    },
    team2Player4Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.blk--;
        }else{
          this.team2Player4.blk++;
        }
    },
    team2Player4Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player4.to--;
        }else{
          this.team2Player4.to++;
        }
    },
    //-
    //-
    team2Player5Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.points--;
        }else{
          this.team2Player5.points++;
        }
    },
    team2Player5PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.pf--;
        }else{
          this.team2Player5.pf++;
        }
    },
    team2Player5TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.tf--;
        }else{
          this.team2Player5.tf++;
        }
    },
    team2Player5Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.reb--;
        }else{
          this.team2Player5.reb++;
        }
    },
    team2Player5Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.ast--;
        }else{
          this.team2Player5.ast++;
        }
    },
    team2Player5Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.stl--;
        }else{
          this.team2Player5.stl++;
        }
    },
    team2Player5Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.blk--;
        }else{
          this.team2Player5.blk++;
        }
    },
    team2Player5Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player5.to--;
        }else{
          this.team2Player5.to++;
        }
    },
    //-
    //-
    team2Player6Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.points--;
        }else{
          this.team2Player6.points++;
        }
    },
    team2Player6PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.pf--;
        }else{
          this.team2Player6.pf++;
        }
    },
    team2Player6TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.tf--;
        }else{
          this.team2Player6.tf++;
        }
    },
    team2Player6Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.reb--;
        }else{
          this.team2Player6.reb++;
        }
    },
    team2Player6Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.ast--;
        }else{
          this.team2Player6.ast++;
        }
    },
    team2Player6Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.stl--;
        }else{
          this.team2Player6.stl++;
        }
    },
    team2Player6Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.blk--;
        }else{
          this.team2Player6.blk++;
        }
    },
    team2Player6Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player6.to--;
        }else{
          this.team2Player6.to++;
        }
    },
    //-
    //-
    team2Player7Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.points--;
        }else{
          this.team2Player7.points++;
        }
    },
    team2Player7PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.pf--;
        }else{
          this.team2Player7.pf++;
        }
    },
    team2Player7TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.tf--;
        }else{
          this.team2Player7.tf++;
        }
    },
    team2Player7Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.reb--;
        }else{
          this.team2Player7.reb++;
        }
    },
    team2Player7Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.ast--;
        }else{
          this.team2Player7.ast++;
        }
    },
    team2Player7Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.stl--;
        }else{
          this.team2Player7.stl++;
        }
    },
    team2Player7Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.blk--;
        }else{
          this.team2Player7.blk++;
        }
    },
    team2Player7Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player7.to--;
        }else{
          this.team2Player7.to++;
        }
    },
    //-
    //-
    team2Player8Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.points--;
        }else{
          this.team2Player8.points++;
        }
    },
    team2Player8PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.pf--;
        }else{
          this.team2Player8.pf++;
        }
    },
    team2Player8TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.tf--;
        }else{
          this.team2Player8.tf++;
        }
    },
    team2Player8Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.reb--;
        }else{
          this.team2Player8.reb++;
        }
    },
    team2Player8Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.ast--;
        }else{
          this.team2Player8.ast++;
        }
    },
    team2Player8Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.stl--;
        }else{
          this.team2Player8.stl++;
        }
    },
    team2Player8Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.blk--;
        }else{
          this.team2Player8.blk++;
        }
    },
    team2Player8Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player8.to--;
        }else{
          this.team2Player8.to++;
        }
    },
    //-
    //-
    team2Player9Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.points--;
        }else{
          this.team2Player9.points++;
        }
    },
    team2Player9PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.pf--;
        }else{
          this.team2Player9.pf++;
        }
    },
    team2Player9TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.tf--;
        }else{
          this.team2Player9.tf++;
        }
    },
    team2Player9Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.reb--;
        }else{
          this.team2Player9.reb++;
        }
    },
    team2Player9Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.ast--;
        }else{
          this.team2Player9.ast++;
        }
    },
    team2Player9Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.stl--;
        }else{
          this.team2Player9.stl++;
        }
    },
    team2Player9Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.blk--;
        }else{
          this.team2Player9.blk++;
        }
    },
    team2Player9Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player9.to--;
        }else{
          this.team2Player9.to++;
        }
    },
    //-
    //-
    team2Player10Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.points--;
        }else{
          this.team2Player10.points++;
        }
    },
    team2Player10PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.pf--;
        }else{
          this.team2Player10.pf++;
        }
    },
    team2Player10TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.tf--;
        }else{
          this.team2Player10.tf++;
        }
    },
    team2Player10Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.reb--;
        }else{
          this.team2Player10.reb++;
        }
    },
    team2Player10Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.ast--;
        }else{
          this.team2Player10.ast++;
        }
    },
    team2Player10Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.stl--;
        }else{
          this.team2Player10.stl++;
        }
    },
    team2Player10Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.blk--;
        }else{
          this.team2Player10.blk++;
        }
    },
    team2Player10Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player10.to--;
        }else{
          this.team2Player10.to++;
        }
    },
    //-
    //-
    team2Player11Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.points--;
        }else{
          this.team2Player11.points++;
        }
    },
    team2Player11PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.pf--;
        }else{
          this.team2Player11.pf++;
        }
    },
    team2Player11TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.tf--;
        }else{
          this.team2Player11.tf++;
        }
    },
    team2Player11Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.reb--;
        }else{
          this.team2Player11.reb++;
        }
    },
    team2Player11Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.ast--;
        }else{
          this.team2Player11.ast++;
        }
    },
    team2Player11Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.stl--;
        }else{
          this.team2Player11.stl++;
        }
    },
    team2Player11Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.blk--;
        }else{
          this.team2Player11.blk++;
        }
    },
    team2Player11Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player11.to--;
        }else{
          this.team2Player11.to++;
        }
    },
    //-
    //-
    team2Player12Points(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.points--;
        }else{
          this.team2Player12.points++;
        }
    },
    team2Player12PersonalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.pf--;
        }else{
          this.team2Player12.pf++;
        }
    },
    team2Player12TehnicalFouls(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.tf--;
        }else{
          this.team2Player12.tf++;
        }
    },
    team2Player12Rebounds(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.reb--;
        }else{
          this.team2Player12.reb++;
        }
    },
    team2Player12Assists(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.ast--;
        }else{
          this.team2Player12.ast++;
        }
    },
    team2Player12Steals(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.stl--;
        }else{
          this.team2Player12.stl++;
        }
    },
    team2Player12Blocks(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.blk--;
        }else{
          this.team2Player12.blk++;
        }
    },
    team2Player12Turnovers(e,isDoubleClick){
        if (isDoubleClick){
          this.team2Player12.to--;
        }else{
          this.team2Player12.to++;
        }
    },

    //-
    minuteOdmoraPrvoPolMinus() {
      this.minuteOdmoraPrvoPol--;
      if(this.minuteOdmoraPrvoPol < 0)
      {
        this.minuteOdmoraPrvoPol = 0;
      }
    },
    minuteOdmoraPrvoPolPlus() {
      this.minuteOdmoraPrvoPol++;
      if(this.minuteOdmoraPrvoPol > 2)
      {
        this.minuteOdmoraPrvoPol = 2;
      }
    },
    minuteOdmoraDrugoPolMinus() {
      this.minuteOdmoraDrugoPol--;
      if(this.minuteOdmoraDrugoPol < 0)
      {
        this.minuteOdmoraDrugoPol = 0;
      }
    },
    minuteOdmoraDrugoPolPlus() {
      this.minuteOdmoraDrugoPol++;
      if(this.minuteOdmoraDrugoPol > 2)
      {
        this.minuteOdmoraDrugoPol = 2;
      }
    },
    //
    ekipnePogreskePrvaCetPlus() {
      this.ekipnePogreskePrvaCet++;
      if(this.ekipnePogreskePrvaCet > 4)
      {
        this.ekipnePogreskePrvaCet = 4;
      }
    },
    ekipnePogreskePrvaCetMinus() {
      this.ekipnePogreskePrvaCet--;
      if(this.ekipnePogreskePrvaCet < 0)
      {
        this.ekipnePogreskePrvaCet = 0;
      }
    },
    ekipnePogreskeDrugaCetPlus() {
      this.ekipnePogreskeDrugaCet++;
      if(this.ekipnePogreskeDrugaCet > 4)
      {
        this.ekipnePogreskeDrugaCet = 4;
      }
    },
    ekipnePogreskeDrugaCetMinus() {
      this.ekipnePogreskeDrugaCet--;
      if(this.ekipnePogreskeDrugaCet < 0)
      {
        this.ekipnePogreskeDrugaCet = 0;
      }
    },
    ekipnePogreskeTrecaCetPlus() {
      this.ekipnePogreskeTrecaCet++;
      if(this.ekipnePogreskeTrecaCet > 4)
      {
        this.ekipnePogreskeTrecaCet = 4;
      }
    },
    ekipnePogreskeTrecaCetMinus() {
      this.ekipnePogreskeTrecaCet--;
      if(this.ekipnePogreskeTrecaCet < 0)
      {
        this.ekipnePogreskeTrecaCet = 0;
      }
    },
    ekipnePogreskeCetvrtaCetPlus() {
      this.ekipnePogreskeCetvrtaCet++;
      if(this.ekipnePogreskeCetvrtaCet > 4)
      {
        this.ekipnePogreskeCetvrtaCet = 4;
      }
    },
    ekipnePogreskeCetvrtaCetMinus() {
      this.ekipnePogreskeCetvrtaCet--;
      if(this.ekipnePogreskeCetvrtaCet < 0)
      {
        this.ekipnePogreskeCetvrtaCet = 0;
      }
    },
    //
     //-
    team2minuteOdmoraPrvoPolMinus() {
      this.team2minuteOdmoraPrvoPol--;
      if(this.team2minuteOdmoraPrvoPol < 0)
      {
        this.team2minuteOdmoraPrvoPol = 0;
      }
    },
    team2minuteOdmoraPrvoPolPlus() {
      this.team2minuteOdmoraPrvoPol++;
      if(this.team2minuteOdmoraPrvoPol > 2)
      {
        this.team2minuteOdmoraPrvoPol = 2;
      }
    },
    team2minuteOdmoraDrugoPolMinus() {
      this.team2minuteOdmoraDrugoPol--;
      if(this.team2minuteOdmoraDrugoPol < 0)
      {
        this.team2minuteOdmoraDrugoPol = 0;
      }
    },
    team2minuteOdmoraDrugoPolPlus() {
      this.team2minuteOdmoraDrugoPol++;
      if(this.team2minuteOdmoraDrugoPol > 2)
      {
        this.team2minuteOdmoraDrugoPol = 2;
      }
    },
    //
    team2ekipnePogreskePrvaCetPlus() {
      this.team2ekipnePogreskePrvaCet++;
      if(this.team2ekipnePogreskePrvaCet > 4)
      {
        this.team2ekipnePogreskePrvaCet = 4;
      }
    },
    team2ekipnePogreskePrvaCetMinus() {
      this.team2ekipnePogreskePrvaCet--;
      if(this.team2ekipnePogreskePrvaCet < 0)
      {
        this.team2ekipnePogreskePrvaCet = 0;
      }
    },
    team2ekipnePogreskeDrugaCetPlus() {
      this.team2ekipnePogreskeDrugaCet++;
      if(this.team2ekipnePogreskeDrugaCet > 4)
      {
        this.team2ekipnePogreskeDrugaCet = 4;
      }
    },
    team2ekipnePogreskeDrugaCetMinus() {
      this.team2ekipnePogreskeDrugaCet--;
      if(this.team2ekipnePogreskeDrugaCet < 0)
      {
        this.team2ekipnePogreskeDrugaCet = 0;
      }
    },
    team2ekipnePogreskeTrecaCetPlus() {
      this.team2ekipnePogreskeTrecaCet++;
      if(this.team2ekipnePogreskeTrecaCet > 4)
      {
        this.team2ekipnePogreskeTrecaCet = 4;
      }
    },
    team2ekipnePogreskeTrecaCetMinus() {
      this.team2ekipnePogreskeTrecaCet--;
      if(this.team2ekipnePogreskeTrecaCet < 0)
      {
        this.team2ekipnePogreskeTrecaCet = 0;
      }
    },
    team2ekipnePogreskeCetvrtaCetPlus() {
      this.team2ekipnePogreskeCetvrtaCet++;
      if(this.team2ekipnePogreskeCetvrtaCet > 4)
      {
        this.team2ekipnePogreskeCetvrtaCet = 4;
      }
    },
    team2ekipnePogreskeCetvrtaCetMinus() {
      this.team2ekipnePogreskeCetvrtaCet--;
      if(this.team2ekipnePogreskeCetvrtaCet < 0)
      {
        this.team2ekipnePogreskeCetvrtaCet = 0;
      }
    },
    //
    createUtakmica() {
      axios.post('http://localhost:8000/utakmica/zapisnik', {
        id_home: this.id_home,
        id_away: this.id_away,
        name_home: 'asds',
        name_away: 'asds',
        natjecanje: this.natjecanje,
        date: this.date,
        mjesto: this.mjesto,
        prvi_sudac: this.prvi_sudac,
        drugi_sudac: this.drugi_sudac,
        treci_sudac: this.treci_sudac,
        zapisnicar: this.zapisnicar,
      }).then((res) => {
        this.tryer2 = 'test',
        this.tryer = '',
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    getTeams() {
      axios.get('http://localhost:8000/teams').then((response) => {
        this.teams = response.data;
      })
    },
    getHomeTeamName() {
      axios.get(`http://localhost:8000/team/${this.id_home}`).then((response) => {
        this.homeName = response.data.name;
      })
    },
    getAwayTeamName() {
      axios.get(`http://localhost:8000/team/${this.id_away}`).then((response) => {
        this.awayName = response.data.name;
      })
    },
    getHomeTeam() {
      axios.get(`http://localhost:8000/players/${this.id_home}/team`).then((response) => {
        this.players = response.data;
      })
    },
    getAwayTeam() {
      axios.get(`http://localhost:8000/players/${this.id_away}/team`).then((response) => {
        this.players2 = response.data;
      })
    },
    createResult() {
      axios.post('http://localhost:8000/result', {
        home: this.homeName,
        away: this.awayName,
        date: new Date().toISOString().substr(0, 10),
        home_points: this.team1Player1.points + this.team1Player2.points + this.team1Player3.points + this.team1Player4.points + this.team1Player5.points + this.team1Player6.points + this.team1Player7.points + this.team1Player8.points + this.team1Player9.points + this.team1Player10.points + this.team1Player11.points + this.team1Player12.points,
        away_points: this.team2Player1.points + this.team2Player2.points + this.team2Player3.points + this.team2Player4.points + this.team2Player5.points + this.team2Player6.points + this.team2Player7.points + this.team2Player8.points + this.team2Player9.points + this.team2Player10.points + this.team2Player11.points + this.team2Player12.points,
      }).then((res) => {
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
  },
  created() {
    this.getTeams();
    window.addEventListener('beforeunload', (event) => {
      event.returnValue = `Are you sure you want to leave?`;
    });
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
.statistika1 {
    margin-top: 7px;
    padding-left: 12px;

}
.homeTitle {
    margin-bottom: 22px;
    text-align: center;
}

.btncollapsemargin {
    margin-right: 285px;
}

.rowIgrac1 {
    margin-top: 10px;
}

.rowIgrac2 {
    margin-top: 20px;
}

.rowIgrac3 {
    margin-top: 18px;
}

.rowIgrac4 {
    margin-top: 14px;
}
.rowIgrac5 {
    margin-top: 14px;
}

.rowIgrac6 {
    margin-top: 16px;
}

.rowIgrac7 {
    margin-top: 16px;
}

.rowIgrac8 {
    margin-top: 16px;
}

.rowIgrac9 {
    margin-top: 16px;
}

.rowIgrac10 {
    margin-top: 16px;
}

.rowIgrac11 {
    margin-top: 16px;
}

.rowIgrac12 {
    margin-top: 16px;
}
</style>
