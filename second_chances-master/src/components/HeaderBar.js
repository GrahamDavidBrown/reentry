import React from 'react';

const HeaderBar = (props) => {


  const barStyle = {
    width: "100%",
    backgroundColor: "#000",
    padding: "0 auto",
    color: "#fff",
    fontSize: "1.2rem",
    clear: "both",
    textTransform: 'uppercase'
  }

  let innerText = props.innerText;

  return (
    <h1 style={barStyle}>{innerText}</h1>
    )
  }

export default HeaderBar;
