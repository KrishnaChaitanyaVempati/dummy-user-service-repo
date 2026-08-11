from fastapi import APIRouter, HTTPException
from app.schemas.users import CreateUserRequest, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

_USERS = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
}

@router.get("/{user_id}", response_model=UserResponse, summary="Fetch a user by ID")
async def get_user(user_id: int) -> UserResponse:
    """Return one user record by numeric identifier."""
    user = _USERS.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(**user)

@router.post("", response_model=UserResponse, summary="Create a user")
async def create_user(payload: CreateUserRequest) -> UserResponse:
    """Create a new user from the posted request body."""
    new_id = max(_USERS.keys()) + 1
    user = {"id": new_id, "name": payload.name, "email": payload.email}
    _USERS[new_id] = user
    return UserResponse(**user)
