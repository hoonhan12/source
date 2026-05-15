from dotenv import load_dotenv
import os
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
import gradio as gr

# .env 내용 가져오기
load_dotenv()
apikey        = os.getenv("WATSONX_API_KEY")
project_id    = os.getenv("WATSONX_PROJECT_ID")
watsonx_ai_url = os.getenv("WATSON_URL")

# 모델 선언 ✅ 추가
credentials = Credentials(url=watsonx_ai_url, api_key=apikey)
client = APIClient(credentials)
model = ModelInference(
    model_id="ibm/granite-4-h-small",
    api_client=client,
    project_id=f"{project_id}",
    params={"max_new_tokens": 1000}
)

def summarize_text(text):
    if not text.strip():
        return "텍스트를 입력해 주세요"

    system_prompt = """                          
    당신은 텍스트를 한국어로 요약하는 전문가
    - 당신의 임무는 주어진 텍스트를 한국어로 요약.
    - 요약 시 중복되지 않고 반복되는 걸 지양하고 요약해서 강조.
    - 3줄 이내 요약
    - 블릿 기호 형식으로 작성
    """                                          # ✅ 변수명 수정

    messages = [
        {"role": "system", "content": system_prompt},  # ✅ 따옴표 제거
        {"role": "user",   "content": text},           # ✅ prompt → text
    ]

    generated_response = model.chat(messages=messages)

    return generated_response['choices'][0]['message']['content']  # ✅ print 제거

demo = gr.Interface(
    fn=summarize_text,
    inputs=[gr.TextArea(lines=10, placeholder="요약할 내용의 텍스트 입력..", label="입력")],
    outputs=["text"],
    title="watsonx 기반의 요약 프로그램",
    description="텍스트 입력 시 ai 요약"
)

demo.launch()