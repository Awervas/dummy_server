import argparse

from aiohttp import web

from routes import setup_routes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="aiohttp server example")
    parser.add_argument('--path', default="")
    parser.add_argument('--port', default=8082)
    args = parser.parse_args()

    app = web.Application()
    setup_routes(app)

    kwargs = {}
    if args.port:
        kwargs.update({'port': args.port})

    if args.path:
        kwargs.update({'path': args.path})

    web.run_app(app, **kwargs)