from fastapi import APIRouter
from climsoft_api.utils.deployment import load_deployment_configs


router = APIRouter()


@router.post("/databases")
def list_databases():
    deployment_configs = load_deployment_configs()

    return {k: v.get("DATABASE_URI").split("/")[-1] for k, v in deployment_configs.items()}
