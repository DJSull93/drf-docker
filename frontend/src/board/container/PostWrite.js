import React,{useState} from 'react'
import './PostWrite.css'
import { userPostwrite } from 'api/index.js'
//import { useHistory } from 'react-router'
//import { Button } from '@material-ui/core';
const PostWrite = () => {
    const [postInfo, setPostInfo] = useState({
        title: '',
        content: '',
      })
        
    const {title, content} = postInfo

    const handleChange = e => {
        const { name, value } = e.target
        setPostInfo({
          ...postInfo,
          [name]:value
        })
      }
    const handleSubmit = e => {
        e.preventDefault()
        alert(`전송 클릭: ${JSON.stringify({...postInfo})}`)
        userPostwrite({...postInfo})
        .then(res => {
          alert(`게시 완료 : ${res.data.result} `)          
        })
        .catch(err => {
          alert(`게시 실패 : ${err} `)
        })
      }
    const handleClick = e => {
        e.preventDefault()
        alert('취소 클릭')
      }

  return (<>
    <div className="PostWrite">
    <form onSubmit={handleSubmit} method="post" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>Post Write</h1>
        <p>Please fill in this form to write a post.</p>
        <hr/>

        <label for="title"><b>title</b></label>
        <input type="text" placeholder="Enter title" onChange={handleChange}   name="title" value={title}/>

        <label for="content"><b>text</b></label>
        <input type="text" placeholder="Enter content" onChange={handleChange}  name="content" value={content}/>

        <div class="clearfix">
          <button type="submit" className="signupbtn">Post</button>
          <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
          
        </div>
      </div>
  </form>
</div>
</>)
}

export default PostWrite