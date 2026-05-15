import gradio as gr
# pillow ==> 밝기 변경
from PIL import ImageEnhance

def process_image(editor_value):
    '''

    composite : 원본 그림 위에레이어 반영한 최종 이미지
    '''
    image = editor_value['composite']
    enhance = ImageEnhance.Brightness(image)
    result = enhance.enhance(3)


    return result


interface = gr.Interface(process_image, gr.ImageEditor(type="pil"), gr.Textbox())
interface.launch()