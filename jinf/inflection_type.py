import enum


class InflectionType(enum.Enum):
    BOIN_DOSHI = "母音動詞"
    SHIIN_DOSHI_KAGYO = "子音動詞カ行"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
