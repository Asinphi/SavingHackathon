from fastapi import Request, Depends

from app import app, render_template
from users import User, fastapi_users


optional_user = Depends(fastapi_users.current_user(active=True, optional=True))


@app.get("/")
async def root(request: Request, user: User = optional_user):
    return render_template("index.html", request)
