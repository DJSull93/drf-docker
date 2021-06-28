import React, {useState} from 'react'
import './SignUp.css'

const SingUp = () => {
  const [ userInfo, setUserInfo ] = useState({
    username : '',
    password : '',
    name : '',
    email : ''
  })

  const { username, password, name, email } = userInfo

  const handleChange = e => {
    const { name, value } = e.target
    alert('키 : ${name}, 밸류 : ${value}')
  }
  const handleSubmit = e => {
    e.preventDefault()
  }



    return (
        <>
        <form action="/action_page.php" style={{border:"1px solid #ccc"}}>
        <div className="container">
          <h1>Sign Up</h1>
          <p>Please fill in this form to create an account.</p>
          <hr/>
      
          <label for="username"><b>Email</b></label>
          <input type="text" placeholder="Enter ID" name="username" required/>
          
          <label for="password"><b>Password</b></label>
          <input type="password" placeholder="Enter Password" name="password" required/>
      
          <label for="name"><b>Name</b></label>
          <input type="text" placeholder="Enter Your name" name="name" required/>
      
          <label for="email"><b>Email</b></label>
          <input type="text" placeholder="Enter Email" name="email" required/>
      
          <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>
      
          <div className="clearfix">
            <button type="button" className="cancelbtn">Cancel</button>
            <button type="submit" className="signupbtn">Sign Up</button>
          </div>
        </div>
      </form>
      </>
    )
}

export default SingUp