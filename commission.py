import os
import sys
import json
import shutil
import hashlib


if len(sys.argv) != 2:
    print("Usage: python %s mqtt.conf" % sys.argv[0])
    sys.exit(-1)


config_root = "/opt/rocket/config_rw/"
current_root = os.path.join(config_root, "config/v1/current")


def make_config_fs():
    # Create the subset path
    if not os.path.exists(current_root):
        if os.path.exists(config_root + "/config/v1/0/"):
            shutil.rmtree(os.path.dirname(config_root + "/config/v1/0/"))
        os.makedirs(os.path.dirname(config_root + "/config/v1/0/"))
        os.symlink(config_root + "/config/v1/0", current_root)


with open(sys.argv[1], "r") as f:
    config = json.load(f)
    commqtt = None
    for subset in config["subsets"]:
        if subset["name"] == "commqtt":
            commqtt = subset["fields"]
    if commqtt is None:
        print("commqtt subset not found in %s" % sys.argv[1])
        sys.exit(-1)
    make_config_fs()
    commqtt = json.dumps(commqtt, indent=4)
    with open(os.path.join(current_root, "commqtt.json"), "w") as out:
        out.write(commqtt)
    # Write the subset hash file
    hashed_string = hashlib.sha256(commqtt.encode('utf-8')).hexdigest()
    # Write the subset hash file
    with open(current_root + "/commqtt.sha256", 'w') as f:
        f.write(hashed_string)    
    # Create log records
    print("Generated OAM MQTT subset data: " + commqtt)
    print("Generated OAM MQTT subset hash: " + hashed_string)
    print("MQTT config migration success")
