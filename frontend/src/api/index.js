import axios from 'axios'

const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type':'application/json'}

export const userSignUp = body => axios.post(`${SERVER}member/signup`, {headers, body})
export const userLogin = body => axios.post(`${SERVER}member/login`, {headers, body})
export const userPostwrite = body => axios.post(`${SERVER}boards/postwrite`, {headers, body})