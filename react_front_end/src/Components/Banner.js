import Carousel from 'react-bootstrap/Carousel';
import slide1 from '../assets/img/slides/slide1.jpg';
import slide2 from '../assets/img/slides/slide2.jpg';
import slide3 from '../assets/img/slides/slide3.jpg';
import { Container } from 'react-bootstrap';
function UncontrolledExample() {
  return (
    <Carousel id='banner-carousel' interval={4000} indicators={false} controls={false} slide={true}>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src={slide1}
          alt="First slide"
        />
        <Carousel.Caption>
          <Container className=''>
            <div className="background">
                <div className="text">
                    <h1>Diseños Vanguardistas y Versátiles</h1>
                    <p>Diseñamos con Pasión</p>
                </div>
            </div>
            
          </Container>
        </Carousel.Caption>
      </Carousel.Item>

      {/* Segundo SLide */}
      <Carousel.Item>
        <img
          className="d-block w-100"
          src ={slide2}
          alt="Second slide"
        />

        <Carousel.Caption>
          <Container className=''>
            <div className="background">
                <div className="text">
                    <h1>Avanzadas Técnicas de Construcción</h1>
                    <p>Construimos cumpliendo los más altos estándares del sector </p>
                </div>
            </div>
          
          </Container>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src={slide3}
          alt="Third slide"
        />

        <Carousel.Caption>
          <Container className=''>
            <div className="background">
                <div className="text">
                    <h1>Personal Técnico Certificado</h1>
                    <p>
                        Conocimientos Técnicos y Experiencia
                    </p>
                </div>
            </div>
          
          </Container>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
}

export default UncontrolledExample;