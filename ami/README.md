## Purpose:

Return the latest AMI boto3 can find with some filters. (https://github.com/crielly/sceptre-custom-resolvers)

### Usage:
`vars.yml` - included at the CLI via `--var-file vars.yml` flag:
```
hvm1604filters:
  aminame: "*ssd/ubuntu-xenial-16.04-amd64-server*"
  amiowner: "099720109477"
  amiarch: "x86_64"
  amistate: "available"
  amirootdevicetype: "ebs"
  amivirttype: "hvm"
```

`config/envname/stack.yml`:
```
template_path: templates/workers.yaml.j2
parameters:
  LatestXenialAmi: !ami_resolver "{{ var.hvm1604filters }}"
```

This should make the latest Ubuntu 16 AMI available as a parameter in your stack.

`templates/stack.yaml.j2`:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: "Some Description"
Parameters:
  LatestXenialAmi:
    Type: String
```