# -*- coding: utf-8 -*-
from __future__ import print_function
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
 
 
    if (event['clickType']=='SINGLE'):
        pipe = boto3.client('codepipeline')
        body_text = pipe.get_pipeline_state(name='TEST')
 
        stageStates = body_text["stageStates"]
 
        for dic_iter in stageStates:
 
            actualAction = dic_iter["actionStates"][0]["actionName"]
            actualDic = dic_iter["actionStates"][0]
 
            if( actualAction == "ApprovalAction" ):
                tokenVal = actualDic["latestExecution"]["token"]
 
        pipe.put_approval_result(pipelineName='TEST',stageName='Approval-TEST',actionName='ApprovalAction',result={'summary': 'Deploy approvato','status': 'Approved'},token=tokenVal)
 
 
    if (event['clickType']=='DOUBLE'):
        ec2 = boto3.client('ec2')
        ec2.create_image(InstanceId='i-07bbdf03e7a763586',Name='Bastion',NoReboot=True)
 

    if (event['clickType']=='LONG'):
        cform = boto3.client('cloudformation')
        cform.delete_stack(StackName='TEST')
