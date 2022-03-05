from pydantic import BaseModel, Field


class MyModel(BaseModel):
    tx_type: str = Field(title="Transmission type")

    class Config:
        fields = {
            "tx_type": "transmission_type"
        }


print(MyModel.schema())
