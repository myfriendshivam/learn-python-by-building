# Advance Data Types

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

brewing_time = datetime.now(timezone.utc).astimezone(ZoneInfo("Europe/Rome"))

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])