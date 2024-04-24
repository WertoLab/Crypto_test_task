import asyncio
import json

from service.CONSTS import *
from controller.dto.models.request_dto import *
import aiohttp
from datetime import datetime
from dateutil import parser
from service.blocks_filter.model import *


async def get_blocks_by_timestamp(timestamp: int, blocks_amount: int) -> dict:
    blocks = {}
    async with aiohttp.ClientSession() as session:
        while blocks_amount > len(blocks):
            async with session.get(
                    f'https://api-sepolia.etherscan.io/api?module=block&action=getblocknobytime&timestamp={timestamp}'
                    f'&closest=before&apikey={API_KEY_ETHERSCAN}') as response:
                response_dict = await response.json()
                if response_dict["status"] == '1':
                    blocks[response_dict["result"]] = [hex(int(response_dict["result"])), timestamp]
                    timestamp -= 1
    return blocks


async def get_transactions_of_blocks(blocks: dict) -> list:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for key in list(blocks.keys()):
            tasks.append(asyncio.create_task(session.get(f'https://api-sepolia.etherscan.io/api?module=proxy'
                                                         f'&action=eth_getBlockByNumber&tag'
                                                         f'={blocks[key][0]}&boolean=true&apikey={API_KEY_ETHERSCAN}')))

        responses = await asyncio.gather(*tasks)
        transactions = [await r.json() for r in responses]

        all_transactions = []
        for block_index in range(len(blocks.keys())):
            try:
                all_transactions += transactions[block_index]["result"]["transactions"]
            except:
                print("Exception occurred during transactions extraction")

    return all_transactions


async def get_data(request: RequestDTO) -> list[TransactionModel]:
    get_blocks_task = asyncio.create_task(
        get_blocks_by_timestamp(int(datetime.timestamp(parser.parse(request.datetime))), request.integer))
    blocks = await get_blocks_task
    transactions_hex = await get_transactions_of_blocks(blocks)
    transactions = list(
        map(lambda transaction: TransactionModel(transaction["blockNumber"], transaction["to"], transaction["from"],
                                                 transaction["value"],
                                                 blocks[str(int(transaction["blockNumber"], 16))][1]),
            transactions_hex))

    return transactions
