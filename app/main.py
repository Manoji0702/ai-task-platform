from fastapi import FastAPI, HTTPException
from openai import OpenAI
import os

app = FastAPI(title="AI Task Processor")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/process")
def process_task(payload: dict):
    try:
        task = payload.get("task")
        content = payload.get("content")

        if not task or not content:
            raise HTTPException(status_code=400, detail="task and content are required")

        prompt = f"""
You are a helpful assistant.

Task:
{task}

Content:
{content}
"""

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return {
            "result": response.output_text
        }

    except Exception as e:
        # Return readable error instead of silent 500
        raise HTTPException(status_code=500, detail=str(e))
