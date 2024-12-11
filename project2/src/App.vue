<script setup>
import Footer from './components/Footer.vue';
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-success">
    <div class="container">
      <span class="navbar-brand">Clothing Store</span>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link" active-class="active"
              >Home</router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="/inventory" class="nav-link" active-class="active"
              >Inventory</router-link
            >
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link">About</a>
          </li>
          <li class="nav-item">
            <router-link to="/inventory" class="nav-link" active-class="active"
              >Inventory</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <main class="flex-grow-1">
    <router-view></router-view>
  </main>

  <Footer />
</template>

<style>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
