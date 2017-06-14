import React from 'react';
import {render} from 'react-dom';
import {browserHistory, Router, Route, IndexRoute} from 'react-router';

import App from './components/App';
import Login from './components/Login';
import Profile from './components/Profile';
import Find from './components/Find';
import Post from './components/Post';
import Resources from './components/Resources';
import NotFound from './components/NotFound';

const Root = () => {

  return (
    <Router history={browserHistory}>
      <Route path='/' component={App}>
        <IndexRoute component={Login} />
        <Route path='login' component={Login} />
        <Route path='profile' component={Profile} />
        <Route path='find' component={Find} />
        <Route path='post' component={Post} />
        <Route path='resources' component={Resources} />
        <Route path='*' component={NotFound} />
      </Route>

    </Router>
  )
}

render(<Root />, document.querySelector('#root'));
