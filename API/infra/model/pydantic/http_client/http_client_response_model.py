from typing import Dict, Optional

from pydantic import BaseModel

from infra.model.pydantic.http_client.request_model import Request


class HttpClientResponseModel(BaseModel):
    headers: Optional[Dict]
    status_code: int
    payload: Optional[Dict]
    response_text: Optional[str]
    url: str
    method: str
    process_time: float
    event_request: Optional[Request]
