from fastapi import APIRouter

router = APIRouter()

#@router.get("/health")
#async def health_check():
#    return {"status": "ok"}

@router.get("/health", response_model=dict)
async def health_check():
    return {"status": "ok"}
