import uvicorn
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from src import __version__
from src.handlers.users import users_router
from src.services.database import engine, Base
from src.utils.exceptions import UserNotFoundException, is_business_logic_exception

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User API",
    description="ZPE Service User API",
    version=__version__
)

app.include_router(users_router)


@app.exception_handler(Exception)
async def unknown_error(request, exc: Exception):
    http_status_code = HTTP_500_INTERNAL_SERVER_ERROR

    if isinstance(exc, UserNotFoundException):
        http_status_code = HTTP_404_NOT_FOUND
    elif is_business_logic_exception(exc):
        http_status_code = HTTP_400_BAD_REQUEST

    return UJSONResponse(content={'message': str(exc)}, status_code=http_status_code)

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=8080, workers=1, reload=True)
