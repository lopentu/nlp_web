import './color-toggle.css';
import { CSS_COLOR_NAMES } from './css_colors';
import { useState } from 'react';

export default function ColorToggle() {

  const [color, setColor] = useState("aliceblue");

  let toggleBackground = function (event) {
    let ncolor = CSS_COLOR_NAMES.length;
    let color = CSS_COLOR_NAMES[Math.floor(Math.random() * ncolor)];
    setColor(color);
  };

  let onColorInputChange = function(event) {
    let target = event.target;
    let newColor = target.value;
    setColor(newColor);
  }  

  return (
    <div className="container">
      <div style={{
          width: "100vw", height: "100vh", 
          backgroundColor: color}}
        onClick={toggleBackground}>
        <div id="see-wrap">I see
          <input type="text" id="color-input" value={color}
            onChange={onColorInputChange} />
        </div>
      </div>
    </div>
  )
}