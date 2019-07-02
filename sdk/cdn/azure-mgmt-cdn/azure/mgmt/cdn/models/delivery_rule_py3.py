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

from msrest.serialization import Model


class DeliveryRule(Model):
    """A rule that specifies a set of actions and conditions.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the rule
    :type name: str
    :param order: Required. The order in which the rules are applied for the
     endpoint. Possible values {0,1,2,3,………}. A rule with a lesser order will
     be applied before a rule with a greater order. Rule with order 0 is a
     special rule. It does not require any condition and actions listed in it
     will always be applied.
    :type order: int
    :param conditions: A list of conditions that must be matched for the
     actions to be executed
    :type conditions: list[~azure.mgmt.cdn.models.DeliveryRuleCondition]
    :param actions: Required. A list of actions that are executed when all the
     conditions of a rule are satisfied.
    :type actions: list[~azure.mgmt.cdn.models.DeliveryRuleAction]
    """

    _validation = {
        'name': {'required': True},
        'order': {'required': True},
        'actions': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'conditions': {'key': 'conditions', 'type': '[DeliveryRuleCondition]'},
        'actions': {'key': 'actions', 'type': '[DeliveryRuleAction]'},
    }

    def __init__(self, *, name: str, order: int, actions, conditions=None, **kwargs) -> None:
        super(DeliveryRule, self).__init__(**kwargs)
        self.name = name
        self.order = order
        self.conditions = conditions
        self.actions = actions
