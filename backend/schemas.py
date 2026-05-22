from pydantic import BaseModel


class EmailRequest(BaseModel):
    name: str
    age: int
    gender: str
    location: str
    profession: str
    income_level: str

    purpose: str
    recipient_type: str
    relationship: str
    tone: str
    length: str
    urgency: str
    language: str

    additional_context: str