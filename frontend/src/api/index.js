import axios from 'axios'

const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type':'application/json'}
/* Board */
export const postDetail = body => axios.post(`${SERVER}post/detail`,{headers, body})
export const postDelete = body => axios.post(`${SERVER}post/delete`,{headers, body})
export const postList = body => axios.post(`${SERVER}post/list`,{headers, body})
export const postModify = body => axios.post(`${SERVER}post/modify`,{headers, body})
export const postRegister = body => axios.post(`${SERVER}post/register`,{headers, body})
export const postRetrieve = body => axios.post(`${SERVER}post/retrieve`,{headers, body})
/* Common */
/* 공통은 네이밍 컨벤션에서 벗어남 */
/* Item */
export const itemDetail = body => axios.post(`${SERVER}item/detail`,{headers, body})
export const itemDelete = body => axios.post(`${SERVER}item/delete`,{headers, body})
export const itemList = body => axios.post(`${SERVER}item/list`,{headers, body})
export const itemModify = body => axios.post(`${SERVER}item/modify`,{headers, body})
export const itemRegister = body => axios.post(`${SERVER}item/register`,{headers, body})
export const itemRetrieve = body => axios.post(`${SERVER}item/retrieve`,{headers, body})
/* Member */
export const memberDetail = body => axios.post(`${SERVER}member/detail`,{headers, body})
export const memberDelete = body => axios.delete(`${SERVER}member/delete`,{headers, body})
export const memberList = () => axios.get(`${SERVER}member/list`)
export const memberModify = body => axios.post(`${SERVER}member/modify`,{headers, body})
export const memberRegister = body => axios.post(`${SERVER}member/register`,{headers, body})
export const memberRetrieve = body => axios.post(`${SERVER}member/retrieve`,{headers, body})
export const memberLogin = body => axios.post(`${SERVER}member/login`,{headers, body})