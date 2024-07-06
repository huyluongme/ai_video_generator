# Simple AI Video Gererator

## Intro
This is a simple AI Video Generator tool built on top of [SadTalker](https://github.com/OpenTalker/SadTalker) and deployed as webui using Gradio

## Installation
1. Install [Anaconda](https://www.anaconda.com/), Python and `git`.

2. Creating the env and install the requirements.
```bash
git clone https://github.com/huyluongme/ai_video_generator.git

cd ai_video_generator 

conda create -n ai_video_generator python=3.9

conda activate ai_video_generator

pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

conda install ffmpeg

pip install -r requirements.txt

```

## Download Models
You can run the download_model.py to automatically download all the models (in Windows):
```bash
python download_model.py
```
Or you can download it manually
### Pre-Trained Models

* [Google Drive](https://drive.google.com/file/d/1gwWh45pF7aelNP_P78uDJL8Sycep-K7j/view?usp=sharing)
* [GitHub Releases](https://github.com/OpenTalker/SadTalker/releases)
* [Baidu (百度云盘)](https://pan.baidu.com/s/1kb1BCPaLOWX1JJb9Czbn6w?pwd=sadt) (Password: `sadt`)

<!-- TODO add Hugging Face links -->

### GFPGAN Offline Patch

* [Google Drive](https://drive.google.com/file/d/19AIBsmfcHW6BRJmeqSFlG5fL445Xmsyi?usp=sharing)
* [GitHub Releases](https://github.com/OpenTalker/SadTalker/releases)
* [Baidu (百度云盘)](https://pan.baidu.com/s/1P4fRgk9gaSutZnn8YW034Q?pwd=sadt) (Password: `sadt`)

<!-- TODO add Hugging Face links -->

## WebUI Demo
```bash
python app.py
```

## Result Demo
https://github.com/huyluongme/ai_video_generator/assets/48280785/0179e811-7d8f-4fdd-a89a-3c815e93082f


