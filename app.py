import uvicorn
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import OPENAI_API_KEY, LABELS

app = FastAPI()
client = OpenAI(api_key=OPENAI_API_KEY)


class PickupRequest(BaseModel):
    label: str

# Set your OpenAI API key here

@app.post("/generate-pickup-line/")
async def generate_pickup_line(request: PickupRequest):
    label = request.label.lower()
    if label not in LABELS:
        raise HTTPException(status_code=400, detail="Invalid label provided.")

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a witty AI trained to generate pickup lines."},
            {"role": "user", "content": f"Give me a {label} pickup line."}
        ])
        return {"pickup_line": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)

