#!/usr/bin/env python
from __future__ import print_function

import os
import base64
import requests
import argparse

SERVER_ADDRESS = 'http://192.168.0.32'
ACCOUNT_KEY = "83a190db1eb3735f4b06a6d4defe151b"

def attach_preview_attr(selected_asset, img_path):
    with open(img_path, "rb") as file_buff:
        base64_string = base64.b64encode(file_buff.read())
        url = "{}/api/p4/files/preview".format(SERVER_ADDRESS)

        params = {
            "account_key": ACCOUNT_KEY,
            "depot_path": selected_asset,
        }

        payload = {
            "content": base64_string,
            "encoding": 'base64'
        }
        
        response = requests.put(
            url, 
            params=params, 
            data=payload
        )
        
        response_json = response.json()
        if response_json.get('api_status') == 200:
            print(selected_asset,'preview updated.')
        else:
            print(selected_asset,'preview update failed.')
            print(response_json)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("selected_asset") 
    parser.add_argument("image_file")

    parsed_args = parser.parse_args()
    attach_preview_attr(parsed_args.selected_asset, parsed_args.image_file)
