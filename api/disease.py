from fastapi import APIRouter, UploadFile, Form
from tools.disease_model import predict_disease, recommend_treatment

router = APIRouter()

@router.post("/disease/detect")
async def detect_disease(file: UploadFile, crop: str = Form(...)):
    image_bytes = await file.read()
    disease, confidence = predict_disease(image_bytes, crop)
    steps = recommend_treatment(crop, disease)
    return {"crop": crop, "disease": disease, "confidence": confidence, "steps": steps}
