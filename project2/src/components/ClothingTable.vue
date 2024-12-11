<script setup>
import { ref, computed } from 'vue';
import SearchBar from './SearchBar.vue';
import AddClothingForm from './AddClothingForm.vue';

const nextItemNumber = ref(1001);

const clothing = ref([
  { id: 1, itemNumber: '1001', type: 'Shirt', size: 'XS', color: 'Red' },
  { id: 2, itemNumber: '1002', type: 'Coat', size: 'M', color: 'Blue' },
  { id: 3, itemNumber: '1003', type: 'Pants', size: 'L', color: 'Black' },
  { id: 4, itemNumber: '1004', type: 'Jacket', size: 'S', color: 'Green' },
  { id: 5, itemNumber: '1005', type: 'Sweater', size: 'XS', color: 'Purple' },
]);

const searchQuery = ref('');

const filteredClothing = computed(() => {
  if (!searchQuery.value) return clothing.value;
  return clothing.value.filter(item => 
    item.itemNumber.includes(searchQuery.value)
  );
});

const removeItem = (id) => {
  clothing.value = clothing.value.filter(item => item.id !== id);
};

const findExistingItem = (type, size, color) => {
  return clothing.value.find(item => 
    item.type === type && 
    item.size === size && 
    item.color === color
  );
};

const addItem = (newItem) => {
  const existingItem = findExistingItem(newItem.type, newItem.size, newItem.color);
  
  if (existingItem) {
    searchQuery.value = existingItem.itemNumber;
    return false;
  }

  const itemWithNumber = {
    ...newItem,
    itemNumber: nextItemNumber.value.toString()
  };
  
  clothing.value.push(itemWithNumber);
  nextItemNumber.value++;
  return true;
};

const handleSearch = (query) => {
  searchQuery.value = query;
};

const availableColors = computed(() => {
  const allColors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'Black', 'White', 'Purple', 'Brown', 'Gray'];
  return (type, size) => {
    const usedColors = clothing.value
      .filter(item => item.type === type && item.size === size)
      .map(item => item.color);
    return allColors.filter(color => !usedColors.includes(color));
  };
});

const clothingTypes = [
  'Shirt',
  'Coat',
  'Pants',
  'Jacket',
  'Sweater',
  'Dress',
  'Skirt',
  'Hoodie',
  'Vest'
];
</script>

<template>
  <div class="clothing-inventory">
    <AddClothingForm 
      @add-item="addItem" 
      :getAvailableColors="availableColors"
      :clothingTypes="clothingTypes"
    />
    
    <div class="card shadow-sm">
      <div class="card-header bg-white">
        <h2 class="h5 mb-0">Clothing Inventory</h2>
      </div>
      
      <div class="card-body">
        <SearchBar @search="handleSearch" />
        
        <div class="table-responsive">
          <table class="table table-hover">
            <thead class="table-light">
              <tr>
                <th>Item #</th>
                <th>Type</th>
                <th>Size</th>
                <th>Color</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in filteredClothing" :key="item.id">
                <td>{{ item.itemNumber }}</td>
                <td>{{ item.type }}</td>
                <td>{{ item.size }}</td>
                <td>
                  <span class="badge rounded-pill" :style="{ backgroundColor: item.color.toLowerCase() }">
                    &nbsp;
                  </span>
                  {{ item.color }}
                </td>
                <td>
                  <button class="btn btn-danger btn-sm" @click="removeItem(item.id)">
                    Remove
                  </button>
                </td>
              </tr>
              <tr v-if="filteredClothing.length === 0">
                <td colspan="5" class="text-center text-muted fst-italic">
                  No items found
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>