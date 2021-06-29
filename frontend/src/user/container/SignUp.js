import React,{useState} from 'react'
import './SignUp.css'
import { Button } from '@material-ui/core';
const SignUp = () => {
  const [userInfo, setUserInfo] = useState({
    username: '',
    password: '',
    name: '',
    email: ''
  })

  const {username, password, name, email} = userInfo

  const handleChange = e => {
    const { name, value } = e.target
    alert(`키: ${name}, 밸류: ${value}`)
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert('전송 클릭')
  }

    return (<>
    <div className="Signup">
    <form onSubmit={handleSubmit} style={{border:"1px solid #ccc"}}>
  <div className="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form to create an account.</p>
    <hr/>

    <label for="username"><b>User ID</b></label>
    <input type="text" placeholder="Enter ID" name="username" />

    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" />

    <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Your Name" name="name" />

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" />

    <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

    <div class="clearfix">
      <button type="submit" className="signupbtn">Sign Up</button>
      <button type="button" className="cancelbtn">Cancel</button>
      
    </div>
  </div>
</form>
</div>
</>)
}

export default SignUp