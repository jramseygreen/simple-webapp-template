<template>
  <button
    class="flex items-center justify-center gap-2 px-4 py-2 rounded-md text-white"
    :class="`${colourClasses}`"
    :disabled="disabled"
  >
    <i v-if="icon" :class="icon" />
    <span>{{ label }}</span>
  </button>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
    label: {
      type: String,
      required: true,
    },
    colour: {
      type: String,
      default: 'indigo',
      required: false,
      validator: (value: string) =>
        ['indigo', 'red', 'yellow', 'green'].includes(value),
    },
    disabled: {
      type: Boolean,
      required: false,
      default: false,
    },
    icon: {
      type: String,
      required: false
    },
  })

const colourClasses = computed(() => `bg-${props.colour}-500 hover:bg-${props.colour}-600`)
</script>