export default function ChatBox() {
  return (
    <div className="w-50 mx-auto mt-5 fs-4">
      <div className="d-flex flex-column">
        <div className="align-self-end bg-light rounded-pill p-3">
          Prompt message
        </div>
        <div className="align-self-start bg-light rounded-pill p-3">
          Reply message
        </div>
      </div>
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