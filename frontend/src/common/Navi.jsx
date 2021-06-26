import React from 'react'
import { Link } from 'react-router-dom'

const Navi = () => (<>
    <nav style={{width: '500px', margin: '0 auto'}}>
        <ol>
            <li><Link to='/home'>Home</Link></li>
            <li><Link to='/counter'>Counter</Link></li>
            <li><Link to='/schedule'>Todos</Link></li>
            <li><Link to='/user'>User</Link></li>
        </ol>
    </nav>
</>)

export default Navi