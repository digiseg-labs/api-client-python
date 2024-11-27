# coding: utf-8

"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-ts\">     <i class=\"api-client-sdk-logo devicon-typescript-plain\"></i>     <p>API client for TypeScript</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  Digiseg audiences are grouped into private and business audiences. In each group there are categories that then contain the audiences. The API endpoints that communicate audiences and household characteristics, audience codes are being used.  The following table can be used as a reference for audience codes. Note that Digiseg will at times update names of audiences for purposes of internationalization, clarity or other such purposes - but the codes will remain as-is and should be considered a stable point of reference for the audience.  ### Core audiences | Group | Category code | Audience Code | Category name | Audience Name | |-------|---------------|---------------|---------------|---------------| |  private  |  home_type  |  a1  |  Home Type  |  Apartment  | |    |    |  a2  |  Home Type  |  House  | |    |  savings  |  b1  |  Savings  |  No Savings  | |    |    |  b2  |  Savings  |  Smaller Savings  | |    |    |  b3  |  Savings  |  Larger Savings  | |    |  lifecycle  |  c1  |  Lifecycle  |  Young couples and singles  | |    |    |  c2  |  Lifecycle  |  Early family life  | |    |    |  c3  |  Lifecycle  |  Middle-aged families  | |    |    |  c4  |  Lifecycle  |  Mature families  | |    |    |  c5  |  Lifecycle  |  Pensioners / Retirees  | |    |  cars  |  d1  |  Cars in Household  |  No cars  | |    |    |  d2  |  Cars in Household  |  1 car  | |    |    |  d3  |  Cars in Household  |  2 or more cars  | |    |  children  |  e1  |  Children in the Household  |  No children  | |    |    |  e2  |  Children in the Household  |  1 child  | |    |    |  e3  |  Children in the Household  |  2 or more children  | |    |  education  |  f1  |  Education  |  Basic  | |    |    |  f2  |  Education  |  Medium  | |    |    |  f3  |  Education  |  Higher  | |    |  neighbourhood_type  |  g1  |  Neighbourhood Type  |  Countryside  | |    |    |  g2  |  Neighbourhood Type  |  Village  | |    |    |  g3  |  Neighbourhood Type  |  Suburban  | |    |    |  g4  |  Neighbourhood Type  |  City  | |    |  income  |  h1  |  Household Income  |  Lowest 20%  | |    |    |  h2  |  Household Income  |  Lowest 20-40%  | |    |    |  h3  |  Household Income  |  Middle 40-60%  | |    |    |  h4  |  Household Income  |  Highest 60-80%  | |    |    |  h5  |  Household Income  |  Top 20%  | |    |  home_ownership  |  j1  |  Home Ownership  |  Rent  | |    |    |  j2  |  Home Ownership  |  Own  | |    |  building_age  |  k1  |  Building Age  |  Pre 1945  | |    |    |  k2  |  Building Age  |  1945-1989  | |    |    |  k3  |  Building Age  |  1990 until today  | |    |  living_space  |  l1  |  Living space  |  Small  | |    |    |  l2  |  Living space  |  Medium  | |    |    |  l3  |  Living space  |  Large  | |    |  tech_level  |  n1  |  Tech-Level in Household  |  Basic  | |    |    |  n2  |  Tech-Level in Household  |  Medium  | |    |    |  n3  |  Tech-Level in Household  |  High  | |  business  |  size  |  ba1  |  Business  |  Small Business  | |    |    |  ba2  |  Business  |  Medium Business  | |    |    |  ba3  |  Business  |  Larger Business  | ### Composite audiences | Category code | Audience Code | Category name | Audience Name | |---------------|---------------|---------------|---------------| |  composite_betting  |  060  |  Betting Online  |  Betting, Casino & Poker  | |  composite_buyingpower  |  092  |  Buying Power  |  Buying Power Low  | |    |  093  |  Buying Power  |  Buying Power High  | |  composite_carclass  |  001  |  Car Classes  |  Micro & City  | |    |  002  |  Car Classes  |  Mini  | |    |  003  |  Car Classes  |  Small Medium / Compact  | |    |  004  |  Car Classes  |  Large Medium  | |    |  005  |  Car Classes  |  Large Premium  | |    |  006  |  Car Classes  |  Large Luxury Sedan  | |    |  007  |  Car Classes  |  MPV / Minivans  | |    |  008  |  Car Classes  |  SUV  | |    |  009  |  Car Classes  |  Electric & Hybrid  | |    |  010  |  Car Classes  |  Sport  | |  composite_career  |  110  |  Recruitment & Career  |  Employment in Large Companies  | |    |  111  |  Recruitment & Career  |  C-Level Positions  | |    |  112  |  Recruitment & Career  |  Management Positions  | |    |  113  |  Recruitment & Career  |  Graduate Programs & First Job  | |    |  114  |  Recruitment & Career  |  IT Positions  | |    |  158  |  Recruitment & Career  |  Employment in Small Companies  | |  composite_carservice  |  011  |  Car Services  |  Service & Car Parts  | |    |  012  |  Car Services  |  Car Tires  | |    |  013  |  Car Services  |  Car Leasing (Private)  | |  composite_childrensarticles  |  044  |  Children Articles  |  Games & Toys  | |  composite_computer_games  |  059  |  Computer Games  |  Games & Consoles  | |  composite_culture_entertainment  |  045  |  Culture & Entertainment  |  Cinema Tickets  | |    |  046  |  Culture & Entertainment  |  Opera & Theater  | |    |  047  |  Culture & Entertainment  |  Concert & Festival  | |    |  048  |  Culture & Entertainment  |  Museum & Exhibition  | |    |  049  |  Culture & Entertainment  |  Books  | |    |  050  |  Culture & Entertainment  |  Audiobooks  | |  composite_electronics  |  061  |  Electronics  |  TV  | |    |  062  |  Electronics  |  Phones & Smartphones  | |    |  063  |  Electronics  |  Small Domestic Appliances  | |    |  064  |  Electronics  |  Major Domestic Appliances  | |    |  065  |  Electronics  |  Garden Articles  | |    |  066  |  Electronics  |  HiFi Audio  | |    |  067  |  Electronics  |  Computer Tablet  | |    |  068  |  Electronics  |  Software & Apps  | |  composite_fashion  |  130  |  Fashion & Shopping  |  Shopping Mall Visitors  | |    |  131  |  Fashion & Shopping  |  Footwear & Shoes  | |    |  132  |  Fashion & Shopping  |  Jewellery  | |    |  133  |  Fashion & Shopping  |  Clothes  | |  composite_financials  |  014  |  Banking / Financing  |  House Loan  | |    |  015  |  Banking / Financing  |  Car Loan  | |    |  016  |  Banking / Financing  |  Consumer Loan  | |    |  017  |  Banking / Financing  |  Renovation  | |    |  018  |  Banking / Financing  |  Quick Loan  | |    |  019  |  Banking / Financing  |  Mobile Banking  | |    |  020  |  Banking / Financing  |  Investors  | |  composite_fmcg  |  069  |  Fast-Moving Consumer Good (FMCG)  |  Candy & Sweets  | |    |  070  |  Fast-Moving Consumer Good (FMCG)  |  Energy Drinks  | |    |  071  |  Fast-Moving Consumer Good (FMCG)  |  Sodas  | |    |  072  |  Fast-Moving Consumer Good (FMCG)  |  Chips  | |    |  073  |  Fast-Moving Consumer Good (FMCG)  |  Washing Detergents  | |    |  074  |  Fast-Moving Consumer Good (FMCG)  |  Bio & Organic Products  | |    |  075  |  Fast-Moving Consumer Good (FMCG)  |  Baby Food  | |    |  076  |  Fast-Moving Consumer Good (FMCG)  |  Dairy Products  | |    |  077  |  Fast-Moving Consumer Good (FMCG)  |  Beer  | |  composite_homerenovation  |  031  |  Home Renovation  |  House or apartment decoration  | |    |  032  |  Home Renovation  |  Kitchen  | |    |  033  |  Home Renovation  |  Bathroom & Plumbing  | |    |  034  |  Home Renovation  |  Windows, Doors & Tiles  | |    |  035  |  Home Renovation  |  Garden  | |    |  036  |  Home Renovation  |  Furniture  | |  composite_homesecurity  |  094  |  Home Security  |  House Alarms & Video Surveillance  | |  composite_insurance  |  021  |  Insurance  |  Car  | |    |  022  |  Insurance  |  House & Apartment  | |    |  023  |  Insurance  |  Accident Insurance  | |    |  024  |  Insurance  |  Life Insurance  | |    |  025  |  Insurance  |  Pension Fund  | |    |  026  |  Insurance  |  Travel Insurance  | |  composite_lifecycle  |  083  |  Lifestyle  |  Fitness, Gym & Workout  | |    |  084  |  Lifestyle  |  Stop Smoking  | |    |  085  |  Lifestyle  |  Natural Medicin  | |    |  086  |  Lifestyle  |  Gym Supplements & Nutrients  | |    |  087  |  Lifestyle  |  Small Pets  | |    |  088  |  Lifestyle  |  Large Pets  | |    |  089  |  Lifestyle  |  Weight Loss  | |    |  091  |  Lifestyle  |  Students  | |  composite_occasions  |  102  |  Occasions & Presents  |  Valentine's Day  | |    |  103  |  Occasions & Presents  |  Mothers's Day  | |    |  104  |  Occasions & Presents  |  Fathers's Day  | |    |  105  |  Occasions & Presents  |  Children's Day  | |    |  106  |  Occasions & Presents  |  Wedding & Engagement  | |    |  107  |  Occasions & Presents  |  Women's Day  | |    |  108  |  Occasions & Presents  |  Black Friday  | |    |  109  |  Occasions & Presents  |  Cyber Monday  | |    |  152  |  Occasions & Presents  |  Presents for young / inexpensive  | |    |  153  |  Occasions & Presents  |  Presents for young / expensive  | |    |  154  |  Occasions & Presents  |  Presents for families with children / inexpensive  | |    |  155  |  Occasions & Presents  |  Presents for families with children / expensive  | |    |  156  |  Occasions & Presents  |  Presents for mature / inexpensive  | |    |  157  |  Occasions & Presents  |  Presents for mature / expensive  | |  composite_olympics  |  159  |  Olympics  |  Olympics Visitors  | |    |  160  |  Olympics  |  Olympics Watchers  | |  composite_personalhygiene  |  078  |  Personal Hygiene  |  Baby Hygiene  | |    |  079  |  Personal Hygiene  |  SPF Sunscreen  | |    |  080  |  Personal Hygiene  |  Toothbrushes & Toothpaste  | |    |  081  |  Personal Hygiene  |  Cosmetics  | |    |  082  |  Personal Hygiene  |  Parfumes  | |  composite_politics  |  115  |  Political Themes  |  Children & Youth  | |    |  116  |  Political Themes  |  Elder Care  | |    |  117  |  Political Themes  |  Research & Education System  | |    |  118  |  Political Themes  |  Public Transport  | |    |  119  |  Political Themes  |  Car Transport & Road Infrastructure  | |    |  120  |  Political Themes  |  Art & Culture  | |    |  121  |  Political Themes  |  Green Transition & Environment  | |    |  122  |  Political Themes  |  Law & Order  | |    |  123  |  Political Themes  |  Immigration  | |    |  124  |  Political Themes  |  Tax Reliefs  | |    |  126  |  Political Themes  |  Euro-supporters  | |    |  128  |  Political Themes  |  Women's Rights & Gender Equality  | |    |  129  |  Political Themes  |  Corruption & Bureaucracy  | |  composite_realestatetrading  |  027  |  Real Estate Trading  |  First-time Buyers  | |    |  028  |  Real Estate Trading  |  Summerhouse  | |    |  029  |  Real Estate Trading  |  Apartment  | |    |  030  |  Real Estate Trading  |  House & Villa  | |  composite_restaurants  |  037  |  Restaurants  |  Fastfood  | |    |  038  |  Restaurants  |  Restaurant  | |    |  039  |  Restaurants  |  Cafe & Bar  | |  composite_telecom  |  040  |  Telecommunication  |  Internet  | |    |  041  |  Telecommunication  |  Mobile Phone Subscription  | |    |  042  |  Telecommunication  |  Satellite TV  | |    |  043  |  Telecommunication  |  Streaming Services  | |  composite_travel  |  051  |  Travel & Vacation  |  Airplane Tickets  | |    |  052  |  Travel & Vacation  |  Business Travelers  | |    |  053  |  Travel & Vacation  |  Car Vacation  | |    |  054  |  Travel & Vacation  |  All Inclusive / Resorts  | |    |  055  |  Travel & Vacation  |  Adventure  | |    |  056  |  Travel & Vacation  |  Luxury  | |    |  057  |  Travel & Vacation  |  City Break  | |    |  058  |  Travel & Vacation  |  Hotels  | |  composite_winter  |  134  |  Christmas & Winter  |  Christmas Gifts - Young people | Over 100 €  | |    |  135  |  Christmas & Winter  |  Christmas Gifts - Young people | Under 100 €  | |    |  136  |  Christmas & Winter  |  Christmas Gifts | Families with children | Over 100 €  | |    |  137  |  Christmas & Winter  |  Christmas Gifts | Families with children | Under 100 €  | |    |  138  |  Christmas & Winter  |  Christmas Gifts | 50+ | Over 100 €  | |    |  139  |  Christmas & Winter  |  Christmas Gifts | 50+ | Under 100 €  | |    |  140  |  Christmas & Winter  |  Personal Gifts | Online Photo Books & Calendars  | |    |  141  |  Christmas & Winter  |  Winter Outerwear | Over 250 €  | |    |  142  |  Christmas & Winter  |  Winter Outerwear | Under 250 €  | |    |  143  |  Christmas & Winter  |  Winter Outerwear for Children  | |    |  144  |  Christmas & Winter  |  Winter Sports Clothing & Gear  | |    |  145  |  Christmas & Winter  |  Decoration | House & Garden  | |    |  146  |  Christmas & Winter  |  Decoration | Apartment & Balcony  | |    |  147  |  Christmas & Winter  |  Food and Wine | Online Supermarket w. Delivery  | |    |  148  |  Christmas & Winter  |  Food and Wine | Online Store  | |    |  149  |  Christmas & Winter  |  Fireplace & Wood Burning Stove  | |    |  151  |  Christmas & Winter  |  Winter to Summer Tire Change  |  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBytes, StrictStr
from typing import Optional, Tuple, Union
from typing_extensions import Annotated
from digiseg_api.models.create_measurement_client201_response import CreateMeasurementClient201Response
from digiseg_api.models.list_measurement_clients200_response import ListMeasurementClients200Response
from digiseg_api.models.measurement_client_mutation import MeasurementClientMutation

from digiseg_api.api_client import ApiClient, RequestSerialized
from digiseg_api.api_response import ApiResponse
from digiseg_api.rest import RESTResponseType


class MeasurementClientsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_measurement_client(
        self,
        measurement_client_mutation: MeasurementClientMutation,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CreateMeasurementClient201Response:
        """Create measurement client

        Create a measurement client in the account of the user 

        :param measurement_client_mutation: (required)
        :type measurement_client_mutation: MeasurementClientMutation
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_measurement_client_serialize(
            measurement_client_mutation=measurement_client_mutation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def create_measurement_client_with_http_info(
        self,
        measurement_client_mutation: MeasurementClientMutation,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CreateMeasurementClient201Response]:
        """Create measurement client

        Create a measurement client in the account of the user 

        :param measurement_client_mutation: (required)
        :type measurement_client_mutation: MeasurementClientMutation
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_measurement_client_serialize(
            measurement_client_mutation=measurement_client_mutation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def create_measurement_client_without_preload_content(
        self,
        measurement_client_mutation: MeasurementClientMutation,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create measurement client

        Create a measurement client in the account of the user 

        :param measurement_client_mutation: (required)
        :type measurement_client_mutation: MeasurementClientMutation
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_measurement_client_serialize(
            measurement_client_mutation=measurement_client_mutation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_measurement_client_serialize(
        self,
        measurement_client_mutation,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if measurement_client_mutation is not None:
            _body_params = measurement_client_mutation


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/measurement/clients',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def delete_client_logo(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Delete measurement client logo

        Deletes the logo for a client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_client_logo_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_client_logo_with_http_info(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Delete measurement client logo

        Deletes the logo for a client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_client_logo_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_client_logo_without_preload_content(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete measurement client logo

        Deletes the logo for a client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_client_logo_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_client_logo_serialize(
        self,
        client_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if client_id is not None:
            _path_params['client_id'] = client_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/measurement/clients/{client_id}/assets/logo',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def delete_measurement_client_by_id(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Delete measurement client

        Deletes a measurement client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_measurement_client_by_id_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_measurement_client_by_id_with_http_info(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Delete measurement client

        Deletes a measurement client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_measurement_client_by_id_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_measurement_client_by_id_without_preload_content(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete measurement client

        Deletes a measurement client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_measurement_client_by_id_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_measurement_client_by_id_serialize(
        self,
        client_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if client_id is not None:
            _path_params['client_id'] = client_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/measurement/clients/{client_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_client_logo(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Get measurement client logo

        Gets the client logo, if the image is hosted on the Digiseg platform. Refer to the clients's `logo_url` to get a non-authenticated and shareable URL for the logo. 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_client_logo_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_client_logo_with_http_info(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Get measurement client logo

        Gets the client logo, if the image is hosted on the Digiseg platform. Refer to the clients's `logo_url` to get a non-authenticated and shareable URL for the logo. 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_client_logo_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_client_logo_without_preload_content(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get measurement client logo

        Gets the client logo, if the image is hosted on the Digiseg platform. Refer to the clients's `logo_url` to get a non-authenticated and shareable URL for the logo. 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_client_logo_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_client_logo_serialize(
        self,
        client_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if client_id is not None:
            _path_params['client_id'] = client_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/measurement/clients/{client_id}/assets/logo',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_measurement_client_by_id(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CreateMeasurementClient201Response:
        """Get measurement client

        Get information for a specific measurement client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_measurement_client_by_id_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_measurement_client_by_id_with_http_info(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CreateMeasurementClient201Response]:
        """Get measurement client

        Get information for a specific measurement client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_measurement_client_by_id_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_measurement_client_by_id_without_preload_content(
        self,
        client_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get measurement client

        Get information for a specific measurement client 

        :param client_id: (required)
        :type client_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_measurement_client_by_id_serialize(
            client_id=client_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_measurement_client_by_id_serialize(
        self,
        client_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if client_id is not None:
            _path_params['client_id'] = client_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/measurement/clients/{client_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_measurement_clients(
        self,
        filter_account_id: Annotated[Optional[StrictStr], Field(description="Optional parameter used to query measurement clients by specific account IDs (only available to super admins). The value `*` is synonymous for \"all accounts\". ")] = None,
        filter_name_contains: Annotated[Optional[StrictStr], Field(description="Optional parameter used to search for clients where the name contains a substring (case insensitive)")] = None,
        page_size: Annotated[Optional[Annotated[int, Field(le=500, strict=True, ge=1)]], Field(description="The desired page size")] = None,
        page_after: Annotated[Optional[StrictStr], Field(description="Optional pagination parameter, indicating the previous cursor value to paginate beyond. The value to provide here is opaque, but can be found in previous requests in the `meta.page.last_cursor` field. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ListMeasurementClients200Response:
        """List measurement clients

        List measurement clients that the user has access to 

        :param filter_account_id: Optional parameter used to query measurement clients by specific account IDs (only available to super admins). The value `*` is synonymous for \"all accounts\". 
        :type filter_account_id: str
        :param filter_name_contains: Optional parameter used to search for clients where the name contains a substring (case insensitive)
        :type filter_name_contains: str
        :param page_size: The desired page size
        :type page_size: int
        :param page_after: Optional pagination parameter, indicating the previous cursor value to paginate beyond. The value to provide here is opaque, but can be found in previous requests in the `meta.page.last_cursor` field. 
        :type page_after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_measurement_clients_serialize(
            filter_account_id=filter_account_id,
            filter_name_contains=filter_name_contains,
            page_size=page_size,
            page_after=page_after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListMeasurementClients200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_measurement_clients_with_http_info(
        self,
        filter_account_id: Annotated[Optional[StrictStr], Field(description="Optional parameter used to query measurement clients by specific account IDs (only available to super admins). The value `*` is synonymous for \"all accounts\". ")] = None,
        filter_name_contains: Annotated[Optional[StrictStr], Field(description="Optional parameter used to search for clients where the name contains a substring (case insensitive)")] = None,
        page_size: Annotated[Optional[Annotated[int, Field(le=500, strict=True, ge=1)]], Field(description="The desired page size")] = None,
        page_after: Annotated[Optional[StrictStr], Field(description="Optional pagination parameter, indicating the previous cursor value to paginate beyond. The value to provide here is opaque, but can be found in previous requests in the `meta.page.last_cursor` field. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ListMeasurementClients200Response]:
        """List measurement clients

        List measurement clients that the user has access to 

        :param filter_account_id: Optional parameter used to query measurement clients by specific account IDs (only available to super admins). The value `*` is synonymous for \"all accounts\". 
        :type filter_account_id: str
        :param filter_name_contains: Optional parameter used to search for clients where the name contains a substring (case insensitive)
        :type filter_name_contains: str
        :param page_size: The desired page size
        :type page_size: int
        :param page_after: Optional pagination parameter, indicating the previous cursor value to paginate beyond. The value to provide here is opaque, but can be found in previous requests in the `meta.page.last_cursor` field. 
        :type page_after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_measurement_clients_serialize(
            filter_account_id=filter_account_id,
            filter_name_contains=filter_name_contains,
            page_size=page_size,
            page_after=page_after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListMeasurementClients200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_measurement_clients_without_preload_content(
        self,
        filter_account_id: Annotated[Optional[StrictStr], Field(description="Optional parameter used to query measurement clients by specific account IDs (only available to super admins). The value `*` is synonymous for \"all accounts\". ")] = None,
        filter_name_contains: Annotated[Optional[StrictStr], Field(description="Optional parameter used to search for clients where the name contains a substring (case insensitive)")] = None,
        page_size: Annotated[Optional[Annotated[int, Field(le=500, strict=True, ge=1)]], Field(description="The desired page size")] = None,
        page_after: Annotated[Optional[StrictStr], Field(description="Optional pagination parameter, indicating the previous cursor value to paginate beyond. The value to provide here is opaque, but can be found in previous requests in the `meta.page.last_cursor` field. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List measurement clients

        List measurement clients that the user has access to 

        :param filter_account_id: Optional parameter used to query measurement clients by specific account IDs (only available to super admins). The value `*` is synonymous for \"all accounts\". 
        :type filter_account_id: str
        :param filter_name_contains: Optional parameter used to search for clients where the name contains a substring (case insensitive)
        :type filter_name_contains: str
        :param page_size: The desired page size
        :type page_size: int
        :param page_after: Optional pagination parameter, indicating the previous cursor value to paginate beyond. The value to provide here is opaque, but can be found in previous requests in the `meta.page.last_cursor` field. 
        :type page_after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_measurement_clients_serialize(
            filter_account_id=filter_account_id,
            filter_name_contains=filter_name_contains,
            page_size=page_size,
            page_after=page_after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListMeasurementClients200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_measurement_clients_serialize(
        self,
        filter_account_id,
        filter_name_contains,
        page_size,
        page_after,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if filter_account_id is not None:
            
            _query_params.append(('filter[account_id]', filter_account_id))
            
        if filter_name_contains is not None:
            
            _query_params.append(('filter[name][contains]', filter_name_contains))
            
        if page_size is not None:
            
            _query_params.append(('page[size]', page_size))
            
        if page_after is not None:
            
            _query_params.append(('page[after]', page_after))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/measurement/clients',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def update_measurement_client_by_id(
        self,
        client_id: StrictStr,
        measurement_client_mutation: MeasurementClientMutation,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CreateMeasurementClient201Response:
        """Update measurement client

        Updates properties of a measurement client 

        :param client_id: (required)
        :type client_id: str
        :param measurement_client_mutation: (required)
        :type measurement_client_mutation: MeasurementClientMutation
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_measurement_client_by_id_serialize(
            client_id=client_id,
            measurement_client_mutation=measurement_client_mutation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def update_measurement_client_by_id_with_http_info(
        self,
        client_id: StrictStr,
        measurement_client_mutation: MeasurementClientMutation,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CreateMeasurementClient201Response]:
        """Update measurement client

        Updates properties of a measurement client 

        :param client_id: (required)
        :type client_id: str
        :param measurement_client_mutation: (required)
        :type measurement_client_mutation: MeasurementClientMutation
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_measurement_client_by_id_serialize(
            client_id=client_id,
            measurement_client_mutation=measurement_client_mutation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def update_measurement_client_by_id_without_preload_content(
        self,
        client_id: StrictStr,
        measurement_client_mutation: MeasurementClientMutation,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update measurement client

        Updates properties of a measurement client 

        :param client_id: (required)
        :type client_id: str
        :param measurement_client_mutation: (required)
        :type measurement_client_mutation: MeasurementClientMutation
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_measurement_client_by_id_serialize(
            client_id=client_id,
            measurement_client_mutation=measurement_client_mutation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateMeasurementClient201Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_measurement_client_by_id_serialize(
        self,
        client_id,
        measurement_client_mutation,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if client_id is not None:
            _path_params['client_id'] = client_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if measurement_client_mutation is not None:
            _body_params = measurement_client_mutation


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/measurement/clients/{client_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def upload_client_logo(
        self,
        client_id: StrictStr,
        body: Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Upload measurement client logo

        Upload a logo for a client 

        :param client_id: (required)
        :type client_id: str
        :param body: (required)
        :type body: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_client_logo_serialize(
            client_id=client_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def upload_client_logo_with_http_info(
        self,
        client_id: StrictStr,
        body: Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Upload measurement client logo

        Upload a logo for a client 

        :param client_id: (required)
        :type client_id: str
        :param body: (required)
        :type body: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_client_logo_serialize(
            client_id=client_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def upload_client_logo_without_preload_content(
        self,
        client_id: StrictStr,
        body: Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Upload measurement client logo

        Upload a logo for a client 

        :param client_id: (required)
        :type client_id: str
        :param body: (required)
        :type body: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_client_logo_serialize(
            client_id=client_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _upload_client_logo_serialize(
        self,
        client_id,
        body,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if client_id is not None:
            _path_params['client_id'] = client_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            # convert to byte array if the input is a file name (str)
            if isinstance(body, str):
                with open(body, "rb") as _fp:
                    _body_params = _fp.read()
            elif isinstance(body, tuple):
                # drop the filename from the tuple
                _body_params = body[1]
            else:
                _body_params = body



        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'image/gif', 
                        'image/png', 
                        'image/jpeg', 
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'oAuth', 
            'bearerAuth', 
            'apiKeyHeaderAuth', 
            'apiKeyQueryParamAuth'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/measurement/clients/{client_id}/assets/logo',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


