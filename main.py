from controller.blocks_filter_controller import init_routes
from fastapi import FastAPI

app = FastAPI()

init_routes(app)