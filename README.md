# AWS Jump

Tool to access EC2 servers from multiple AWS accounts

## Install

    pip install awsjump

If you'd like to install from GitHub:


    pip install git+https://github.com/ministryofjustice/awsjump.git

v0.0.6 shows `Name` from the Tags:


    +-------+---------+-----------------------------------------+-------------+-------------------------+--------------------+----------------+---------------+
    | Index | AWS     | Name                                    | Environment | Apps                    | Role               | Public         | Private       |
    +-------+---------+-----------------------------------------+-------------+-------------------------+--------------------+----------------+---------------+
    | 7     | default | example01                               |             |                         |                    | xx.xx.xx.xx    | xx.xx.xx.xx   |
    | 8     | default | example02                               |             |                         |                    | xx.xx.xx.xx    | xx.xx.xx.xx   |
    | 9     | default | example03                               |             |                         |                    | xx.xx.xx.xx    | xx.xx.xx.xx   |
    | 10    | default |                                         |             |                         |                    | xx.xx.xx.xx    | xx.xx.xx.xx   |

## Requirements

A credentials file  `~/.aws/credentials` in the format explained here: http://boto.readthedocs.org/en/latest/boto_config_tut.html

Example configuration (notice the optional `default = True` line):

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


If you want to always default to one particular account, set the `default = True` within the account section


## Example Usage

### If no default flag has is set this command will list all the accounts for you to choose
### If the default is set, it will search for servers in that account

    bash$ jump
    +-------+-------------+
    | Index | AWS Account |
    +-------+-------------+
    | 0     | dev         |
    | 1     | staging     |
    | 2     | prod        |
    +-------+-------------+
    Select an AWS Account:

### If you have the default flag set, but you want to list and choose another account, use this

    bash$ jump -l
    +-------+-------------+
    | Index | AWS Account |
    +-------+-------------+
    | 0     | dev         |
    | 1     | staging     |
    | 2     | prod        |
    +-------+-------------+
    Select an AWS Account:

### If you know which account you want, you can specify it like this

    bash$ jump -a dev
    +-------+-----+-------------+------------+--------+----------------+---------------+
    | Index | AWS  | Environment | Apps       | Role   | Public         | Private       |
    +-------+-----+-------------+------------+--------+----------------+---------------+
    | 1     | dev | dev         | Frontend   | docker | 54.x.x.x       | 10.x.x.x      |
    | 2     | dev | dev         | Backend    | docker | 54.x.x.x       | 10.x.x.x      |
    | 3     | dev | dev         | Database   | docker | 54.x.x.x       | 10.x.x.x      |
    +-------+-----+-------------+------------+--------+----------------+---------------+

Enter the server number to SSH to:


## Help

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
