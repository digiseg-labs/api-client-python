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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from digiseg_api.models.account_subscription_item import AccountSubscriptionItem
from digiseg_api.models.company_size import CompanySize
from digiseg_api.models.plan_feature_set import PlanFeatureSet
from typing import Optional, Set
from typing_extensions import Self

class AccountItem(BaseModel):
    """
    AccountItem
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique ID for the object")
    name: Optional[StrictStr] = Field(default=None, description="Human readable name of the account")
    logo_url: Optional[StrictStr] = Field(default=None, description="The URL to the logo of the account")
    website_url: Optional[StrictStr] = Field(default=None, description="URL of the account's primary website")
    billing_country: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, description="Country code of the account. Requires `owner` role to change.")
    company_type: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="The type of company that the account represents. Note that for forward-compatibility the data type here is simply a string. The values, if present, will however typically originate from the `CompanyType` enum. ")
    company_size: Optional[CompanySize] = None
    has_clients: Optional[StrictBool] = Field(default=None, description="Determines whether the account has clients that they work for, or if their activities are for themselves.")
    slug: Optional[Annotated[str, Field(min_length=4, strict=True, max_length=12)]] = Field(default=None, description="A short human-readable name to identify the account. Must be lower-case and between 4 and 16 characters.")
    feature_set: Optional[PlanFeatureSet] = None
    subscriptions: Optional[List[AccountSubscriptionItem]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "logo_url", "website_url", "billing_country", "company_type", "company_size", "has_clients", "slug", "feature_set", "subscriptions"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-z]{4,16}$", value):
            raise ValueError(r"must validate the regular expression /^[a-z]{4,16}$/")
        return value

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
        """Create an instance of AccountItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "subscriptions",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of feature_set
        if self.feature_set:
            _dict['feature_set'] = self.feature_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subscriptions (list)
        _items = []
        if self.subscriptions:
            for _item in self.subscriptions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subscriptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "logo_url": obj.get("logo_url"),
            "website_url": obj.get("website_url"),
            "billing_country": obj.get("billing_country"),
            "company_type": obj.get("company_type"),
            "company_size": obj.get("company_size"),
            "has_clients": obj.get("has_clients"),
            "slug": obj.get("slug"),
            "feature_set": PlanFeatureSet.from_dict(obj["feature_set"]) if obj.get("feature_set") is not None else None,
            "subscriptions": [AccountSubscriptionItem.from_dict(_item) for _item in obj["subscriptions"]] if obj.get("subscriptions") is not None else None
        })
        return _obj


