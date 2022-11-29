export async function process_api(prompt_text){
  const HF_TOKEN = process.env.REACT_APP_HF_TOKEN;
  const query_prompt = prompt_text.replace(/[。！]$/, "，");  
  const response = await query({ inputs: query_prompt }, HF_TOKEN);
  const gentext = response[0].generated_text;  
  const reply_text = gentext.replace(new RegExp(`^${query_prompt}`), "");
  return reply_text;
}

export function debug_api(prompt_text){  
  return new Promise((resolve, _)=>{
    setTimeout(()=>{
      resolve("reply to: " + prompt_text);
    }, 500)
  });
}

async function query(data, api_token) {
  const response = await fetch(
    "https://api-inference.huggingface.co/models/bigscience/bloomz",
    {
      headers: { Authorization: `Bearer ${api_token}` },
      method: "POST",
      body: JSON.stringify(data),
    }
  );
  const result = await response.json();      
  return result;
}