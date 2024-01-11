import logging

from gpt_task.inference import run_task

logging.basicConfig(
    format="[{asctime}] [{levelname:<8}] {name}: {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    style="{",
    level=logging.INFO,
)


messages = [
    {"role": "user", "content": "I want to create a chat bot. Any suggestions?"}
]


res = run_task(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=messages,
    seed=42,
    quantize_bits=4,
)
print(res)
