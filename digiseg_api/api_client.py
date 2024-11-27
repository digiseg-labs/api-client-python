# coding: utf-8

"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-ts\">     <i class=\"api-client-sdk-logo devicon-typescript-plain\"></i>     <p>API client for TypeScript</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  Digiseg audiences are grouped into private and business audiences. In each group there are categories that then contain the audiences. The API endpoints that communicate audiences and household characteristics, audience codes are being used.  The following table can be used as a reference for audience codes. Note that Digiseg will at times update names of audiences for purposes of internationalization, clarity or other such purposes - but the codes will remain as-is and should be considered a stable point of reference for the audience.  ### Core audiences | Group | Category code | Audience Code | Category name | Audience Name | |-------|---------------|---------------|---------------|---------------| |  private  |  home_type  |  a1  |  Home Type  |  Apartment  | |    |    |  a2  |  Home Type  |  House  | |    |  savings  |  b1  |  Savings  |  No Savings  | |    |    |  b2  |  Savings  |  Smaller Savings  | |    |    |  b3  |  Savings  |  Larger Savings  | |    |  lifecycle  |  c1  |  Lifecycle  |  Young couples and singles  | |    |    |  c2  |  Lifecycle  |  Early family life  | |    |    |  c3  |  Lifecycle  |  Middle-aged families  | |    |    |  c4  |  Lifecycle  |  Mature families  | |    |    |  c5  |  Lifecycle  |  Pensioners / Retirees  | |    |  cars  |  d1  |  Cars in Household  |  No cars  | |    |    |  d2  |  Cars in Household  |  1 car  | |    |    |  d3  |  Cars in Household  |  2 or more cars  | |    |  children  |  e1  |  Children in the Household  |  No children  | |    |    |  e2  |  Children in the Household  |  1 child  | |    |    |  e3  |  Children in the Household  |  2 or more children  | |    |  education  |  f1  |  Education  |  Basic  | |    |    |  f2  |  Education  |  Medium  | |    |    |  f3  |  Education  |  Higher  | |    |  neighbourhood_type  |  g1  |  Neighbourhood Type  |  Countryside  | |    |    |  g2  |  Neighbourhood Type  |  Village  | |    |    |  g3  |  Neighbourhood Type  |  Suburban  | |    |    |  g4  |  Neighbourhood Type  |  City  | |    |  income  |  h1  |  Household Income  |  Lowest 20%  | |    |    |  h2  |  Household Income  |  Lowest 20-40%  | |    |    |  h3  |  Household Income  |  Middle 40-60%  | |    |    |  h4  |  Household Income  |  Highest 60-80%  | |    |    |  h5  |  Household Income  |  Top 20%  | |    |  home_ownership  |  j1  |  Home Ownership  |  Rent  | |    |    |  j2  |  Home Ownership  |  Own  | |    |  building_age  |  k1  |  Building Age  |  Pre 1945  | |    |    |  k2  |  Building Age  |  1945-1989  | |    |    |  k3  |  Building Age  |  1990 until today  | |    |  living_space  |  l1  |  Living space  |  Small  | |    |    |  l2  |  Living space  |  Medium  | |    |    |  l3  |  Living space  |  Large  | |    |  tech_level  |  n1  |  Tech-Level in Household  |  Basic  | |    |    |  n2  |  Tech-Level in Household  |  Medium  | |    |    |  n3  |  Tech-Level in Household  |  High  | |  business  |  size  |  ba1  |  Business  |  Small Business  | |    |    |  ba2  |  Business  |  Medium Business  | |    |    |  ba3  |  Business  |  Larger Business  | ### Composite audiences | Category code | Audience Code | Category name | Audience Name | |---------------|---------------|---------------|---------------| |  composite_betting  |  060  |  Betting Online  |  Betting, Casino & Poker  | |  composite_buyingpower  |  092  |  Buying Power  |  Buying Power Low  | |    |  093  |  Buying Power  |  Buying Power High  | |  composite_carclass  |  001  |  Car Classes  |  Micro & City  | |    |  002  |  Car Classes  |  Mini  | |    |  003  |  Car Classes  |  Small Medium / Compact  | |    |  004  |  Car Classes  |  Large Medium  | |    |  005  |  Car Classes  |  Large Premium  | |    |  006  |  Car Classes  |  Large Luxury Sedan  | |    |  007  |  Car Classes  |  MPV / Minivans  | |    |  008  |  Car Classes  |  SUV  | |    |  009  |  Car Classes  |  Electric & Hybrid  | |    |  010  |  Car Classes  |  Sport  | |  composite_career  |  110  |  Recruitment & Career  |  Employment in Large Companies  | |    |  111  |  Recruitment & Career  |  C-Level Positions  | |    |  112  |  Recruitment & Career  |  Management Positions  | |    |  113  |  Recruitment & Career  |  Graduate Programs & First Job  | |    |  114  |  Recruitment & Career  |  IT Positions  | |    |  158  |  Recruitment & Career  |  Employment in Small Companies  | |  composite_carservice  |  011  |  Car Services  |  Service & Car Parts  | |    |  012  |  Car Services  |  Car Tires  | |    |  013  |  Car Services  |  Car Leasing (Private)  | |  composite_childrensarticles  |  044  |  Children Articles  |  Games & Toys  | |  composite_computer_games  |  059  |  Computer Games  |  Games & Consoles  | |  composite_culture_entertainment  |  045  |  Culture & Entertainment  |  Cinema Tickets  | |    |  046  |  Culture & Entertainment  |  Opera & Theater  | |    |  047  |  Culture & Entertainment  |  Concert & Festival  | |    |  048  |  Culture & Entertainment  |  Museum & Exhibition  | |    |  049  |  Culture & Entertainment  |  Books  | |    |  050  |  Culture & Entertainment  |  Audiobooks  | |  composite_electronics  |  061  |  Electronics  |  TV  | |    |  062  |  Electronics  |  Phones & Smartphones  | |    |  063  |  Electronics  |  Small Domestic Appliances  | |    |  064  |  Electronics  |  Major Domestic Appliances  | |    |  065  |  Electronics  |  Garden Articles  | |    |  066  |  Electronics  |  HiFi Audio  | |    |  067  |  Electronics  |  Computer Tablet  | |    |  068  |  Electronics  |  Software & Apps  | |  composite_fashion  |  130  |  Fashion & Shopping  |  Shopping Mall Visitors  | |    |  131  |  Fashion & Shopping  |  Footwear & Shoes  | |    |  132  |  Fashion & Shopping  |  Jewellery  | |    |  133  |  Fashion & Shopping  |  Clothes  | |  composite_financials  |  014  |  Banking / Financing  |  House Loan  | |    |  015  |  Banking / Financing  |  Car Loan  | |    |  016  |  Banking / Financing  |  Consumer Loan  | |    |  017  |  Banking / Financing  |  Renovation  | |    |  018  |  Banking / Financing  |  Quick Loan  | |    |  019  |  Banking / Financing  |  Mobile Banking  | |    |  020  |  Banking / Financing  |  Investors  | |  composite_fmcg  |  069  |  Fast-Moving Consumer Good (FMCG)  |  Candy & Sweets  | |    |  070  |  Fast-Moving Consumer Good (FMCG)  |  Energy Drinks  | |    |  071  |  Fast-Moving Consumer Good (FMCG)  |  Sodas  | |    |  072  |  Fast-Moving Consumer Good (FMCG)  |  Chips  | |    |  073  |  Fast-Moving Consumer Good (FMCG)  |  Washing Detergents  | |    |  074  |  Fast-Moving Consumer Good (FMCG)  |  Bio & Organic Products  | |    |  075  |  Fast-Moving Consumer Good (FMCG)  |  Baby Food  | |    |  076  |  Fast-Moving Consumer Good (FMCG)  |  Dairy Products  | |    |  077  |  Fast-Moving Consumer Good (FMCG)  |  Beer  | |  composite_homerenovation  |  031  |  Home Renovation  |  House or apartment decoration  | |    |  032  |  Home Renovation  |  Kitchen  | |    |  033  |  Home Renovation  |  Bathroom & Plumbing  | |    |  034  |  Home Renovation  |  Windows, Doors & Tiles  | |    |  035  |  Home Renovation  |  Garden  | |    |  036  |  Home Renovation  |  Furniture  | |  composite_homesecurity  |  094  |  Home Security  |  House Alarms & Video Surveillance  | |  composite_insurance  |  021  |  Insurance  |  Car  | |    |  022  |  Insurance  |  House & Apartment  | |    |  023  |  Insurance  |  Accident Insurance  | |    |  024  |  Insurance  |  Life Insurance  | |    |  025  |  Insurance  |  Pension Fund  | |    |  026  |  Insurance  |  Travel Insurance  | |  composite_lifecycle  |  083  |  Lifestyle  |  Fitness, Gym & Workout  | |    |  084  |  Lifestyle  |  Stop Smoking  | |    |  085  |  Lifestyle  |  Natural Medicin  | |    |  086  |  Lifestyle  |  Gym Supplements & Nutrients  | |    |  087  |  Lifestyle  |  Small Pets  | |    |  088  |  Lifestyle  |  Large Pets  | |    |  089  |  Lifestyle  |  Weight Loss  | |    |  091  |  Lifestyle  |  Students  | |  composite_occasions  |  102  |  Occasions & Presents  |  Valentine's Day  | |    |  103  |  Occasions & Presents  |  Mothers's Day  | |    |  104  |  Occasions & Presents  |  Fathers's Day  | |    |  105  |  Occasions & Presents  |  Children's Day  | |    |  106  |  Occasions & Presents  |  Wedding & Engagement  | |    |  107  |  Occasions & Presents  |  Women's Day  | |    |  108  |  Occasions & Presents  |  Black Friday  | |    |  109  |  Occasions & Presents  |  Cyber Monday  | |    |  152  |  Occasions & Presents  |  Presents for young / inexpensive  | |    |  153  |  Occasions & Presents  |  Presents for young / expensive  | |    |  154  |  Occasions & Presents  |  Presents for families with children / inexpensive  | |    |  155  |  Occasions & Presents  |  Presents for families with children / expensive  | |    |  156  |  Occasions & Presents  |  Presents for mature / inexpensive  | |    |  157  |  Occasions & Presents  |  Presents for mature / expensive  | |  composite_olympics  |  159  |  Olympics  |  Olympics Visitors  | |    |  160  |  Olympics  |  Olympics Watchers  | |  composite_personalhygiene  |  078  |  Personal Hygiene  |  Baby Hygiene  | |    |  079  |  Personal Hygiene  |  SPF Sunscreen  | |    |  080  |  Personal Hygiene  |  Toothbrushes & Toothpaste  | |    |  081  |  Personal Hygiene  |  Cosmetics  | |    |  082  |  Personal Hygiene  |  Parfumes  | |  composite_politics  |  115  |  Political Themes  |  Children & Youth  | |    |  116  |  Political Themes  |  Elder Care  | |    |  117  |  Political Themes  |  Research & Education System  | |    |  118  |  Political Themes  |  Public Transport  | |    |  119  |  Political Themes  |  Car Transport & Road Infrastructure  | |    |  120  |  Political Themes  |  Art & Culture  | |    |  121  |  Political Themes  |  Green Transition & Environment  | |    |  122  |  Political Themes  |  Law & Order  | |    |  123  |  Political Themes  |  Immigration  | |    |  124  |  Political Themes  |  Tax Reliefs  | |    |  126  |  Political Themes  |  Euro-supporters  | |    |  128  |  Political Themes  |  Women's Rights & Gender Equality  | |    |  129  |  Political Themes  |  Corruption & Bureaucracy  | |  composite_realestatetrading  |  027  |  Real Estate Trading  |  First-time Buyers  | |    |  028  |  Real Estate Trading  |  Summerhouse  | |    |  029  |  Real Estate Trading  |  Apartment  | |    |  030  |  Real Estate Trading  |  House & Villa  | |  composite_restaurants  |  037  |  Restaurants  |  Fastfood  | |    |  038  |  Restaurants  |  Restaurant  | |    |  039  |  Restaurants  |  Cafe & Bar  | |  composite_telecom  |  040  |  Telecommunication  |  Internet  | |    |  041  |  Telecommunication  |  Mobile Phone Subscription  | |    |  042  |  Telecommunication  |  Satellite TV  | |    |  043  |  Telecommunication  |  Streaming Services  | |  composite_travel  |  051  |  Travel & Vacation  |  Airplane Tickets  | |    |  052  |  Travel & Vacation  |  Business Travelers  | |    |  053  |  Travel & Vacation  |  Car Vacation  | |    |  054  |  Travel & Vacation  |  All Inclusive / Resorts  | |    |  055  |  Travel & Vacation  |  Adventure  | |    |  056  |  Travel & Vacation  |  Luxury  | |    |  057  |  Travel & Vacation  |  City Break  | |    |  058  |  Travel & Vacation  |  Hotels  | |  composite_winter  |  134  |  Christmas & Winter  |  Christmas Gifts - Young people | Over 100 €  | |    |  135  |  Christmas & Winter  |  Christmas Gifts - Young people | Under 100 €  | |    |  136  |  Christmas & Winter  |  Christmas Gifts | Families with children | Over 100 €  | |    |  137  |  Christmas & Winter  |  Christmas Gifts | Families with children | Under 100 €  | |    |  138  |  Christmas & Winter  |  Christmas Gifts | 50+ | Over 100 €  | |    |  139  |  Christmas & Winter  |  Christmas Gifts | 50+ | Under 100 €  | |    |  140  |  Christmas & Winter  |  Personal Gifts | Online Photo Books & Calendars  | |    |  141  |  Christmas & Winter  |  Winter Outerwear | Over 250 €  | |    |  142  |  Christmas & Winter  |  Winter Outerwear | Under 250 €  | |    |  143  |  Christmas & Winter  |  Winter Outerwear for Children  | |    |  144  |  Christmas & Winter  |  Winter Sports Clothing & Gear  | |    |  145  |  Christmas & Winter  |  Decoration | House & Garden  | |    |  146  |  Christmas & Winter  |  Decoration | Apartment & Balcony  | |    |  147  |  Christmas & Winter  |  Food and Wine | Online Supermarket w. Delivery  | |    |  148  |  Christmas & Winter  |  Food and Wine | Online Store  | |    |  149  |  Christmas & Winter  |  Fireplace & Wood Burning Stove  | |    |  151  |  Christmas & Winter  |  Winter to Summer Tire Change  |  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import datetime
from dateutil.parser import parse
from enum import Enum
import decimal
import json
import mimetypes
import os
import re
import tempfile

from urllib.parse import quote
from typing import Tuple, Optional, List, Dict, Union
from pydantic import SecretStr

from digiseg_api.configuration import Configuration
from digiseg_api.api_response import ApiResponse, T as ApiResponseT
import digiseg_api.models
from digiseg_api import rest
from digiseg_api.exceptions import (
    ApiValueError,
    ApiException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ServiceException
)

RequestSerialized = Tuple[str, str, Dict[str, str], Optional[str], List[str]]

class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int, # TODO remove as only py3 is supported?
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'decimal': decimal.Decimal,
        'object': object,
    }
    _pool = None

    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None
    ) -> None:
        # use default configuration if none is provided
        if configuration is None:
            configuration = Configuration.get_default()
        self.configuration = configuration

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'
        self.client_side_validation = configuration.client_side_validation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value


    _default = None

    @classmethod
    def get_default(cls):
        """Return new instance of ApiClient.

        This method returns newly created, based on default constructor,
        object of ApiClient class or returns a copy of default
        ApiClient.

        :return: The ApiClient object.
        """
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        """Set default instance of ApiClient.

        It stores default ApiClient.

        :param default: object of ApiClient.
        """
        cls._default = default

    def param_serialize(
        self,
        method,
        resource_path,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None, auth_settings=None,
        collection_formats=None,
        _host=None,
        _request_auth=None
    ) -> RequestSerialized:

        """Builds the HTTP request params needed by the request.
        :param method: Method to call.
        :param resource_path: Path to method endpoint.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :return: tuple of form (path, http_method, query_params, header_params,
            body, post_params, files)
        """

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params,collection_formats)
            )

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(
                path_params,
                collection_formats
            )
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(
                post_params,
                collection_formats
            )
            if files:
                post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(
            header_params,
            query_params,
            auth_settings,
            resource_path,
            method,
            body,
            request_auth=_request_auth
        )

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        if _host is None or self.configuration.ignore_operation_servers:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(
                query_params,
                collection_formats
            )
            url += "?" + url_query

        return method, url, header_params, body, post_params


    def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ) -> rest.RESTResponse:
        """Makes the HTTP request (synchronous)
        :param method: Method to call.
        :param url: Path to method endpoint.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param _request_timeout: timeout setting for this request.
        :return: RESTResponse
        """

        try:
            # perform request and return response
            response_data = self.rest_client.request(
                method, url,
                headers=header_params,
                body=body, post_params=post_params,
                _request_timeout=_request_timeout
            )

        except ApiException as e:
            raise e

        return response_data

    def response_deserialize(
        self,
        response_data: rest.RESTResponse,
        response_types_map: Optional[Dict[str, ApiResponseT]]=None
    ) -> ApiResponse[ApiResponseT]:
        """Deserializes response into an object.
        :param response_data: RESTResponse object to be deserialized.
        :param response_types_map: dict of response types.
        :return: ApiResponse
        """

        msg = "RESTResponse.read() must be called before passing it to response_deserialize()"
        assert response_data.data is not None, msg

        response_type = response_types_map.get(str(response_data.status), None)
        if not response_type and isinstance(response_data.status, int) and 100 <= response_data.status <= 599:
            # if not found, look for '1XX', '2XX', etc.
            response_type = response_types_map.get(str(response_data.status)[0] + "XX", None)

        # deserialize response data
        response_text = None
        return_data = None
        try:
            if response_type == "bytearray":
                return_data = response_data.data
            elif response_type == "file":
                return_data = self.__deserialize_file(response_data)
            elif response_type is not None:
                match = None
                content_type = response_data.getheader('content-type')
                if content_type is not None:
                    match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
                encoding = match.group(1) if match else "utf-8"
                response_text = response_data.data.decode(encoding)
                return_data = self.deserialize(response_text, response_type, content_type)
        finally:
            if not 200 <= response_data.status <= 299:
                raise ApiException.from_response(
                    http_resp=response_data,
                    body=response_text,
                    data=return_data,
                )

        return ApiResponse(
            status_code = response_data.status,
            data = return_data,
            headers = response_data.getheaders(),
            raw_data = response_data.data
        )

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is SecretStr, return obj.get_secret_value()
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is decimal.Decimal return string representation.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, SecretStr):
            return obj.get_secret_value()
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            ]
        elif isinstance(obj, tuple):
            return tuple(
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            )
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return str(obj)

        elif isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `openapi_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
                obj_dict = obj.to_dict()
            else:
                obj_dict = obj.__dict__

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in obj_dict.items()
        }

    def deserialize(self, response_text: str, response_type: str, content_type: Optional[str]):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.
        :param content_type: content type of response.

        :return: deserialized object.
        """

        # fetch data from response object
        if content_type is None:
            try:
                data = json.loads(response_text)
            except ValueError:
                data = response_text
        elif re.match(r'^application/(json|[\w!#$&.+-^_]+\+json)\s*(;|$)', content_type, re.IGNORECASE):
            if response_text == "":
                data = ""
            else:
                data = json.loads(response_text)
        elif re.match(r'^text\/[a-z.+-]+\s*(;|$)', content_type, re.IGNORECASE):
            data = response_text
        else:
            raise ApiException(
                status=0,
                reason="Unsupported content type: {0}".format(content_type)
            )

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith('List['):
                m = re.match(r'List\[(.*)]', klass)
                assert m is not None, "Malformed List type definition"
                sub_kls = m.group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('Dict['):
                m = re.match(r'Dict\[([^,]*), (.*)]', klass)
                assert m is not None, "Malformed Dict type definition"
                sub_kls = m.group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in data.items()}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(digiseg_api.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        elif klass == decimal.Decimal:
            return decimal.Decimal(data)
        elif issubclass(klass, Enum):
            return self.__deserialize_enum(data, klass)
        else:
            return self.__deserialize_model(data, klass)

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: URL query string (e.g. a=Hello%20World&b=123)
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = json.dumps(v)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, str(value)) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v))
                    )
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(map(str, item)) for item in new_params])

    def files_parameters(
        self,
        files: Dict[str, Union[str, bytes, List[str], List[bytes], Tuple[str, bytes]]],
    ):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []
        for k, v in files.items():
            if isinstance(v, str):
                with open(v, 'rb') as f:
                    filename = os.path.basename(f.name)
                    filedata = f.read()
            elif isinstance(v, bytes):
                filename = k
                filedata = v
            elif isinstance(v, tuple):
                filename, filedata = v
            elif isinstance(v, list):
                for file_param in v:
                    params.extend(self.files_parameters({k: file_param}))
                continue
            else:
                raise ValueError("Unsupported file value")
            mimetype = (
                mimetypes.guess_type(filename)[0]
                or 'application/octet-stream'
            )
            params.append(
                tuple([k, tuple([filename, filedata, mimetype])])
            )
        return params

    def select_header_accept(self, accepts: List[str]) -> Optional[str]:
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        for accept in accepts:
            if re.search('json', accept, re.IGNORECASE):
                return accept

        return accepts[0]

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        for content_type in content_types:
            if re.search('json', content_type, re.IGNORECASE):
                return content_type

        return content_types[0]

    def update_params_for_auth(
        self,
        headers,
        queries,
        auth_settings,
        resource_path,
        method,
        body,
        request_auth=None
    ) -> None:
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param request_auth: if set, the provided settings will
                             override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auth:
            self._apply_auth_params(
                headers,
                queries,
                resource_path,
                method,
                body,
                request_auth
            )
        else:
            for auth in auth_settings:
                auth_setting = self.configuration.auth_settings().get(auth)
                if auth_setting:
                    self._apply_auth_params(
                        headers,
                        queries,
                        resource_path,
                        method,
                        body,
                        auth_setting
                    )

    def _apply_auth_params(
        self,
        headers,
        queries,
        resource_path,
        method,
        body,
        auth_setting
    ) -> None:
        """Updates the request parameters based on a single auth_setting

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param auth_setting: auth settings for the endpoint
        """
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        handle file downloading
        save response body into a tmp file and return the instance

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            m = re.search(
                r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                content_disposition
            )
            assert m is not None, "Unexpected 'content-disposition' header value"
            filename = m.group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_enum(self, data, klass):
        """Deserializes primitive type to enum.

        :param data: primitive type.
        :param klass: class literal.
        :return: enum value.
        """
        try:
            return klass(data)
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as `{1}`"
                    .format(data, klass)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        return klass.from_dict(data)
