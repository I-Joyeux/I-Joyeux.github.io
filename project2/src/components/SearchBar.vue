<script setup>
import { ref } from 'vue';

const emit = defineEmits(['search']);
const searchQuery = ref('');

const handleSearch = () => {
  emit('search', searchQuery.value);
};
</script>

<template>
  <div class="mb-4">
    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search by item number (e.g., 1001)"
      @input="handleSearch"
      pattern="\d*"
      maxlength="4"
      class="form-control form-control-lg"
    />
  </div>
</template>
