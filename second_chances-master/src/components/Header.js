import React from 'react';
import logo from '../images/reEntrylogo_h.png'

const Header = (props) => {


      const styles = {
        headerBar: {
          backgroundColor: '#c1dceb',
          borderBottom: '1px solid #328cc1',
          boxShadow: '2px 2px 5px #000',
          width: '100%'
        },
        smallLogo: {
          width: '50%',
          paddingTop: '10px'

        }
      }

        return (
            <div style={styles.headerBar}>
                <img style={styles.smallLogo} src={logo} alt='second chances'/>
            </div>
        );
    }

export default Header;
