import React from 'react';

let Panel = require('react-bootstrap').Panel;
let Button = require('react-bootstrap').Button;

class Job extends React.Component {

  constructor() {
    super();
    this.state = {
      open: false
    };
  }


  render() {

    const jobstyle = {
      textAlign:'left',
      margin: '5px',
      padding: '5px'
    }
    const jobheader = {
      backgroundColor: '#ccc',
      padding: '5px'
    }
    const jobcontainer = {
      width: '90%',
      margin: '0 auto',
    }

    const jobwrapper = {
      margin: '5px',
      backgroundColor: '#eee'
    }


		return (
      <div style={jobcontainer}>
        <p style={jobheader} onClick={ () => this.setState({open: !this.state.open})}>{this.props.job.title}</p>
        <Panel collapsible expanded={this.state.open} style={jobwrapper}  >
          <p style={jobstyle}>{this.props.job.description}</p>
          <Button bsSize='xsmall'>Message the Job Owner</Button>
        </Panel>
      </div>
		);
  }
}

export default Job;
