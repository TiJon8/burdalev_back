from fastapi import Depends
from app_config import app

from sqlalchemy.ext.asyncio import AsyncSession
from engine import db_helper
from sqlalchemy import select
from schemas import User
from models import UserResponse, RequestParams
import uvicorn


@app.post('/', response_model=UserResponse)
async def get_user(user_id: RequestParams, session: AsyncSession = Depends(db_helper.session_getter)):
    async with session.begin():
        stm = select(User).where(User.id == int(user_id.id))
        res = await session.execute(stm)
        user_row = res.fetchone()
        user = user_row[0]
        return UserResponse(id=str(user.id), is_member=user.is_member)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)