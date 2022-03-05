// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package elasticstack

import (
	"fmt"
	"path/filepath"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/vinaybabu16/pulumi-elasticstack/provider/pkg/version"
	elasticstack "github.com/vinaybabu16/terraform-provider-elasticstack/elasticstack/provider"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "elasticstack"
	// modules:
	mainMod = "index" // the elasticstack module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(elasticstack.New("refactor-provider")())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "elasticstack",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "Pulumi",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "",
		Description:       "A Pulumi package for creating and managing elasticstack cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:   []string{"pulumi", "elasticstack", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.pulumi.com",
		Repository: "https://github.com/pulumi/pulumi-elasticstack",
		// The GitHub Org for the provider - defaults to `terraform-providers`
		GitHubOrg: "vinaybabu16",
		Config:    map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			// "aws_iam_role": {Tok: tfbridge.MakeResource(mainMod, "IamRole")}
			//
			// "aws_acm_certificate": {
			// 	Tok: tfbridge.MakeResource(mainMod, "Certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: tfbridge.MakeType(mainPkg, "Tags")},
			// 	},
			// },
			"elasticstack_elasticsearch_cluster_settings":    {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchClusterSettings")},
			"elasticstack_elasticsearch_component_template":  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchComponentTemplate")},
			"elasticstack_elasticsearch_data_stream":         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchDataStream")},
			"elasticstack_elasticsearch_index":               {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchIndex")},
			"elasticstack_elasticsearch_index_lifecycle":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchIndexLifecycle")},
			"elasticstack_elasticsearch_index_template":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchIndexTemplate")},
			"elasticstack_elasticsearch_ingest_pipeline":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchIngestPipeline")},
			"elasticstack_elasticsearch_security_role":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchSecurityRole")},
			"elasticstack_elasticsearch_security_user":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchSecurityUser")},
			"elasticstack_elasticsearch_snapshot_lifecycle":  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchSnapshotLifecycle")},
			"elasticstack_elasticsearch_snapshot_repository": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ElasticsearchSnapshotRepository")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: tfbridge.MakeDataSource(mainMod, "getAmi")},
			"elasticstack_elasticsearch_ingest_processor_append":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorAppend")},
			"elasticstack_elasticsearch_ingest_processor_bytes":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorBytes")},
			"elasticstack_elasticsearch_ingest_processor_circle":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorCircle")},
			"elasticstack_elasticsearch_ingest_processor_community_id":      {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorCommunityId")},
			"elasticstack_elasticsearch_ingest_processor_convert":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorConvert")},
			"elasticstack_elasticsearch_ingest_processor_csv":               {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorCsv")},
			"elasticstack_elasticsearch_ingest_processor_date":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorDate")},
			"elasticstack_elasticsearch_ingest_processor_date_index_name":   {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorDateIndexName")},
			"elasticstack_elasticsearch_ingest_processor_dissect":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorDissect")},
			"elasticstack_elasticsearch_ingest_processor_dot_expander":      {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorDotExpander")},
			"elasticstack_elasticsearch_ingest_processor_drop":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorDrop")},
			"elasticstack_elasticsearch_ingest_processor_enrich":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorEnrich")},
			"elasticstack_elasticsearch_ingest_processor_fail":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorFail")},
			"elasticstack_elasticsearch_ingest_processor_fingerprint":       {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorFingerprint")},
			"elasticstack_elasticsearch_ingest_processor_foreach":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorForeach")},
			"elasticstack_elasticsearch_ingest_processor_geoip":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorGeoip")},
			"elasticstack_elasticsearch_ingest_processor_grok":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorGrok")},
			"elasticstack_elasticsearch_ingest_processor_gsub":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorGsub")},
			"elasticstack_elasticsearch_ingest_processor_html_strip":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorHtmlStrip")},
			"elasticstack_elasticsearch_ingest_processor_join":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorJoin")},
			"elasticstack_elasticsearch_ingest_processor_json":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorJson")},
			"elasticstack_elasticsearch_ingest_processor_kv":                {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorKv")},
			"elasticstack_elasticsearch_ingest_processor_lowercase":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorLowercase")},
			"elasticstack_elasticsearch_ingest_processor_network_direction": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorNetworkDirection")},
			"elasticstack_elasticsearch_ingest_processor_pipeline":          {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorPipeline")},
			"elasticstack_elasticsearch_ingest_processor_registered_domain": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorRegisteredDomain")},
			"elasticstack_elasticsearch_ingest_processor_remove":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorRemove")},
			"elasticstack_elasticsearch_ingest_processor_rename":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorRename")},
			"elasticstack_elasticsearch_ingest_processor_script":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorScript")},
			"elasticstack_elasticsearch_ingest_processor_set":               {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorSet")},
			"elasticstack_elasticsearch_ingest_processor_set_security_user": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorSetSecurityUser")},
			"elasticstack_elasticsearch_ingest_processor_sort":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorSort")},
			"elasticstack_elasticsearch_ingest_processor_split":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorSplit")},
			"elasticstack_elasticsearch_ingest_processor_trim":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorTrim")},
			"elasticstack_elasticsearch_ingest_processor_uppercase":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorUppercase")},
			"elasticstack_elasticsearch_ingest_processor_uri_parts":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorUriParts")},
			"elasticstack_elasticsearch_ingest_processor_urldecode":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorUrldecode")},
			"elasticstack_elasticsearch_ingest_processor_user_agent":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchIngestProcessorUserAgent")},
			//"elasticstack_elasticsearch_security_user":                      {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchSecurityUser")},
			//"elasticstack_elasticsearch_snapshot_repository":                {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "ElasticsearchSnapshotRepository")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
