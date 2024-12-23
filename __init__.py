from utils.torch_utils import default_device, device_list

MODULE_MAP = {
    "DepthEstimator": {
        "label": "Depth Estimator",
        "category": "ImageGenAux",
        "params": {
            "model_id": {
                "label": "Model ID",
                "type": "string",
                "description": "The ID of the model to use",
                "default": "depth-anything/Depth-Anything-V2-Large-hf",
            },
            "image": {
                "label": "Source image",
                "type": "image",
                "display": "input",
            },
            "resolution_scale": {
                "label": "Resolution Scale",
                "type": "float",
                "display": "slider",
                "default": 1.0,
                "min": 0,
                "max": 1,
            },
            "invert": {
                "label": "Invert image",
                "type": "boolean",
                "default": False,
            },
            "device": {
                "label": "Device",
                "type": "string",
                "options": device_list,
                "default": default_device,
            },
            "depth_image": {
                "label": "Depth Image",
                "display": "output",
                "type": "image",
            },
        },
    },
}
