#Author: Joaldir Rani

import requests
import json

headers = {
    'Accept': 'application/json',
    'Vicarius-Token': apikey,
}

response = requests.get(
    'https://vicarius-joaldir.vicarius.cloud/vicarius-external-data-api/aggregation/searchGroup?from=0&group=organizationEndpointPublisherProductVersionsEndpoint.endpointHash%3BpublisherProductHash%3B%3E%3BorganizationEndpointPublisherProductVersionsProduct.productName.raw%3BorganizationEndpointPublisherProductVersionsPublisher.publisherName.raw&includeOriginalDoc=false&newParser=false&objectName=OrganizationEndpointPublisherProductVersions&q=organizationEndpointPublisherProductVersionsEndpoint.endpointHash%3Din%3D(060802e18725477c04ef0be83c59c506)&size=1&subAggregationLevel=0&sumLastSubAggregationBuckets=0',
    headers=headers,
)

def parseResponse(response):
    jreponse = json.loads(response)
    print(json.dumps(jreponse,indent=2))

parseResponse(response.text)



