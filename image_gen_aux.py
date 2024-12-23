from image_gen_aux import DepthPreprocessor

from utils.node_utils import NodeBase


class DepthEstimator(NodeBase):
    def execute(self, model_id, image, resolution_scale, invert, device):
        depth_preprocessor = DepthPreprocessor.from_pretrained(model_id).to(device)
        image = depth_preprocessor(
            image, resolution_scale=resolution_scale, invert=invert
        )[0]
        return {"depth_image": image}
