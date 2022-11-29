import ChatTurn from "./chat-turn"

export default function ChatBox() {
  return (
    <div className="w-50 mx-auto mt-5 fs-4">
      <ChatTurn prompt="Prompt Message - 1" reply="Reply Message - 1"/>
      <ChatTurn prompt="Prompt Message - 2" reply="Reply Message - 2"/>

      <div>
        <div className="w-100 mb-5 position-fixed bottom-0 start-0">
          <div className="w-50 mx-auto mt-5 fs-4">
            <input type="text" class="form-control form-control-lg" placeholder="Type here"/>
          </div>
        </div>
      </div>
    </div >
  )
}