# AWS Jump

Tool to access EC2 servers from multiple AWS accounts

## Install

`pip install awsjump`

## Requirements

A credentials file  `~/.aws/credentials` in the format explain here: http://boto.readthedocs.org/en/latest/boto_config_tut.html

Example configuration (notice the optional `default = True` line):
```
[dev]
aws_access_key_id = AKIA**************
aws_secret_access_key = ****************************************
default = True
[staging]
aws_access_key_id = AKIA**************
aws_secret_access_key = ****************************************
[prod]
aws_access_key_id = AKIA**************
aws_secret_access_key = ****************************************
```

If you want to always default to one particular account, set the `default = True` within the account section


## Example Usage

```
## If no default flag has is set this command will list all the accounts for you to choose
## If the default is set, it will search for servers in that account
bash$ jump

## If you have the default flag set, but you want to list and choose another account, use this
bash$ jump -l

## If you know which account you want, you can specify it like this
bash$ jump -a prod

```

## Help

```
bash$ jump --help

Usage: jump [options]

Options:
  -h, --help            show this help message and exit
  -d, --debug           Try to login with the ubuntu user
  -a AWS, --aws=AWS     Set the AWS account from within the ~/.aws/credentials
                        file
  -l, --list            List all AWS account from within the
                        ~/.aws/credentials file
  -r REGION, --region=REGION
                        Set the AWS region if different from `eu-west-1`
```
