from app.services.update_service import update_order_status
from app.auth.jwt_utils import decode_token


def resolve_update_order_status(obj, info, id):
    request = info.context["request"]
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise Exception("Token no proporcionado o inválido")

    token = auth_header.split(" ")[1]

    user_data = decode_token(token)

    return update_order_status(
        order_id=id, email=user_data["email"], roles=user_data["roles"]
    )
