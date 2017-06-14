import React from 'react';
import {slide as Menu} from 'react-burger-menu';

const Nav = (props) => {

        const styles = {
            bmBurgerButton: {
                position: 'fixed',
                width: '36px',
                height: '30px',
                right: '20px',
                top: '20px'
            },
            bmBurgerBars: {
                background: '#373a47'
            },
            bmCrossButton: {
                height: '25px',
                width: '100px'
            },
            bmCross: {
                background: '#000'
            },
            bmMenu: {
                padding: '1.5rem .5rem',
                fontSize: '1.15rem',
                height: 'auto',
                width: 'auto',
                background: '#ccc',
                border: '1px solid #000',
            },
            bmItemList: {
                color: '#b8b7ad',
                textAlign: 'right',
                margin: '1rem 0'
            }
        }

        return (
                <Menu right noOverlay styles={styles} width={200}>
                    <a id="home" className="menu-item" href="/">Home(login)</a>
                    <a id="profile" className="menu-item" href="/profile">My Profile</a>
                    <a id="find" className="menu-item" href="/find">Find Opportunities</a>
                    <a id="post" className="menu-item" href="/post">Post Opportunities</a>
                    <a id="resources" className="menu-item" href="/resources">Resources</a>
                </Menu>
        );
    }

export default Nav;
