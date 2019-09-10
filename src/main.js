import React from 'react';
import Login from './login_page';
import Feed from './feed_page';
import { BrowserRouter as Switch, Route } from "react-router-dom";

const Main = () => (
    <Switch>
        <Route path='/' exact component={Login}/>
        <Route path='/feed' component={Feed}/>
        <Route path='/login' component={Login}/>
    </Switch>
)

export default Main