# this file defines the base response class
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel


class ResponseBase(BaseModel):
    code: int
    message: str
    data: Optional[Union[List, Dict, Any]] = None
