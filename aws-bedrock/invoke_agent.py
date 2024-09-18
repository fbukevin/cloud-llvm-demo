import boto3
import json
import uuid

# Create Bedrock client (make sure the region is where the agent exist)
bedrock_client = boto3.client('bedrock-agent-runtime', region_name='ap-northeast-1')

# Set agent ID
agent_id = 'XXXXXXXXXX'

# Set agent alias ID
agent_alias_id = 'XXXXXXXXXX'

# Create a unique session ID for the conversation
session_id = uuid.uuid4().hex


# Invoke AWS Bedrock Agent
response = bedrock_client.invoke_agent(
    agentId=agent_id,
    agentAliasId=agent_alias_id,
    sessionId=session_id,
    inputText='Write a short story about a futuristic city where AI controls everything.',
)

print(response)

completion = ""
for event in response.get("completion"):
	chunk = event["chunk"]
	completion = completion + chunk["bytes"].decode()

print(completion)
