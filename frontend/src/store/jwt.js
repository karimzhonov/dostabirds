import axios from "axios";

export default {
    actions: {
        async get_jwt(context) {
            if (localStorage.getItem('access_token')) {
                try {
                    await axios.get(`http://${context.state.host}/auth/users/me/`, {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('access_token')}`
                        }
                    })
                    return localStorage.getItem('access_token')
                } catch (e) {
                    console.log(e)
                    try {
                        let response = await axios.post(`http://${context.state.host}/auth/jwt/refresh/`, {
                            refresh: `${localStorage.getItem('refresh_token')}`
                        })
                        localStorage.setItem('access_token', response.data.access)
                        return response.data.access
                    } catch (e) {
                        console.log(e)
                        return null
                    }
                }
            }
        },
        async set_jwt(context, data) {
            try {
                let response = await axios.post(`http://${context.state.host}/auth/jwt/create/`, {
                    username: data.username,
                    password: data.password
                })
                localStorage.setItem('access_token', response.data.access)
                localStorage.setItem('refresh_token', response.data.refresh)
            } catch (e) {
                console.log(e)
                return e.response.data
            }
        },
    }
}