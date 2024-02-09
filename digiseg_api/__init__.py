# coding: utf-8

# flake8: noqa

"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  For a catalog of Digisegs audiences, refer to the [Audience list](https://digiseg.io/audiences-list).  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from digiseg_api.api.accounts_api import AccountsApi
from digiseg_api.api.audiences_api import AudiencesApi
from digiseg_api.api.auth_api import AuthApi
from digiseg_api.api.campaigns_api import CampaignsApi
from digiseg_api.api.populations_api import PopulationsApi
from digiseg_api.api.users_api import UsersApi

# import ApiClient
from digiseg_api.api_response import ApiResponse
from digiseg_api.api_client import ApiClient
from digiseg_api.configuration import Configuration
from digiseg_api.exceptions import OpenApiException
from digiseg_api.exceptions import ApiTypeError
from digiseg_api.exceptions import ApiValueError
from digiseg_api.exceptions import ApiKeyError
from digiseg_api.exceptions import ApiAttributeError
from digiseg_api.exceptions import ApiException

# import models into sdk package
from digiseg_api.models.access_token_data import AccessTokenData
from digiseg_api.models.account_aux import AccountAux
from digiseg_api.models.account_base import AccountBase
from digiseg_api.models.account_creation import AccountCreation
from digiseg_api.models.account_creation_aux import AccountCreationAux
from digiseg_api.models.account_full import AccountFull
from digiseg_api.models.account_item import AccountItem
from digiseg_api.models.account_links import AccountLinks
from digiseg_api.models.account_mutation import AccountMutation
from digiseg_api.models.account_owner_creation import AccountOwnerCreation
from digiseg_api.models.api_key_aux import ApiKeyAux
from digiseg_api.models.api_key_base import ApiKeyBase
from digiseg_api.models.api_key_full import ApiKeyFull
from digiseg_api.models.api_key_full_with_token import ApiKeyFullWithToken
from digiseg_api.models.api_key_item import ApiKeyItem
from digiseg_api.models.api_key_links import ApiKeyLinks
from digiseg_api.models.api_key_mutation import ApiKeyMutation
from digiseg_api.models.api_key_token import ApiKeyToken
from digiseg_api.models.audience import Audience
from digiseg_api.models.audience_category_stats import AudienceCategoryStats
from digiseg_api.models.audience_response import AudienceResponse
from digiseg_api.models.audience_response_status import AudienceResponseStatus
from digiseg_api.models.audience_stats import AudienceStats
from digiseg_api.models.auth_token_request import AuthTokenRequest
from digiseg_api.models.auth_token_response import AuthTokenResponse
from digiseg_api.models.business_audience_stats import BusinessAudienceStats
from digiseg_api.models.business_audience_stats_audience_categories import BusinessAudienceStatsAudienceCategories
from digiseg_api.models.campaign_audience_stats import CampaignAudienceStats
from digiseg_api.models.campaign_aux import CampaignAux
from digiseg_api.models.campaign_base import CampaignBase
from digiseg_api.models.campaign_country_stats import CampaignCountryStats
from digiseg_api.models.campaign_creation import CampaignCreation
from digiseg_api.models.campaign_creation_data import CampaignCreationData
from digiseg_api.models.campaign_event_link import CampaignEventLink
from digiseg_api.models.campaign_event_link_parameter_info import CampaignEventLinkParameterInfo
from digiseg_api.models.campaign_event_links import CampaignEventLinks
from digiseg_api.models.campaign_event_set import CampaignEventSet
from digiseg_api.models.campaign_frequency_stats import CampaignFrequencyStats
from digiseg_api.models.campaign_full import CampaignFull
from digiseg_api.models.campaign_ingestion_status import CampaignIngestionStatus
from digiseg_api.models.campaign_item import CampaignItem
from digiseg_api.models.campaign_lifecycle_stage import CampaignLifecycleStage
from digiseg_api.models.campaign_links import CampaignLinks
from digiseg_api.models.campaign_mutation import CampaignMutation
from digiseg_api.models.campaign_timing_stats import CampaignTimingStats
from digiseg_api.models.category_populations_full import CategoryPopulationsFull
from digiseg_api.models.comparison import Comparison
from digiseg_api.models.comparisons_container import ComparisonsContainer
from digiseg_api.models.country_stats import CountryStats
from digiseg_api.models.create_api_key201_response import CreateApiKey201Response
from digiseg_api.models.create_campaign201_response import CreateCampaign201Response
from digiseg_api.models.create_user_in_account201_response import CreateUserInAccount201Response
from digiseg_api.models.day_of_month_stats import DayOfMonthStats
from digiseg_api.models.day_of_week_stats import DayOfWeekStats
from digiseg_api.models.error_response import ErrorResponse
from digiseg_api.models.frequency_stats import FrequencyStats
from digiseg_api.models.get_account_by_id200_response import GetAccountById200Response
from digiseg_api.models.get_api_key_by_id200_response import GetApiKeyById200Response
from digiseg_api.models.get_popuplation_by_key200_response import GetPopuplationByKey200Response
from digiseg_api.models.hour_of_day_stats import HourOfDayStats
from digiseg_api.models.identifyable_object import IdentifyableObject
from digiseg_api.models.identifyable_object1 import IdentifyableObject1
from digiseg_api.models.list_api_keys_by_user_id200_response import ListApiKeysByUserId200Response
from digiseg_api.models.list_campaigns200_response import ListCampaigns200Response
from digiseg_api.models.list_pagination_links import ListPaginationLinks
from digiseg_api.models.list_pagination_meta import ListPaginationMeta
from digiseg_api.models.list_pagination_meta_page import ListPaginationMetaPage
from digiseg_api.models.list_popuplations200_response import ListPopuplations200Response
from digiseg_api.models.list_users_by_account_id200_response import ListUsersByAccountId200Response
from digiseg_api.models.measurement import Measurement
from digiseg_api.models.measurements_container import MeasurementsContainer
from digiseg_api.models.passwordless_auth_request import PasswordlessAuthRequest
from digiseg_api.models.permission_scopes import PermissionScopes
from digiseg_api.models.population_audience_category_set_section import PopulationAudienceCategorySetSection
from digiseg_api.models.population_full import PopulationFull
from digiseg_api.models.population_item import PopulationItem
from digiseg_api.models.population_source import PopulationSource
from digiseg_api.models.population_source_business_category_set import PopulationSourceBusinessCategorySet
from digiseg_api.models.population_source_business_category_set_size import PopulationSourceBusinessCategorySetSize
from digiseg_api.models.population_source_business_section import PopulationSourceBusinessSection
from digiseg_api.models.population_source_not_resolved_section import PopulationSourceNotResolvedSection
from digiseg_api.models.population_source_private_category_set import PopulationSourcePrivateCategorySet
from digiseg_api.models.population_source_private_category_set_building_age import PopulationSourcePrivateCategorySetBuildingAge
from digiseg_api.models.population_source_private_category_set_cars import PopulationSourcePrivateCategorySetCars
from digiseg_api.models.population_source_private_category_set_children import PopulationSourcePrivateCategorySetChildren
from digiseg_api.models.population_source_private_category_set_education import PopulationSourcePrivateCategorySetEducation
from digiseg_api.models.population_source_private_category_set_home_ownership import PopulationSourcePrivateCategorySetHomeOwnership
from digiseg_api.models.population_source_private_category_set_home_type import PopulationSourcePrivateCategorySetHomeType
from digiseg_api.models.population_source_private_category_set_income import PopulationSourcePrivateCategorySetIncome
from digiseg_api.models.population_source_private_category_set_lifecycle import PopulationSourcePrivateCategorySetLifecycle
from digiseg_api.models.population_source_private_category_set_living_space import PopulationSourcePrivateCategorySetLivingSpace
from digiseg_api.models.population_source_private_category_set_neighbourhood_type import PopulationSourcePrivateCategorySetNeighbourhoodType
from digiseg_api.models.population_source_private_category_set_savings import PopulationSourcePrivateCategorySetSavings
from digiseg_api.models.population_source_private_category_set_tech_level import PopulationSourcePrivateCategorySetTechLevel
from digiseg_api.models.population_source_private_section import PopulationSourcePrivateSection
from digiseg_api.models.private_audience_stats import PrivateAudienceStats
from digiseg_api.models.private_audience_stats_audience_categories import PrivateAudienceStatsAudienceCategories
from digiseg_api.models.query_campaign_audience_stats200_response import QueryCampaignAudienceStats200Response
from digiseg_api.models.query_campaign_country_stats200_response import QueryCampaignCountryStats200Response
from digiseg_api.models.query_campaign_frequency_stats200_response import QueryCampaignFrequencyStats200Response
from digiseg_api.models.query_campaign_timing_stats200_response import QueryCampaignTimingStats200Response
from digiseg_api.models.registration_by_id_response_data import RegistrationByIdResponseData
from digiseg_api.models.registration_creation_response_data import RegistrationCreationResponseData
from digiseg_api.models.registration_request import RegistrationRequest
from digiseg_api.models.registration_verification_response_data import RegistrationVerificationResponseData
from digiseg_api.models.registration_verification_response_links import RegistrationVerificationResponseLinks
from digiseg_api.models.resolve_audiences_of_multiple_request import ResolveAudiencesOfMultipleRequest
from digiseg_api.models.resolve_audiences_of_multiple_request_item import ResolveAudiencesOfMultipleRequestItem
from digiseg_api.models.resolve_audiences_of_multiple_response import ResolveAudiencesOfMultipleResponse
from digiseg_api.models.resolve_audiences_of_multiple_response_item import ResolveAudiencesOfMultipleResponseItem
from digiseg_api.models.timestamped_object import TimestampedObject
from digiseg_api.models.timestamped_object1 import TimestampedObject1
from digiseg_api.models.user_account_role import UserAccountRole
from digiseg_api.models.user_aux import UserAux
from digiseg_api.models.user_base import UserBase
from digiseg_api.models.user_credentials import UserCredentials
from digiseg_api.models.user_full import UserFull
from digiseg_api.models.user_item import UserItem
from digiseg_api.models.user_links import UserLinks
from digiseg_api.models.user_mutation import UserMutation
