import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { Login, SignUp, UserDetail, UserEdit, UserList } from 'user'
import { Home, User, Item, Blog, Stock } from 'templates'
import { Navi } from 'common'
import { BrowserRouter as Router } from 'react-router-dom'
import { Link } from 'react-router-dom'
const App = () => {
  return (<div>
    <Router>
        <Navi/>
        <nav style={{width: '500px', margin:'0 auto'}}>
          <ol>
              <li><Link to='/home'>Home</Link></li>
              <li><Link to='/user'>User</Link></li>
              <li><Link to='/item'>Item</Link></li>
              <li><Link to='/blog'>Blog</Link></li>
              <li><Link to='/stock'>Stock</Link></li>
          </ol>
      </nav>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/user' component={User}/>
        <Route exact path='/login' component={Login}/>
        <Route exact path='/signup-form' component={SignUp}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-edit' component={UserEdit}/>
        <Route exact path='/user-list' component={UserList}/>
        <Route exact path='/item' component={Item}/>
        <Route exact path='/blog' component={Blog}/>
        <Route exact path='/stock' component={Stock}/>
    </Router>
  </div>)
}

export default App