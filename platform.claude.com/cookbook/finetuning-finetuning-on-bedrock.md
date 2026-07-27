<!-- source: https://platform.claude.com/cookbook/finetuning-finetuning-on-bedrock -->

# Finetuning Claude 3 Haiku on Bedrock

In this notebook, we'll walk you through the process of finetuning Claude 3 Haiku on Amazon Bedrock

## What You'll Need

* An AWS account with access to Bedrock
* A dataset (or you can use the sample dataset provided here)
* [A service role capable of accessing the s3 bucket where you save your training data](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html)

## Install Dependencies

python

```
!pip install boto3
```

python

```
import boto3
```

## Prep a Dataset

Your dataset for bedrock finetuning needs to be a JSONL file (i.e. a file with a json object on each line).

Each line in the JSONL file should be a JSON object with the following structure:

```
{
  "system": "<optional_system_message>",
  "messages": [
    {"role": "user", "content": "user message"},
    {"role": "assistant", "content": "assistant response"},
    ...
  ]
}
```

* The `system` field is optional.
* There must be at least two messages.
* The first message must be from the "user".
* The last message must be from the "assistant".
* User and assistant messages must alternate.
* No extraneous keys are allowed.

## Sample Dataset - JSON Mode

We've included a sample dataset that teaches a model to respond to all questions with JSON. Here's what that dataset looks like:

python

```
import json

sample_dataset = []
dataset_path = "datasets/json_mode_dataset.jsonl"
with open(dataset_path) as f:
    for line in f:
        sample_dataset.append(json.loads(line))

print(json.dumps(sample_dataset[0], indent=2))
```

## Upload your dataset to S3

Your dataset for finetuning should be available on s3; for this demo we'll write the sample dataset to an s3 bucket you control

python

```
bucket_name = "YOUR_BUCKET_NAME"
s3_path = "json_mode_dataset.jsonl"

s3 = boto3.client("s3")
s3.upload_file(dataset_path, bucket_name, s3_path)
```

## Launch Bedrock Finetuning Job

Now that you have your dataset ready, you can launch a finetuning job using `boto3`. First we'll configure a few parameters for the job:

python

```
# Configuration
job_name = "anthropic-finetuning-cookbook-training"
custom_model_name = "anthropic_finetuning_cookbook"
role = "YOUR_AWS_SERVICE_ROLE_ARN"
output_path = f"s3://{bucket_name}/finetuning_example_results/"
base_model_id = (
    "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-haiku-4-5-20251001-v1:0:200k"
)

# Hyperparameters
epoch_count = 5
batch_size = 4
learning_rate_multiplier = 1.0
```

Then we can launch the job with `boto3`

python

```
bedrock = boto3.client(service_name="bedrock")
bedrock_runtime = boto3.client(service_name="bedrock-runtime")

bedrock.create_model_customization_job(
    customizationType="FINE_TUNING",
    jobName=job_name,
    customModelName=custom_model_name,
    roleArn=role,
    baseModelIdentifier=base_model_id,
    hyperParameters={
        "epochCount": f"{epoch_count}",
        "batchSize": f"{batch_size}",
        "learningRateMultiplier": f"{learning_rate_multiplier}",
    },
    trainingDataConfig={"s3Uri": f"s3://{bucket_name}/{s3_path}"},
    outputDataConfig={"s3Uri": output_path},
)
```

You can use this to check the status of your job while its training:

python

```
# Check for the job status
status = bedrock.get_model_customization_job(jobIdentifier=job_name)["status"]
```

## Use your finetuned model!

To use your finetuned model, [you'll need to host it using Provisioned Throughput in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html). Once your model is ready with Provisioned Throughput, you can invoked your model via the Bedrock API.

python

```
provisioned_throughput_arn = "YOUR_PROVISIONED_THROUGHPUT_ARN"
```

python

```
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "system": "JSON Mode: Enabled",
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": "What is a large language model?"}],
            }
        ],
    }
)
response = bedrock_runtime.invoke_model(modelId=provisioned_throughput_arn, body=body)
body = json.loads(response["body"].read().decode("utf-8"))
```

python

```
print(body["content"][0]["text"])
```
