'''
Author: SpenserCai
Date: 2024-10-04 13:54:01
version: 
LastEditors: SpenserCai
LastEditTime: 2024-10-04 14:04:58
Description: file content
'''
import modelscope
import os
import folder_paths
from modelscope import snapshot_download

# Download the model
base_cosyvoice_model_path = os.path.join(folder_paths.models_dir, "CosyVoice")

def download_cosyvoice_300m(is_25hz=False):
    model_name = "CosyVoice-300M"
    model_id = "iic/CosyVoice-300M"
    if is_25hz:
        model_name = "CosyVoice-300M-25Hz"
        model_id = "iic/CosyVoice-300M-25Hz"
    model_dir = os.path.join(base_cosyvoice_model_path, model_name)
    snapshot_download(model_id=model_id, local_dir=model_dir)
    return model_name, model_dir