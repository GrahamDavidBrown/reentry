import React, {Component} from 'react';
import '../stylesheets/reset.css';
import '../stylesheets/App.css';
import {browserHistory} from 'react-router';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import injectTapEventPlugin from 'react-tap-event-plugin';
import axios from 'axios';


injectTapEventPlugin();

class App extends Component {

  constructor() {
      super();
      this.setUser = this.setUser.bind(this);
      this.state = {
          username: '',
          userid: null,
          baseurl: `https://${window.location.host}`
      };
  }

  setUser(user, url) {
    console.log('in setUser: ', user, url);
    axios({
      method: 'post',
      url: url,
      auth: {
        username: user.username,
        password: user.password
      },

      data: user
    }).then((response) => {
      console.log(response);
      let userid=response.data.id;
      this.setState({userid});
      this.setState(user);
      localStorage.setItem('userID', `${this.state.userid}`);
      localStorage.setItem('username', `${this.state.username}`);
      console.log('id: ', userid);
      console.log('user', user);
      browserHistory.push('/profile');
    })
    .catch(function(error) {
      console.log(error);
      if (error.response.status===401) {
        document.getElementById('errorMsg').innerHTML='<p style={styles.invalid}>--Invalid Login--</p>';
      } else {
        return;
      };
    });
    localStorage.getItem('userID');
    localStorage.getItem('username');
    this.setState(user);
  }

    render() {

      const childWithProp = React.Children.map(this.props.children, (child) => {
        return React.cloneElement(child, {
          setUser: this.setUser,
          username: this.state.username,
          userid: this.state.userid,
          email: this.state.email,
          baseurl: this.state.baseurl
        });
      });
        return (
          <MuiThemeProvider muiTheme={getMuiTheme()}>
              <main>
                {childWithProp}
              </main>
          </MuiThemeProvider>

        );
    }
}

export default App;
