import axios from '@/service'

export default {
    fetchUsers: async () => {
        return await axios.get('/users')
    },
    submitUser: async (payload: any) => {
        return await axios.post('/users', payload)
    }
}