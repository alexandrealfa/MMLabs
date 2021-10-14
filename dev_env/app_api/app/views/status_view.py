from typing import Dict

from fastapi import APIRouter

router_status = APIRouter()


@router_status.get('/')
def status_router() -> Dict[str, str]:
    """
    Rota destinada a verificar se a api está no ar
    :return: um dicionário com uma mensagem ok sinalizando o funcionamento da rota.
    """
    return {"status": "Ok"}
