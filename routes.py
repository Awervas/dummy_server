# aiohttpdemo_polls/routes.py
from views import index


def setup_routes(app):
    app.router.add_get('/api/v1/hello/', index)
