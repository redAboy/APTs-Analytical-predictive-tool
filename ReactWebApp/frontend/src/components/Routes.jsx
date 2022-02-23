import React from 'react'

import {Route, Switch} from 'react-router-dom'

import Dashboard from '../pages/Dashboard'
import Rawdata from '../pages/Rawdata'
import Analytics from '../pages/Analytics'
import Maps from '../pages/Maps'
import Prediction from '../pages/Prediction'

const Routes = () => {
    return (
        <Switch>
            <Route path='/' exact component={Dashboard}/>
            <Route path='/rawdata' component={Rawdata}/>
            <Route path='/analytics' component={Analytics}/>
            <Route path='/maps' component={Maps}/>
            <Route path='/prediction' component={Prediction}/>
        </Switch>
    )
}

export default Routes
