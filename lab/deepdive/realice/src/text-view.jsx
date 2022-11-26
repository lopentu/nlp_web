import {useState} from 'react';

export default function TextView({rawText, target}){      

  let pat = new RegExp(`\\b${target}\\b`, 'ig');
  let displayText = rawText.replace(pat,
    `<span class='alice-highlight'>${target}</span>`);
  
  return (
    <div id="alice-text" dangerouslySetInnerHTML={{__html: displayText}}/>
  )
}