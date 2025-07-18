from typing import Dict, Optional, List, Union
from pydantic import BaseModel


class InputTextBlock(BaseModel):
    type: str
    text: Optional[str] = None
    styles: Optional[dict] = None
    underline: Optional[bool] = False
    highlight: Optional[str] = None
    bold: Optional[bool] = False
    italic: Optional[bool] = False

    children: Optional[List["InputTextBlock"]] = None
    attrs: Optional[Dict[str, Union[str, bool]]] = None

    level: Optional[int] = None
    start: Optional[int] = None
    #  have to check why i add this twice
    # children: Optional[List["InputTextBlock"]] = None
    # attrs: Optional[dict] = None
    link: Optional[dict] = None

    # for paragraph attributes
    textAlign: Optional[str] = None
    indent: Optional[int] = 0
    lineHeight: Optional[float] = None
    dir: Optional[str] = "auto"


InputTextBlock.update_forward_refs()
