<template>
    <div class="sign-up">
        <h1><i>Viaggi ToDo</i></h1>
        <hr>
        <div class="intro">
            <p>Qui potrai tenere traccia di tutti i tuoi viaggi! Passati, presenti e futuri. <br>
            Potrai inoltre programmare tutte le attività che ti piacerebbe fare, descrivere le esperienze che hai vissuto oppure esprimere tutte le tue considerazioni personali sul viaggio.<br>
            <br>
            <h4><i>Accedi o registrati qui sotto!</i></h4>
            </p>
        </div>
        <div class="form">
            <div class="login">
                <div class="elementi2" v-if="!accedi">
                    <h2>Hai già un account? Accedi</h2>
                    <p>Accedi al tuo account per gestire tutti i tuoi viaggi</p>
                    <br>
                    <button type="submit" @click="accediAccount">Accedi</button>
                </div>
                <div class="elementi3" v-if="accedi"><!--form di login, richiamando il metodo submitLogin permette l'accesso autenticato al sito-->
                    <form @submit.prevent="submitLogin">
                        <h2>Accedi!</h2>
                        <p>Username: </p>
                        <input type="username" name="username" v-model="username">
                        <p>Password: </p>
                        <input type="password" name="password" v-model="password"><br>
                        <br>
                        <button type="submit">Accedi</button>
                    </form>
                    <div class="regCompleta" v-if="conferma">
                        <br>
                        <p>Registrazione completata con successo!</p>
                    </div>
                    <div class="errori" v-if="errori.length">
                        <br>
                        <p v-for="errore in errori" v-bind:key="errore">{{ errore }}</p>
                    </div>
                </div>  
            </div>
            <div class="registrati">
                <div class="elementi1" v-if="!crea">
                    <h2>Sei Nuovo? Registrati</h2>
                    <p>Crea un account e tieni traccia di tutti i tuoi viaggi</p>
                    <br>
                    <button type="submit" @click="creaAccount">Registrati</button>
                </div>
                <div class="elementi4" v-if="crea"><!--form di registrazione, permette di registrarti associando un token specifico all'account per effettuare poi l'accesso autenticato-->
                    <form @submit.prevent="submitRegistrazione">
                        <h2>Crea il tuo account!</h2>
                        <p>Username: </p>
                        <input type="username" name="username" v-model="username">
                        <p>Password: </p>
                        <input type="password" name="password" v-model="password"><br>
                        <br>
                        <button type="submit">Registrati</button>
                    </form>
                    <div class="errori" v-if="errori.length">
                        <br>
                        <p v-for="errore in errori" v-bind:key="errore">{{ errore }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name : 'SignUp',
    data(){
        return {
            username: '',
            password: '',
            crea:false,
            accedi:true,
            errori: [],
            conferma: false
        }
    },
    methods:{
        submitRegistrazione(e){//metodo di registrazione
            //controllo dei campi inseriti nel form
            this.errori = []
            if(this.username === ''){
                this.errori.push('Username mancante!')
            }
            if(this.password.length<9){
                this.errori.push('Password troppo corta!(minimo 9 caratteri)')
            }
            
                const formData = {
                    username : this.username,
                    password : this.password,
                }
            //chiamata al backend per la registrazione
            axios
                .post('/api/v1/users/', formData)
                .then(response => {
                    this.crea = false
                    this.accedi = true
                    this.conferma = true
                    console.log(response)
                })
                .catch(error => {
                    this.conferma = false
                    if(this.errori.length === 0){
                        this.errori.push('Username già in uso!')
                    }
                    console.log(error)
                })
        },
        submitLogin(e){//metodo login
            this.errori = []

            const formData = {
                username : this.username,
                password : this.password,
            }
            //chiamata al backend per la Login autenticata
            axios
                .post('/api/v1/token/login', formData)
                .then(response => {
                    console.log(response)
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization']= "Token " + token
                    localStorage.setItem("token", token)
                    this.$router.push('/home')
                })
                .catch(error =>{
                    this.conferma = false
                    this.errori.push('Username o password errati!')
                    console.log(error)
                })
        },
        creaAccount(){
            this.errori = []
            this.crea = true
            this.accedi = false
        },
        accediAccount(){
            this.errori = []
            this.crea = false
            this.accedi = true
        }
    }
}
</script>

<style>
.regCompleta{
    color: green;
}
.errori{
    color: red;
}
.intro{
    margin-top: 10%;
    width: 70%;
    margin: auto;
    margin-bottom: 3%;
}
.elementi1 button,
.elementi4 button{
    background-color: lightcyan;
    border-color: white;
}
.elementi2 button,
.elementi3 button{
    background-color: lavender; 
    border-color: white;
}

.elementi1,
.elementi2{
    margin-top: 14%;
    margin-bottom: 13.5%;
    font-style: italic;
}
.elementi1 p,
.elementi2 p,
.elementi3 p,
.elementi4 p{
    margin: auto;
    width: 55%;
}

.elementi3,
.elementi4{
    margin-top: 10%;
    margin-bottom: 10%;
}

.form button{
    border-radius: 10px;
    width: 80px; 
    height: 30px; 
    border: 1px solid black;
    color: black;
    cursor: pointer;
}

.form{
    width: 60%;
    margin:auto;
}

.registrati{
    border: 1px transparent;
    border-radius : 20px;
    width: 50%;
    height: 100%;
    margin: auto;
    float: right;
    background-color: lightcyan;
    
}
.login{
    border: 1px transparent;
    border-radius : 20px;
    width: 49.99%;
    height: 100%;
    margin: auto;
    float: left;
    background-color: lavender; 
}
@media only screen and (max-width: 1000px){
.registrati{
    border: 2px solid black;
    border-radius : 20px;
    width: 70%;
    margin: auto;
    float: none;
    background-color: lightcyan;
    
}
.login{
    border: 2px solid black;
    border-radius : 20px;
    width: 70%;
    margin: auto;
    float: none;
    background-color: lavender; 
}
.form{
    width: 80%;
}
}
</style>