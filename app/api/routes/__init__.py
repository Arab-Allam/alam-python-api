from fastapi import APIRouter, HTTPException
from app.services.example_service import get_result

router = APIRouter()

@router.get("/result")
async def get_result_route():
    try:
        result = get_result()
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))