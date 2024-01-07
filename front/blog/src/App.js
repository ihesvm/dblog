import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';
import Contact from './components/Contact';
import axios from 'axios';

function App() {


  

  const get_api = () => {


    axios.get('http://127.0.0.1:8000/api/contact/').then((resp) => {
      console.log(resp.data)
    }).catch((err) => {
      console.log(err)
    })
  }


  return (
    <div>

      {get_api()}
      <Navbar />

      <div className='container mt-4'>
        <Contact />
      </div>
    </div>
  );
}

export default App;
