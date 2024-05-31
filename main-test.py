import pytest
from cdktf import Testing
from main import MyStack, MyMultipleStacksConfig
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from cdktf_cdktf_provider_azurerm.resource_group import ResourceGroup


# The tests below are example tests, you can find more information at
# https://cdk.tf/testing


class TestMain:

    config = MyMultipleStacksConfig(environment="test", location="East US 2")
    stack = MyStack(Testing.app(), "test-stack", config)
    synthesized = Testing.synth(stack)

    
    def test_should_have_azurerm_provider(self):
        assert Testing.to_have_provider(self.synthesized, AzurermProvider.TF_RESOURCE_TYPE)

    def test_should_have_resource_group(self):
        assert Testing.to_have_resource(self.synthesized, ResourceGroup.TF_RESOURCE_TYPE)

    def test_check_validity(self):
       assert Testing.to_be_valid_terraform(Testing.full_synth(self.stack))
