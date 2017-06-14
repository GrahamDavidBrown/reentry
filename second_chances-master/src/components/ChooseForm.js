import React from 'react';
import AutoComplete from 'material-ui/AutoComplete';


class ChooseForm extends React.Component {

  constructor() {
    super();
    this.makeData = this.makeData.bind(this);
    this.displayPrompt = this.displayPrompt.bind(this);
    this.handleUpdateInput = this.handleUpdateInput.bind(this);
    this.state = {
      hintText: '',
      searchText: ''
    }
  }

  makeData(show) {
    let sourceObj;
    let arr = [];
    if (show==='skills') {
      sourceObj = this.props.allskills;
      for (let i in sourceObj) {
        arr.push(
          {data: sourceObj[i].skill,
            id: sourceObj[i].id});
      }
    } else if (show==='locations') {
      sourceObj = this.props.alllocations;
      for (let i in sourceObj) {
        arr.push(
          { data: sourceObj[i].city,
            id: sourceObj[i].id});
          }
        }
    return arr;
  }

  displayPrompt(choose) {
    if (choose==='skills') {
      return 'What are your skills?'
    } else if (choose==='locations') {
      return 'Where would you like to work?'
    };
  }

  handleUpdateInput = (dataSource) => {

    this.setState({
      hintText: `enter some more ${this.props.choose}`,
      searchText: ''
    });

    console.log(dataSource);
    if (this.props.choose==='skills') {
      let skill = {
        owner: this.props.userid,
        skill: dataSource.id,
        skill_string: dataSource.data
      };
      this.props.postSkill(skill);
    } else {
      let location = {
        owner: this.props.userid,
        location: dataSource.id
      };
      this.props.postLocation(location);
    }
  }

  setText() {
    this.setState({
      hintText: `enter some more ${this.props.choose}`,
      searchText: ''
    });
  }

render() {

  const autoData = this.makeData(this.props.choose);
  const dataSourceConfig = {
    text: 'data',
    value: 'id'
  };

  const styles = {
      hintStyle: {
        width: '100%',
        textAlign: 'center',
      },
      underlineFocusStyle: {
        borderColor: '#d9b310',
      }
  }


  return (
    <div>
    <form>
      <h2>{this.displayPrompt(this.props.choose)}</h2>
      <AutoComplete
      id={'chooseForm'}
      filter={AutoComplete.fuzzyFilter}
      openOnFocus={true}
      dataSource={autoData}
      dataSourceConfig={dataSourceConfig}
      onNewRequest={this.handleUpdateInput}
      onUpdateInput={this.setText.bind(this)}
      searchText={this.state.searchText}
      hintText={this.state.hintText}
      hintStyle={styles.hintStyle}
      underlineFocusStyle={styles.underlineFocusStyle}
      maxSearchResults={55}
      menuProps={{maxHeight: 400}}
      />
      </form>
      </div>
  );
}
}

export default ChooseForm;
