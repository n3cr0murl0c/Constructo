import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import React from 'react'
import {Container, Stack} from 'react-bootstrap'
import './posts.css'


//Animations
import {motion} from 'framer-motion'

//

const Posts = (props) => {
  const { posts } = props;
	if (!posts || posts.length === 0) return <p>Disculpa las molestias, por el momento no se encuetra ninguna publicación</p>;
  return (
    <React.Fragment>
      <Stack gap={3} direction="horizontal" className='stackering ms-auto p-0 items-align-center'>
      {posts.map(
              (post) => {
                return (
                  
                  
                  
                      <motion.div
                        className='box'
                        drag
                        whileHover={
                          {
                            scale:1.1,
                            margin:5
                          }
                        }
                        whileTap={{
                          scale:0.9
                        }}
                      >
                      <Container id='CardsWrapper' key={post.id}>
                        <Card >
                          <Button variant="" href={post.url}>
                            <Card.Img variant="top" src='{post.img.url}' />
                            <Card.Body>
                              {/* <Card.Title>{post.titulo}</Card.Title> */}
                              <Card.Text>
                                {post.excerpt}
                              </Card.Text>
                              {post.titulo}
                            </Card.Body>
                            
                          </Button>
                        </Card>
                        </Container>
                      </motion.div>
                    
                );
              })}
      </Stack>
       
            
    </React.Fragment>
    
      
    );
}
export default Posts;

