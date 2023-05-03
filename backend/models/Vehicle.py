from sqlmodel import SQLModel, Field
import sqlalchemy as sa


class Vehicle(SQLModel, table=True):
    __tablename__ = "vehicles"

    vehicle_id: int = Field(default=None, primary_key=True)
    vehicle_name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False, unique=True))
