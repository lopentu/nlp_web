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
    setTimeout(() => {
      let new_dialogue = Array.from(dialogue_data);
      let last_turn = new_dialogue[new_dialogue.length - 1];
      last_turn.reply = "hello there!"
      setIsProcessing(false);
      setDialogue(new_dialogue);
    }, 100)
  }
  return (
    <div className="d-flex flex-column w-50 vh-100 mx-auto mt-1 fs-4 ">
      <div className="flex-grow-1 overflow-auto">
        {dialogue.map((dialogue_x, idx) => {
          return (
            <ChatTurn key={`dialogue_${idx}`}
              prompt={dialogue_x.prompt}
              reply={dialogue_x.reply} />)
        })}
      </div>
      <div className="w-100 mb-5">
        <div className="mx-auto mt-1 fs-4">
          <input type="text" disabled={isProcessing}
            className="form-control form-control-lg"
            placeholder="Type here"
            onKeyDown={onInputHandler} />
        </div>
      </div>
    </div >
  )
};