<template>
    <div class="home">
      <h1 class="titolo"><i>Viaggi ToDo</i></h1>
      <nav>
      <router-link to="/home">Home</router-link> |
      <router-link to="/gestisci">Gestisci</router-link> |
      <button class="logout" type="submit" @click="logout">Logout</button>
      </nav>
      <hr class="linea_titolo">
      <div class="p1">
        <h5>Introduzione</h5>
        <p>Nella sezione <i>HOME</i> saranno visualizzati tutti i viaggi che sono stati salvati e avrai la possibilità di aggiungerne altri.</p>
        <p> 
          Inoltre, con un semplice click su "segna come fatto" potrai spostare un viaggio dalla tabella "Viaggi da Fare" a "Viaggi Fatti".
        </p>
        <p>Nella sezione <i>GESTISCI</i>, invece, potrai eliminare e modificare tutti i tuoi viaggi.</p>
      </div>
      <div class="tabelle"> <!--Sezione dove sono contenuti le tabelle dei viaggi fatti e da fare-->
        <TransitionGroup tag="div" name="fade" appear>
        <div class="table1" v-if="true"><!--Table che contiene tutti i viaggi fatti presenti nel db-->
          <h4>Viaggi Fatti</h4>
          <table v-for="elementi in listaViaggiFatti" :key="elementi.id" @dblclick="$data.element = ViaggiFatti">
            <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
            <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
            <tr><th>Racconto</th><td>{{ elementi.Descrizione }}</td></tr>
            <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
            <hr>
          </table>
          <div class="bottoneA">
            <button @click="toggleAggiungiVF">Aggiungi</button>
          </div>
          <table v-if="aggiungiVFTrue"><!--Sezione che permette di aggiungere elementi-->
            <tr><th>Titolo</th><input v-model="ViaggiFatti.Titolo" type="text" placeholder="Titolo"></tr>
            <tr><th>Data</th><input v-model="ViaggiFatti.Data" type="date" placeholder="Data"></tr>
            <tr><th>Racconto</th><textarea v-model="ViaggiFatti.Descrizione" type="textarea" placeholder="Racconto"></textarea></tr>
            <tr><th>Luogo </th><input v-model="ViaggiFatti.Luogo" type="text" placeholder="Luogo"></tr>
            <hr>
            <button class="bottone" @click="createElementVF">Conferma</button>
          </table>
          <br>
        </div>
        </TransitionGroup>
        <TransitionGroup tag="div" name="fade2" appear>
        <div class="table2" v-if="true"><!--Table contenente tutti i viaggi da fare presenti nel db-->
          <h4>Viaggi Da Fare</h4> 
          <table v-for="elementi in listaViaggiDaFare" :key="elementi.id" @dblclick="$data.element = ViaggiDaFare">
            <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>  
            <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
            <tr><th>Attività</th><td>{{ elementi.Attivita }}</td></tr>
            <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
            <button v-if="fatto" class="fatto" @click="spostaViaggio(elementi)">Fatto</button>
            <hr>
          </table>
          <div class="bottoneA">
            <button @click="toggleAggiungiVdF">Aggiungi</button> |
            <button @click="segnaFatto">Segna come fatto</button><!--Attiva la funzione che fa comparire i button per spostare gli elementi-->
          </div>
          <table v-if="aggiungiVdFTrue"><!--Sezione che permette di aggiungere elementi-->
            <tr><th>Titolo</th><input v-model="ViaggiDaFare.Titolo" type="text" placeholder="Titolo"></tr>
            <tr><th>Data</th><input v-model="ViaggiDaFare.Data" type="date" placeholder="Data"></tr>
            <tr><th>Attività</th><textarea v-model="ViaggiDaFare.Attivita" type="textarea" placeholder="Attività da svolgere"></textarea></tr>
            <tr><th>Luogo </th><input v-model="ViaggiDaFare.Luogo" type="text" placeholder="Luogo"></tr>
            <hr>
            <button class="bottone" @click="createElementVdF">Conferma</button>
          </table>
          <br>
        </div>
        </TransitionGroup>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'Home',
    data(){
      return{
        ViaggiFatti:{
          'Titolo':'',
          'Data':'',
          'Descrizione':'',
          'Luogo':'',
        },
        ViaggiDaFare:{
          'Titolo':'',
          'Data':'',
          'Attivita':'',
          'Luogo':'',
        },
        listaViaggiFatti: [],
        listaViaggiDaFare: [],
        aggiungiVFTrue : false,
        aggiungiVdFTrue : false,
        fatto: false,
      }
    },
    mounted(){/*popola le due liste*/
       this.getViaggiFatti();
       this.getViaggiDaFare();
    },
    methods:{
      async logout(){
        await axios
          .post('api/v1/token/logout/')
          .then(response =>{
            console.log('Logged out')
          })
          .catch(error =>{
            console.log(JSON.stringify(error))
          })
        
          axios.defaults.headers.common['Authorization'] = ''
          localStorage.removeItem('token')
          this.$store.commit('removeToken')

          this.$router.push('/')
      },
      async getViaggiFatti(){/*Recupera dati dal db Viaggi Fatti*/
        this.$store.commit('setIsLoading', true)
        axios
            .get('api/viaggi-fatti/')
            .then(response => {
                this.listaViaggiFatti = response.data
            })
            .catch(error => {
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
      },
      async getViaggiDaFare(){/*Recupera dati dal db Viaggi Da Fare*/
        this.$store.commit('setIsLoading', true)
        axios
            .get('api/viaggi-da-fare/')
            .then(response => {
                this.listaViaggiDaFare = response.data
            })
            .catch(error => {
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
      },
      toggleAggiungiVF(){
        this.aggiungiVFTrue = !this.aggiungiVFTrue;
      },
      toggleAggiungiVdF(){
        this.aggiungiVdFTrue = !this.aggiungiVdFTrue;
      },
      segnaFatto(){
        this.fatto =! this.fatto;
      },
      async createElementVdF(){/*Crea un elemento nel db Viaggi Da Fare*/
            axios
                .post('/api/viaggi-da-fare/', this.ViaggiDaFare)
                .then(response => {
                    this.getViaggiDaFare()
                    this.ViaggiDaFare = {}
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async createElementVF(){/*Crea un elemento nel db Viaggi Da Fare*/
            axios
                .post('/api/viaggi-fatti/', this.ViaggiFatti)
                .then(response => {
                    this.getViaggiFatti()
                    this.ViaggiFatti = {}
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async spostaViaggio(element){/*sposta i viaggi da fare nel db viaggi fatti*/
            this.ViaggiFatti = element;
            this.ViaggiFatti.Descrizione = element.Attivita  
          axios
                .post('/api/viaggi-fatti/', this.ViaggiFatti)
                .then(response => {
                    this.getViaggiFatti()
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
            axios
                .delete(`/api/viaggi-da-fare/${element.id}`)
                .then(response => {
                    this.getViaggiDaFare()
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
  }
  </script>
  
  <style>
  /*css e transizioni*/
  .fade-enter-from{
    opacity: 0;
    transform: scale(0.6);
  }
  .fade-enter-to{
    opacity: 1;
    transform: scale(1);
  }
  .fade-enter-active{
    transition: 600ms ease-out;
  }
  
  .fade2-enter-from{
    opacity: 0;
    transform: scale(0.6);
  }
  .fade2-enter-to{
    opacity: 1;
    transform: scale(1);
  }
  .fade2-enter-active{
    transition: 600ms ease-out;
  }
  
  #app {
    text-align: center;
    font-family:Georgia, 'Times New Roman', Times, serif;
    color: black;
  }

  .p1{
    margin-top: -5px;  
    width: auto;
  }
  .linea_titolo{
    width: 80%;
  }
  .table1{
    text-align: left;
    float: right;
    width: 45%;
    margin-left: 2%;
    border: solid 1px;
    border-radius: 40px;
    background-color: lavender;
  }
  .tabelle table{
    margin-left: 2%;
  }
  .table2{
    text-align: left;
    float: left;
    width: 45%; 
    margin-right: 2%;
    border: solid 1px;
    border-radius: 40px;
    background-color: lightcyan;
  }
  h4{
    text-align: center;
  }
  .bottone{
    background-color: rgb(172, 104, 236);
    border: rgb(120, 38, 197) solid 1px;
    border-radius: 5px;
    color:white;
    cursor: pointer;
  }
  .fatto{
    color:deeppink;
    border: solid 1px midnightblue;
    background-color: white;
    border-radius: 5px;
  }
  .bottoneA{
    margin: auto;
    text-align: center;
    margin-bottom: 2%;
    cursor: pointer;
  }
  .bottoneA button{
    background-color: rgb(172, 104, 236);
    border: rgb(120, 38, 197) solid 1px;
    border-radius: 5px;
    color:white;
    cursor: pointer;
  }
  .logout{
    background-color: red;
    color: white;
    border: 1px solid red;
    border-radius: 15px;
    height: 20px;
    width: 60px;
    cursor: pointer;
  }
  @media only screen and (max-width: 1000px){
    .table1{
      margin: auto;
      float: none;
      width: 85%;
      margin-bottom: 3%;
    }
    .table2{
      margin: auto;
      float: none;
      width: 85%;
    }
  }
  </style>
  