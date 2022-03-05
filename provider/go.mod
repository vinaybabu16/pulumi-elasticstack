module github.com/vinaybabu16/pulumi-elasticstack/provider

go 1.16

replace (
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20211230170131-3a7c83bfab87
)

require (
	github.com/hashicorp/terraform-plugin-sdk v1.9.1 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.18.0
	github.com/pulumi/pulumi/sdk/v3 v3.23.2
	github.com/vinaybabu16/terraform-provider-elasticstack v0.2.1-0.20220227074316-ffd36833fd5b
)
