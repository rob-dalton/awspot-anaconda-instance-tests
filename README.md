# base-awspot-anaconda-resource
Base files for awspot anaconda resources. Contains configuration and setup tests. New awspot based anaconda projects should be forked from this repo.

## Setup
This repo assumes that you're using a custom AMI derived from the [official Anaconda3 AMI](https://aws.amazon.com/marketplace/pp/B07CNFWMPC?qid=1534302028839&sr=0-1&ref_=srh_res_product_title). It should only allow `SSH` access, and you should have at least one key pair with access to the instance.

Before running tests, ensure that `awscli` has been configured on the resource. Tests assume the machine is configured with AWS credentials for a user with S3 read, write and list permissions.

## Usage

### Jupyter Notebook
You can run a Jupyter notebook on the instance and access it locally with these steps:
1. `ssh` into the instance.
2. Run `jupyter notebook` in the desired project directory.
  - OPTIONAL: Use `tmux` to run a persistent server. Run `tmux` first, then `ctl+b d` to detach after you start the server.
3. Open a new terminal window on your local computer.
4. Run `ssh -i <path to aws access key> -N -L 8000:localhost:8888 <user>@<public DNS>`.
5. Open a browser. Navigate to `localhost:8000`.
