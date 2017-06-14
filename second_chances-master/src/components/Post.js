import React, {Component} from 'react';
import ChooseForm from './ChooseForm';
import JobForm from './JobForm';

class Post extends Component {

  constructor() {
    super();
    this.displayMessage = this.displayMessage.bind(this);
    this.state = {
      owner: localStorage.getItem("userID"),
      title: '',
      description: '',
      jobID: null
    };
  }

  // createJob(event) {
  //   event.preventDefault();
  //   console.log('in createJob');
  //   const job = {
  //     owner: this.state.owner,
  //     title: this.state.title,
  //     description: this.state.description
  //   };
  //   this.postJob(job);
  // }
  //
  // postJob(job) {
  //   console.log('in postJob');
  //
  //   axios({
  //     method: 'POST',
  //     url: `${this.props.baseurl}/api/job/`,
  //     data: job
  //   }).then((response) => {
  //     console.log('success! job posted', response);
  //     this.setState({jobID: response.data.id});
  //     this.displayMessage();
  //   }).catch(function(error) {
  //     console.log(error);
  //   })
  // }



  displayMessage() {
    document.getElementById('message').innerHTML = '';
    document.getElementById('message').innerHTML = 'Job Posted! Now enter some skills';
    document.getElementById('job-form').reset();
  }

  showChooseForm() {

    if (this.state.jobID === null) {
      return (
        <JobForm />
      )
    } else if (this.state.jobID !== null){
      return (
        <div>
          <p id='message'>Tell us about your job</p>
          <ChooseForm jobID={this.state.jobID} baseurl={this.props.baseurl} owner={this.state.owner} />
        </div>
      )};
  }

    render() {

        return (
            <div>
              {this.showChooseForm()}
            </div>
        );
    }
}

export default Post;
