import jwt
from datetime import datetime, timedelta

secret_key = "secret_key"


class Authtication:
    
    def generate_token(payload):
        token_payload={
            **payload,
            "excepire": datetime.utcnow() + timedelta(minutes=10)
        }
        return jwt.encode(token_payload, secret_key, algorithm="HS256")
    
    def validate_token(token):
        try:
            payload = jwt.decode(token,secret_key,algorithm="HS256")
            return payload
        except jwt.invalidsignature:
            return "token has expired"
        except jwt.invalidToken:
            return "invalid token  "


