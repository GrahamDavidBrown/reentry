import React from 'react';
import Chip from 'material-ui/Chip';



class Chips extends React.Component {

	constructor(props) {
		super(props);
		this.handleRequestDelete = this.handleRequestDelete.bind(this);
		this.renderChip = this.renderChip.bind(this);
		this.state = {
		};
		this.styles = {
			chip: {
				margin: 4,
			},
			wrapper: {
				display: 'flex',
				flexWrap: 'wrap',
				justifyContent: 'center'
			},
		};
	}



	handleRequestDelete = (key) => {
	  console.log('You clicked the delete button.');

		this.chipData = this.props.chipData;
		const chipToDelete = this.chipData.map((chip) => chip.key).indexOf(key);
		this.chipData.splice(chipToDelete, 1);
		this.setState({chipData: this.chipData});
		this.props.deleteChip(key, this.props.choose);
	}

		renderChip(data) {

			return (
				<Chip
					key={data.key}
					onRequestDelete={() => this.handleRequestDelete(data.key)}
					style={this.styles.chip}
				>
				{data.label}
			</Chip>

			);
		}

		render() {

			return(
				<div style={this.styles.wrapper}>
					{this.props.chipData.map(this.renderChip, this)}
				</div>
			);
		}
	}

		export default Chips;
