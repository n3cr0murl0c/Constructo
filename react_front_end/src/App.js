import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from'./Components/NavBar/NavBar.js'
// import Banner from './Components/Banner'
import Preloader from './Components/Preloader/Prealoader'
import Footer from './Components/Footer/Footer'
import Posts from './Components/Post/Post'
import PostLoadingComponent from './Components/Post/PostLoading'
// import { Container } from 'react-bootstrap';
import {React, useEffect, useState} from 'react'

//Conexion a la API
// class Connection extends React.Component{
//   componentDidMount() {
//     const apiURL = 'http://127.0.0.1:8000/api';
//     fetch(apiURL)
//         .then((response) => response.json())
//         .then((data)=>console.log(data));
//   }
//   render () {
//     return (
//       <div>
//         Example
//       </div>
//     )
//   }
// }


function App() {

  const PostLoading = PostLoadingComponent(Posts);
  const [appState, setAppState] = useState({
    loading:false,
    posts:null, //toda la informacion del fetch se guarda en posts, y se cambia el valor
    //de loading a true para avisar a la app que se esta cargando data
  });

  //Conexion a la API con useEffect... metodo component did mount and componentDidUpdate
  //al mismo tiempo

  useEffect(()=>{
    setAppState({ loading: true});
    const apiURL = 'http://constructo_db:8000/api';
    fetch(apiURL)
        .then((data) => data.json())
        .then((posts)=> {
          setAppState( { loading:false, posts:posts});

        });
    },[setAppState]
  );

  return (

    <>
    <Preloader />
    
    <div className="root">
      <Navbar />

      <PostLoading isLoading={appState.loading} posts={appState.posts}/>  
      
      <Footer />
    </div>
    </>
    
  );
}

export default App;
