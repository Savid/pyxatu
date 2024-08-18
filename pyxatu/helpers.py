from datetime import datetime, timezone
from pyxatu.utils import CONSTANTS


class PyXatuHelpers:
    
    def get_slot_datetime(self, slot: int, as_type: str = "str") -> int:
        slot_timestamp = CONSTANTS["GENESIS_TIME_ETH_POS"] + (slot * CONSTANTS["SECONDS_PER_SLOT"])
        slot_datetime = datetime.fromtimestamp(slot_timestamp, tz=timezone.utc)
        if as_type == "str":
            return slot_datetime.strftime('%Y-%m-%d %H:%M:%S')
        elif as_type == "int":
            return int(slot_datetime.timestamp())
            

    def get_time_in_slot(self, slot: int, ts: int) -> int:
        return ts - self.get_slot_datetime(slot, as_type = "int")*1000