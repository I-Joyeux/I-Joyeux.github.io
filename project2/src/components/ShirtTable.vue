<script setup>
import { ref, computed } from 'vue';
import AddShirtForm from './AddShirtForm.vue';

const shirts = ref([
  { id: 1, size: 'XS', color: 'Red' },
  { id: 2, size: 'XS', color: 'Orange' },
  { id: 3, size: 'XS', color: 'Yellow' },
  { id: 4, size: 'XS', color: 'Green' },
  { id: 5, size: 'XS', color: 'Blue' },
  { id: 6, size: 'XS', color: 'Indigo' },
  { id: 7, size: 'XS', color: 'Violet' },
  { id: 8, size: 'S', color: 'Red' },
  { id: 9, size: 'S', color: 'Orange' },
  { id: 10, size: 'S', color: 'Yellow' },
  { id: 11, size: 'S', color: 'Green' },
  { id: 12, size: 'S', color: 'Blue' },
  { id: 13, size: 'S', color: 'Indigo' },
  { id: 14, size: 'S', color: 'Violet' },
  { id: 15, size: 'M', color: 'Red' },
  { id: 16, size: 'M', color: 'Orange' },
  { id: 17, size: 'M', color: 'Yellow' },
  { id: 18, size: 'M', color: 'Green' },
  { id: 19, size: 'M', color: 'Blue' },
  { id: 20, size: 'M', color: 'Indigo' },
  { id: 21, size: 'M', color: 'Violet' },
  { id: 22, size: 'L', color: 'Red' },
  { id: 23, size: 'L', color: 'Orange' },
  { id: 24, size: 'L', color: 'Yellow' },
  { id: 25, size: 'L', color: 'Green' },
  { id: 26, size: 'L', color: 'Blue' },
  { id: 27, size: 'L', color: 'Indigo' },
  { id: 28, size: 'L', color: 'Violet' },
]);

const removeShirt = (id) => {
  shirts.value = shirts.value.filter(shirt => shirt.id !== id);
};

const addShirt = (newShirt) => {
  const exists = shirts.value.some(
    shirt => shirt.size === newShirt.size && shirt.color === newShirt.color
  );
  
  if (!exists) {
    shirts.value.push(newShirt);
    return true;
  }
  return false;
};

const availableColors = computed(() => {
  const allColors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'];
  return (size) => {
    const usedColors = shirts.value
      .filter(shirt => shirt.size === size)
      .map(shirt => shirt.color);
    return allColors.filter(color => !usedColors.includes(color));
  };
});
</script>

<template>
  <div class="shirt-inventory">
    <AddShirtForm 
      @add-shirt="addShirt" 
      :getAvailableColors="availableColors"
    />
    
    <div class="shirt-table">
      <h2>Shirt Inventory</h2>
      <table>
        <thead>
          <tr>
            <th>Size</th>
            <th>Color</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="shirt in shirts" :key="shirt.id">
            <td>{{ shirt.size }}</td>
            <td>
              <span class="color-dot" :style="{ backgroundColor: shirt.color.toLowerCase() }"></span>
              {{ shirt.color }}
            </td>
            <td>
              <button class="remove-button" @click="removeShirt(shirt.id)">Remove</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.shirt-inventory {
  max-width: 600px;
  margin: 0 auto;
}

.shirt-table {
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #eee;
}

th {
  background-color: #f4f4f4;
  font-weight: 600;
}

.remove-button {
  background-color: #ff4444;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.remove-button:hover {
  background-color: #ff2222;
}

.color-dot {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  margin-right: 8px;
}

h2 {
  margin: 0;
  padding: 1rem;
  background-color: #f4f4f4;
  border-bottom: 1px solid #eee;
}
</style>