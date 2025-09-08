import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

_CLIENT_SINGLETON = None

def get_image_client() -> ImageAnalysisClient:
    """Create once, reuse thereafter."""
    global _CLIENT_SINGLETON
    if _CLIENT_SINGLETON is None:
        _CLIENT_SINGLETON = ImageAnalysisClient(
            endpoint=os.environ["VISION_ENDPOINT"],
            credential=AzureKeyCredential(os.environ["VISION_KEY"])
        )
    return _CLIENT_SINGLETON

def analyze(image_bytes):
    """
    Returns (alt_text, keywords) using Azure Image Analysis 4.0.
    """
    client = get_image_client()
    result = client.analyze(
        image_data=image_bytes,
        visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS],
        gender_neutral_caption=True
    )
    alt = result.caption.text if getattr(result, "caption", None) else None
    tags = [t.name for t in (getattr(result, "tags", None).list or [])] if getattr(result, "tags", None) else []
    return alt, tags