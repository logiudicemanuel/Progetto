<template>
    <div class="gestisci">
      <h1><i>Viaggi ToDo</i></h1> 
      <nav>
        <router-link to="/home">Home</router-link> |
        <router-link to="/gestisci">Gestisci</router-link> |
        <button class="logout" type="submit" @click="logout">Logout</button>
      </nav>
      <hr>
      <div class="row"><!--Sezioni con i 4 bottoni che permettono la gestione dei vari viaggi-->
        <h4>Gestisci tutti i viaggi che hai fatto qui sotto : </h4>
        <Transition name="mod1" appear>
        <button @click="togglemodVF" class="btModifica1"><img src="../img/modifica.png"><br>Modifica Viaggio</button>
        </Transition>
        <Transition name="rim1" appear>
        <button @click="togglerimVF" class="btRimuovi1"><img src="../img/rimuovi.png"><br>Rimuovi Viaggio</button>
        </Transition> 
        <h4>Gestisci tutti i viaggi che vorrai fare qui sotto : </h4>
        <Transition name="mod2" appear>
        <button @click="togglemodVdF" class="btModifica2"><img class="VdF" src="../img/modifica.png"><br>Modifica Viaggio</button>
        </Transition>
        <Transition name="rim2" appear>
        <button @click="togglerimVdF" class="btRimuovi2"><img class="VdF" src="../img/rimuovi.png"><br>Rimuovi Viaggio</button>
        </Transition>
        <br>
        <br>
      </div>
      <br>
      <TransitionGroup tag="div" name="comparsa">
      <div class="table1Mod" v-if="modVF"><!--Contenitore dove è possibile modificare i viaggi fatti-->
        <h4>Modifica Viaggi Fatti</h4>
        <div class="ricerca" v-if="ricercaModVF">
        <h4>Vuoi ricercare il viaggio da modificare o rimuovere?</h4>
        <table>
          <tr><th>Titolo</th><input v-model="Ricerca.Titolo" type="text" placeholder="Titolo"></tr>
          <tr><th>Data</th><input v-model="Ricerca.Data" type="date" placeholder="Data"></tr>
          <tr><th>Luogo </th><input v-model="Ricerca.Luogo" type="text" placeholder="Luogo"></tr>
        </table>
        </div>
        <div class="conferma" v-if="ricercaModVF"> 
          <button v-if="btconferma" @click="ricercaViaggio(Ricerca)">Conferma</button> |
          <button @click="stopMod">Vedi Tutti</button> |
        </div>
        <hr>
        <div class="ricercaON" v-if="ricercaON"><!--Contiene la lista degli elementi ricercati-->
        <table v-for="elementi in listaRicerca" :key="elementi.id">
          <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
          <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
          <tr><th>Racconto</th><td>{{ elementi.Descrizione }}</td></tr>
          <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
          <button class="modifica" @click="abilitaModVF(elementi)">Modifica</button>
        </table>
        </div>
        <div class="divModifica" v-if="modificaVF">
        <h4>Puoi modificare qui sotto : </h4>
        <table>
          <tr><th>Titolo</th><input v-model="ViaggiFatti.Titolo" type="text" placeholder="Titolo"></tr>
          <tr><th>Data</th><input v-model="ViaggiFatti.Data" type="date" placeholder="Data"></tr>
          <tr><th>Racconto</th><textarea v-model="ViaggiFatti.Descrizione" type="textarea" placeholder="Racconto"></textarea></tr>
          <tr><th>Luogo </th><input v-model="ViaggiFatti.Luogo" type="text" placeholder="Luogo"></tr>
        </table>
        <button class="conferma" @click="editVF">Conferma</button> |
        <button class="vediTutti" @click="stopMod">Vedi Tutti</button> |
        </div>
        <div v-if="!ricercaON"><!--Contiene la lista di tutti gli elementi del db viaggi fatti-->
        <table v-for="elementi in listaViaggiFatti" :key="elementi.id">
          <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
          <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
          <tr><th>Racconto</th><td>{{ elementi.Descrizione }}</td></tr>
          <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
          <button class="modifica" @click="abilitaModVF(elementi)">Modifica</button>
          <hr>
        </table>
        </div>
      </div>
      </TransitionGroup>
      <TransitionGroup tag="div" name="comparsa">
      <div class="table1Mod" v-if="rimVF"><!--Contenitore dove è possibile eliminare i viaggi fatti-->
        <h4>Rimuovi Viaggi Fatti</h4>
        <div class="ricerca">
          <h4>Vuoi ricercare il viaggio da modificare o rimuovere?</h4>
          <table>
            <tr><th>Titolo</th><input v-model="Ricerca.Titolo" type="text" placeholder="Titolo"></tr>
            <tr><th>Data</th><input v-model="Ricerca.Data" type="date" placeholder="Data"></tr>
            <tr><th>Luogo </th><input v-model="Ricerca.Luogo" type="text" placeholder="Luogo"></tr>
          </table>
        </div>
        <div class="conferma">
          <button v-if="btconferma" @click="ricercaViaggio(Ricerca)">Conferma</button> |
          <button @click="stopMod">Vedi Tutti</button> |
        </div>
        <hr>
        <div class="ricercaON" v-if="ricercaON"><!--Contiene la lista degli elementi ricercati-->
          <table v-for="elementi in listaRicerca" :key="elementi.id">
            <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
            <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
            <tr><th>Racconto</th><td>{{ elementi.Descrizione }}</td></tr>
            <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
            <button class="cancella" @click="eliminaVF(elementi)">Cancella</button>
            <hr>
          </table>
        </div>
        <div v-if="ricercaOFF"><!--Contiene la lista di tutti gli elementi del db viaggi fatti-->
        <table v-for="elementi in listaViaggiFatti" :key="elementi.id">
          <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
          <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
          <tr><th>Racconto</th><td>{{ elementi.Descrizione }}</td></tr>
          <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
          <button class="cancella" @click="eliminaVF(elementi)">Cancella</button>
          <hr>
        </table>
        </div>
      </div>
      </TransitionGroup>
      <TransitionGroup tag="div" name="comparsa">
      <div class="table2Mod" v-if="modVdF"><!--Contenitore dove è possibile modificare i viaggi da fare-->
        <h4>Modifica Viaggi Da Fare</h4>
        <div class="ricerca" v-if="ricercaModVdF"><!--Sezione che permette la ricerca-->
          <h4>Vuoi ricercare il viaggio da modificare o rimuovere?</h4>
          <table>
            <tr><th>Titolo</th><input v-model="Ricerca.Titolo" type="text" placeholder="Titolo"></tr>
            <tr><th>Data</th><input v-model="Ricerca.Data" type="date" placeholder="Data"></tr>
            <tr><th>Luogo </th><input v-model="Ricerca.Luogo" type="text" placeholder="Luogo"></tr>
          </table>
        </div>
        <div class="conferma" v-if="ricercaModVdF">
          <button v-if="btconferma" @click="ricercaVdF(Ricerca)">Conferma</button> |
          <button @click="stopMod">Vedi Tutti</button> |
        </div>
        <hr>
        <div class="ricercaON" v-if="ricercaON"><!--Contiene la lista dei viaggi ricercati-->
          <table v-for="elementi in listaRicerca" :key="elementi.id">
            <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
            <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
            <tr><th>Attività</th><td>{{ elementi.Attivita }}</td></tr>
            <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
            <button class="modifica" @click="abilitaModVdF(elementi)">Modifica</button>
            <hr>
          </table>
        </div>
        <div class="divModifica" v-if="modificaVdF"><!--Sezione che permette la modifica-->
          <h4>Puoi modificare qui sotto : </h4>
          <table>
            <tr><th>Titolo</th><input v-model="ViaggiDaFare.Titolo" type="text" placeholder="Titolo"></tr>
            <tr><th>Data</th><input v-model="ViaggiDaFare.Data" type="date" placeholder="Data"></tr>
            <tr><th>Attivita'</th><textarea v-model="ViaggiDaFare.Attivita" type="textarea" placeholder="Attività da svolgere"></textarea></tr>
            <tr><th>Luogo </th><input v-model="ViaggiDaFare.Luogo" type="text" placeholder="Luogo"></tr>
          </table>
          <button @click="editVdF">Conferma</button> |
          <button class="vediTutti" @click="stopMod">Vedi Tutti</button> |
          <hr>  
        </div>
        <div v-if="!ricercaON"><!--Contiene la lista dei viaggi da fare presenti nel db-->
          <table v-for="elementi in listaViaggiDaFare" :key="elementi.id">
            <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
            <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
            <tr><th>Attivita'</th><td>{{ elementi.Attivita }}</td></tr>
            <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
            <button class="modifica" @click="abilitaModVdF(elementi)">Modifica</button>
            <hr>
          </table>
        </div>
      </div>
      </TransitionGroup>
      <TransitionGroup tag="div" name="comparsa">
      <div class="table2Mod" v-if="rimVdF"><!--Contenitore dove è possibile eliminare viaggi-->
        <h4>Rimuovi Viaggi Da Fare</h4>
        <div class="ricerca"><!--Sezione che permette la ricerca-->
          <h4>Vuoi ricercare il viaggio da modificare o rimuovere?</h4>
          <table>
            <tr><th>Titolo</th><input v-model="Ricerca.Titolo" type="text" placeholder="Titolo"></tr>
            <tr><th>Data</th><input v-model="Ricerca.Data" type="date" placeholder="Data"></tr>
            <tr><th>Luogo </th><input v-model="Ricerca.Luogo" type="text" placeholder="Luogo"></tr>
          </table>
        </div>
        <div class="conferma">
          <button v-if="btconferma" @click="ricercaVdF(Ricerca)">Conferma</button> |
          <button @click="stopMod">Vedi Tutti</button> |  
        </div>
        <hr>
        <div class="ricercaON" v-if="ricercaON"><!--contiene la lista dei viaggi da fare ricercati-->
          <table v-for="elementi in listaRicerca" :key="elementi.id">
            <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
            <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
            <tr><th>Attività</th><td>{{ elementi.Attivita }}</td></tr>
            <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
            <button class="cancella" @click="eliminaVdF(elementi)">Cancella</button>
            <hr>
          </table>
        </div>
        <div v-if="ricercaOFF"><!--contiene la lista di tutti i viaggi da fare presenti nel db-->
        <table v-for="elementi in listaViaggiDaFare" :key="elementi.id">
          <tr><th>Titolo</th><td>{{ elementi.Titolo }}</td></tr>
          <tr><th>Data</th><td>{{ elementi.Data }}</td></tr>
          <tr><th>Attivita'</th><td>{{ elementi.Attivita }}</td></tr>
          <tr><th>Luogo </th><td>{{ elementi.Luogo }}</td></tr>
          <button class="cancella" @click="eliminaVdF(elementi)">Cancella</button>
          <hr>
        </table>
        </div>
      </div>
      </TransitionGroup>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'Gestisci',
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
        Ricerca:{
          'Titolo': null,
          'Data': null,
          'Luogo': null,
        },
        listaRicerca: [],
        listaViaggiFatti: [],
        listaViaggiDaFare: [],
        modVF : false,
        rimVF : false,
        modVdF : false,
        rimVdF : false,
        ricercaModVF:true,
        modificaVF:false,
        ricercaModVdF:true,
        modificaVdF:false,
        ricercaON:false,
        ricercaOFF:true,
        btconferma: true,
        splitted: [],
      }
    },
    mounted(){
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
      togglemodVF(){/*permette di far comparire/scomparire determinati elementi dopo aver schiacciato il bottone*/
        this.Ricerca.Titolo = null;
        this.Ricerca.Data = null;
        this.Ricerca.Luogo = null;
        this.modVF=!this.modVF;
        this.rimVF=false;
        this.modVdF=false;
        this.rimVdF=false;
        this.ricercaOFF=true;
        this.ricercaON=false;
        this.listaRicerca=[];
        this.btconferma=true;
      },
      togglerimVF(){/*permette di far comparire/scomparire determinati elementi dopo aver schiacciato il bottone*/
        this.Ricerca.Titolo = null;
        this.Ricerca.Data = null;
        this.Ricerca.Luogo = null;
        this.rimVF=!this.rimVF;
        this.modVF=false;
        this.modVdF=false;
        this.rimVdF=false;
        this.ricercaOFF=true;
        this.ricercaON=false;
        this.listaRicerca=[];
        this.btconferma=true;
      },
      togglemodVdF(){/*permette di far comparire/scomparire determinati elementi dopo aver schiacciato il bottone*/
        this.Ricerca.Titolo = null;
        this.Ricerca.Data = null;
        this.Ricerca.Luogo = null;
        this.modVdF=!this.modVdF;
        this.rimVF=false;
        this.modVF=false;
        this.rimVdF=false;
        this.ricercaOFF=true;
        this.ricercaON=false;
        this.listaRicerca=[];
        this.btconferma=true;
      },
      togglerimVdF(){/*permette di far comparire/scomparire determinati elementi dopo aver schiacciato il bottone*/
        this.Ricerca.Titolo = null;
        this.Ricerca.Data = null;
        this.Ricerca.Luogo = null;
        this.rimVdF=!this.rimVdF;
        this.rimVF=false;
        this.modVdF=false;
        this.modVF=false;
        this.ricercaOFF=true;
        this.ricercaON=false;
        this.listaRicerca=[];
        this.btconferma=true;
      },
      abilitaModVF(element){/*abilita la modifica degli elementi*/
        this.ricercaModVF = false;
        this.modificaVF = true;
        this.ViaggiFatti = element;
      },
      abilitaModVdF(element){
        this.ricercaModVdF = false;
        this.modificaVdF = true;
        this.ViaggiDaFare = element;
      },
      stopMod(){/*esce dalla modalità ricerca*/
        this.Ricerca.Titolo = null;
        this.Ricerca.Data = null;
        this.Ricerca.Luogo = null;
        this.listaRicerca=[];
        this.ricercaON=false;
        this.ricercaModVF=true;
        this.ricercaModVdF=true;
        this.modificaVF=false;
        this.modificaVdF=false;
        this.ricercaOFF=true;
        this.btconferma=true;
      },
      async editVF(){/*permette modifica degli elementi del db*/
        axios
          .put(`/api/viaggi-fatti/${this.ViaggiFatti.id}/`, this.ViaggiFatti)
          .then(response =>{
            
            if(this.ricercaON!==false){
              this.refreshRicerca()
            }
            this.getViaggiFatti()
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
        
        this.ViaggiFatti = {};
        this.modificaVF = false;
        this.ricercaModVF = true;

      },
      async editVdF(){/*permette modifica degli elementi del db*/
        axios
          .put(`/api/viaggi-da-fare/${this.ViaggiDaFare.id}/`, this.ViaggiDaFare)
          .then(response =>{
            if(this.ricercaON!==false){
              this.refreshRicercaVdF()
            }
            this.getViaggiDaFare()
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      
        this.ViaggiDaFare = {};
        this.modificaVdF = false;
        this.ricercaModVdF = true;
      },
      async eliminaVF(element){/*permette di eliminare elementi dal db*/
        axios
          .delete(`/api/viaggi-fatti/${element.id}`)
          .then(response => {
            this.getViaggiFatti()
            if(this.ricercaON!==false){
              this.refreshRicerca()
            }
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      },
      async eliminaVdF(element){/*permette di eliminare elementi dal db*/
        axios
          .delete(`/api/viaggi-da-fare/${element.id}`)
          .then(response => {
            this.getViaggiDaFare()
            if(this.ricercaON!==false){
              this.refreshRicercaVdF()
            }
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })

      },
      async refreshRicerca(){/*refresh della lista ricerca, in modo da visualizzare la lista aggiornata dopo l'elimina*/
        await this.ricercaViaggio(this.Ricerca);
      },
      async refreshRicercaVdF(){
        await this.ricercaVdF(this.Ricerca);
      },
      /*Inizio Ricerca Viaggi Fatti*/
      async ricercaViaggio(element){/*permette di richiamare il corretto metodo per la ricerca*/
        if(element.Titolo !== null && element.Data === null && element.Luogo === null){
          this.ricercaTitolo(element);
        }else if(element.Titolo === null && element.Data !== null && element.Luogo === null){
          this.ricercaData(element);
        }else if(element.Titolo === null && element.Data === null && element.Luogo !== null){
          this.ricercaLuogo(element);
        }else{
          this.ricercaCompleta(element);
        }
        this.ricercaON=true;
        this.ricercaOFF=false;
        this.btconferma=false;
      },
      async ricercaTitolo(element){/*ricerca per titolo*/
        axios
          .get(`/api/viaggi-fatti/titolo/?search=${element.Titolo}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      async ricercaData(element){/*ricerca per data*/
        axios
          .get(`/api/viaggi-fatti/data/?search=${element.Data}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      async ricercaLuogo(element){/*ricerca per luogo*/
        axios
          .get(`/api/viaggi-fatti/luogo/?search=${element.Luogo}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      async ricercaCompleta(element){/*ricerca completa*/
        var elemento = '';
        if(element.Titolo === null){
           elemento = element.Data + '+' + element.Luogo;
        }else if(element.Data === null){
           elemento = element.Titolo + '+' + element.Luogo;
        }else if(element.Luogo === null){
           elemento = element.Titolo + '+' + element.Data;
        }else{
           elemento = element.Titolo + '+' + element.Data + '+' + element.Luogo;
        }
        axios
          .get(`/api/viaggi-fatti/?search=${elemento}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      /*Fine Ricerca Viaggi Fatti*/
  
      /*Inizio Ricerca Viaggi Da Fare*/
      async ricercaVdF(element){
        if(element.Titolo !== null && element.Data === null && element.Luogo === null){
          this.ricercaTitoloVdF(element);
        }else if(element.Titolo === null && element.Data !== null && element.Luogo === null){
          this.ricercaDataVdF(element);
        }else if(element.Titolo === null && element.Data === null && element.Luogo !== null){
          this.ricercaLuogoVdF(element);
        }else{
          this.ricercaCompletaVdF(element);
        }
        this.ricercaON=true;
        this.ricercaOFF=false;
        this.btconferma=false;
      },
      async ricercaTitoloVdF(element){
        axios
          .get(`/api/viaggi-da-fare/titolo/?search=${element.Titolo}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      async ricercaDataVdF(element){
        axios
          .get(`/api/viaggi-da-fare/data/?search=${element.Data}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      async ricercaLuogoVdF(element){
        axios
          .get(`/api/viaggi-da-fare/luogo/?search=${element.Luogo}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      async ricercaCompletaVdF(element){
        var elemento = '';
        if(element.Titolo === null){
           elemento = element.Data + '+' + element.Luogo;
        }else if(element.Data === null){
           elemento = element.Titolo + '+' + element.Luogo;
        }else if(element.Luogo === null){
           elemento = element.Titolo + '+' + element.Data;
        }else{
           elemento = element.Titolo + '+' + element.Data + '+' + element.Luogo;
        }
        axios
          .get(`/api/viaggi-da-fare/?search=${elemento}`)
          .then(response =>{
            this.listaRicerca = response.data
            console.log(response)
          })
          .catch(error =>{
            console.log(error)
          })
      },
      /*Fine Ricerca Viaggi Da Fare*/
    }
  }
  </script>
  
  <style>
  
  /*transizioni*/
  
  .comparsa-enter-from{
    opacity: 0;
  }
  .comparsa-enter-to{
    opacity: 1;
  }
  .comparsa-enter-active{
    transition: all 0.5s ease;
  }
  .comparsa-leave-from{
    opacity: 1;
  }
  .comparsa-leave-to{
    opacity: 0;
  }
  .comparsa-leave-active{
    transition: all 0.5s ease;
  }
  .mod1-enter-from{
    opacity: 0;
    transform: translateX(-100px);
  }
  .mod1-enter-to{
    opacity: 1;
    transform: translateX(auto);
  }
  .mod1-enter-active{
    transition: all 0.35s ease-in;
  }
  .mod2-enter-from{
    opacity: 0;
    transform: translateY(100px);
  }
  .mod2-enter-to{
    opacity: 1;
    transform: translateY(auto);
  }
  .mod2-enter-active{
    transition: all 0.4s ease-in;
  }
  .rim1-enter-from{
    opacity: 0;
    transform: translateY(-100px);
  }
  .rim1-enter-to{
    opacity: 1;
    transform: translateY(auto);
  }
  .rim1-enter-active{
    transition: all 0.45s ease-in;
  }
  .rim2-enter-from{
    opacity: 0;
    transform: translateX(100px);
  }
  .rim2-enter-to{
    opacity: 1;
    transform: translateX(auto);
  }
  .rim2-enter-active{
    transition: all 0.5s ease-in;
  }
  
    /*Css*/
    .divModifica{
      text-align: center;
    }
    .divModifica button{
      background-color:rgb(172, 104, 236);
      color: white;
      border: solid 1px rgb(120, 38, 197);
      border-radius: 5px;
      cursor: pointer;
    }
    table hr{
      align-items: center;
      margin-left: 50%;
    }
    .conferma{
      margin-top: 15%;
      margin:auto;
      text-align: center;
    }
    .conferma button{
      background-color:rgb(172, 104, 236);
      color: white;
      border: solid 1px rgb(120, 38, 197);
      border-radius: 5px;
      cursor: pointer;
    }
    .row{
      border-radius: 20px;
      border: solid 2px;
      background-color:#f5f5f5;
      margin-bottom: 0.5%;
      width:90%;
      margin: auto;
    }
    .btModifica1{
      color: black;
      border: blueviolet solid 2px;
      border-radius: 10px;
      background-color: lavender;
      cursor: pointer;
    }
    .btModifica2{
      color: black;
      border: blueviolet solid 2px;
      border-radius: 10px;
      background-color:lightcyan;
      cursor: pointer;
    }
    img{
      width: 70%;
    }
    .btRimuovi1{
      color: black;
      border: blueviolet solid 2px;
      border-radius: 10px;
      background-color:  lavender;
      cursor: pointer;
    }
    .btRimuovi2{
      color: black;
      border: blueviolet solid 2px;
      border-radius: 10px;
      background-color: lightcyan;
      cursor: pointer;
    }
    .table1Mod{
      text-align: left;
      width: 65%;
      margin: auto;
      border: solid 1px;
      border-radius: 40px;
      background-color:lavender;
    }
    .table1Mod hr{
      width: 80%;
    }
    .table1Mod table{
      margin-left: 25%;
    }
    .table2Mod table{
      margin-left: 25%;
    }
    .cancella{
      color:tomato;
      border: solid 1px rgb(201, 1, 1);
      background-color: white;
      border-radius: 5px;
      cursor: pointer;
    }
    .modifica{
      color:deeppink;
      border: solid 1px midnightblue;
      background-color: white;
      border-radius: 5px;
      cursor: pointer;
    }
    .table2Mod{ 
      text-align: left;
      width: 65%;
      margin: auto;
      border: solid 1px;
      border-radius: 40px;
      background-color: lightcyan;
    }
    .table2Mod hr{
      width: 80%;
    }
    .ricerca table{
      margin-top: 2%;
      margin-bottom: 2%;
      margin: auto;
      align-items: center;
    }
    .divModifica table{
      margin: auto;
      margin-bottom: 2%;
    }
    @media only screen and (max-width: 1000px){
    .table1Mod{
      margin: auto;
      float: none;
      width: 85%;
      margin-bottom: 3%;
    }
    .table2Mod{
      margin: auto;
      float: none;
      width: 85%;
    }
  
  }
  </style>