<script setup>
const currentYear = new Date().getFullYear();
</script>

<template>
  <footer class="footer bg-dark text-white py-5 mt-auto">
    <div class="container">
      <div class="row">
        <div class="col-md-4 mb-4 mb-md-0">
          <h5 class="text-success mb-3">About Us</h5>
          <p class="text-light">
            Managing your clothing inventory with style and efficiency.
          </p>
        </div>
        <div class="col-md-4 mb-4 mb-md-0">
          <h5 class="text-success mb-3">Quick Links</h5>
          <ul class="list-unstyled">
            <li class="mb-2">
              <router-link
                to="/"
                class="text-light text-decoration-none hover-success"
                >Home</router-link
              >
            </li>
            <li class="mb-2">
              <router-link
                to="/inventory"
                class="text-light text-decoration-none hover-success"
                >Inventory</router-link
              >
            </li>
            <li class="mb-2">
              <a href="#" class="text-light text-decoration-none hover-success"
                >About</a
              >
            </li>
            <li class="mb-2">
              <a href="#" class="text-light text-decoration-none hover-success"
                >Contact</a
              >
            </li>
          </ul>
        </div>
        <div class="col-md-4">
          <h5 class="text-success mb-3">Contact</h5>
          <ul class="list-unstyled">
            <li class="mb-2">
              <i class="bi bi-envelope me-2"></i>
              Email: wontwork@fakestore.com
            </li>
            <li class="mb-2">
              <i class="bi bi-telephone me-2"></i>
              Phone: (208) 208-2082
            </li>
            <li class="mb-2">
              <i class="bi bi-geo-alt me-2"></i>
              Address: 888 nowhere St
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="border-top border-secondary mt-4 pt-4">
      <div class="container">
        <p class="text-center text-light-50 m-0">
          &copy; {{ currentYear }} fake Clothing Store. All rights reserved?.
        </p>
      </div>
    </div>
  </footer>
</template>
