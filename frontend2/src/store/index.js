
import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    isAuthenticated: false
  },
  mutations: {
    initializeStore(state) {//inizializzazione Store e se nel local storage è già presente un token lo assegna
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }else{
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token){//metodo per settare il token
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){//metodo per rimuovere il token
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
