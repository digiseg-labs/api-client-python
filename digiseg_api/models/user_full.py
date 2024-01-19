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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from digiseg_api.models.user_account_role import UserAccountRole
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserFull(BaseModel):
    """
    UserFull
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique ID for the object")
    email: Optional[StrictStr] = Field(default=None, description="The email of the user (used as username when authenticating with password)")
    name: Optional[StrictStr] = Field(default=None, description="Human readable name of the user")
    roles: Optional[List[UserAccountRole]] = Field(default=None, description="The roles that the user has within the account")
    avatar_url: Optional[StrictStr] = Field(default=None, description="The URL to an avatar of the user")
    account_id: Optional[StrictStr] = Field(default=None, description="ID of the account that this user pertains to")
    is_super_admin: Optional[StrictBool] = Field(default=None, description="Determines if the user is a super admin of Digiseg API services")
    created_at: Optional[datetime] = Field(default=None, description="Date and time of the object creation")
    created_by: Optional[StrictStr] = Field(default=None, description="ID of the user who created the object")
    updated_at: Optional[datetime] = Field(default=None, description="Date and time of the latest update to the object")
    updated_by: Optional[StrictStr] = Field(default=None, description="ID of the user who last updated the object")
    __properties: ClassVar[List[str]] = ["id", "email", "name", "roles", "avatar_url", "account_id", "is_super_admin", "created_at", "created_by", "updated_at", "updated_by"]

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
        """Create an instance of UserFull from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserFull from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "name": obj.get("name"),
            "roles": obj.get("roles"),
            "avatar_url": obj.get("avatar_url"),
            "account_id": obj.get("account_id"),
            "is_super_admin": obj.get("is_super_admin"),
            "created_at": obj.get("created_at"),
            "created_by": obj.get("created_by"),
            "updated_at": obj.get("updated_at"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


