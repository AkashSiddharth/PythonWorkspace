import boto3
import jmespath
import logging

class AIS_Tagging:
  def __init__(self, profile):
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    logging.info(f"Creating a new AWS session for {profile}")
    self.session = boto3.session.Session(profile_name = profile)

    # Create ConfigService session
    logging.info("Creating a client for AWS ConfigService.")
    self.conService = self.session.client('config')

  def get_resource_info(self, resource_id: str, resource_type: str) -> dict:
    ###
    # Get the Resouce ARN and existing tags
    ###
    info_dict = dict()
    response = self.conService.get_resource_config_history(
                resourceType = resource_type,
                resourceId = resource_id
            )
    info_filter_query = "configurationItems[0].[arn, tags]"
    info_dict['arn'], info_dict['tags'] = jmespath.search(info_filter_query, response)

    for key, value in info_dict.items():
      logging.info(f"{key.upper()}: ")
      if type(value) is dict:
        if len(value) != 0:
          for k,v in value.items():
            logging.info(f"{k}: {v}")
      else:
        logging.info(f"{value}")
    
    return info_dict

  def get_tagging_violations(self) -> None:
    ###
    # List resources with tag vulnerabilities
    ###
    AIS_TAGGING_RULE = "ais-require-tagging-compliance-rule"
    logging.info(f"Checking the violations for the rule: {AIS_TAGGING_RULE}")
    resourceID_filter_query = "EvaluationResults[*].EvaluationResultIdentifier.EvaluationResultQualifier.[ResourceType, ResourceId]"

    # Generate the iterator
    pages = self.conService.get_paginator('get_compliance_details_by_config_rule')

    # Generate the list of resources
    for page in pages.paginate( ConfigRuleName = AIS_TAGGING_RULE,
                                ComplianceTypes=[ 'NON_COMPLIANT' ],
                                PaginationConfig={  'MaxItems': 300,
                                                    'PageSize': 1
                                                  }
                              ):
      
      # extract resourcesIds from the output
      resourceType, resourceID = jmespath.search(resourceID_filter_query, page)[0]
      
      logging.info(f"Resource Type: {resourceType}, Resource ID: {resourceID}")

      resource_info = self.get_resource_info(resourceID, resourceType)

      # Apply the AIS mandated tags
      



   

if __name__ == "__main__":
  ais_tagging = AIS_Tagging('FAS_ALCHEMY_DEV')

  ais_tagging.get_tagging_violations()

