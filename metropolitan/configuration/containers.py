import datetime
import enum
from dataclasses import dataclass
from pathlib import Path
from typing import List
from typing import Optional
from typing import Union


class OrderBy(enum.Enum):
    TITLE = enum.auto()
    DATE = enum.auto()
    DATE_INVERTED = enum.auto()
    NATIVE = enum.auto()


@dataclass
class MetroPostMedia:
    title: Optional[str]
    description: Optional[str]
    image: Union[str, Path]
    embed: str
    datetime: Union[datetime.date, datetime.datetime]


@dataclass
class MetroPost:
    slug: str
    title: Optional[str]
    subtitle: Optional[str]
    unlist: bool
    media: List[MetroPostMedia]


@dataclass
class MetroMediaLicense:
    name: str
    link: str
    badge: str


@dataclass
class MetroMediaImagesSizes:
    desktop: int
    mobile: int
    preview: int


@dataclass
class MetroMediaImage:
    sizes: MetroMediaImagesSizes
    link_original: bool
    force_download: bool


@dataclass
class MetroMedia:
    license: MetroMediaLicense
    image: MetroMediaImage


@dataclass
class MetroSettings:

    title: str
    base_url: str
    source: Path
    output: Path
    theme: str
    orderby: OrderBy
    media: MetroMedia
    posts: List[MetroPost]
