from fastapi import FastAPI
from .config import ALLOWED_HOSTS, engine
from .routers import users, auth, muscles, userprofiles, exercises, workouts, workout_exercises
from fastapi.middleware.cors import CORSMiddleware

import app.models.muscle.muscle

app.models.muscle.muscle.Base.metadata.create_all(bind=engine)

app = FastAPI()

## Allow cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(userprofiles.router)
app.include_router(muscles.router)
app.include_router(exercises.router)
app.include_router(workouts.router)
app.include_router(workout_exercises.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}