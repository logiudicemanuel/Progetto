<template>
  <div class="titolo">
    <h1><i>Viaggi ToDo</i></h1> 
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/gestisci">Gestisci</router-link>
    </nav>
  </div>
  <router-view v-slot="{ Component }">
    <transition name="route" mode="out-in">
      <component :is="Component"></component>
    </transition>
  </router-view>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.titolo{
  font-weight: bold;
  margin-top: -1%;  
  width: 100%;  
} 
.titolo nav{

  margin-top: -1%;
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: white;
  background-color: rgb(172, 104, 236);
  border: #2c3e50 solid 1px;
  border-radius: 5px;
}

/*route transition*/
.route-enter-from{
  opacity: 0;
  transform: translateX(100px);
}
.route-enter-active{
  transition: all 0.3s ease-out;
}
.route-leave-to{
  opacity: 0;
  transform: translateX(-100px);
}
.route-leave-from{
  transition: all 0.3s ease-in;
}
</style>
