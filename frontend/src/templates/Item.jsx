import React from 'react'
import { ItemMenu as Menu } from '../common'
import './table.style.css'

const Item = ({children}) => (<>
    
    <h1>User</h1>
    <Menu/>
    
    {children}
</>)

export default Item