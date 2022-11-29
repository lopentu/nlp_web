import Spinner from "./spinner";

export default function ChatTurn({
  prompt, reply
}) {
  return (
    <div className="d-flex flex-column">
      <div className="align-self-end bg-light rounded-pill py-2 px-3 mt-2">
        {prompt}
      </div>
      
        <div className="align-self-start bg-light rounded-pill py-2 px-3 mt-2">
          {reply ? reply: (<Spinner/>)}
        </div>        
    </div>
  )
}