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

class DayOfWeekStats(BaseModel):
    """
    Contains statistics about the week days that campaign activity has been measured. The time zone used to record these measurements is the time zone of the measured user, or UTC if the user's location cannot be resolved. 
    """ # noqa: E501
    monday: Optional[MeasurementsContainer] = Field(default=None, alias="Monday")
    tuesday: Optional[MeasurementsContainer] = Field(default=None, alias="Tuesday")
    wednesday: Optional[MeasurementsContainer] = Field(default=None, alias="Wednesday")
    thursday: Optional[MeasurementsContainer] = Field(default=None, alias="Thursday")
    friday: Optional[MeasurementsContainer] = Field(default=None, alias="Friday")
    saturday: Optional[MeasurementsContainer] = Field(default=None, alias="Saturday")
    sunday: Optional[MeasurementsContainer] = Field(default=None, alias="Sunday")
    __properties: ClassVar[List[str]] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
        """Create an instance of DayOfWeekStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of monday
        if self.monday:
            _dict['Monday'] = self.monday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tuesday
        if self.tuesday:
            _dict['Tuesday'] = self.tuesday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wednesday
        if self.wednesday:
            _dict['Wednesday'] = self.wednesday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thursday
        if self.thursday:
            _dict['Thursday'] = self.thursday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of friday
        if self.friday:
            _dict['Friday'] = self.friday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of saturday
        if self.saturday:
            _dict['Saturday'] = self.saturday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sunday
        if self.sunday:
            _dict['Sunday'] = self.sunday.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DayOfWeekStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Monday": MeasurementsContainer.from_dict(obj.get("Monday")) if obj.get("Monday") is not None else None,
            "Tuesday": MeasurementsContainer.from_dict(obj.get("Tuesday")) if obj.get("Tuesday") is not None else None,
            "Wednesday": MeasurementsContainer.from_dict(obj.get("Wednesday")) if obj.get("Wednesday") is not None else None,
            "Thursday": MeasurementsContainer.from_dict(obj.get("Thursday")) if obj.get("Thursday") is not None else None,
            "Friday": MeasurementsContainer.from_dict(obj.get("Friday")) if obj.get("Friday") is not None else None,
            "Saturday": MeasurementsContainer.from_dict(obj.get("Saturday")) if obj.get("Saturday") is not None else None,
            "Sunday": MeasurementsContainer.from_dict(obj.get("Sunday")) if obj.get("Sunday") is not None else None
        })
        return _obj

