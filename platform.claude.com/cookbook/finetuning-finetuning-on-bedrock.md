<!-- source: https://platform.claude.com/cookbook/finetuning-finetuning-on-bedrock -->

#  Finetuning Claude 3 Haiku on Bedrock

In this notebook, we'll walk you through the process of finetuning Claude 3 Haiku on Amazon Bedrock

##  What You'll Need

* An AWS account with access to Bedrock
* A dataset (or you can use the sample dataset provided here)
* [A service role capable of accessing the s3 bucket where you save your training data(opens in new tab)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html)

##  Install Dependencies



!pip install boto3



import boto3

##  Prep a Dataset

Your dataset for bedrock finetuning needs to be a JSONL file (i.e. a file with a json object on each line).

Each line in the JSONL file should be a JSON object with the following structure:



{

"system": "<optional\_system\_message>",

"messages": [

{"role": "user", "content": "user message"},

{"role": "assistant", "content": "assistant response"},

...

]

}

* The `system` field is optional.
* There must be at least two messages.
* The first message must be from the "user".
* The last message must be from the "assistant".
* User and assistant messages must alternate.
* No extraneous keys are allowed.

##  Sample Dataset - JSON Mode

We've included a sample dataset that teaches a model to respond to all questions with JSON. Here's what that dataset looks like:



import json

sample\_dataset = []

dataset\_path = "datasets/json\_mode\_dataset.jsonl"

with open(dataset\_path) as f:

for line in f:

sample\_dataset.append(json.loads(line))

print(json.dumps(sample\_dataset[0], indent=2))

##  Upload your dataset to S3

Your dataset for finetuning should be available on s3; for this demo we'll write the sample dataset to an s3 bucket you control



bucket\_name = "YOUR\_BUCKET\_NAME"

s3\_path = "json\_mode\_dataset.jsonl"

s3 = boto3.client("s3")

s3.upload\_file(dataset\_path, bucket\_name, s3\_path)

##  Launch Bedrock Finetuning Job

Now that you have your dataset ready, you can launch a finetuning job using `boto3`. First we'll configure a few parameters for the job:



# Configuration

job\_name = "anthropic-finetuning-cookbook-training"

custom\_model\_name = "anthropic\_finetuning\_cookbook"

role = "YOUR\_AWS\_SERVICE\_ROLE\_ARN"

output\_path = f"s3://{bucket\_name}/finetuning\_example\_results/"

base\_model\_id = (

"arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-haiku-4-5-20251001-v1:0:200k"

)

# Hyperparameters

epoch\_count = 5

batch\_size = 4

learning\_rate\_multiplier = 1.0

Then we can launch the job with `boto3`



bedrock = boto3.client(service\_name="bedrock")

bedrock\_runtime = boto3.client(service\_name="bedrock-runtime")

bedrock.create\_model\_customization\_job(

customizationType="FINE\_TUNING",

jobName=job\_name,

customModelName=custom\_model\_name,

roleArn=role,

baseModelIdentifier=base\_model\_id,

hyperParameters={

"epochCount": f"{epoch\_count}",

"batchSize": f"{batch\_size}",

"learningRateMultiplier": f"{learning\_rate\_multiplier}",

},

trainingDataConfig={"s3Uri": f"s3://{bucket\_name}/{s3\_path}"},

outputDataConfig={"s3Uri": output\_path},

)

You can use this to check the status of your job while its training:



# Check for the job status

status = bedrock.get\_model\_customization\_job(jobIdentifier=job\_name)["status"]

##  Use your finetuned model!

To use your finetuned model, [you'll need to host it using Provisioned Throughput in Amazon Bedrock(opens in new tab)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html). Once your model is ready with Provisioned Throughput, you can invoked your model via the Bedrock API.



provisioned\_throughput\_arn = "YOUR\_PROVISIONED\_THROUGHPUT\_ARN"



bedrock = boto3.client("bedrock-runtime", region\_name="us-east-1")

body = json.dumps(

{

"anthropic\_version": "bedrock-2023-05-31",

"max\_tokens": 1000,

"system": "JSON Mode: Enabled",

"messages": [

{

"role": "user",

"content": [{"type": "text", "text": "What is a large language model?"}],

}

],

}

)

response = bedrock\_runtime.invoke\_model(modelId=provisioned\_throughput\_arn, body=body)

body = json.loads(response["body"].read().decode("utf-8"))



print(body["content"][0]["text"])
