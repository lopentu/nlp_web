export default function ChatTurn({
  prompt, reply
}){
  return (
    <div className="d-flex flex-column">
      <div className="align-self-end bg-light rounded-pill p-3">
        {prompt}
      </div>
      <div className="align-self-start bg-light rounded-pill p-3">
        {reply}
      </div>
    </div>
  )
}