from aiohttp import web


def download_rar(request: web.Request) -> web.Response:
	path = 'D:\\SoftwarePackage\\BaiduNetdiskDownload\\21 数据分析\\'
	filename = '10-数据的合并和分组聚合.rar'
	print('下载中... ...')
	return web.Response(content_type='application/octet-stream', headers={'Content-Disposition': 'attachment;filename={}'.format(filename)}, body=open(f'{path}{filename}', 'rb').read())


def run():
	app = web.Application()
	app.router.add_get('/', download_rar)
	web.run_app(app, host='0.0.0.0', port=8880)


if __name__ == '__main__':
	run()
