import React, {Component} from 'react';
import TextField from 'material-ui/TextField';
import BtnSubmit from './BtnSubmit';
import DjangoCSRFToken from 'django-react-csrftoken';

class LoginForm extends Component {

  constructor() {
      super();
      this.loginUser = this.loginUser.bind(this);
      this.handleChange = this.handleChange.bind(this);
      this.hideError = this.hideError.bind(this);
      this.state = {
        username: '',
        password: ''
      };
  }

  loginUser(event, type) {
    event.preventDefault();
    console.log('in loginUser: ');
    const user = {
      username: this.state.username,
      password: this.state.password,
    }
    let url = '';
    if (type==='login') {
      url=`${this.props.baseurl}/api-auth/login/`;
  } else if (type==='create') {
      url=`${this.props.baseurl}/api/user/`;
  } else {
    event.preventDefault();
    return;
  };
    this.props.setUser(user, url);
  }

  hideError() {
    document.getElementById('errorMsg').innerText='';
  }

  handleChange = (e) => {
    let newState = {};
    newState[e.target.name] = e.target.value;
    this.setState(newState);
  };

  render() {

    const styles = {
      inputForm: {
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        alignItems: 'center',
      },
      hintStyle: {
        width: '100%',
        textAlign: 'center',
      },
      underlineFocusStyle: {
        borderColor: '#d9b310',
      },
      buttons: {
        marginTop: '10px'
      },
      invalid: {
        fontSize: '1.2rem',
        color: '#F00'
      }
    };

  return (
    <div>
      <h2 className='space-after'>Login or Create an Account</h2>
      <form id="login-form" style={styles.inputForm} onSubmit={this.loginUser}>
        <TextField
          type="text"
          name='username'
          id='username'
          value={this.state.username}
          onFocus={this.hideError}
          onChange={this.handleChange}
          hintText='enter a username'
          hintStyle={styles.hintStyle}
          underlineFocusStyle={styles.underlineFocusStyle}
          required
        />
        <TextField
          type="password"
          name='password'
          id='password'
          value={this.state.password}
          onFocus={this.hideError}
          onChange={this.handleChange}
          hintText='enter a password'
          hintStyle={styles.hintStyle}
          underlineFocusStyle={styles.underlineFocusStyle}
          required
          />
        <DjangoCSRFToken/>
        <div style={styles.buttons}>
          <div style={styles.invalid} id='errorMsg'></div>
          <BtnSubmit
            type="submit"
            onClick={(e) => this.loginUser(e, 'login')}>
            Login Account
          </BtnSubmit>
          <BtnSubmit
            type="submit"
            onClick={(e) => this.loginUser(e, 'create')}>
            Create Account
          </BtnSubmit>
        </div>

      </form>
    </div>
  );
}

}

export default LoginForm;
