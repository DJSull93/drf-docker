import React from "react"
import { Redirect, Route } from "react-router-dom"
import { Home, Counter } from 'templates'
import { Navi } from 'common'
import { BrowserRouter as Router } from "react-router-dom"

const App = () => {
return(<div>
    <Router>
        <Navi/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/counter' component={Counter}/>
    </Router>
  </div>)
}

export default App