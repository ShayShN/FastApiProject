from fastapi import FastAPI
import uvicorn
from string_ops import (
    reverse_str, to_upper, remove_vowels,
    remove_every_third, letter_counts_map
)


app = FastAPI()

@app.get("/revers/")
def revers(text: str):
    a = reverse_str(text)
    return { "original": text, "reversed_text": a }

@app.get("/uppercase/{text}")
def uppercase(text: str):
    b = to_upper(text)
    return { "original": text, "uppercased": b }

@app.post("/reamove-vowels/")
def vowels()

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)