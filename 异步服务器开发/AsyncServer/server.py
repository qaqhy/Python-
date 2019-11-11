# server.py
#
# 一个简单的概念证明服务器，仅供内部使用。
# 使用asnycio有效地处理并发连接。
import asyncio
import ssl
import nats.aio.client
import aioredis

HEADER_BUFFER_SIZE = 36


class MyServer:
	def __init__(self, host: str = '127.0.0.1', port: int = 8888):
		self._host = host
		self._port = port

	async def init(self):
		self._nats = nats.aio.client.Client()  # 声明nats服务，订阅---发布
		# await self._nats.connect(self._host, max_reconnect_attempts=1)
		# await self._nats.connect("nats://127.0.0.1:4222", max_reconnect_attempts=1)
		await self._nats.connect("demo.nats.io:4222", max_reconnect_attempts=1)  # 连接


	async def run(self) -> None:
		'''
		run（）将服务器绑定到提供的主机和端口，并开始处理传入的连接。
		'''
		await self.init()
		context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
		path = './cert'
		context.load_cert_chain(certfile=path + '/mycert.crt', keyfile=path + '/rsa_private.key', password='lukseun1')
		context.check_hostname = False

		server = await asyncio.start_server(self._handle_connection, self._host, self._port, ssl=context)
		print(f'启动的服务器IP和端口：{server.sockets[0].getsockname()}')
		# asyncio.create_task(server.serve_forever())
		async with server:
			await server.serve_forever()  # 挂起服务器

	async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
		'''
		服务器被访问，需要执行的方法
		_handle_connection（）根据在文件顶部定义的协议。
		'''
		print(f'来自客户端的IP和端口：{writer.get_extra_info("peername")}')
		await self._nats.publish("我的主题", f'我的内容:{writer.get_extra_info("peername")}'.encode())  # 发布
		# message = await reader.read(HEADER_BUFFER_SIZE)
		message = await reader.readline()
		print(f'收到的信息：{message.decode()}')
		writer.write(('{"方法":"你好"}' + '\r\n').encode())
		await writer.drain()
		writer.close()



async def main() -> None:
	server = MyServer()
	await server.run()

if __name__ == '__main__':
	asyncio.run(main())
	# asyncio.run(MyServer().run())


