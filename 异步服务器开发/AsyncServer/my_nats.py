import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers


async def run(loop):
    nc = NATS()

    await nc.connect("demo.nats.io:4222", loop=loop)
    # await nc.connect("nats://127.0.0.1:4222", loop=loop)

    # 示例1
    # async def message_handler(msg):
    #     subject = msg.subject
    #     reply = msg.reply
    #     data = msg.data.decode()
    #     print(f"收到关于主题 '{subject} {reply}'的信息: {data}")
    #
    # # Simple publisher and async subscriber via coroutine.
    # # 简单的发布者和异步订阅通过协同程序。
    # sid = await nc.subscribe("测试主题", cb=message_handler)  # 订阅
    #
    # # Stop receiving after 2 messages.
    # # 收到两条信息后停止接收。
    # # await nc.auto_unsubscribe(sid, 2)
    # await nc.publish("测试主题", b'Hello')  # 发布
    # await nc.publish("测试主题", b'World')
    # await nc.publish("Test theme", b'!!!!!')

    # 示例2
    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print(f"收到关于主题 '{subject} {reply}'的信息: {data}")
        # 发布
        # await nc.publish(reply, b'I can help')
        await nc.publish(reply, '消息体'.encode())  # reply发布信息
        await nc.publish(subject, '消息体2'.encode())  # 方法2使用主题发布信息

    # 使用名为“workers”的队列在订阅者之间分发请求。
    # 主题  队列名  分发方法
    sid = await nc.subscribe("我的主题", "workers", message_handler)  # 订阅者

    # 发送一个请求，如果不超过1秒，则期望单个响应和触发超时。
    try:
        # response = await nc.request("测试主题", b'help me', timeout=5)
        # 队列形式收到信息做处理
        response = await nc.request("我的主题", '发送的消息主体'.encode(), timeout=5)
        print(f"收到的信息: {response.data.decode()}")
    except ErrTimeout:
        print("请求超时")

    # 删除订阅兴趣。
    await nc.unsubscribe(sid)

    # 终止与NATS的连接
    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()

