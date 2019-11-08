# server.py
#
# 一个简单的概念证明服务器，仅供内部使用。
# 使用asnycio有效地处理并发连接。
#
# 服务器实现以下协议：
# 1）从客户端读取标头
# 2）如果标题可以验证，请阅读剩余的消息
# 否则丢弃消息并关闭连接
# 3）完成要求的工作，并将验证发送回客户端。
# 必须通过header_tool生成新的头。
# 4）关闭连接
import nats.aio.client
import asyncio
import ssl
import platform
import signal

HEADER_BUFFER_SIZE = 36
channel = '工人'


class MyServer:
	def __init__(self, host: str = '127.0.0.1', port: int = 8888, nats_host: str = '127.0.0.1'):
		self._host = host
		self._port = port
		# self.nats = None
		# self._nats_host = nats_host

	async def run(self) -> None:
		'''
		run（）将服务器绑定到提供的主机和端口，并开始处理传入的连接。
		'''
		context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
		path = './cert'
		context.load_cert_chain(certfile=path + '/mycert.crt', keyfile=path + '/rsa_private.key', password='lukseun1')
		context.check_hostname = False
		server = await asyncio.start_server(self._handle_connection, self._host, self._port, ssl=context)
		print(f'启动的服务器IP和端口：{server.sockets[0].getsockname()}')
		async with server:
			await server.serve_forever()  # 挂起服务器

	# async def init(self):
	# 	self.nats = nats.aio.client.Client()
	# 	await self.nats.connect(self._nats_host, max_reconnect_attempts=1)
	# 	if platform.system() != 'Windows':
	# 		print('Windows')
	# 		# asyncio.get_running_loop().add_signal_handler(signal.SIGINT, lambda: asyncio.create_task(self.shutdown()))
	#
	# async def start(self):
	# 	await self.init()
	# 	print(f'目前的操作工人: {channel}')
	# 	self.sid = await self.nats.subscribe(channel, 'workers', self.process_job)
	# 	await asyncio.sleep(1)
	# 	await self.nats.flush()

	async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
		'''
		_handle_connection（）根据在文件顶部定义的协议。
		'''
		# message = await reader.read(HEADER_BUFFER_SIZE)
		message = await reader.readline()
		print(f'收到的信息：{message}')
		print(f'收到的信息：{message.decode()}')
		writer.write(('{"方法":"你好"}' + '\r\n').encode())
		await writer.drain()
		print(f'来自客户端的IP和端口：{writer.get_extra_info("peername")}')
		writer.close()


async def main() -> None:
	server = MyServer()
	await server.run()

if __name__ == '__main__':
	asyncio.run(main())
