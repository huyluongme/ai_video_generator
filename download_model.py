import os
import requests
from tqdm import tqdm

# Create directories
os.makedirs('./checkpoints', exist_ok=True)
os.makedirs('./gfpgan/weights', exist_ok=True)

# Function to download a file from a URL with a progress bar
def download_file(url, output_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Ensure we raise an exception for bad responses

    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 8192

    with open(output_path, 'wb') as file, tqdm(
        desc=output_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            size = file.write(chunk)
            bar.update(size)

    print(f"Downloaded: {output_path}")

# List of URLs and their corresponding output paths
downloads = [
    ("https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00109-model.pth.tar", "./checkpoints/mapping_00109-model.pth.tar"),
    ("https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00229-model.pth.tar", "./checkpoints/mapping_00229-model.pth.tar"),
    ("https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_256.safetensors", "./checkpoints/SadTalker_V0.0.2_256.safetensors"),
    ("https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_512.safetensors", "./checkpoints/SadTalker_V0.0.2_512.safetensors"),
    ("https://github.com/xinntao/facexlib/releases/download/v0.1.0/alignment_WFLW_4HG.pth", "./gfpgan/weights/alignment_WFLW_4HG.pth"),
    ("https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth", "./gfpgan/weights/detection_Resnet50_Final.pth"),
    ("https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth", "./gfpgan/weights/GFPGANv1.4.pth"),
    ("https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth", "./gfpgan/weights/parsing_parsenet.pth")
]

# Download each file
for url, output_path in downloads:
    download_file(url, output_path)
