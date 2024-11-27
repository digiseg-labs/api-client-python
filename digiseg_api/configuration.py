# coding: utf-8

"""
    Digiseg API

    ### Digiseg API documentation  # Introduction  This API let you harness the power of Digisegs powerful and tracking-free segmentation engine.  Audiences by Digiseg are available in 50+ countries, probablistically mapping neighborhood characteristics to the IP addresses observed on the internet - Household targeting & measurement for the post-cookie world.  ## Developer SDKs  In addition to using these APIs directly through any HTTP client, we provide a set of API client SDKs for popular programming languages:  <div class=\"api-clients\">   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-python\">     <i class=\"api-client-sdk-logo devicon-python-plain\"></i>     <p>API client for Python</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-ts\">     <i class=\"api-client-sdk-logo devicon-typescript-plain\"></i>     <p>API client for TypeScript</p>   </a>   <a class=\"api-client-box\" href=\"https://github.com/digiseg-labs/api-client-go\">     <i class=\"api-client-sdk-logo devicon-go-original-wordmark\"></i>     <p>API client for Go</p>   </a> </div> <div class=\"api-clients-breaker\" />  ## Audience taxonomy  Digiseg audiences are grouped into private and business audiences. In each group there are categories that then contain the audiences. The API endpoints that communicate audiences and household characteristics, audience codes are being used.  The following table can be used as a reference for audience codes. Note that Digiseg will at times update names of audiences for purposes of internationalization, clarity or other such purposes - but the codes will remain as-is and should be considered a stable point of reference for the audience.  ### Core audiences | Group | Category code | Audience Code | Category name | Audience Name | |-------|---------------|---------------|---------------|---------------| |  private  |  home_type  |  a1  |  Home Type  |  Apartment  | |    |    |  a2  |  Home Type  |  House  | |    |  savings  |  b1  |  Savings  |  No Savings  | |    |    |  b2  |  Savings  |  Smaller Savings  | |    |    |  b3  |  Savings  |  Larger Savings  | |    |  lifecycle  |  c1  |  Lifecycle  |  Young couples and singles  | |    |    |  c2  |  Lifecycle  |  Early family life  | |    |    |  c3  |  Lifecycle  |  Middle-aged families  | |    |    |  c4  |  Lifecycle  |  Mature families  | |    |    |  c5  |  Lifecycle  |  Pensioners / Retirees  | |    |  cars  |  d1  |  Cars in Household  |  No cars  | |    |    |  d2  |  Cars in Household  |  1 car  | |    |    |  d3  |  Cars in Household  |  2 or more cars  | |    |  children  |  e1  |  Children in the Household  |  No children  | |    |    |  e2  |  Children in the Household  |  1 child  | |    |    |  e3  |  Children in the Household  |  2 or more children  | |    |  education  |  f1  |  Education  |  Basic  | |    |    |  f2  |  Education  |  Medium  | |    |    |  f3  |  Education  |  Higher  | |    |  neighbourhood_type  |  g1  |  Neighbourhood Type  |  Countryside  | |    |    |  g2  |  Neighbourhood Type  |  Village  | |    |    |  g3  |  Neighbourhood Type  |  Suburban  | |    |    |  g4  |  Neighbourhood Type  |  City  | |    |  income  |  h1  |  Household Income  |  Lowest 20%  | |    |    |  h2  |  Household Income  |  Lowest 20-40%  | |    |    |  h3  |  Household Income  |  Middle 40-60%  | |    |    |  h4  |  Household Income  |  Highest 60-80%  | |    |    |  h5  |  Household Income  |  Top 20%  | |    |  home_ownership  |  j1  |  Home Ownership  |  Rent  | |    |    |  j2  |  Home Ownership  |  Own  | |    |  building_age  |  k1  |  Building Age  |  Pre 1945  | |    |    |  k2  |  Building Age  |  1945-1989  | |    |    |  k3  |  Building Age  |  1990 until today  | |    |  living_space  |  l1  |  Living space  |  Small  | |    |    |  l2  |  Living space  |  Medium  | |    |    |  l3  |  Living space  |  Large  | |    |  tech_level  |  n1  |  Tech-Level in Household  |  Basic  | |    |    |  n2  |  Tech-Level in Household  |  Medium  | |    |    |  n3  |  Tech-Level in Household  |  High  | |  business  |  size  |  ba1  |  Business  |  Small Business  | |    |    |  ba2  |  Business  |  Medium Business  | |    |    |  ba3  |  Business  |  Larger Business  | ### Composite audiences | Category code | Audience Code | Category name | Audience Name | |---------------|---------------|---------------|---------------| |  composite_betting  |  060  |  Betting Online  |  Betting, Casino & Poker  | |  composite_buyingpower  |  092  |  Buying Power  |  Buying Power Low  | |    |  093  |  Buying Power  |  Buying Power High  | |  composite_carclass  |  001  |  Car Classes  |  Micro & City  | |    |  002  |  Car Classes  |  Mini  | |    |  003  |  Car Classes  |  Small Medium / Compact  | |    |  004  |  Car Classes  |  Large Medium  | |    |  005  |  Car Classes  |  Large Premium  | |    |  006  |  Car Classes  |  Large Luxury Sedan  | |    |  007  |  Car Classes  |  MPV / Minivans  | |    |  008  |  Car Classes  |  SUV  | |    |  009  |  Car Classes  |  Electric & Hybrid  | |    |  010  |  Car Classes  |  Sport  | |  composite_career  |  110  |  Recruitment & Career  |  Employment in Large Companies  | |    |  111  |  Recruitment & Career  |  C-Level Positions  | |    |  112  |  Recruitment & Career  |  Management Positions  | |    |  113  |  Recruitment & Career  |  Graduate Programs & First Job  | |    |  114  |  Recruitment & Career  |  IT Positions  | |    |  158  |  Recruitment & Career  |  Employment in Small Companies  | |  composite_carservice  |  011  |  Car Services  |  Service & Car Parts  | |    |  012  |  Car Services  |  Car Tires  | |    |  013  |  Car Services  |  Car Leasing (Private)  | |  composite_childrensarticles  |  044  |  Children Articles  |  Games & Toys  | |  composite_computer_games  |  059  |  Computer Games  |  Games & Consoles  | |  composite_culture_entertainment  |  045  |  Culture & Entertainment  |  Cinema Tickets  | |    |  046  |  Culture & Entertainment  |  Opera & Theater  | |    |  047  |  Culture & Entertainment  |  Concert & Festival  | |    |  048  |  Culture & Entertainment  |  Museum & Exhibition  | |    |  049  |  Culture & Entertainment  |  Books  | |    |  050  |  Culture & Entertainment  |  Audiobooks  | |  composite_electronics  |  061  |  Electronics  |  TV  | |    |  062  |  Electronics  |  Phones & Smartphones  | |    |  063  |  Electronics  |  Small Domestic Appliances  | |    |  064  |  Electronics  |  Major Domestic Appliances  | |    |  065  |  Electronics  |  Garden Articles  | |    |  066  |  Electronics  |  HiFi Audio  | |    |  067  |  Electronics  |  Computer Tablet  | |    |  068  |  Electronics  |  Software & Apps  | |  composite_fashion  |  130  |  Fashion & Shopping  |  Shopping Mall Visitors  | |    |  131  |  Fashion & Shopping  |  Footwear & Shoes  | |    |  132  |  Fashion & Shopping  |  Jewellery  | |    |  133  |  Fashion & Shopping  |  Clothes  | |  composite_financials  |  014  |  Banking / Financing  |  House Loan  | |    |  015  |  Banking / Financing  |  Car Loan  | |    |  016  |  Banking / Financing  |  Consumer Loan  | |    |  017  |  Banking / Financing  |  Renovation  | |    |  018  |  Banking / Financing  |  Quick Loan  | |    |  019  |  Banking / Financing  |  Mobile Banking  | |    |  020  |  Banking / Financing  |  Investors  | |  composite_fmcg  |  069  |  Fast-Moving Consumer Good (FMCG)  |  Candy & Sweets  | |    |  070  |  Fast-Moving Consumer Good (FMCG)  |  Energy Drinks  | |    |  071  |  Fast-Moving Consumer Good (FMCG)  |  Sodas  | |    |  072  |  Fast-Moving Consumer Good (FMCG)  |  Chips  | |    |  073  |  Fast-Moving Consumer Good (FMCG)  |  Washing Detergents  | |    |  074  |  Fast-Moving Consumer Good (FMCG)  |  Bio & Organic Products  | |    |  075  |  Fast-Moving Consumer Good (FMCG)  |  Baby Food  | |    |  076  |  Fast-Moving Consumer Good (FMCG)  |  Dairy Products  | |    |  077  |  Fast-Moving Consumer Good (FMCG)  |  Beer  | |  composite_homerenovation  |  031  |  Home Renovation  |  House or apartment decoration  | |    |  032  |  Home Renovation  |  Kitchen  | |    |  033  |  Home Renovation  |  Bathroom & Plumbing  | |    |  034  |  Home Renovation  |  Windows, Doors & Tiles  | |    |  035  |  Home Renovation  |  Garden  | |    |  036  |  Home Renovation  |  Furniture  | |  composite_homesecurity  |  094  |  Home Security  |  House Alarms & Video Surveillance  | |  composite_insurance  |  021  |  Insurance  |  Car  | |    |  022  |  Insurance  |  House & Apartment  | |    |  023  |  Insurance  |  Accident Insurance  | |    |  024  |  Insurance  |  Life Insurance  | |    |  025  |  Insurance  |  Pension Fund  | |    |  026  |  Insurance  |  Travel Insurance  | |  composite_lifecycle  |  083  |  Lifestyle  |  Fitness, Gym & Workout  | |    |  084  |  Lifestyle  |  Stop Smoking  | |    |  085  |  Lifestyle  |  Natural Medicin  | |    |  086  |  Lifestyle  |  Gym Supplements & Nutrients  | |    |  087  |  Lifestyle  |  Small Pets  | |    |  088  |  Lifestyle  |  Large Pets  | |    |  089  |  Lifestyle  |  Weight Loss  | |    |  091  |  Lifestyle  |  Students  | |  composite_occasions  |  102  |  Occasions & Presents  |  Valentine's Day  | |    |  103  |  Occasions & Presents  |  Mothers's Day  | |    |  104  |  Occasions & Presents  |  Fathers's Day  | |    |  105  |  Occasions & Presents  |  Children's Day  | |    |  106  |  Occasions & Presents  |  Wedding & Engagement  | |    |  107  |  Occasions & Presents  |  Women's Day  | |    |  108  |  Occasions & Presents  |  Black Friday  | |    |  109  |  Occasions & Presents  |  Cyber Monday  | |    |  152  |  Occasions & Presents  |  Presents for young / inexpensive  | |    |  153  |  Occasions & Presents  |  Presents for young / expensive  | |    |  154  |  Occasions & Presents  |  Presents for families with children / inexpensive  | |    |  155  |  Occasions & Presents  |  Presents for families with children / expensive  | |    |  156  |  Occasions & Presents  |  Presents for mature / inexpensive  | |    |  157  |  Occasions & Presents  |  Presents for mature / expensive  | |  composite_olympics  |  159  |  Olympics  |  Olympics Visitors  | |    |  160  |  Olympics  |  Olympics Watchers  | |  composite_personalhygiene  |  078  |  Personal Hygiene  |  Baby Hygiene  | |    |  079  |  Personal Hygiene  |  SPF Sunscreen  | |    |  080  |  Personal Hygiene  |  Toothbrushes & Toothpaste  | |    |  081  |  Personal Hygiene  |  Cosmetics  | |    |  082  |  Personal Hygiene  |  Parfumes  | |  composite_politics  |  115  |  Political Themes  |  Children & Youth  | |    |  116  |  Political Themes  |  Elder Care  | |    |  117  |  Political Themes  |  Research & Education System  | |    |  118  |  Political Themes  |  Public Transport  | |    |  119  |  Political Themes  |  Car Transport & Road Infrastructure  | |    |  120  |  Political Themes  |  Art & Culture  | |    |  121  |  Political Themes  |  Green Transition & Environment  | |    |  122  |  Political Themes  |  Law & Order  | |    |  123  |  Political Themes  |  Immigration  | |    |  124  |  Political Themes  |  Tax Reliefs  | |    |  126  |  Political Themes  |  Euro-supporters  | |    |  128  |  Political Themes  |  Women's Rights & Gender Equality  | |    |  129  |  Political Themes  |  Corruption & Bureaucracy  | |  composite_realestatetrading  |  027  |  Real Estate Trading  |  First-time Buyers  | |    |  028  |  Real Estate Trading  |  Summerhouse  | |    |  029  |  Real Estate Trading  |  Apartment  | |    |  030  |  Real Estate Trading  |  House & Villa  | |  composite_restaurants  |  037  |  Restaurants  |  Fastfood  | |    |  038  |  Restaurants  |  Restaurant  | |    |  039  |  Restaurants  |  Cafe & Bar  | |  composite_telecom  |  040  |  Telecommunication  |  Internet  | |    |  041  |  Telecommunication  |  Mobile Phone Subscription  | |    |  042  |  Telecommunication  |  Satellite TV  | |    |  043  |  Telecommunication  |  Streaming Services  | |  composite_travel  |  051  |  Travel & Vacation  |  Airplane Tickets  | |    |  052  |  Travel & Vacation  |  Business Travelers  | |    |  053  |  Travel & Vacation  |  Car Vacation  | |    |  054  |  Travel & Vacation  |  All Inclusive / Resorts  | |    |  055  |  Travel & Vacation  |  Adventure  | |    |  056  |  Travel & Vacation  |  Luxury  | |    |  057  |  Travel & Vacation  |  City Break  | |    |  058  |  Travel & Vacation  |  Hotels  | |  composite_winter  |  134  |  Christmas & Winter  |  Christmas Gifts - Young people | Over 100 €  | |    |  135  |  Christmas & Winter  |  Christmas Gifts - Young people | Under 100 €  | |    |  136  |  Christmas & Winter  |  Christmas Gifts | Families with children | Over 100 €  | |    |  137  |  Christmas & Winter  |  Christmas Gifts | Families with children | Under 100 €  | |    |  138  |  Christmas & Winter  |  Christmas Gifts | 50+ | Over 100 €  | |    |  139  |  Christmas & Winter  |  Christmas Gifts | 50+ | Under 100 €  | |    |  140  |  Christmas & Winter  |  Personal Gifts | Online Photo Books & Calendars  | |    |  141  |  Christmas & Winter  |  Winter Outerwear | Over 250 €  | |    |  142  |  Christmas & Winter  |  Winter Outerwear | Under 250 €  | |    |  143  |  Christmas & Winter  |  Winter Outerwear for Children  | |    |  144  |  Christmas & Winter  |  Winter Sports Clothing & Gear  | |    |  145  |  Christmas & Winter  |  Decoration | House & Garden  | |    |  146  |  Christmas & Winter  |  Decoration | Apartment & Balcony  | |    |  147  |  Christmas & Winter  |  Food and Wine | Online Supermarket w. Delivery  | |    |  148  |  Christmas & Winter  |  Food and Wine | Online Store  | |    |  149  |  Christmas & Winter  |  Fireplace & Wood Burning Stove  | |    |  151  |  Christmas & Winter  |  Winter to Summer Tire Change  |  There is also an interactive [Audience builder](https://digiseg.io/cookieless-audience-builder/) which lets you discover the targeting reach and power of combining various household characteristics into composite audiences. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@digiseg.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import copy
import logging
from logging import FileHandler
import multiprocessing
import sys
from typing import Optional
import urllib3

import http.client as httplib

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param ignore_operation_servers
      Boolean to ignore operation servers for the API client.
      Config will use `host` as the base url regardless of the operation servers.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.
    :param retries: Number of retries for API requests.

    :Example:

    API Key Authentication Example.
    Given the following security scheme in the OpenAPI specification:
      components:
        securitySchemes:
          cookieAuth:         # name for the security scheme
            type: apiKey
            in: cookie
            name: JSESSIONID  # cookie name

    You can programmatically set the cookie:

conf = digiseg_api.Configuration(
    api_key={'cookieAuth': 'abc123'}
    api_key_prefix={'cookieAuth': 'JSESSIONID'}
)

    The following cookie will be added to the HTTP request:
       Cookie: JSESSIONID abc123
    """

    _default = None

    def __init__(self, host=None,
                 api_key=None, api_key_prefix=None,
                 username=None, password=None,
                 access_token=None,
                 server_index=None, server_variables=None,
                 server_operation_index=None, server_operation_variables=None,
                 ignore_operation_servers=False,
                 ssl_ca_cert=None,
                 retries=None,
                 *,
                 debug: Optional[bool] = None
                 ) -> None:
        """Constructor
        """
        self._base_path = "https://api.digiseg.net" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.ignore_operation_servers = ignore_operation_servers
        """Ignore operation servers
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.access_token = access_token
        """Access token
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("digiseg_api")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler: Optional[FileHandler] = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        if debug is not None:
            self.debug = debug
        else:
            self.__debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy: Optional[str] = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = retries
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default_copy(cls):
        """Deprecated. Please use `get_default` instead.

        Deprecated. Please use `get_default` instead.

        :return: The configuration object.
        """
        return cls.get_default()

    @classmethod
    def get_default(cls):
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = Configuration()
        return cls._default

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if self.access_token is not None:
            auth['bearerAuth'] = {
                'type': 'bearer',
                'in': 'header',
                'format': 'JWT',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        if 'apiKeyHeaderAuth' in self.api_key:
            auth['apiKeyHeaderAuth'] = {
                'type': 'api_key',
                'in': 'header',
                'key': 'X-API-KEY',
                'value': self.get_api_key_with_prefix(
                    'apiKeyHeaderAuth',
                ),
            }
        if 'apiKeyQueryParamAuth' in self.api_key:
            auth['apiKeyQueryParamAuth'] = {
                'type': 'api_key',
                'in': 'query',
                'key': 'api_key',
                'value': self.get_api_key_with_prefix(
                    'apiKeyQueryParamAuth',
                ),
            }
        if self.access_token is not None:
            auth['oAuth'] = {
                'type': 'oauth2',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://api.digiseg.net",
                'description': "Digiseg API - production",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None
