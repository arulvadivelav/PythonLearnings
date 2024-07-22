from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import StreamingResponse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from app.routers import user_routes
import base64
import io

app = FastAPI()


# # AES encryption/decryption key and IV (must be 16, 24, or 32 bytes long for key and 16 bytes for IV)
# key = b'!CjOyJ=y|1LwEQKgGl98:UH-FmFrq*)>'  # Replace with your key (32 bytes for AES-256)
# iv = b'pAykua8m3Z0pbwIF'                   # Initialization vector (16 bytes for AES)

# def encrypt(data: str) -> str:
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
#     return base64.b64encode(encrypted_data).decode()

# def decrypt(data: str) -> str:
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     decrypted_data = unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size)
#     return decrypted_data.decode()

# class EncryptionDecryptionMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         # Decrypt incoming request data
#         if request.method in ["POST", "PUT", "PATCH"]:
#             body = await request.body()
#             if body:
#                 print("Bodeeeeeeeeeeeeeeeeeeeeeeeeee", body)
#         response = await call_next(request)
#         # Consuming FastAPI response and grabbing body here
#         resp_body = [section async for section in response.__dict__['body_iterator']]
#         # Repairing FastAPI response
#         response.__setattr__('body_iterator', aiwrap(resp_body)
#         return response
# # Add the middleware to the app
# app.add_middleware(EncryptionDecryptionMiddleware)

app.include_router(user_routes.router)
