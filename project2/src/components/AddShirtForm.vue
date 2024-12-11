<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  getAvailableColors: {
    type: Function,
    required: true,
  },
});

const emit = defineEmits(['add-shirt']);

const newShirt = ref({
  size: 'XS',
  color: '',
});

const sizes = ['XS', 'S', 'M', 'L'];
const availableColors = ref([]);

const updateAvailableColors = () => {
  availableColors.value = props.getAvailableColors(newShirt.value.size);
  if (
    availableColors.value.length > 0 &&
    !availableColors.value.includes(newShirt.value.color)
  ) {
    newShirt.value.color = availableColors.value[0];
  }
};

watch(() => newShirt.value.size, updateAvailableColors, { immediate: true });

const addShirt = () => {
  if (
    newShirt.value.color &&
    availableColors.value.includes(newShirt.value.color)
  ) {
    const success = emit('add-shirt', {
      id: Date.now(),
      size: newShirt.value.size,
      color: newShirt.value.color,
    });

    if (success) {
      updateAvailableColors();
    }
  }
};
</script>

<template>
  <div class="add-shirt-form">
    <h3>Add New Shirt</h3>
    <form @submit.prevent="addShirt">
      <div class="form-group">
        <label for="size">Size:</label>
        <select id="size" v-model="newShirt.size">
          <option v-for="size in sizes" :key="size" :value="size">
            {{ size }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="color">Color:</label>
        <select
          id="color"
          v-model="newShirt.color"
          :disabled="!availableColors.length"
        >
          <option v-for="color in availableColors" :key="color" :value="color">
            {{ color }}
          </option>
        </select>
      </div>

      <button
        type="submit"
        class="add-button"
        :disabled="!availableColors.length"
      >
        {{ availableColors.length ? 'Add Shirt' : 'No Colors Available' }}
      </button>
    </form>
  </div>
</template>

