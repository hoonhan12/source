import gradio as gr

def greet(name, level):
    return name + "님 화이팅 " + "👍" * int(level)   # ✅

def review(name, level):                              # ✅ 함수 추가
    return name + " " + "🌟" * int(level)

def bmi_calculator(height, weight):
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        result = "저체중"
    elif bmi < 23.0:
        result = "정상체중"
    elif bmi < 25.0:
        result = "과체중"
    else:
        result = "비만"
    return f"당신의 BMI 지수는 키: {height}cm, 몸무게: {weight}kg, 판정: {result}"

with gr.Blocks() as demo:
    with gr.Tab("응원"):
        name = gr.Text(label="이름")
        cheer_strength = gr.Slider(1, 5, step=1, label="응원강도")
        msg = gr.Textbox(label="응원 메시지")
        cheer_btn = gr.Button("응원")
        cheer_btn.click(fn=greet, inputs=[name, cheer_strength], outputs=[msg])  # ✅ fn=greet

    with gr.Tab("별점"):
        name2 = gr.Text(label="음식명")                    # ✅ gr.Text
        level = gr.Slider(1, 5, step=1, label="별점")      # ✅ gr.Slider, step=1
        msg2 = gr.Textbox(label="만족도 확인")
        review_btn = gr.Button("별점등록")
        review_btn.click(fn=review, inputs=[name2, level], outputs=[msg2])  # ✅

    with gr.Tab("BMI"):
        height = gr.Number(label="키 (cm)")
        weight = gr.Number(label="몸무게 (kg)")
        result = gr.Text(label="BMI 판정")
        gr.Button("BMI 판정").click(fn=bmi_calculator, inputs=[height, weight], outputs=[result])

demo.launch()