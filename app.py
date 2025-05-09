import gradio as gr
import time
import os


def interface_fun(Super_card_key):
    time.sleep(3)
    if Super_card_key == "Bear loves Tiger":
        output_txt = f"Congrats! You won a night in [Jiva Hotel](https://www.jivahill.com/en/index.html)"
    else:
        output_txt = "You won nothing! Try again"
    return output_txt


with gr.Blocks() as demo:
    gr.Markdown("# Coop Birthday game ")
    gr.Markdown("## Click below to see what you won for your birthday")

    gr.Interface(fn=interface_fun, inputs="text", outputs=gr.Markdown())

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
