import enum


class InflectionForm(enum.Enum):
    GOKAN = "語幹"
    KIHON = "基本形"
    MIZEN = "未然形"
    ISHI = "意志形"
    SHORYAKU_ISHI = "省略意志形"
    MEIREI = "命令形"
    KIHON_JOKEN = "基本条件形"
    KIHON_RENYO = "基本連用形"
    TASETSU_RENYO = "タ接連用形"
    TAKE = "タ形"
    TAKE_SUIRYO = "タ系推量形"
    TAKE_SHORYAKU_SUIRYO = "タ系省略推量形"
    TAKE_JOKEN = "タ系条件形"
    TAKE_RENYO_TE = "タ系連用テ形"
    TAKE_RENYO_TARI = "タ系連用タリ形"
    TAKE_RENYO_CHA = "タ系連用チャ形"
    ONBIN_JOKEN = "音便条件形"
    BUNGO_MEIREI = "文語命令形"
    BUNGO_IZEN = "文語巳然形"
