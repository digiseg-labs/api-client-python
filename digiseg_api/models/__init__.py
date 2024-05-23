# coding: utf-8

# flake8: noqa
"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  Digiseg audiences are grouped into private and business audiences. In each group there are categories that then contain the audiences. The API endpoints that communicate audiences and household characteristics, audience codes are being used.  The following table can be used as a reference for audience codes. Note that Digiseg will at times update names of audiences for purposes of internationalization, clarity or other such purposes - but the codes will remain as-is and should be considered a stable point of reference for the audience.  | Group | Category | Audience Code | Audience Name | |-------|----------|---------------|---------------| | private | home_type | a1 | Apartment | |  |  | a2 | House | |  | savings | b1 | No Savings | |  |  | b2 | Smaller Savings | |  |  | b3 | Larger Savings | |  | lifecycle | c1 | Young couples and singles | |  |  | c2 | Early family life | |  |  | c3 | Middle-aged families | |  |  | c4 | Mature families | |  |  | c5 | Pensioners | |  | cars | d1 | No cars | |  |  | d2 | 1 car | |  |  | d3 | 2 or more cars | |  | children | e1 | No children | |  |  | e2 | 1 child | |  |  | e3 | 2 or more children | |  | education | f1 | Basic | |  |  | f2 | Medium | |  |  | f3 | Higher | |  | neighbourhood_type | g1 | Countryside | |  |  | g2 | Village | |  |  | g3 | Suburban | |  |  | g4 | City | |  | income | h1 | Lowest 20% | |  |  | h2 | Lowest 20-40% | |  |  | h3 | Middle 40-60% | |  |  | h4 | Highest 60-80% | |  |  | h5 | Top 20% | |  | home_ownership | j1 | Rent | |  |  | j2 | Own | |  | building_age | k1 | Pre 1945 | |  |  | k2 | 1945-1989 | |  |  | k3 | 1990 until today | |  | living_space | l1 | Small | |  |  | l2 | Medium | |  |  | l3 | Large | |  | tech_level | n1 | Basic | |  |  | n2 | Medium | |  |  | n3 | High | | business | size | ba1 | Small Business | |  |  | ba2 | Medium Business | |  |  | ba3 | Larger Business |  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from digiseg_api.models.access_token_data import AccessTokenData
from digiseg_api.models.account_aux import AccountAux
from digiseg_api.models.account_base import AccountBase
from digiseg_api.models.account_creation import AccountCreation
from digiseg_api.models.account_creation_aux import AccountCreationAux
from digiseg_api.models.account_full import AccountFull
from digiseg_api.models.account_item import AccountItem
from digiseg_api.models.account_links import AccountLinks
from digiseg_api.models.account_mutation import AccountMutation
from digiseg_api.models.account_mutation_aux import AccountMutationAux
from digiseg_api.models.account_owner_creation import AccountOwnerCreation
from digiseg_api.models.api_key_aux import ApiKeyAux
from digiseg_api.models.api_key_base import ApiKeyBase
from digiseg_api.models.api_key_creation import ApiKeyCreation
from digiseg_api.models.api_key_full import ApiKeyFull
from digiseg_api.models.api_key_full_with_token import ApiKeyFullWithToken
from digiseg_api.models.api_key_item import ApiKeyItem
from digiseg_api.models.api_key_links import ApiKeyLinks
from digiseg_api.models.api_key_mutation import ApiKeyMutation
from digiseg_api.models.api_key_status import ApiKeyStatus
from digiseg_api.models.api_key_token import ApiKeyToken
from digiseg_api.models.audience import Audience
from digiseg_api.models.audience_category_stats import AudienceCategoryStats
from digiseg_api.models.audience_data_daily_usage import AudienceDataDailyUsage
from digiseg_api.models.audience_data_monthly_usage import AudienceDataMonthlyUsage
from digiseg_api.models.audience_data_realtime_usage import AudienceDataRealtimeUsage
from digiseg_api.models.audience_data_usage import AudienceDataUsage
from digiseg_api.models.audience_example_input import AudienceExampleInput
from digiseg_api.models.audience_example_inputs_response import AudienceExampleInputsResponse
from digiseg_api.models.audience_response import AudienceResponse
from digiseg_api.models.audience_response_status import AudienceResponseStatus
from digiseg_api.models.audience_stats import AudienceStats
from digiseg_api.models.auth_token_request import AuthTokenRequest
from digiseg_api.models.auth_token_response import AuthTokenResponse
from digiseg_api.models.business_audience_stats import BusinessAudienceStats
from digiseg_api.models.business_audience_stats_audience_categories import BusinessAudienceStatsAudienceCategories
from digiseg_api.models.category_populations_full import CategoryPopulationsFull
from digiseg_api.models.company_size import CompanySize
from digiseg_api.models.company_type import CompanyType
from digiseg_api.models.comparison import Comparison
from digiseg_api.models.comparisons_container import ComparisonsContainer
from digiseg_api.models.country_stats import CountryStats
from digiseg_api.models.create_api_key201_response import CreateApiKey201Response
from digiseg_api.models.create_measurement_client201_response import CreateMeasurementClient201Response
from digiseg_api.models.create_study201_response import CreateStudy201Response
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
from digiseg_api.models.list_api_keys_by_account_id200_response import ListApiKeysByAccountId200Response
from digiseg_api.models.list_audience_data_daily_usage200_response import ListAudienceDataDailyUsage200Response
from digiseg_api.models.list_audience_data_monthly_usage200_response import ListAudienceDataMonthlyUsage200Response
from digiseg_api.models.list_audience_data_realtime_usage200_response import ListAudienceDataRealtimeUsage200Response
from digiseg_api.models.list_measurement_clients200_response import ListMeasurementClients200Response
from digiseg_api.models.list_measurement_labels200_response import ListMeasurementLabels200Response
from digiseg_api.models.list_pagination_links import ListPaginationLinks
from digiseg_api.models.list_pagination_meta import ListPaginationMeta
from digiseg_api.models.list_pagination_meta_page import ListPaginationMetaPage
from digiseg_api.models.list_popuplations200_response import ListPopuplations200Response
from digiseg_api.models.list_studies200_response import ListStudies200Response
from digiseg_api.models.list_users_by_account_id200_response import ListUsersByAccountId200Response
from digiseg_api.models.measurement import Measurement
from digiseg_api.models.measurement_client_base import MeasurementClientBase
from digiseg_api.models.measurement_client_full import MeasurementClientFull
from digiseg_api.models.measurement_client_item import MeasurementClientItem
from digiseg_api.models.measurement_client_mutation import MeasurementClientMutation
from digiseg_api.models.measurement_event_link import MeasurementEventLink
from digiseg_api.models.measurement_event_link_parameter_info import MeasurementEventLinkParameterInfo
from digiseg_api.models.measurement_event_links import MeasurementEventLinks
from digiseg_api.models.measurement_event_set import MeasurementEventSet
from digiseg_api.models.measurement_integration_platform import MeasurementIntegrationPlatform
from digiseg_api.models.measurements_container import MeasurementsContainer
from digiseg_api.models.passwordless_auth_request import PasswordlessAuthRequest
from digiseg_api.models.permission_scopes import PermissionScopes
from digiseg_api.models.population_audience_category_set_business_section import PopulationAudienceCategorySetBusinessSection
from digiseg_api.models.population_audience_category_set_private_section import PopulationAudienceCategorySetPrivateSection
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
from digiseg_api.models.postal_address import PostalAddress
from digiseg_api.models.private_audience_stats import PrivateAudienceStats
from digiseg_api.models.private_audience_stats_audience_categories import PrivateAudienceStatsAudienceCategories
from digiseg_api.models.query_study_audience_stats200_response import QueryStudyAudienceStats200Response
from digiseg_api.models.query_study_country_stats200_response import QueryStudyCountryStats200Response
from digiseg_api.models.query_study_frequency_stats200_response import QueryStudyFrequencyStats200Response
from digiseg_api.models.query_study_timing_stats200_response import QueryStudyTimingStats200Response
from digiseg_api.models.registration_by_id_response_data import RegistrationByIdResponseData
from digiseg_api.models.registration_creation_response_data import RegistrationCreationResponseData
from digiseg_api.models.registration_request import RegistrationRequest
from digiseg_api.models.registration_verification_response_data import RegistrationVerificationResponseData
from digiseg_api.models.registration_verification_response_links import RegistrationVerificationResponseLinks
from digiseg_api.models.resolve_audiences_of_multiple_request import ResolveAudiencesOfMultipleRequest
from digiseg_api.models.resolve_audiences_of_multiple_request_item import ResolveAudiencesOfMultipleRequestItem
from digiseg_api.models.resolve_audiences_of_multiple_response import ResolveAudiencesOfMultipleResponse
from digiseg_api.models.resolve_audiences_of_multiple_response_item import ResolveAudiencesOfMultipleResponseItem
from digiseg_api.models.study_audience_stats import StudyAudienceStats
from digiseg_api.models.study_aux import StudyAux
from digiseg_api.models.study_base import StudyBase
from digiseg_api.models.study_country_stats import StudyCountryStats
from digiseg_api.models.study_creation import StudyCreation
from digiseg_api.models.study_creation_data import StudyCreationData
from digiseg_api.models.study_frequency_stats import StudyFrequencyStats
from digiseg_api.models.study_full import StudyFull
from digiseg_api.models.study_ingestion_status import StudyIngestionStatus
from digiseg_api.models.study_item import StudyItem
from digiseg_api.models.study_lifecycle_stage import StudyLifecycleStage
from digiseg_api.models.study_links import StudyLinks
from digiseg_api.models.study_meta import StudyMeta
from digiseg_api.models.study_mutation import StudyMutation
from digiseg_api.models.study_permissions import StudyPermissions
from digiseg_api.models.study_summary_stats import StudySummaryStats
from digiseg_api.models.study_timing_stats import StudyTimingStats
from digiseg_api.models.timestamped_object import TimestampedObject
from digiseg_api.models.timestamped_object1 import TimestampedObject1
from digiseg_api.models.user_account_membership import UserAccountMembership
from digiseg_api.models.user_account_role import UserAccountRole
from digiseg_api.models.user_aux import UserAux
from digiseg_api.models.user_base import UserBase
from digiseg_api.models.user_creation import UserCreation
from digiseg_api.models.user_creation_notification import UserCreationNotification
from digiseg_api.models.user_credentials import UserCredentials
from digiseg_api.models.user_full import UserFull
from digiseg_api.models.user_item import UserItem
from digiseg_api.models.user_links import UserLinks
from digiseg_api.models.user_mutation import UserMutation
from digiseg_api.models.user_platform_role import UserPlatformRole
from digiseg_api.models.user_sort_option import UserSortOption
