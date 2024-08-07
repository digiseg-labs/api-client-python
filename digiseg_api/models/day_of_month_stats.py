# coding: utf-8

"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-ts\">     <i class=\"api-client-sdk-logo devicon-typescript-plain\"></i>     <p>API client for TypeScript</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  Digiseg audiences are grouped into private and business audiences. In each group there are categories that then contain the audiences. The API endpoints that communicate audiences and household characteristics, audience codes are being used.  The following table can be used as a reference for audience codes. Note that Digiseg will at times update names of audiences for purposes of internationalization, clarity or other such purposes - but the codes will remain as-is and should be considered a stable point of reference for the audience.  | Group | Category | Audience Code | Audience Name | |-------|----------|---------------|---------------| | private | home_type | a1 | Apartment | |  |  | a2 | House | |  | savings | b1 | No Savings | |  |  | b2 | Smaller Savings | |  |  | b3 | Larger Savings | |  | lifecycle | c1 | Young couples and singles | |  |  | c2 | Early family life | |  |  | c3 | Middle-aged families | |  |  | c4 | Mature families | |  |  | c5 | Pensioners / Retirees | |  | cars | d1 | No cars | |  |  | d2 | 1 car | |  |  | d3 | 2 or more cars | |  | children | e1 | No children | |  |  | e2 | 1 child | |  |  | e3 | 2 or more children | |  | education | f1 | Basic | |  |  | f2 | Medium | |  |  | f3 | Higher | |  | neighbourhood_type | g1 | Countryside | |  |  | g2 | Village | |  |  | g3 | Suburban | |  |  | g4 | City | |  | income | h1 | Lowest 20% | |  |  | h2 | Lowest 20-40% | |  |  | h3 | Middle 40-60% | |  |  | h4 | Highest 60-80% | |  |  | h5 | Top 20% | |  | home_ownership | j1 | Rent | |  |  | j2 | Own | |  | building_age | k1 | Pre 1945 | |  |  | k2 | 1945-1989 | |  |  | k3 | 1990 until today | |  | living_space | l1 | Small | |  |  | l2 | Medium | |  |  | l3 | Large | |  | tech_level | n1 | Basic | |  |  | n2 | Medium | |  |  | n3 | High | | business | size | ba1 | Small Business | |  |  | ba2 | Medium Business | |  |  | ba3 | Larger Business |  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from digiseg_api.models.measurements_container import MeasurementsContainer
from typing import Optional, Set
from typing_extensions import Self

class DayOfMonthStats(BaseModel):
    """
    Contains statistics about the day of the month that study activity has been measured. The time zone used to record these measurements is the time zone of the measured user, or UTC if the user's location cannot be resolved. 
    """ # noqa: E501
    var_0: Optional[MeasurementsContainer] = Field(default=None, alias="0")
    var_1: Optional[MeasurementsContainer] = Field(default=None, alias="1")
    var_2: Optional[MeasurementsContainer] = Field(default=None, alias="2")
    var_3: Optional[MeasurementsContainer] = Field(default=None, alias="3")
    var_4: Optional[MeasurementsContainer] = Field(default=None, alias="4")
    var_5: Optional[MeasurementsContainer] = Field(default=None, alias="5")
    var_6: Optional[MeasurementsContainer] = Field(default=None, alias="6")
    var_7: Optional[MeasurementsContainer] = Field(default=None, alias="7")
    var_8: Optional[MeasurementsContainer] = Field(default=None, alias="8")
    var_9: Optional[MeasurementsContainer] = Field(default=None, alias="9")
    var_10: Optional[MeasurementsContainer] = Field(default=None, alias="10")
    var_11: Optional[MeasurementsContainer] = Field(default=None, alias="11")
    var_12: Optional[MeasurementsContainer] = Field(default=None, alias="12")
    var_13: Optional[MeasurementsContainer] = Field(default=None, alias="13")
    var_14: Optional[MeasurementsContainer] = Field(default=None, alias="14")
    var_15: Optional[MeasurementsContainer] = Field(default=None, alias="15")
    var_16: Optional[MeasurementsContainer] = Field(default=None, alias="16")
    var_17: Optional[MeasurementsContainer] = Field(default=None, alias="17")
    var_18: Optional[MeasurementsContainer] = Field(default=None, alias="18")
    var_19: Optional[MeasurementsContainer] = Field(default=None, alias="19")
    var_20: Optional[MeasurementsContainer] = Field(default=None, alias="20")
    var_21: Optional[MeasurementsContainer] = Field(default=None, alias="21")
    var_22: Optional[MeasurementsContainer] = Field(default=None, alias="22")
    var_23: Optional[MeasurementsContainer] = Field(default=None, alias="23")
    var_24: Optional[MeasurementsContainer] = Field(default=None, alias="24")
    var_25: Optional[MeasurementsContainer] = Field(default=None, alias="25")
    var_26: Optional[MeasurementsContainer] = Field(default=None, alias="26")
    var_27: Optional[MeasurementsContainer] = Field(default=None, alias="27")
    var_28: Optional[MeasurementsContainer] = Field(default=None, alias="28")
    var_29: Optional[MeasurementsContainer] = Field(default=None, alias="29")
    var_30: Optional[MeasurementsContainer] = Field(default=None, alias="30")
    var_31: Optional[MeasurementsContainer] = Field(default=None, alias="31")
    __properties: ClassVar[List[str]] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DayOfMonthStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_0
        if self.var_0:
            _dict['0'] = self.var_0.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_1
        if self.var_1:
            _dict['1'] = self.var_1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_2
        if self.var_2:
            _dict['2'] = self.var_2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_3
        if self.var_3:
            _dict['3'] = self.var_3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_4
        if self.var_4:
            _dict['4'] = self.var_4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_5
        if self.var_5:
            _dict['5'] = self.var_5.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_6
        if self.var_6:
            _dict['6'] = self.var_6.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_7
        if self.var_7:
            _dict['7'] = self.var_7.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_8
        if self.var_8:
            _dict['8'] = self.var_8.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_9
        if self.var_9:
            _dict['9'] = self.var_9.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_10
        if self.var_10:
            _dict['10'] = self.var_10.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_11
        if self.var_11:
            _dict['11'] = self.var_11.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_12
        if self.var_12:
            _dict['12'] = self.var_12.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_13
        if self.var_13:
            _dict['13'] = self.var_13.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_14
        if self.var_14:
            _dict['14'] = self.var_14.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_15
        if self.var_15:
            _dict['15'] = self.var_15.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_16
        if self.var_16:
            _dict['16'] = self.var_16.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_17
        if self.var_17:
            _dict['17'] = self.var_17.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_18
        if self.var_18:
            _dict['18'] = self.var_18.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_19
        if self.var_19:
            _dict['19'] = self.var_19.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_20
        if self.var_20:
            _dict['20'] = self.var_20.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_21
        if self.var_21:
            _dict['21'] = self.var_21.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_22
        if self.var_22:
            _dict['22'] = self.var_22.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_23
        if self.var_23:
            _dict['23'] = self.var_23.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_24
        if self.var_24:
            _dict['24'] = self.var_24.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_25
        if self.var_25:
            _dict['25'] = self.var_25.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_26
        if self.var_26:
            _dict['26'] = self.var_26.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_27
        if self.var_27:
            _dict['27'] = self.var_27.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_28
        if self.var_28:
            _dict['28'] = self.var_28.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_29
        if self.var_29:
            _dict['29'] = self.var_29.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_30
        if self.var_30:
            _dict['30'] = self.var_30.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_31
        if self.var_31:
            _dict['31'] = self.var_31.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DayOfMonthStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "0": MeasurementsContainer.from_dict(obj["0"]) if obj.get("0") is not None else None,
            "1": MeasurementsContainer.from_dict(obj["1"]) if obj.get("1") is not None else None,
            "2": MeasurementsContainer.from_dict(obj["2"]) if obj.get("2") is not None else None,
            "3": MeasurementsContainer.from_dict(obj["3"]) if obj.get("3") is not None else None,
            "4": MeasurementsContainer.from_dict(obj["4"]) if obj.get("4") is not None else None,
            "5": MeasurementsContainer.from_dict(obj["5"]) if obj.get("5") is not None else None,
            "6": MeasurementsContainer.from_dict(obj["6"]) if obj.get("6") is not None else None,
            "7": MeasurementsContainer.from_dict(obj["7"]) if obj.get("7") is not None else None,
            "8": MeasurementsContainer.from_dict(obj["8"]) if obj.get("8") is not None else None,
            "9": MeasurementsContainer.from_dict(obj["9"]) if obj.get("9") is not None else None,
            "10": MeasurementsContainer.from_dict(obj["10"]) if obj.get("10") is not None else None,
            "11": MeasurementsContainer.from_dict(obj["11"]) if obj.get("11") is not None else None,
            "12": MeasurementsContainer.from_dict(obj["12"]) if obj.get("12") is not None else None,
            "13": MeasurementsContainer.from_dict(obj["13"]) if obj.get("13") is not None else None,
            "14": MeasurementsContainer.from_dict(obj["14"]) if obj.get("14") is not None else None,
            "15": MeasurementsContainer.from_dict(obj["15"]) if obj.get("15") is not None else None,
            "16": MeasurementsContainer.from_dict(obj["16"]) if obj.get("16") is not None else None,
            "17": MeasurementsContainer.from_dict(obj["17"]) if obj.get("17") is not None else None,
            "18": MeasurementsContainer.from_dict(obj["18"]) if obj.get("18") is not None else None,
            "19": MeasurementsContainer.from_dict(obj["19"]) if obj.get("19") is not None else None,
            "20": MeasurementsContainer.from_dict(obj["20"]) if obj.get("20") is not None else None,
            "21": MeasurementsContainer.from_dict(obj["21"]) if obj.get("21") is not None else None,
            "22": MeasurementsContainer.from_dict(obj["22"]) if obj.get("22") is not None else None,
            "23": MeasurementsContainer.from_dict(obj["23"]) if obj.get("23") is not None else None,
            "24": MeasurementsContainer.from_dict(obj["24"]) if obj.get("24") is not None else None,
            "25": MeasurementsContainer.from_dict(obj["25"]) if obj.get("25") is not None else None,
            "26": MeasurementsContainer.from_dict(obj["26"]) if obj.get("26") is not None else None,
            "27": MeasurementsContainer.from_dict(obj["27"]) if obj.get("27") is not None else None,
            "28": MeasurementsContainer.from_dict(obj["28"]) if obj.get("28") is not None else None,
            "29": MeasurementsContainer.from_dict(obj["29"]) if obj.get("29") is not None else None,
            "30": MeasurementsContainer.from_dict(obj["30"]) if obj.get("30") is not None else None,
            "31": MeasurementsContainer.from_dict(obj["31"]) if obj.get("31") is not None else None
        })
        return _obj


