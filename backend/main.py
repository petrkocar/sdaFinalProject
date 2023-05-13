from datetime import date
from typing import Optional
from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel

from batabase import init_db

app = FastAPI()

refuel_list = []

class Refuel(BaseModel):
    id: Optional[int]
    date: date
    milage: int
    amount: float

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Refueling overview application"}

@app.get("/refuels")
async def get_refuels():
    pass

@app.get("/refuels/{refuel_id}")
async def get_refuel():
    pass

@app.post("/refuels")
async def create_refuel(refuel: Refuel = Body()):
    new_refuel = Refuel(id=len(refuel_list) + 1, date=9999999, milage=99999, amount=40)
    refuel_list.append(new_refuel)
    return new_refuel

@app.patch("/refuels/{refuel_id}")
async def update_refuel(refuel: Refuel = Body()):
    for refuel_item in refuel_list:
        if refuel_item.id == refuel.id:
            refuel_item = refuel.value
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": f"Refueling [{refuel.id}] not found",
                "code": "REFUELING_NOT_FOUND",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        )

@app.delete("/refuels/{refuel_id}")
async def delete_refuel(refuel_id: int):
    for index, refuel in enumerate(refuel_list):
        if refuel.id == refuel_id:
            refuel_list.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": f"Refueling [{refuel_id}] not found",
                "code": "REFUELING_NOT_FOUND",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        )
