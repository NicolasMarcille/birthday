import gradio as gr
import time
import os


# Your game logic
def birthday_game(super_card_key):
    # Generate output message using Markdown formatting
    if super_card_key == "Bear":
        return "## 🎉 Congrats! \nYou won a night in [Jiva Hotel](https://www.jivahill.com/en/index.html)"
    else:
        return "## ❌ You won nothing! \nTry again next time."


# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Coop Birthday Game 🎂🎉")  # Markdown header for the app

    super_card_input = gr.Textbox(label="Enter Super Card Key")  # Input box

    # Markdown component for displaying result
    output = gr.Markdown(label="Result")

    # Button and functionality to run the game
    submit_button = gr.Button("Submit")
    submit_button.click(fn=birthday_game, inputs=super_card_input, outputs=output)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
