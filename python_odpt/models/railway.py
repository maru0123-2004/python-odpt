from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.railway_type import RailwayType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle
    from ..models.railway_ugregion import RailwayUgregion
    from ..models.station_order import StationOrder


T = TypeVar("T", bound="Railway")


@_attrs_define
class Railway:
    """鉄道路線(運行系統)の情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (RailwayType): クラス名 Example: odpt:Railway.
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dctitle (str): 路線名(日本語) Example: 山手線.
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptstation_order (List['StationOrder']): 駅の順序を表すリスト Example: [{'odpt:station': 'odpt.Station:JR-
            East.Yamanote.Tokyo', 'odpt:index': 1}].
        odptrailway_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptkana (Union[Unset, str]): 路線名のよみがな(ひらがな表記) Example: やまのてせん.
        odptline_code (Union[Unset, str]): 路線コード、路線シンボル表記 e.g. 丸ノ内線=>M Example: M.
        odptcolor (Union[Unset, str]): 路線のラインカラー Example: #80C241.
        ugregion (Union[Unset, RailwayUgregion]): GeoJSON形式による地物情報
        odptascending_rail_direction (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptdescending_rail_direction (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
    """

    context: str
    id: str
    type: RailwayType
    dcdate: str
    owlsame_as: str
    dctitle: str
    odptoperator: str
    odptstation_order: List["StationOrder"]
    odptrailway_title: Union[Unset, "MultilingualTitle"] = UNSET
    odptkana: Union[Unset, str] = UNSET
    odptline_code: Union[Unset, str] = UNSET
    odptcolor: Union[Unset, str] = UNSET
    ugregion: Union[Unset, "RailwayUgregion"] = UNSET
    odptascending_rail_direction: Union[Unset, str] = UNSET
    odptdescending_rail_direction: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        dctitle = self.dctitle

        odptoperator = self.odptoperator

        odptstation_order = []
        for odptstation_order_item_data in self.odptstation_order:
            odptstation_order_item = odptstation_order_item_data.to_dict()
            odptstation_order.append(odptstation_order_item)

        odptrailway_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptrailway_title, Unset):
            odptrailway_title = self.odptrailway_title.to_dict()

        odptkana = self.odptkana

        odptline_code = self.odptline_code

        odptcolor = self.odptcolor

        ugregion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ugregion, Unset):
            ugregion = self.ugregion.to_dict()

        odptascending_rail_direction = self.odptascending_rail_direction

        odptdescending_rail_direction = self.odptdescending_rail_direction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "dc:date": dcdate,
                "owl:sameAs": owlsame_as,
                "dc:title": dctitle,
                "odpt:operator": odptoperator,
                "odpt:stationOrder": odptstation_order,
            }
        )
        if odptrailway_title is not UNSET:
            field_dict["odpt:railwayTitle"] = odptrailway_title
        if odptkana is not UNSET:
            field_dict["odpt:kana"] = odptkana
        if odptline_code is not UNSET:
            field_dict["odpt:lineCode"] = odptline_code
        if odptcolor is not UNSET:
            field_dict["odpt:color"] = odptcolor
        if ugregion is not UNSET:
            field_dict["ug:region"] = ugregion
        if odptascending_rail_direction is not UNSET:
            field_dict["odpt:ascendingRailDirection"] = odptascending_rail_direction
        if odptdescending_rail_direction is not UNSET:
            field_dict["odpt:descendingRailDirection"] = odptdescending_rail_direction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle
        from ..models.railway_ugregion import RailwayUgregion
        from ..models.station_order import StationOrder

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = RailwayType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        dctitle = d.pop("dc:title")

        odptoperator = d.pop("odpt:operator")

        odptstation_order = []
        _odptstation_order = d.pop("odpt:stationOrder")
        for odptstation_order_item_data in _odptstation_order:
            odptstation_order_item = StationOrder.from_dict(odptstation_order_item_data)

            odptstation_order.append(odptstation_order_item)

        _odptrailway_title = d.pop("odpt:railwayTitle", UNSET)
        odptrailway_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptrailway_title, Unset):
            odptrailway_title = UNSET
        else:
            odptrailway_title = MultilingualTitle.from_dict(_odptrailway_title)

        odptkana = d.pop("odpt:kana", UNSET)

        odptline_code = d.pop("odpt:lineCode", UNSET)

        odptcolor = d.pop("odpt:color", UNSET)

        _ugregion = d.pop("ug:region", UNSET)
        ugregion: Union[Unset, RailwayUgregion]
        if isinstance(_ugregion, Unset):
            ugregion = UNSET
        else:
            ugregion = RailwayUgregion.from_dict(_ugregion)

        odptascending_rail_direction = d.pop("odpt:ascendingRailDirection", UNSET)

        odptdescending_rail_direction = d.pop("odpt:descendingRailDirection", UNSET)

        railway = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            dctitle=dctitle,
            odptoperator=odptoperator,
            odptstation_order=odptstation_order,
            odptrailway_title=odptrailway_title,
            odptkana=odptkana,
            odptline_code=odptline_code,
            odptcolor=odptcolor,
            ugregion=ugregion,
            odptascending_rail_direction=odptascending_rail_direction,
            odptdescending_rail_direction=odptdescending_rail_direction,
        )

        railway.additional_properties = d
        return railway

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
