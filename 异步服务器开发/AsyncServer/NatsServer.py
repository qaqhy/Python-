# NatsServer.py
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

HEADER_BUFFER_SIZE = 36
channel = '我的主题'


class MyServer:
	def __init__(self, host: str = '127.0.0.1', port: int = 8888, nats_host: str = '127.0.0.1'):
		self._host = host
		self._port = port

		self.running = False
		self._nats = None
		self._nats_host = nats_host

	async def init(self):
		self.running = True
		self._nats = nats.aio.client.Client()
		# await self._nats.connect(self._nats_host, max_reconnect_attempts=1)
		# await self._nats.connect("nats://127.0.0.1:4222", max_reconnect_attempts=1)
		await self._nats.connect("demo.nats.io:4222", max_reconnect_attempts=1)

	async def start(self):
		await self.init()
		print(f'目前的操作主题: {channel}')
		self.sid = await self._nats.subscribe(channel, 'workers', self.process_job)  # 订阅workers队列
		while self.running:
			await asyncio.sleep(1)
			await self._nats.flush()

	async def process_job(self, job):
		response = await asyncio.wait_for(self.my_handler(), 3)
		print(f'工作内容：{job.data.decode()}')
		print(f'结果：{response}')

	async def my_handler(self):
		a = [i for i in range(100)]
		return a


if __name__ == '__main__':
	server = MyServer()
	asyncio.run(server.start())


