import gradio as gr
from elevenlabs import save
from elevenlabs.client import ElevenLabs
import shutil
import os
import glob

client = ElevenLabs(
  api_key="ENTER YOUR API KEY",
)

with gr.Blocks(title="AI Video Generator") as demo:
    with gr.Row():
        gr.Markdown("<div align='center'> <h1> AI Video Generator </h1> \
                    <a style='font-size:18px;color: #efefef' href='https://github.com/huyluongme'> Github </div>")
    with gr.Row():
        with gr.Column():
            with gr.Tabs():
                with gr.TabItem("Input"):
                    with gr.Row():
                        with gr.Tabs():
                            with gr.TabItem("Script"):
                                script = gr.Textbox(show_label=False, placeholder="Type your script", container=False, lines=2)
                    with gr.Row():
                        with gr.Tabs():
                            with gr.TabItem("Choose voice"):
                                voice = gr.Radio(['Male', 'Female'], value='Male', show_label=False, container=False, interactive=True)
                                # voice = gr.Dropdown(["Male", "Female"], value="Male" ,interactive=True, show_label=False, container=False)
                    with gr.Row():
                        with gr.Tabs():
                            with gr.TabItem("Upload Image"):
                                source_image = gr.Image(label="Source image", sources="upload", type="filepath")
                    with gr.Row():
                        gen_btn = gr.Button("Generate")
        with gr.Column():
            with gr.Tabs():
                with gr.TabItem("Output"):
                    gen_video = gr.Video(label="Generated video", format="mp4", interactive=False)

        def gen_audio(script, voice):
            if os.path.exists("./tmp"):
                shutil.rmtree("./tmp")
            os.mkdir('./tmp')
            vce = "Harry"
            if voice == 'Female':
                vce = "Mimi"
            audio = client.generate(
            text=script,
            voice=vce,
            model="eleven_multilingual_v2"
            )
            save(audio, 'tmp/audio.wav')


        def process(script, voice, img):
            gr.Info("Generating, please wait!")
            gen_audio(script, voice)
            if os.path.exists("./results"):
                shutil.rmtree("./results")
            os.system(f'python inference.py --driven_audio tmp\\audio.wav --source_image {img} --still --enhancer gfpgan --preprocess full')
            mp4_files = glob.glob(os.path.join('./results', '**', '*.mp4'), recursive=True)
            return mp4_files[0]


        gen_btn.click(process, inputs=[script, voice, source_image], outputs=gen_video)
    
if __name__ == "__main__":
    demo.queue().launch()
