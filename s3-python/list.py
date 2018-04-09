# install boto3 using python pip install boto3 and edit the config file in ~.aws/
# Object store is StorageGrid Webscale

import boto3
import boto3.session

session = boto3.session.Session(profile_name='my_profile')
endpoint = 'https://s3.datafabric.com:8082'

'''
Do not use this in production - disabling SSL verification is discouraged!
When using a self-signed certificate, make sure to pass it into the constructor:

s3 = session.resource(service_name='s3', endpoint_url=endpoint, verify='server_cert.pem')
'''
cert = 'C:\\Users\\promise\\Documents\\Coding\\Webscale\\VirtualHostStyle\\chain_root.pem'
s3 = session.resource(service_name='s3', endpoint_url=endpoint, verify=cert)
client = s3.meta.client

'''
Bucket related operations
'''

# Create new bucket for S3 account
# s3.Bucket('my-bucket').create()

# List all buckets for S3 account
#for bucket in s3.buckets.all():
#    print(bucket.name)

# Delete bucket
# s3.Bucket('my-bucket').delete()

'''
Object related operations
'''

# Put a new object to a bucket
obj = s3.Object('promise', 'my-key')
obj.put(Body='This is my object\'s data',
        Metadata={'customerid': '1234', 'location': 'england', 'owner': 'presenter', 'doc-type': 'pptx', 'department': 'engineering'},
        ServerSideEncryption='AES256')

# Put object directly from a file

#old_obj = s3.Object('my-bucket', 'existing-file-key')
#old_obj.upload_file('C:\\Users\\promise\\Desktop\\permit.pdf', ExtraArgs={'Metadata': {'customer_id': '4321'}, 'ServerSideEncryption':'AES256'})

# Get an object directly to a file
#obj.download_file('target-file')

# Copy an existing object
#copied_obj = s3.Object('my-bucket', 'my-copied-key')
#copied_obj.copy_from(CopySource='/my-bucket/my-key')

# Get object from bucket
#response = obj.get()
#data = response['Body'].read()
#metadata = response['Metadata']
#print("Data: %s // Metadata: %s" % (data, metadata))

# List all objects for a bucket
for obj in s3.Bucket('promise').objects.all():
    print(obj.key)

# Generate a pre-signed URL (only possible via client, not directly via Object object)
url = client.generate_presigned_url('get_object', {'Bucket': 'promise', 'Key': 'my-key'}, ExpiresIn=3600)
print("Pre-signed URL: %s" % (url))

# Delete the object from its bucket
# obj.delete()

