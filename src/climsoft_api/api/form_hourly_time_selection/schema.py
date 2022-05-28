from pydantic import BaseModel


class CreateFormHourlyTimeSelection(BaseModel):
    hh: int
    hh_selection: int


class UpdateFormHourlyTimeSelection(CreateFormHourlyTimeSelection):
    pass


class FormHourlyTimeSelection(CreateFormHourlyTimeSelection):
    class Config:
        orm_mode = True
