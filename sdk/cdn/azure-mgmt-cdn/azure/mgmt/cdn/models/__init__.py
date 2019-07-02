# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .sku_py3 import Sku
    from .profile_py3 import Profile
    from .profile_update_parameters_py3 import ProfileUpdateParameters
    from .sso_uri_py3 import SsoUri
    from .supported_optimization_types_list_result_py3 import SupportedOptimizationTypesListResult
    from .deep_created_origin_py3 import DeepCreatedOrigin
    from .endpoint_py3 import Endpoint
    from .geo_filter_py3 import GeoFilter
    from .delivery_rule_condition_py3 import DeliveryRuleCondition
    from .delivery_rule_action_py3 import DeliveryRuleAction
    from .delivery_rule_py3 import DeliveryRule
    from .endpoint_properties_update_parameters_delivery_policy_py3 import EndpointPropertiesUpdateParametersDeliveryPolicy
    from .endpoint_properties_update_parameters_web_application_firewall_policy_link_py3 import EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink
    from .endpoint_update_parameters_py3 import EndpointUpdateParameters
    from .remote_address_match_condition_parameters_py3 import RemoteAddressMatchConditionParameters
    from .delivery_rule_remote_address_condition_py3 import DeliveryRuleRemoteAddressCondition
    from .request_method_match_condition_parameters_py3 import RequestMethodMatchConditionParameters
    from .delivery_rule_request_method_condition_py3 import DeliveryRuleRequestMethodCondition
    from .query_string_match_condition_parameters_py3 import QueryStringMatchConditionParameters
    from .delivery_rule_query_string_condition_py3 import DeliveryRuleQueryStringCondition
    from .post_args_match_condition_parameters_py3 import PostArgsMatchConditionParameters
    from .delivery_rule_post_args_condition_py3 import DeliveryRulePostArgsCondition
    from .request_uri_match_condition_parameters_py3 import RequestUriMatchConditionParameters
    from .delivery_rule_request_uri_condition_py3 import DeliveryRuleRequestUriCondition
    from .request_header_match_condition_parameters_py3 import RequestHeaderMatchConditionParameters
    from .delivery_rule_request_header_condition_py3 import DeliveryRuleRequestHeaderCondition
    from .request_body_match_condition_parameters_py3 import RequestBodyMatchConditionParameters
    from .delivery_rule_request_body_condition_py3 import DeliveryRuleRequestBodyCondition
    from .request_scheme_match_condition_parameters_py3 import RequestSchemeMatchConditionParameters
    from .delivery_rule_request_scheme_condition_py3 import DeliveryRuleRequestSchemeCondition
    from .url_path_match_condition_parameters_py3 import UrlPathMatchConditionParameters
    from .delivery_rule_url_path_condition_py3 import DeliveryRuleUrlPathCondition
    from .url_file_extension_match_condition_parameters_py3 import UrlFileExtensionMatchConditionParameters
    from .delivery_rule_url_file_extension_condition_py3 import DeliveryRuleUrlFileExtensionCondition
    from .url_file_name_match_condition_parameters_py3 import UrlFileNameMatchConditionParameters
    from .delivery_rule_url_file_name_condition_py3 import DeliveryRuleUrlFileNameCondition
    from .is_device_match_condition_parameters_py3 import IsDeviceMatchConditionParameters
    from .delivery_rule_is_device_condition_py3 import DeliveryRuleIsDeviceCondition
    from .url_redirect_action_parameters_py3 import UrlRedirectActionParameters
    from .url_redirect_action_py3 import UrlRedirectAction
    from .header_action_parameters_py3 import HeaderActionParameters
    from .delivery_rule_request_header_action_py3 import DeliveryRuleRequestHeaderAction
    from .delivery_rule_response_header_action_py3 import DeliveryRuleResponseHeaderAction
    from .cache_expiration_action_parameters_py3 import CacheExpirationActionParameters
    from .delivery_rule_cache_expiration_action_py3 import DeliveryRuleCacheExpirationAction
    from .purge_parameters_py3 import PurgeParameters
    from .load_parameters_py3 import LoadParameters
    from .origin_py3 import Origin
    from .origin_update_parameters_py3 import OriginUpdateParameters
    from .custom_domain_py3 import CustomDomain
    from .custom_domain_parameters_py3 import CustomDomainParameters
    from .custom_domain_https_parameters_py3 import CustomDomainHttpsParameters
    from .cdn_certificate_source_parameters_py3 import CdnCertificateSourceParameters
    from .cdn_managed_https_parameters_py3 import CdnManagedHttpsParameters
    from .key_vault_certificate_source_parameters_py3 import KeyVaultCertificateSourceParameters
    from .user_managed_https_parameters_py3 import UserManagedHttpsParameters
    from .validate_custom_domain_input_py3 import ValidateCustomDomainInput
    from .validate_custom_domain_output_py3 import ValidateCustomDomainOutput
    from .check_name_availability_input_py3 import CheckNameAvailabilityInput
    from .check_name_availability_output_py3 import CheckNameAvailabilityOutput
    from .validate_probe_input_py3 import ValidateProbeInput
    from .validate_probe_output_py3 import ValidateProbeOutput
    from .resource_usage_py3 import ResourceUsage
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .cidr_ip_address_py3 import CidrIpAddress
    from .ip_address_group_py3 import IpAddressGroup
    from .edge_node_py3 import EdgeNode
    from .resource_py3 import Resource
    from .tracked_resource_py3 import TrackedResource
    from .proxy_resource_py3 import ProxyResource
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .policy_settings_py3 import PolicySettings
    from .rate_limit_rule_py3 import RateLimitRule
    from .rate_limit_rule_list_py3 import RateLimitRuleList
    from .match_condition_py3 import MatchCondition
    from .action_type_py3 import ActionType
    from .custom_rule_py3 import CustomRule
    from .custom_rule_list_py3 import CustomRuleList
    from .managed_rule_override_py3 import ManagedRuleOverride
    from .managed_rule_group_override_py3 import ManagedRuleGroupOverride
    from .managed_rule_set_py3 import ManagedRuleSet
    from .managed_rule_set_list_py3 import ManagedRuleSetList
    from .cdn_endpoint_py3 import CdnEndpoint
    from .cdn_web_application_firewall_policy_py3 import CdnWebApplicationFirewallPolicy
    from .cdn_web_application_firewall_policy_patch_parameters_py3 import CdnWebApplicationFirewallPolicyPatchParameters
    from .managed_rule_definition_py3 import ManagedRuleDefinition
    from .managed_rule_group_definition_py3 import ManagedRuleGroupDefinition
    from .managed_rule_set_definition_py3 import ManagedRuleSetDefinition
except (SyntaxError, ImportError):
    from .sku import Sku
    from .profile import Profile
    from .profile_update_parameters import ProfileUpdateParameters
    from .sso_uri import SsoUri
    from .supported_optimization_types_list_result import SupportedOptimizationTypesListResult
    from .deep_created_origin import DeepCreatedOrigin
    from .endpoint import Endpoint
    from .geo_filter import GeoFilter
    from .delivery_rule_condition import DeliveryRuleCondition
    from .delivery_rule_action import DeliveryRuleAction
    from .delivery_rule import DeliveryRule
    from .endpoint_properties_update_parameters_delivery_policy import EndpointPropertiesUpdateParametersDeliveryPolicy
    from .endpoint_properties_update_parameters_web_application_firewall_policy_link import EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink
    from .endpoint_update_parameters import EndpointUpdateParameters
    from .remote_address_match_condition_parameters import RemoteAddressMatchConditionParameters
    from .delivery_rule_remote_address_condition import DeliveryRuleRemoteAddressCondition
    from .request_method_match_condition_parameters import RequestMethodMatchConditionParameters
    from .delivery_rule_request_method_condition import DeliveryRuleRequestMethodCondition
    from .query_string_match_condition_parameters import QueryStringMatchConditionParameters
    from .delivery_rule_query_string_condition import DeliveryRuleQueryStringCondition
    from .post_args_match_condition_parameters import PostArgsMatchConditionParameters
    from .delivery_rule_post_args_condition import DeliveryRulePostArgsCondition
    from .request_uri_match_condition_parameters import RequestUriMatchConditionParameters
    from .delivery_rule_request_uri_condition import DeliveryRuleRequestUriCondition
    from .request_header_match_condition_parameters import RequestHeaderMatchConditionParameters
    from .delivery_rule_request_header_condition import DeliveryRuleRequestHeaderCondition
    from .request_body_match_condition_parameters import RequestBodyMatchConditionParameters
    from .delivery_rule_request_body_condition import DeliveryRuleRequestBodyCondition
    from .request_scheme_match_condition_parameters import RequestSchemeMatchConditionParameters
    from .delivery_rule_request_scheme_condition import DeliveryRuleRequestSchemeCondition
    from .url_path_match_condition_parameters import UrlPathMatchConditionParameters
    from .delivery_rule_url_path_condition import DeliveryRuleUrlPathCondition
    from .url_file_extension_match_condition_parameters import UrlFileExtensionMatchConditionParameters
    from .delivery_rule_url_file_extension_condition import DeliveryRuleUrlFileExtensionCondition
    from .url_file_name_match_condition_parameters import UrlFileNameMatchConditionParameters
    from .delivery_rule_url_file_name_condition import DeliveryRuleUrlFileNameCondition
    from .is_device_match_condition_parameters import IsDeviceMatchConditionParameters
    from .delivery_rule_is_device_condition import DeliveryRuleIsDeviceCondition
    from .url_redirect_action_parameters import UrlRedirectActionParameters
    from .url_redirect_action import UrlRedirectAction
    from .header_action_parameters import HeaderActionParameters
    from .delivery_rule_request_header_action import DeliveryRuleRequestHeaderAction
    from .delivery_rule_response_header_action import DeliveryRuleResponseHeaderAction
    from .cache_expiration_action_parameters import CacheExpirationActionParameters
    from .delivery_rule_cache_expiration_action import DeliveryRuleCacheExpirationAction
    from .purge_parameters import PurgeParameters
    from .load_parameters import LoadParameters
    from .origin import Origin
    from .origin_update_parameters import OriginUpdateParameters
    from .custom_domain import CustomDomain
    from .custom_domain_parameters import CustomDomainParameters
    from .custom_domain_https_parameters import CustomDomainHttpsParameters
    from .cdn_certificate_source_parameters import CdnCertificateSourceParameters
    from .cdn_managed_https_parameters import CdnManagedHttpsParameters
    from .key_vault_certificate_source_parameters import KeyVaultCertificateSourceParameters
    from .user_managed_https_parameters import UserManagedHttpsParameters
    from .validate_custom_domain_input import ValidateCustomDomainInput
    from .validate_custom_domain_output import ValidateCustomDomainOutput
    from .check_name_availability_input import CheckNameAvailabilityInput
    from .check_name_availability_output import CheckNameAvailabilityOutput
    from .validate_probe_input import ValidateProbeInput
    from .validate_probe_output import ValidateProbeOutput
    from .resource_usage import ResourceUsage
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .cidr_ip_address import CidrIpAddress
    from .ip_address_group import IpAddressGroup
    from .edge_node import EdgeNode
    from .resource import Resource
    from .tracked_resource import TrackedResource
    from .proxy_resource import ProxyResource
    from .error_response import ErrorResponse, ErrorResponseException
    from .policy_settings import PolicySettings
    from .rate_limit_rule import RateLimitRule
    from .rate_limit_rule_list import RateLimitRuleList
    from .match_condition import MatchCondition
    from .action_type import ActionType
    from .custom_rule import CustomRule
    from .custom_rule_list import CustomRuleList
    from .managed_rule_override import ManagedRuleOverride
    from .managed_rule_group_override import ManagedRuleGroupOverride
    from .managed_rule_set import ManagedRuleSet
    from .managed_rule_set_list import ManagedRuleSetList
    from .cdn_endpoint import CdnEndpoint
    from .cdn_web_application_firewall_policy import CdnWebApplicationFirewallPolicy
    from .cdn_web_application_firewall_policy_patch_parameters import CdnWebApplicationFirewallPolicyPatchParameters
    from .managed_rule_definition import ManagedRuleDefinition
    from .managed_rule_group_definition import ManagedRuleGroupDefinition
    from .managed_rule_set_definition import ManagedRuleSetDefinition
from .profile_paged import ProfilePaged
from .resource_usage_paged import ResourceUsagePaged
from .endpoint_paged import EndpointPaged
from .origin_paged import OriginPaged
from .custom_domain_paged import CustomDomainPaged
from .operation_paged import OperationPaged
from .edge_node_paged import EdgeNodePaged
from .cdn_web_application_firewall_policy_paged import CdnWebApplicationFirewallPolicyPaged
from .managed_rule_set_definition_paged import ManagedRuleSetDefinitionPaged
from .cdn_management_client_enums import (
    SkuName,
    ProfileResourceState,
    OptimizationType,
    EndpointResourceState,
    QueryStringCachingBehavior,
    GeoFilterActions,
    RemoteAddressOperator,
    Transform,
    QueryStringOperator,
    PostArgsOperator,
    RequestUriOperator,
    RequestHeaderOperator,
    RequestBodyOperator,
    UrlPathOperator,
    UrlFileExtensionOperator,
    UrlFileNameOperator,
    RedirectType,
    DestinationProtocol,
    HeaderAction,
    CacheBehavior,
    OriginResourceState,
    CustomDomainResourceState,
    CustomHttpsProvisioningState,
    CustomHttpsProvisioningSubstate,
    ProtocolType,
    CertificateType,
    ResourceType,
    PolicyEnabledState,
    PolicyMode,
    CustomRuleEnabledState,
    MatchVariable,
    Operator,
    Action,
    ManagedRuleEnabledState,
    ProvisioningState,
    PolicyResourceState,
)

__all__ = [
    'Sku',
    'Profile',
    'ProfileUpdateParameters',
    'SsoUri',
    'SupportedOptimizationTypesListResult',
    'DeepCreatedOrigin',
    'Endpoint',
    'GeoFilter',
    'DeliveryRuleCondition',
    'DeliveryRuleAction',
    'DeliveryRule',
    'EndpointPropertiesUpdateParametersDeliveryPolicy',
    'EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink',
    'EndpointUpdateParameters',
    'RemoteAddressMatchConditionParameters',
    'DeliveryRuleRemoteAddressCondition',
    'RequestMethodMatchConditionParameters',
    'DeliveryRuleRequestMethodCondition',
    'QueryStringMatchConditionParameters',
    'DeliveryRuleQueryStringCondition',
    'PostArgsMatchConditionParameters',
    'DeliveryRulePostArgsCondition',
    'RequestUriMatchConditionParameters',
    'DeliveryRuleRequestUriCondition',
    'RequestHeaderMatchConditionParameters',
    'DeliveryRuleRequestHeaderCondition',
    'RequestBodyMatchConditionParameters',
    'DeliveryRuleRequestBodyCondition',
    'RequestSchemeMatchConditionParameters',
    'DeliveryRuleRequestSchemeCondition',
    'UrlPathMatchConditionParameters',
    'DeliveryRuleUrlPathCondition',
    'UrlFileExtensionMatchConditionParameters',
    'DeliveryRuleUrlFileExtensionCondition',
    'UrlFileNameMatchConditionParameters',
    'DeliveryRuleUrlFileNameCondition',
    'IsDeviceMatchConditionParameters',
    'DeliveryRuleIsDeviceCondition',
    'UrlRedirectActionParameters',
    'UrlRedirectAction',
    'HeaderActionParameters',
    'DeliveryRuleRequestHeaderAction',
    'DeliveryRuleResponseHeaderAction',
    'CacheExpirationActionParameters',
    'DeliveryRuleCacheExpirationAction',
    'PurgeParameters',
    'LoadParameters',
    'Origin',
    'OriginUpdateParameters',
    'CustomDomain',
    'CustomDomainParameters',
    'CustomDomainHttpsParameters',
    'CdnCertificateSourceParameters',
    'CdnManagedHttpsParameters',
    'KeyVaultCertificateSourceParameters',
    'UserManagedHttpsParameters',
    'ValidateCustomDomainInput',
    'ValidateCustomDomainOutput',
    'CheckNameAvailabilityInput',
    'CheckNameAvailabilityOutput',
    'ValidateProbeInput',
    'ValidateProbeOutput',
    'ResourceUsage',
    'OperationDisplay',
    'Operation',
    'CidrIpAddress',
    'IpAddressGroup',
    'EdgeNode',
    'Resource',
    'TrackedResource',
    'ProxyResource',
    'ErrorResponse', 'ErrorResponseException',
    'PolicySettings',
    'RateLimitRule',
    'RateLimitRuleList',
    'MatchCondition',
    'ActionType',
    'CustomRule',
    'CustomRuleList',
    'ManagedRuleOverride',
    'ManagedRuleGroupOverride',
    'ManagedRuleSet',
    'ManagedRuleSetList',
    'CdnEndpoint',
    'CdnWebApplicationFirewallPolicy',
    'CdnWebApplicationFirewallPolicyPatchParameters',
    'ManagedRuleDefinition',
    'ManagedRuleGroupDefinition',
    'ManagedRuleSetDefinition',
    'ProfilePaged',
    'ResourceUsagePaged',
    'EndpointPaged',
    'OriginPaged',
    'CustomDomainPaged',
    'OperationPaged',
    'EdgeNodePaged',
    'CdnWebApplicationFirewallPolicyPaged',
    'ManagedRuleSetDefinitionPaged',
    'SkuName',
    'ProfileResourceState',
    'OptimizationType',
    'EndpointResourceState',
    'QueryStringCachingBehavior',
    'GeoFilterActions',
    'RemoteAddressOperator',
    'Transform',
    'QueryStringOperator',
    'PostArgsOperator',
    'RequestUriOperator',
    'RequestHeaderOperator',
    'RequestBodyOperator',
    'UrlPathOperator',
    'UrlFileExtensionOperator',
    'UrlFileNameOperator',
    'RedirectType',
    'DestinationProtocol',
    'HeaderAction',
    'CacheBehavior',
    'OriginResourceState',
    'CustomDomainResourceState',
    'CustomHttpsProvisioningState',
    'CustomHttpsProvisioningSubstate',
    'ProtocolType',
    'CertificateType',
    'ResourceType',
    'PolicyEnabledState',
    'PolicyMode',
    'CustomRuleEnabledState',
    'MatchVariable',
    'Operator',
    'Action',
    'ManagedRuleEnabledState',
    'ProvisioningState',
    'PolicyResourceState',
]
