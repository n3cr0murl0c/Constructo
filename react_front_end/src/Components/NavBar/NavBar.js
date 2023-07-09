import { useState, useEffect } from "react";
import Container from 'react-bootstrap/Container';
// import NavbarToggle from 'react-bootstrap/esm/NavbarToggle';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

import Logo_final from './assets/img/Logo_final.png';
// import navIcon1 from './assets/img/navIcon1.svg'
// import navIcon2 from './assets/img/navIcon2.svg'
// import navIcon3 from './assets/img/navIcon3.svg'
// import navIcon4 from '../assets/img/navIcon4.svg'

//Social Media Icons
// import tiktok from './assets/img/tik-tok.png';
// import whatsapp from './assets/img/whatsapp.png';
// import facebook from './assets/img/facebook.png';
// import instagram from './assets/img/instagram.png';
import './navbar.css'

function NavBar() {
    const [activeLink, setActiveLink] = useState('home');
    const [scrolled,seScrolled] = useState(false);

    useEffect(() => {
      const onScroll = () => {
        if (window.scrollY > 50){
            seScrolled(true);
        } else {
            seScrolled(false);
        }
      }

      window.addEventListener("scroll", onScroll);
    
      return () => window.removeEventListener("scroll",onScroll);
    }, [])
    const onUpdateActiveLink =(value) => {
        setActiveLink(value);
    }
  return (
    <Navbar fixed="top" expand="lg" className={scrolled ? "scrolled": "bg-body-tertiary"}>
      <Container >
       <Nav.Link href="#home">
       <img src={Logo_final} alt="" className="d-inline-block align-top" 
            width='166px'
            height='52px'
        />
       </Nav.Link>
        <Navbar.Toggle aria-controls="basic-navbar-nav">
            <span className="navbar-toggler-icon"></span>
        </Navbar.Toggle>
        <Navbar.Collapse id="basic-navbar-nav">
            
          <Nav className="ms-auto" id="navBarCustom">
            
            <Nav.Link href="#home" className={activeLink === 'home' ? 'active-navbar-link':'navbar-link nav-menu-item'} onClick={()=>onUpdateActiveLink('home')}>
                Inicio
            </Nav.Link>
            
            <Nav.Link href="#equipo"className={activeLink === 'equipo' ? 'active-navbar-link':'navbar-link nav-menu-item'} onClick={()=>onUpdateActiveLink('equipo')}>
                Equipo
            </Nav.Link>
                        
            <NavDropdown title="Nosotros" id="basic-nav-dropdown" >
              <NavDropdown.Item className={activeLink === 'valores' ? 'active-navbar-link':'dropdown-item'} onClick={()=>onUpdateActiveLink('valores')} href="#valores">Valores</NavDropdown.Item>
              <NavDropdown.Item className={activeLink === 'vision' ? 'active-navbar-link':'dropdown-item'} onClick={()=>onUpdateActiveLink('vision')} href="#vision">
                Visión
              </NavDropdown.Item>
              <NavDropdown.Item className={activeLink === 'mision' ? 'active-navbar-link':'dropdown-item'} onClick={()=>onUpdateActiveLink('mision')} href="#mision">
                Misión
            </NavDropdown.Item>
              {/* <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Separated link
              </NavDropdown.Item> */}
            </NavDropdown>

            <Nav.Link href="#trabajos" className={activeLink === 'trabajos' ? 'active-navbar-link':'navbar-link'} onClick={()=>onUpdateActiveLink('trabajos')}>
                
                Trabajos
            </Nav.Link>
            <Nav.Link href="#servicios" className={activeLink === 'servicios' ? 'active-navbar-link':'navbar-link'} onClick={()=>onUpdateActiveLink('servicios')}>
                
                Servicios
            </Nav.Link>
            <Nav.Link href="#contactanos" className={activeLink === 'contactanos' ? 'active-navbar-link':'navbar-link'} onClick={()=>onUpdateActiveLink('contactanos')}>
                
                Contáctanos
            </Nav.Link>
          </Nav>
          
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;