import axios from "axios";

export default {
    actions: {
        async get_me(context, jwt_token) {
            try {
                let response = await axios.get(`http://${context.state.host}/auth/users/me/`, {
                    headers: {
                        Authorization: `Bearer ${jwt_token}`
                    }
                })
                return response.data
            } catch (e) {
                return null
            }
        }
    }
}