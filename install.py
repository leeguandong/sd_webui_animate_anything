"""Install requirements for WD14-tagger."""
import os
import sys

from launch import run  # pylint: disable=import-error

NAME = "AnimateAnything"
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        "requirements.txt")
print(f"loading {NAME} reqs from {req_file}")
run(f'"{sys.executable}" -m pip install -q -r "{req_file}"',
    f"Checking {NAME} requirements.",
    f"Couldn't install {NAME} requirements.")

# !wget https://cloudbook-public-production.oss-cn-shanghai.aliyuncs.com/animation/animate_anything_512_v1.02.tar
base_path = os.path.dirname(os.path.realpath(__file__))
run(f"cd {base_path}")
run("wget https://cloudbook-public-production.oss-cn-shanghai.aliyuncs.com/animation/animate_anything_512_v1.02.tar")
run("tar -xvf animate_anything_512_v1.02.tar")
