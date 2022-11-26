import { useState, useEffect } from 'react';
import HistFreq from './hist-freq';

export default function TextView({ name, freqType }) {
  const [rawText, setRawText] = useState("");
  const [target, setTarget] = useState("");
  useEffect(() => {
    if (["alice", "prince"].indexOf(name) < 0) {
      setRawText("(Not found)");
    }

    fetch(`/${name}.txt`)
      .then((resp) => {
        return resp.text();
      })
      .then((text) => {
        setRawText(text);
        console.log(text);
      });
  }, [name]);

  function onTargetUpdate(target) {
    setTarget(target);
  }

  let pat = new RegExp("");
  if (target) {
    if (freqType == "letter") {
      pat = new RegExp(`${target}`, 'ig');
    } else {
      pat = new RegExp(`\\b${target}\\b`, 'ig');
    }
  }

  let displayText = rawText.replace(pat,
    `<span class='alice-highlight'>${target}</span>`);

  return (
    <div id="container">
      <div id="alice-text" dangerouslySetInnerHTML={{ __html: displayText }} />
      <HistFreq
        rawText={rawText}
        target={target}
        freqType={freqType}
        onTargetUpdate={onTargetUpdate} />
    </div>
  )
}