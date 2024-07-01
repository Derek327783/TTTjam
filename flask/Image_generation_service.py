from diffusers import AutoPipelineForText2Image
import torch

pipeline = AutoPipelineForText2Image.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
pipeline.load_lora_weights("../Weights/pytorch_lora_weights.safetensors", weight_name="pytorch_lora_weights.safetensors")
image = pipeline("The track belongs to the blues-rock genre, showcasing a fusion of blues and rock elements. It exudes a sense of longing, introspection, and a touch of melancholy, capturing the listener's attention with its emotive style").images[0]
image