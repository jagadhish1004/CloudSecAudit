#!/usr/bin/env python3
"""
CloudSecAudit - Multi-Cloud Security Assessment Platform
Author: Your Name
Description: Automated security scanner for AWS, Azure, and GCP
"""

import os
import sys
import json
import subprocess
from datetime import datetime
import argparse

class CloudSecAudit:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.report_dir = f"../reports/scan_{self.timestamp}"
        os.makedirs(self.report_dir, exist_ok=True)
        
    def banner(self):
        print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        CloudSecAudit v1.0 - Security Scanner             ║
║        Multi-Cloud Penetration Testing Tool              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)
    
    def scan_aws_prowler(self, profile="default"):
        """Run Prowler AWS security scan"""
        print("\n[*] Starting AWS Security Scan with Prowler...")
        print(f"[*] Using AWS Profile: {profile}")
        
        try:
            cmd = [
                "prowler",
                "aws",
                "--profile", profile,
                "--output-formats", "html,json,csv",
                "--output-directory", self.report_dir
            ]
            
            subprocess.run(cmd, check=True)
            print(f"[+] AWS Scan Complete! Reports saved to {self.report_dir}")
            
        except subprocess.CalledProcessError as e:
            print(f"[-] Error running Prowler: {e}")
            
    def scan_aws_scoutsuite(self, profile="default"):
        """Run ScoutSuite AWS scan"""
        print("\n[*] Starting AWS Security Scan with ScoutSuite...")
        
        try:
            cmd = [
                "python3",
                "../tools/ScoutSuite/scout.py",
                "aws",
                "--profile", profile,
                "--report-dir", self.report_dir,
                "--no-browser"
            ]
            
            subprocess.run(cmd, check=True)
            print(f"[+] ScoutSuite Scan Complete!")
            
        except subprocess.CalledProcessError as e:
            print(f"[-] Error running ScoutSuite: {e}")
    
    def generate_summary(self):
        """Generate executive summary"""
        print("\n[*] Generating Executive Summary...")
        
        summary = {
            "scan_date": datetime.now().isoformat(),
            "scanner_version": "1.0",
            "clouds_scanned": ["AWS"],
            "tools_used": ["Prowler", "ScoutSuite"],
            "report_location": self.report_dir
        }
        
        summary_file = os.path.join(self.report_dir, "summary.json")
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=4)
            
        print(f"[+] Summary saved to {summary_file}")

def main():
    parser = argparse.ArgumentParser(description="CloudSecAudit - Multi-Cloud Security Scanner")
    parser.add_argument("--cloud", choices=["aws", "azure", "gcp", "all"], default="aws", 
                       help="Cloud provider to scan")
    parser.add_argument("--profile", default="default", 
                       help="AWS profile to use")
    parser.add_argument("--tool", choices=["prowler", "scoutsuite", "both"], default="both",
                       help="Security tool to use")
    
    args = parser.parse_args()
    
    scanner = CloudSecAudit()
    scanner.banner()
    
    if args.cloud == "aws" or args.cloud == "all":
        if args.tool in ["prowler", "both"]:
            scanner.scan_aws_prowler(args.profile)
        if args.tool in ["scoutsuite", "both"]:
            scanner.scan_aws_scoutsuite(args.profile)
    
    scanner.generate_summary()
    print("\n[+] All scans completed successfully!")
    print(f"[+] Check reports at: {scanner.report_dir}\n")

if __name__ == "__main__":
    main()
