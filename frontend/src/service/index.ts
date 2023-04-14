import axios from 'axios'

const baseUrl = 'http://localhost:8080/api'

const instance = axios.create({
    baseURL: baseUrl,
})

// interceptor to add / to the end of all requests
instance.interceptors.request.use((config) => {
    if (!config.url?.endsWith('/')) {
        config.url += '/'
    }
    return config
  })

export default instance