from fastapi import APIRouter
from .models import OutputBayers, ImputBayers
from typing import List


router = APIRouter()


@router.get('/')
def get_bayers() -> List[OutputBayers]:
    return ({"id": 1, "fio": "Алексчандр Александрович", "phone": "7903276453", "email": "sdaifg@sdf.ru", "address": "Кирова 102"})


@router.get('/{bayer_id}')
def get_current_bayer(bayer_id: int) -> OutputBayers:
    return ({"id": bayer_id, "fio": "Алексчандр Александрович", "phone": "7903276453", "email": "sdaifg@sdf.ru", "address": "Кирова 102"})


@router.post('/')
def add_bayer(new_bayer: ImputBayers) -> OutputBayers:
    return ({"id": 1, "fio": new_bayer, "phone": "7903276453", "email": "sdaifg@sdf.ru", "address": "Кирова 102"})


@router.post('/{bayer_id}')
def add_bayer(bayer_id: int, new_bayer: ImputBayers) -> OutputBayers:
    return ({"id": bayer_id, "fio": new_bayer, "phone": "7903276453", "email": "sdaifg@sdf.ru", "address": "Кирова 102"})


@router.delete("/{bayer_id}")
def delete_bayer(group_id: int) -> int:
    return 200
