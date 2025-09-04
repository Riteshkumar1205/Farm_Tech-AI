import torch, io
from torchvision import transforms
from PIL import Image

# Placeholder model
model = torch.nn.Identity()
classes = ["healthy", "early_blight", "late_blight"]

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict_disease(image_bytes, crop):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    tensor = transform(image).unsqueeze(0)
    # Mock prediction
    disease = classes[1]
    confidence = 0.85
    return disease, confidence

def recommend_treatment(crop, disease):
    knowledge = {
        ("potato", "late_blight"): [
            "Remove affected leaves",
            "Spray copper fungicide",
            "Improve field drainage"
        ],
    }
    return knowledge.get((crop, disease), ["Consult local agri officer"])
