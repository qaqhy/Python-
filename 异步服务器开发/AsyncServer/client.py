# client.py
#
# 一个简单的概念证明客户端，仅供内部使用。
# 使用asyncio处理向服务器发送和接收消息。
#
import sys
sys.path.insert(0, '..')

import asyncio
import json


class MyClient:
	def __init__(self, client_type: str = '', host: str = '127.0.0.1', port: int = 8888):
		self._host = host
		self._port = port

	async def send_message(self, message: str) -> dict:
		'''
		send_message（）将给定的消息发送到服务器，并
		返回解码后的回调响应
		'''
		# 启动异步连接open_connection
		reader, writer = await asyncio.open_connection(self._host, self._port)
		# 编码字符串message
		writer.write((message + '\r\n').encode())
		# 刷新写缓冲区。预期用途是写
		await writer.drain()
		# 读数据，读到以separator结尾的数据
		raw = await reader.readuntil(separator=b'\r\n')
		# 解码字符串，并删除空字符串
		resp = raw.decode().strip()
		# 关闭写操作
		writer.close()
		# 保持等待，直到底层连接被关闭，应该在close()后调用此方法。
		await writer.wait_closed()
		if resp != '':
			data = json.loads(resp, encoding='utf-8')
			return data
		return {}


async def main():
	myclient = MyClient()
	for i in range(0, 100):
		print(await myclient.send_message('{"方法":"客户端测试", "数据" : {"数据键" : "数据值"}}'))


if __name__ == "__main__":
	asyncio.run(main())
