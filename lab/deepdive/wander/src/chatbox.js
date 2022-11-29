import { useState } from 'react';
import ChatTurn from "./chat-turn"

export default function ChatBox() {
  const [dialogue, setDialogue] = useState(
    [
      {
        prompt: "Prompt Message - 1",
        reply: "Reply Message - 1"
      }, {
        prompt: "Prompt Message - 2",
        reply: "Reply Message - 2"
      }
    ]);
  
  function onInputHandler(event){    
    if (event.key==="Enter"){
      console.log(event.target.value);
      let new_dialogue = Array.from(dialogue);
      new_dialogue.push({
        prompt: event.target.value.trim(),
        reply: ""
      });
      event.target.value = "";
      setDialogue(new_dialogue);
    }    
  }

  return (
    <div className="w-50 mx-auto mt-5 fs-4">
      {dialogue.map((dialogue_x, idx) => {
        return (
          <ChatTurn key={`dialogue_${idx}`}
            prompt={dialogue_x.prompt}
            reply={dialogue_x.reply} />)
      })}
      <div>
        <div className="w-100 mb-5 position-fixed bottom-0 start-0">
          <div className="w-50 mx-auto mt-5 fs-4">
            <input type="text" 
              className="form-control form-control-lg" 
              placeholder="Type here" 
              onKeyDown={onInputHandler}/>
          </div>
        </div>
      </div>
    </div >
  )
};