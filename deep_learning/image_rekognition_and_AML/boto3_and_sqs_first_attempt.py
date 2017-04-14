"""
These scripts are separated into blocks that are all commented out via the triple double quotes.
Just remove the triple double quotes at the beginning and end of the code block you want to use.

IMPORTANT NOTE: Before you begin, you need to install aws acli and configure it,
otherwise you will note be able to create s3 buckets.

This file is created to follow the example on how to use boto3 for image recognition.
Insert your own bucket name.

The second part is about using Amazon Simple Queue Service (SQS)
I don't really have any practical use or SQS quite yet.

address1: boto3.readthedocs.io/en/latest/guide/quickstart.html
address2: boto3.readthedocs.io/en/latest/guide/sqs.html
"""
import boto3


"""
# This block prints out bucket list.

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list of current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)
# If you get an empty bucket list, that means you have no buckets.
"""


"""
# This block creates an Amazon S3 bucket

# Using the create_bucket method
s3 = boto3.client('s3')
s3.create_bucket(Bucket='your_bucket_name')
"""


"""
# This block shows how to delete a bucket

# Create an S3 client
s3 = boto3.client('s3)

# Call S3 to delete the policy for the given bucket
s3.delete_bucket_policy(Bucket='your_bucket_name')
"""


"""
# Print Bucket Policy

# Create an S3 client
s3 = boto3.client('s3')

# Call to S3 to retrieve the policy for the given bucket
result = s3.get_bucket_acl(Bucket='your_bucket_name')
print(result)
"""


"""
# Configure Bucket
# Create an S3 client
s3 = boto3.client('s3')

# Create the CORS configuration
# This allows you to not only get the data, but also push the data
cors_configuration = {
    'CORSRules': [{
        'AllowedHeaders': ['Authorization'],
        'AllowedMethods': ['GET', 'PUT'],
        'AllowedOrigins': ['*'],
        'ExposeHeaders': ['GET', 'PUT'],
        'MaxAgeSeconds': 3000
    }]
}

# Set the new CORS configuration on the selected bucket
s3.put_bucket_cors(Bucket='your_bucket_name', CORSConfiguration=cors_configuration)
"""


"""
# This code block is about uploading a file to an Amazon S3 Bucket

# Create the S3 client
s3 = boto3.client('s3')

filename = 'file.txt'
bucket_name = 'your_bucket_name'

# Uploads the given file using a managed uploader, which will split up large files automatically and upload parts in
# parallel
s3.upload_file(filename, bucket_name, filename)
"""


"""
# This block will upload images to the S3 Bucket
# Create an S3 client
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('image_name', 'rb')
s3.Bucket('your_bucket_name').put_object(Key='image_name', Body=data)
"""


"""
# You only need to run this block once because it creates the queue, running it more the once with the
# the same queue name will result in an exception.

# This block of code does the following:
# Get SQS service resource before creating a queue
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
"""


"""
# Next, use an existing queue (in this case, the Queue "test" that we just created above)
# The two print statements under the identifiers and attributes comment should have the same output as above.

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.queue instance
queue = sqs.get_queue_by_name(QueueName='test')

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Alternatively, you can print a list of all existing queues like this.
for queue in sqs.queues.all():
    print(queue.url)

# NOTE: To get the name from a queue, you must use its ARN (Amazon Resource Name), which is available in
# the queue's attributes attribute. Using queue.attributes['QueueArn'].split(':')[-1] will return its
# name.
"""


"""
# Sending Messages
# Sending a message to the que will at it to the end of the queue.


# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

# Create a new message
response = queue.send_message(MessageBody='world')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5ofMessageBody'))

# You can also create messages with custom attributes:
queue.send_message(MessageBody='botot3', MessageAttributes={
    'Author': {
        'StringValue': 'Emanuel',
        'DataType': 'String'
    }
})

# Messages can also be sent in batches. For example, sending the two messages above in a single request
# would look like this
response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Emanuel',
                'DataType': 'String'
            }
        }
    }
])

# Print out any failures
print(response.get('Failed'))
"""

"""
# Processing Messages
# Messages are processed in batches

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))

    # Let the queue know that the message is processed
    message.delete()
    """