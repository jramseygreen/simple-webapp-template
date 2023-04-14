import type { ActionTree, GetterTree, MutationTree } from 'vuex'
import type { User, UserPayload } from '@/types/User'
import usersService from '@/service/modules/Users'

interface State {
  users: User[];
}

const state: State = {
  users: [
    {
      id: 12345,
      username: 'test'
    }
  ],
}

const getters: GetterTree<State, any> = {
  userGetter: (state: State) => {
    return state.users;
  }
}

const actions: ActionTree<State, any> = {
  fetchUsers: async (context) => {
    const response = await usersService.fetchUsers()
    context.commit('setUsers', response.data)
    return response
  },
  submitUser: async (context, payload: UserPayload) => {
    usersService.submitUser(payload).then((response) => {
      context.commit('addUser', response.data)
    })
  }
}


const mutations: MutationTree<State> = {
  setUsers: (state: State, users: User[]) => {
    state.users = users
  },
  addUser: (state: State, user: User) => {
    state.users.push(user)
  }
}

export const users = {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};
