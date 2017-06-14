import React from 'react';
import AutoComplete from 'material-ui/AutoComplete';
import axios from 'axios';


class LocationForm extends React.Component {

  constructor() {
    super();
    this.getLocations = this.getLocations.bind(this);
    this.makeData = this.makeData.bind(this);
    this.state = {
      locations: []
    }
  }


  makeData() {
    let arr = [];
    let locationObj = this.props.allSkills;
    for ( let i in locationObj ) {
        if (locationObj.hasOwnProperty(i)){
           arr.push(locationObj[i].location);
        }
      }
    return arr;
  }

  getLocations() {
    axios()
      .get(`${this.props.baseurl}/api/location/`)
      .then((response) => {
        this.makeData();
      }).catch(function(error) {
        console.log(error);
      });
  }

render() {

  const data = this.makeData();

  return (
    <div>
    <form>
      <AutoComplete
      floatingLabelText="Where would you like to work?"
      filter={AutoComplete.fuzzyFilter}
      openOnFocus={true}
      dataSource={data}
      />
      </form>
      </div>
  );
}
}

export default LocationForm;
