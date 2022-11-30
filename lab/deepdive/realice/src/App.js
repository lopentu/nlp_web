import './App.css';
import {Routes, Route} from 'react-router-dom';
import TextView from './text-view';


function App() {


  return (
    <Routes>
      <Route index 
        element={<TextView name="alice" freqType="word"/>} />
      <Route path="/alice/word" 
        element={<TextView name="alice" freqType="word"/>} />
      <Route path="/alice/letter" 
        element={<TextView name="alice" freqType="letter"/>} />
      <Route path="/prince/word" 
        element={<TextView name="prince" freqType="word"/>} />
      <Route path="/prince/letter" 
        element={<TextView name="prince" freqType="letter"/>} />
    </Routes>
    
  );
}

export default App;
