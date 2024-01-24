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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from digiseg_api.models.audience_category_stats import AudienceCategoryStats
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PrivateAudienceStatsAudienceCategories(BaseModel):
    """
    PrivateAudienceStatsAudienceCategories
    """ # noqa: E501
    home_type: AudienceCategoryStats
    savings: AudienceCategoryStats
    lifecycle: AudienceCategoryStats
    cars: AudienceCategoryStats
    children: AudienceCategoryStats
    education: AudienceCategoryStats
    neighbourhood_type: AudienceCategoryStats
    income: AudienceCategoryStats
    home_ownership: AudienceCategoryStats
    building_age: AudienceCategoryStats
    living_space: AudienceCategoryStats
    tech_level: AudienceCategoryStats
    __properties: ClassVar[List[str]] = ["home_type", "savings", "lifecycle", "cars", "children", "education", "neighbourhood_type", "income", "home_ownership", "building_age", "living_space", "tech_level"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
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
        """Create an instance of PrivateAudienceStatsAudienceCategories from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of home_type
        if self.home_type:
            _dict['home_type'] = self.home_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of savings
        if self.savings:
            _dict['savings'] = self.savings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lifecycle
        if self.lifecycle:
            _dict['lifecycle'] = self.lifecycle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cars
        if self.cars:
            _dict['cars'] = self.cars.to_dict()
        # override the default output from pydantic by calling `to_dict()` of children
        if self.children:
            _dict['children'] = self.children.to_dict()
        # override the default output from pydantic by calling `to_dict()` of education
        if self.education:
            _dict['education'] = self.education.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neighbourhood_type
        if self.neighbourhood_type:
            _dict['neighbourhood_type'] = self.neighbourhood_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of income
        if self.income:
            _dict['income'] = self.income.to_dict()
        # override the default output from pydantic by calling `to_dict()` of home_ownership
        if self.home_ownership:
            _dict['home_ownership'] = self.home_ownership.to_dict()
        # override the default output from pydantic by calling `to_dict()` of building_age
        if self.building_age:
            _dict['building_age'] = self.building_age.to_dict()
        # override the default output from pydantic by calling `to_dict()` of living_space
        if self.living_space:
            _dict['living_space'] = self.living_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tech_level
        if self.tech_level:
            _dict['tech_level'] = self.tech_level.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PrivateAudienceStatsAudienceCategories from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "home_type": AudienceCategoryStats.from_dict(obj.get("home_type")) if obj.get("home_type") is not None else None,
            "savings": AudienceCategoryStats.from_dict(obj.get("savings")) if obj.get("savings") is not None else None,
            "lifecycle": AudienceCategoryStats.from_dict(obj.get("lifecycle")) if obj.get("lifecycle") is not None else None,
            "cars": AudienceCategoryStats.from_dict(obj.get("cars")) if obj.get("cars") is not None else None,
            "children": AudienceCategoryStats.from_dict(obj.get("children")) if obj.get("children") is not None else None,
            "education": AudienceCategoryStats.from_dict(obj.get("education")) if obj.get("education") is not None else None,
            "neighbourhood_type": AudienceCategoryStats.from_dict(obj.get("neighbourhood_type")) if obj.get("neighbourhood_type") is not None else None,
            "income": AudienceCategoryStats.from_dict(obj.get("income")) if obj.get("income") is not None else None,
            "home_ownership": AudienceCategoryStats.from_dict(obj.get("home_ownership")) if obj.get("home_ownership") is not None else None,
            "building_age": AudienceCategoryStats.from_dict(obj.get("building_age")) if obj.get("building_age") is not None else None,
            "living_space": AudienceCategoryStats.from_dict(obj.get("living_space")) if obj.get("living_space") is not None else None,
            "tech_level": AudienceCategoryStats.from_dict(obj.get("tech_level")) if obj.get("tech_level") is not None else None
        })
        return _obj


