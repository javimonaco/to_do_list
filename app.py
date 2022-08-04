from fastapi import FastAPI
from routes.users import user
from routes.tasks import task

app = FastAPI()

# Routes
app.include_router(user, prefix='/users')
app.include_router(task, prefix='/tasks')

# General Methods
@app.get('/')
def root():
    # Validate if the users and passwords are correct
    return {'message': 'Hello World'}