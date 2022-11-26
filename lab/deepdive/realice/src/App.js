import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';
import TextView from './text-view';
import HistFreq from './hist-freq';

function App() {
  const [displayText, setDisplayText] = useState("");
  const [target, setTarget] = useState("");
  useEffect(() => {
    fetch("alice.txt")
      .then((resp) => {
        return resp.text();
      })
      .then((text) => {
        setDisplayText(text);
      });
  }, []);

  function onTargetUpdate(target){
    setTarget(target);
  }

  return (
    <div id="container">
      <TextView rawText={displayText} target={target} />
      <HistFreq rawText={displayText} onTargetUpdate={onTargetUpdate}/>
    </div>
  );
}

export default App;
