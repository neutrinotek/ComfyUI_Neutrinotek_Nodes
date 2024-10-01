# ComfyUI_Neutrinotek_Nodes
This is my first set of custom nodes for ComfyUI. Folder structure needs some work, so for now, it has to be installed directly in the custom_nodes folder (no subfolders). 


CheckpointPassthrough.py: Allows for manual triggering of Checkpoint loading via passthrough of some other node. Nodes that are passed through do so unchanged, and act as a trigger to load a new checkpoint. Super helpful for complex workflows where VRAM management is critical. I use in combination with Clean GPU and/or Clear Cache to make sure that models are immediately removed from VRAM when they are complete, and new ones are triggered as needed.  


Again, this is my first attempt at custom nodes for Comfy, so if anyone has any tips or improvements, they are most definitely welcome! 


I have also included a workflow I put together for CogVideoX Image to Video, that uses Pixtral or Llama3.2-11B-Vision-Instruct for autocaptioning, outpainting for adjusting images to the proper scale, frame interpolation with RIFE, and upscaling the final video, all with VRAM management along the way. Hope it helps! 
