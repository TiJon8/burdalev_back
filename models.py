from pydantic import BaseModel


class RequestParams(BaseModel):
    id: str


class UserResponse(RequestParams):
    is_member: str | None = None
