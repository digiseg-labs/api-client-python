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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from digiseg_api.models.measurement_client_item import MeasurementClientItem
from digiseg_api.models.measurement_event_links import MeasurementEventLinks
from digiseg_api.models.measurement_event_set import MeasurementEventSet
from digiseg_api.models.measurement_integration_platform import MeasurementIntegrationPlatform
from digiseg_api.models.study_ingestion_status import StudyIngestionStatus
from digiseg_api.models.study_lifecycle_stage import StudyLifecycleStage
from digiseg_api.models.study_summary_stats import StudySummaryStats
from typing import Optional, Set
from typing_extensions import Self

class StudyCreation(BaseModel):
    """
    StudyCreation
    """ # noqa: E501
    name: StrictStr
    labels: Optional[List[StrictStr]] = Field(default=None, description="A set of labels that users can use to categorize their measurements. Can be used to indicate type of study, customer names or other traits. ")
    account_id: Optional[StrictStr] = Field(default=None, description="The ID of the account that owns this study")
    start_date: Optional[datetime] = Field(default=None, description="The date for which the study and its data ingestion will start")
    end_date: Optional[datetime] = Field(default=None, description="The date for which the study and its data ingestion will end")
    life_cycle_stage: Optional[StudyLifecycleStage] = None
    ingestion_status: Optional[StudyIngestionStatus] = None
    summary_stats: Optional[StudySummaryStats] = None
    client: Optional[MeasurementClientItem] = None
    event_links: Optional[MeasurementEventLinks] = None
    event_cap: Optional[StrictInt] = Field(default=None, description="If present, an upper limit on the number of events that will be processed in this study.")
    banner_image_url: Optional[StrictStr] = Field(default=None, description="The URL to a banner image for the study. Note that the banner image is used only for Digiseg study reporting and presentation, it does NOT represent any delivered banner ad creatives or similar. ")
    integration_platform: Optional[MeasurementIntegrationPlatform] = None
    is_example: Optional[StrictBool] = Field(default=None, description="Determines if the study is an example study, used to demonstrate product capabilities")
    event_set: MeasurementEventSet
    client_id: Optional[StrictStr] = Field(default=None, description="The ID of the measurement client that this study is for")
    __properties: ClassVar[List[str]] = ["name", "labels", "account_id", "start_date", "end_date", "life_cycle_stage", "ingestion_status", "summary_stats", "client", "event_links", "event_cap", "banner_image_url", "integration_platform", "is_example", "event_set", "client_id"]

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
        """Create an instance of StudyCreation from a JSON string"""
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
            "account_id",
            "banner_image_url",
            "is_example",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of summary_stats
        if self.summary_stats:
            _dict['summary_stats'] = self.summary_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client
        if self.client:
            _dict['client'] = self.client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event_links
        if self.event_links:
            _dict['event_links'] = self.event_links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of integration_platform
        if self.integration_platform:
            _dict['integration_platform'] = self.integration_platform.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StudyCreation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "labels": obj.get("labels"),
            "account_id": obj.get("account_id"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "life_cycle_stage": obj.get("life_cycle_stage"),
            "ingestion_status": obj.get("ingestion_status"),
            "summary_stats": StudySummaryStats.from_dict(obj["summary_stats"]) if obj.get("summary_stats") is not None else None,
            "client": MeasurementClientItem.from_dict(obj["client"]) if obj.get("client") is not None else None,
            "event_links": MeasurementEventLinks.from_dict(obj["event_links"]) if obj.get("event_links") is not None else None,
            "event_cap": obj.get("event_cap"),
            "banner_image_url": obj.get("banner_image_url"),
            "integration_platform": MeasurementIntegrationPlatform.from_dict(obj["integration_platform"]) if obj.get("integration_platform") is not None else None,
            "is_example": obj.get("is_example"),
            "event_set": obj.get("event_set"),
            "client_id": obj.get("client_id")
        })
        return _obj


