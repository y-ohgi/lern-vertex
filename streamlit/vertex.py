from google import genai
from google.genai import types

import config

client = genai.Client(
    vertexai=True,
    project=config.PROJECT_ID,
    location=config.LOCATION # "us-central1"
)

def ask_ai(steps, water, weight):
    return client.models.generate_content(
        model=config.MODEL_NAME, # "gemini-2.0-flash-exp",
        contents=f'''今日の記録：歩数は${steps}歩、水分摂取量は${water}ml、体重は${weight}kgでした。
        今日の記録をもとに、今日の運動量を1000文字以内で逆ギレ風に評価してください。逆に健康状態が良好な場合は褒めてください'''
    )
