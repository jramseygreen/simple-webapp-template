<template>
  home page

  <div>
    <p v-for="(user, index) in users" :key="index">{{user.id}} - {{user.username}}</p>
  </div>

  <div class="flex space-x-5">
    <cc-button label="Fetch" icon="fa fa-arrow-right" @click="fetchUsers" />
    <div class="flex">
      <text-input label="add user" icon="fa fa-user-plus" v-model="state.userText"/>
      <cc-button label="Add" @click="submitUser"/>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed, reactive } from 'vue'
  import type { User } from '@/types/User'
  import { useStore } from '@/store'
  import CcButton from '@/components/Button.vue'
  import TextInput from '@/components/TextInput.vue'

  const store = useStore()

  const state = reactive({
    userText: ''
  })

  const users = computed((): User[] => store.getters['users/userGetter'])

  const fetchUsers = () => {
    store.dispatch('users/fetchUsers').then((response) => {
      console.log(response)
    })
  }

  const submitUser = () => {
    store.dispatch('users/submitUser', {
      username: state.userText
    }).then(() => state.userText = '')
  }

</script>