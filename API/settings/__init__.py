__version__ = '1.0.0'

import inject

from infra.http_client.httpx.http_client import HttpClient


def configure_http_client(binder):
    binder.bind_to_provider(
        HttpClient,
        lambda: HttpClient()
    )

adapter_binders = [
]


def configure(binder):
    configure_http_client(binder)


inject.configure(configure)