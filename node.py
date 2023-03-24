import asyncio

from tageecoin.blockchain import Blockchain
from tageecoin.connections import ConnectionPool
from tageecoin.peers import P2PProtocol
from tageecoin.server import Server

blockchain = Blockchain()  # <1>
connection_pool = ConnectionPool()  # <2>

server = Server(blockchain, connection_pool, P2PProtocol)


async def main():
    # Start the server
    await server.listen()


asyncio.run(main())
