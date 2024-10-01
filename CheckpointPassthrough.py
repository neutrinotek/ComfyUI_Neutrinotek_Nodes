import os
import comfy.sd
import folder_paths

class Checkpoint_Loader_Trigger:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
            },
            "optional": {
                "trigger": ("TRIGGER",),
                "image_pass": ("IMAGE",),
                "model_pass": ("MODEL",),
                "string_pass": ("STRING",),
            }
        }

    RETURN_TYPES = ("TRIGGER", "IMAGE", "MODEL", "MODEL", "CLIP", "VAE", "STRING")
    RETURN_NAMES = ("trigger_out", "image_out", "model_out", "MODEL", "CLIP", "VAE", "NAME_STRING")
    FUNCTION = "load_checkpoint_trigger"
    CATEGORY = "Custom Nodes/Model Loaders"
    DESCRIPTION = """
Passes through connected inputs and triggers the loading of a selected checkpoint into memory.
Outputs the model, clip, and VAE corresponding to the loaded checkpoint.
"""

    def load_checkpoint_trigger(self, ckpt_name, trigger=None, image_pass=None, model_pass=None, string_pass=None):
        # Pass through the inputs
        trigger_out = trigger
        image_out = image_pass
        model_out = model_pass

        # Load the checkpoint
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(
            ckpt_path,
            output_vae=True,
            output_clip=True,
            embedding_directory=folder_paths.get_folder_paths("embeddings")
        )

        # Extract the base name of the checkpoint for the NAME_STRING output
        name_string = os.path.splitext(os.path.basename(ckpt_name))[0]

        # Return the outputs
        return (trigger_out, image_out, model_out, out[0], out[1], out[2], name_string)

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "Checkpoint Loader Trigger": Checkpoint_Loader_Trigger
}

