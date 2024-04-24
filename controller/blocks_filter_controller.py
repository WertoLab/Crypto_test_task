import json
from controller.dto.models import *
from controller.dto.models.request_dto import RequestDTO
from controller.dto.models.response_dto import *
from service.blocks_filter.blocks_filter_service import *


def init_routes(app):
    @app.get("/actuator")
    async def actuator():
        return {"status": "UP"}

    @app.post("/get_transactions")
    async def get_transactions(request: RequestDTO):
        transactions = await get_data(request)
        transactions_dto = []
        if len(transactions) < request.entities_limit:
            return {"error": "Invalid entities limit value"}
        for i in range(request.entities_limit):
            try:
                transactions_dto.append(
                    TransactionDTO.get_transaction(transactions[i].get_timestep(), transactions[i].get_block_number(),
                                                   transactions[i].get_receiver(), transactions[i].get_sender(),
                                                   transactions[i].get_value()))
            except Exception as e:
                print(e)

        paginated_data = [transactions_dto[i:i + request.offset] for i in
                          range(0, len(transactions_dto), request.offset)]

        return ResponseDTO.get_response(request.entities_limit, paginated_data)
