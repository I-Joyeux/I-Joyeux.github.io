<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  getAvailableColors: {
    type: Function,
    required: true,
  },
  clothingTypes: {
    type: Array,
    required: true,
  },
});

const emit = defineEmits(['add-item']);

const newItem = ref({
  type: 'Coat',
  size: 'M',
  color: '',
});

const sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL'];
const availableColors = ref([]);
const showWarning = ref(false);

const updateAvailableColors = () => {
  availableColors.value = props.getAvailableColors(
    newItem.value.type,
    newItem.value.size
  );
  if (
    availableColors.value.length > 0 &&
    !availableColors.value.includes(newItem.value.color)
  ) {
    newItem.value.color = availableColors.value[0];
  }
  showWarning.value = false;
};

watch(() => newItem.value.type, updateAvailableColors);
watch(() => newItem.value.size, updateAvailableColors, { immediate: true });

const addItem = () => {
  if (
    newItem.value.color &&
    availableColors.value.includes(newItem.value.color)
  ) {
    const success = emit('add-item', {
      id: Date.now(),
      type: newItem.value.type,
      size: newItem.value.size,
      color: newItem.value.color,
    });

    if (!success) {
      showWarning.value = true;
    }
  }
};
</script>

<template>
  <div class="card shadow-sm mb-4">
    <div class="card-header bg-white">
      <h3 class="h5 mb-0">Add New Item</h3>
    </div>

    <div class="card-body">
      <div v-if="showWarning" class="alert alert-warning" role="alert">
        This item already exists in the inventory! Check the highlighted item
        above.
      </div>

      <form @submit.prevent="addItem">
        <div class="row g-3">
          <div class="col-md-4">
            <label for="type" class="form-label">Type:</label>
            <select id="type" v-model="newItem.type" class="form-select">
              <option v-for="type in clothingTypes" :key="type" :value="type">
                {{ type }}
              </option>
            </select>
          </div>

          <div class="col-md-4">
            <label for="size" class="form-label">Size:</label>
            <select id="size" v-model="newItem.size" class="form-select">
              <option v-for="size in sizes" :key="size" :value="size">
                {{ size }}
              </option>
            </select>
          </div>

          <div class="col-md-4">
            <label for="color" class="form-label">Color:</label>
            <select
              id="color"
              v-model="newItem.color"
              class="form-select"
              :disabled="!availableColors.length"
            >
              <option
                v-for="color in availableColors"
                :key="color"
                :value="color"
              >
                {{ color }}
              </option>
            </select>
          </div>
        </div>

        <button
          type="submit"
          class="btn btn-success w-100 mt-4"
          :disabled="!availableColors.length"
        >
          {{ availableColors.length ? 'Add Item' : 'No Colors Available' }}
        </button>
      </form>
    </div>
  </div>
</template>
