<template>
  <div class="flex flex-col">
    <label class="font-bold text-gray-800">{{ label }}</label>
    <div class="relative">
      <input
        v-model="state.value"
        :type="type"
        class="px-4 py-2 w-full border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        @input="updateValue"
      />
      <div v-if="icon" class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
        <i :class="icon" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, reactive, watch } from 'vue';

const props = defineProps({
  label: {
    type: String,
    required: false,
    default: ''
  },
  modelValue: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: false,
    default: 'text',
  },
  icon: {
      type: String,
      required: false
  }
});

const state = reactive({
    value: ''
})

watch(() => props.modelValue, () => state.value = props.modelValue)

const emits = defineEmits(['update:modelValue']);

const updateValue = () => {
    emits('update:modelValue', state.value)
}
</script>