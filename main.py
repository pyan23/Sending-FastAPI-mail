from fastapi import FastAPI

app = FastAPI()

from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME = "dwiPy123@outlook.com",
    MAIL_PASSWORD = "6t5r4e3w2q",
    MAIL_FROM = "dwiPy123@outlook.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp-mail.outlook.com",
    MAIL_FROM_NAME="dwiandika",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

app = FastAPI()


@app.post("/email")
async def simple_send(email: EmailSchema) -> JSONResponse:
    html = """<p>selamat anda telah selesai mengerjakan UAS Python</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})