#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from cdktf_cdktf_provider_azurerm.resource_group import ResourceGroup


class MyMultipleStacksConfig:
    environment: str
    location: str
    def __init__(self, environment: str, location: str):
        self.environment = environment
        self.location = location


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: MyMultipleStacksConfig):
        super().__init__(scope, id)

        location = config.location

        AzurermProvider(self, "AzureRm", features={})

        my_azurerm_resource_group = ResourceGroup(
            self,
            "my_resource_group",
            name=f"resource-group-{config.environment}",
            location=location,
            tags={"environment": config.environment},
        )

multi_stack_app = App()

MyStack(
    multi_stack_app,
    "staging-stack",
    MyMultipleStacksConfig(environment="staging", location="East US"),
)

MyStack(
    multi_stack_app,
    "production-stack",
    MyMultipleStacksConfig(environment="production", location="East US 2"),
)

multi_stack_app.synth()