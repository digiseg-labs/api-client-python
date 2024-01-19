# coding: utf-8

"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  For a catalog of Digisegs audiences, refer to the [Audience list](https://digiseg.io/audiences-list).  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from digiseg_api.models.measurements_container import MeasurementsContainer
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HourOfDayStats(BaseModel):
    """
    Contains statistics about the time of day that campaign activity has been measured. The 24 hour time format is used to represent measurements for each hour. The time zone used to record these measurements is the time zone of the measured user, or UTC if the user's location cannot be resolved. 
    """ # noqa: E501
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
    var_00: Optional[MeasurementsContainer] = Field(default=None, alias="00")
    var_01: Optional[MeasurementsContainer] = Field(default=None, alias="01")
    var_02: Optional[MeasurementsContainer] = Field(default=None, alias="02")
    var_03: Optional[MeasurementsContainer] = Field(default=None, alias="03")
    var_04: Optional[MeasurementsContainer] = Field(default=None, alias="04")
    var_05: Optional[MeasurementsContainer] = Field(default=None, alias="05")
    var_06: Optional[MeasurementsContainer] = Field(default=None, alias="06")
    var_07: Optional[MeasurementsContainer] = Field(default=None, alias="07")
    var_08: Optional[MeasurementsContainer] = Field(default=None, alias="08")
    var_09: Optional[MeasurementsContainer] = Field(default=None, alias="09")
    __properties: ClassVar[List[str]] = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HourOfDayStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
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
        # override the default output from pydantic by calling `to_dict()` of var_00
        if self.var_00:
            _dict['00'] = self.var_00.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_01
        if self.var_01:
            _dict['01'] = self.var_01.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_02
        if self.var_02:
            _dict['02'] = self.var_02.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_03
        if self.var_03:
            _dict['03'] = self.var_03.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_04
        if self.var_04:
            _dict['04'] = self.var_04.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_05
        if self.var_05:
            _dict['05'] = self.var_05.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_06
        if self.var_06:
            _dict['06'] = self.var_06.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_07
        if self.var_07:
            _dict['07'] = self.var_07.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_08
        if self.var_08:
            _dict['08'] = self.var_08.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_09
        if self.var_09:
            _dict['09'] = self.var_09.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HourOfDayStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "10": MeasurementsContainer.from_dict(obj.get("10")) if obj.get("10") is not None else None,
            "11": MeasurementsContainer.from_dict(obj.get("11")) if obj.get("11") is not None else None,
            "12": MeasurementsContainer.from_dict(obj.get("12")) if obj.get("12") is not None else None,
            "13": MeasurementsContainer.from_dict(obj.get("13")) if obj.get("13") is not None else None,
            "14": MeasurementsContainer.from_dict(obj.get("14")) if obj.get("14") is not None else None,
            "15": MeasurementsContainer.from_dict(obj.get("15")) if obj.get("15") is not None else None,
            "16": MeasurementsContainer.from_dict(obj.get("16")) if obj.get("16") is not None else None,
            "17": MeasurementsContainer.from_dict(obj.get("17")) if obj.get("17") is not None else None,
            "18": MeasurementsContainer.from_dict(obj.get("18")) if obj.get("18") is not None else None,
            "19": MeasurementsContainer.from_dict(obj.get("19")) if obj.get("19") is not None else None,
            "20": MeasurementsContainer.from_dict(obj.get("20")) if obj.get("20") is not None else None,
            "21": MeasurementsContainer.from_dict(obj.get("21")) if obj.get("21") is not None else None,
            "22": MeasurementsContainer.from_dict(obj.get("22")) if obj.get("22") is not None else None,
            "23": MeasurementsContainer.from_dict(obj.get("23")) if obj.get("23") is not None else None,
            "00": MeasurementsContainer.from_dict(obj.get("00")) if obj.get("00") is not None else None,
            "01": MeasurementsContainer.from_dict(obj.get("01")) if obj.get("01") is not None else None,
            "02": MeasurementsContainer.from_dict(obj.get("02")) if obj.get("02") is not None else None,
            "03": MeasurementsContainer.from_dict(obj.get("03")) if obj.get("03") is not None else None,
            "04": MeasurementsContainer.from_dict(obj.get("04")) if obj.get("04") is not None else None,
            "05": MeasurementsContainer.from_dict(obj.get("05")) if obj.get("05") is not None else None,
            "06": MeasurementsContainer.from_dict(obj.get("06")) if obj.get("06") is not None else None,
            "07": MeasurementsContainer.from_dict(obj.get("07")) if obj.get("07") is not None else None,
            "08": MeasurementsContainer.from_dict(obj.get("08")) if obj.get("08") is not None else None,
            "09": MeasurementsContainer.from_dict(obj.get("09")) if obj.get("09") is not None else None
        })
        return _obj


