from sceptre.resolvers import Resolver
import boto3
from dateutil import parser
import ast

class CustomResolver(Resolver):

    def __init__(self, *args, **kwargs):
        super(CustomResolver, self).__init__(*args, **kwargs)
        self.args = ast.literal_eval(self.argument) # process input
    def resolve(self):
        """
        resolve is the method called by Sceptre. It should carry out the work
        intended by this resolver. It should return a string to become the
        final value.

        The following parameters are available to Resolvers:

        :param argument: The argument of the resolver. (kwargs passed in as string)
        :type argument: str
        :param stack: The associated stack of the resolver.
        :type stack: sceptre.stack.Stack
        """
        client = boto3.client('ec2', region_name="eu-west-1")

        filters = [{
            'Name': 'name',
            'Values': [self.args['aminame']]
        }, {
            'Name': 'architecture',
            'Values': [self.args['amiarch']]
        }, {
            'Name': 'owner-id',
            'Values': [self.args['amiowner']]
        }, {
            'Name': 'state',
            'Values': [self.args['amistate']]
        }, {
            'Name': 'root-device-type',
            'Values': [self.args['amirootdevicetype']]
        }, {
            'Name': 'virtualization-type',
            'Values': [self.args['amivirttype']]
        }]

        response = client.describe_images(
            Owners=[self.args['amiowner']],
            Filters=filters
        )
        latest = None

        for image in response['Images']:
            if not latest:
                latest = image
                continue

            if parser.parse(image['CreationDate']) > parser.parse(latest['CreationDate']):
                latest = image

        return latest['ImageId']

