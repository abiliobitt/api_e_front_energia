import axios from 'axios'


export const getApiData = (URL) => {
    return axios.get(`http://localhost:8000/${URL}`)
    .then(response => {
        return response
    })
    .catch(error => {
        return error
    })
}