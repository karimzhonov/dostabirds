import {createStore} from 'vuex'
import jwt from './jwt'
import users from './user'

export default createStore({
    state: {
        host: 'localhost:8000',
    },
    getters: {},
    mutations: {},
    actions: {
        ...jwt.actions,
        ...users.actions,
    }
})
