"""
Must aws cli must be configured.
Bucket must be created, refer back to boto3_and_sqs_first_attempt file
"""

import boto3

BUCKET = "mfg54fft"
KEY = "royal_pink_typewriter.jpg"


def detect_labels(bucket, key, max_labels=10, min_confidence=50, region="us-west-2"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    return response['Labels']


for label in detect_labels(BUCKET, KEY):
    print("{Name} - {Confidence}%".format(**label))
