import { useState } from 'react';
import { process_api, debug_api } from './api';
import ChatTurn from "./chat-turn"

export default function ChatBox() {
  const [dialogue, setDialogue] = useState(
    [
      {
        prompt: "你好阿",
        reply: "🤖bigscience/bloomz🌸"
      }
    ]);
  const [isProcessing, setIsProcessing] = useState(false);

  function onInputHandler(event) {
    if (event.key === "Enter") {
      let new_dialogue = Array.from(dialogue);
      const prompt_text = event.target.value.trim()
      new_dialogue.push({
        prompt: prompt_text,
        reply: ""
      });
      event.target.value = "";      
      process_prompt(prompt_text, new_dialogue);
      setDialogue(new_dialogue);
    }
  }

  function process_prompt(intext, dialogue_data) {
    setIsProcessing(true);
    const process_handler = process_api;
    // const process_handler = debug_api;
    process_handler(intext).then((reply) => {
      let new_dialogue = Array.from(dialogue_data);
      let last_turn = new_dialogue[new_dialogue.length - 1];
      console.log("bloomz respond: ", reply);
      if (reply) {
        last_turn.reply = reply;
      } else {
        last_turn.reply = "我不知道🤷‍♂️";
      }
      setIsProcessing(false);
      setDialogue(new_dialogue);
    });
  }
  return (
    <div className="d-flex flex-column w-50 vh-100 mx-auto mt-1 fs-4 ">
      <div className="flex-grow-1 d-flex flex-column-reverse overflow-auto">
        <div className="px-3">
          {dialogue.map((dialogue_x, idx) => {
            return (
              <ChatTurn key={`dialogue_${idx}`}
                prompt={dialogue_x.prompt}
                reply={dialogue_x.reply} />)
          })}
        </div>
      </div>
      <div className="w-100 my-2">
        <div className="mx-auto mt-1 fs-4">
          <input type="text"            
            autoFocus
            disabled={isProcessing}
            className="form-control form-control-lg"
            placeholder="Type here"
            onKeyDown={onInputHandler} />
        </div>
      </div>
    </div >
  )
};