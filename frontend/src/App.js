import './App.css';
import ASide from './components/aside';
import Header from './components/header';

function App() {
  return (
    <div className="App">
      <Header highlight="energia" classes="header" >Dados de </Header>
      <ASide classes="aside" />
    </div>
  );
}

export default App;
