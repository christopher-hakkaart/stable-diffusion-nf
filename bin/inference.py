#!/usr/bin/env python3
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

prompt = "horse watching cricket smoking a vape"
model_id = "stabilityai/stable-diffusion-2"

#scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")

pipe = StableDiffusionPipeline.from_pretrained(model_id) #, scheduler=scheduler,revision="fp16", torch_dtype=torch.float16) 
image = pipe(prompt, height=768, width=768).images[0]
image.save("astronaut_rides_horse.png")