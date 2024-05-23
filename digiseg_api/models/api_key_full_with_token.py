# coding: utf-8

"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  Digiseg audiences are grouped into private and business audiences. In each group there are categories that then contain the audiences. The API endpoints that communicate audiences and household characteristics, audience codes are being used.  The following table can be used as a reference for audience codes. Note that Digiseg will at times update names of audiences for purposes of internationalization, clarity or other such purposes - but the codes will remain as-is and should be considered a stable point of reference for the audience.  | Group | Category | Audience Code | Audience Name | |-------|----------|---------------|---------------| | private | home_type | a1 | Apartment | |  |  | a2 | House | |  | savings | b1 | No Savings | |  |  | b2 | Smaller Savings | |  |  | b3 | Larger Savings | |  | lifecycle | c1 | Young couples and singles | |  |  | c2 | Early family life | |  |  | c3 | Middle-aged families | |  |  | c4 | Mature families | |  |  | c5 | Pensioners | |  | cars | d1 | No cars | |  |  | d2 | 1 car | |  |  | d3 | 2 or more cars | |  | children | e1 | No children | |  |  | e2 | 1 child | |  |  | e3 | 2 or more children | |  | education | f1 | Basic | |  |  | f2 | Medium | |  |  | f3 | Higher | |  | neighbourhood_type | g1 | Countryside | |  |  | g2 | Village | |  |  | g3 | Suburban | |  |  | g4 | City | |  | income | h1 | Lowest 20% | |  |  | h2 | Lowest 20-40% | |  |  | h3 | Middle 40-60% | |  |  | h4 | Highest 60-80% | |  |  | h5 | Top 20% | |  | home_ownership | j1 | Rent | |  |  | j2 | Own | |  | building_age | k1 | Pre 1945 | |  |  | k2 | 1945-1989 | |  |  | k3 | 1990 until today | |  | living_space | l1 | Small | |  |  | l2 | Medium | |  |  | l3 | Large | |  | tech_level | n1 | Basic | |  |  | n2 | Medium | |  |  | n3 | High | | business | size | ba1 | Small Business | |  |  | ba2 | Medium Business | |  |  | ba3 | Larger Business |  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from digiseg_api.models.api_key_status import ApiKeyStatus
from digiseg_api.models.permission_scopes import PermissionScopes
from typing import Optional, Set
from typing_extensions import Self

class ApiKeyFullWithToken(BaseModel):
    """
    ApiKeyFullWithToken
    """ # noqa: E501
    token: Optional[StrictStr] = Field(default=None, description="The actual API key token to use with the `X-API-KEY` header to authenticate with the key")
    id: Optional[StrictStr] = Field(default=None, description="Unique ID for the object")
    name: Optional[StrictStr] = Field(default=None, description="Human readable name of the API key")
    status: Optional[ApiKeyStatus] = None
    expires_at: Optional[datetime] = Field(default=None, description="Optional date/time that the key will expire")
    user_id: Optional[StrictStr] = Field(default=None, description="The ID of the API key's user. ")
    account_id: Optional[StrictStr] = Field(default=None, description="The ID of account that the API key is associated with. ")
    last_used_at: Optional[datetime] = Field(default=None, description="The approximate last time that the API key was used to authenticate API requests")
    token_prefix: Optional[StrictStr] = Field(default=None, description="A prefix of the API key")
    scopes: Optional[PermissionScopes] = None
    created_at: Optional[datetime] = Field(default=None, description="Date and time of the object creation")
    created_by: Optional[StrictStr] = Field(default=None, description="ID of the user who created the object")
    updated_at: Optional[datetime] = Field(default=None, description="Date and time of the latest update to the object")
    updated_by: Optional[StrictStr] = Field(default=None, description="ID of the user who last updated the object")
    __properties: ClassVar[List[str]] = ["token", "id", "name", "status", "expires_at", "user_id", "account_id", "last_used_at", "token_prefix", "scopes", "created_at", "created_by", "updated_at", "updated_by"]

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
        """Create an instance of ApiKeyFullWithToken from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "user_id",
            "last_used_at",
            "token_prefix",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of scopes
        if self.scopes:
            _dict['scopes'] = self.scopes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiKeyFullWithToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token": obj.get("token"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "expires_at": obj.get("expires_at"),
            "user_id": obj.get("user_id"),
            "account_id": obj.get("account_id"),
            "last_used_at": obj.get("last_used_at"),
            "token_prefix": obj.get("token_prefix"),
            "scopes": PermissionScopes.from_dict(obj["scopes"]) if obj.get("scopes") is not None else None,
            "created_at": obj.get("created_at"),
            "created_by": obj.get("created_by"),
            "updated_at": obj.get("updated_at"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


