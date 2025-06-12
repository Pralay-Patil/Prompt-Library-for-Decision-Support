from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key, temperature=0.4)

class PromptRequest(BaseModel):
    prompt_type: str
    input_text: str

PROMPTS = {
    "summarize_report": """You are an executive assistant. Summarize the following report for the CFO.
Focus on key metrics, red flags, and decisions needed.

Report:
{input_text}
""",
    "extract_risks": """Analyze the following content and list the top 3 to 5 business risks mentioned or implied.
Use bullet points and provide 1-sentence reasoning for each.

Content:
{input_text}
""",
    "generate_decision_memo": """You are a strategic advisor. Based on the information provided, write a decision memo for executives.

Include the following:
1. Summary of the issue
2. Context and supporting data
3. Recommended action

Details:
{input_text}
"""
}

@app.post("/generate/")
def generate_response(req: PromptRequest):
    if req.prompt_type not in PROMPTS:
        return {"error": "Invalid prompt_type. Choose from: summarize_report, extract_risks, generate_decision_memo"}

    template = PromptTemplate(input_variables=["input_text"], template=PROMPTS[req.prompt_type])
    prompt = template.format(input_text=req.input_text)
    response = llm.predict(prompt)

    return {"response": response}
