import type { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore, Store } from 'vuex'

// store module imports
import { users } from './modules/Users'


// define injection key
export const key: InjectionKey<Store<any>> = Symbol()

export const store = createStore<any>({
  modules: {
    // define all imported store modules here
    users,
  },
  strict: true,
  plugins: []
})

export function useStore () {
  return baseUseStore(key)
}