#!/usr/bin/env python3
"""
Setup a safe AWS lab environment for testing
Creates intentionally misconfigured resources for learning
"""

import boto3
import json

def create_test_resources():
    print("[*] Setting up AWS Test Lab...")
    print("[!] WARNING: This creates intentionally vulnerable resources")
    print("[!] Only use in isolated test accounts!\n")
    
    # Example: Create an S3 bucket with logging disabled (misconfiguration)
    s3 = boto3.client('s3')
    
    bucket_name = f'cloudsecaudit-test-bucket-{hash(datetime.now())}'
    
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"[+] Created test bucket: {bucket_name}")
        print("[!] This bucket has no logging enabled (security issue)")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    response = input("Are you sure you want to create test resources? (yes/no): ")
    if response.lower() == "yes":
        create_test_resources()
    else:
        print("Setup cancelled.")
