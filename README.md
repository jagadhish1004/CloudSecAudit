# 🔐 CloudSecAudit - Multi-Cloud Security Assessment Platform

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![AWS](https://img.shields.io/badge/AWS-Supported-orange)
![Azure](https://img.shields.io/badge/Azure-Supported-blue)

## 📖 Overview

CloudSecAudit is an automated multi-cloud security assessment platform designed for penetration testers and security professionals. It identifies security misconfigurations, compliance violations, and potential attack vectors across AWS, Azure, and GCP environments.

### Key Features

- ✅ **Multi-Cloud Support**: AWS, Azure, GCP
- ✅ **Automated Scanning**: Prowler, ScoutSuite integration
- ✅ **IAM Analysis**: Identifies privilege escalation paths
- ✅ **Compliance Checks**: CIS, NIST, PCI-DSS benchmarks
- ✅ **Professional Reports**: HTML, JSON, CSV outputs
- ✅ **S3 Bucket Analysis**: Detects public exposure risks
- ✅ **Remediation Guidance**: Actionable security recommendations

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- AWS CLI configured
- Valid AWS credentials (read-only recommended)

### Installation

```bash
git clone https://github.com/yourusername/CloudSecAudit.git
cd CloudSecAudit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Basic Usage

```bash
# Scan AWS with default profile
python3 scripts/cloud_scanner.py --cloud aws

# Scan with specific AWS profile
python3 scripts/cloud_scanner.py --cloud aws --profile myprofile

# Use only Prowler
python3 scripts/cloud_scanner.py --cloud aws --tool prowler
```

## 📊 Sample Findings

### High-Severity Issues Detected:
- IAM users with administrative privileges
- S3 buckets with public read/write access
- Security groups with 0.0.0.0/0 access
- Unencrypted EBS volumes
- CloudTrail logging disabled

## 🛡️ Tested Against

- AWS Free Tier environments
- Intentionally misconfigured test labs
- CIS AWS Foundations Benchmark
- NIST Cybersecurity Framework

## 📝 Project Structure

CloudSecAudit/
├── scripts/          # Python scanning scripts
├── tools/            # Third-party security tools
├── reports/          # Generated security reports
├── config/           # Configuration files
├── docs/             # Documentation
└── README.md
## 🎯 Use Cases

1. **Cloud Penetration Testing**: Identify security weaknesses
2. **Compliance Auditing**: CIS, NIST, PCI-DSS checks
3. **Security Posture Assessment**: Continuous monitoring
4. **Training & Education**: Learn cloud security concepts

## ⚠️ Legal Disclaimer

This tool is for authorized security testing only. Obtain proper authorization before scanning any cloud environment. Unauthorized access to computer systems is illegal.

## 👨‍💻 Author

**JAGADISH.A**  
Cloud Penetration Tester | Security Researcher  
(https:///in/LinkedIn : https://www.linkedin.com/in/jagadish-a-46363a269 GitHub :https://github.com/jagadhish1004 TryHackMe :https://tryhackme.com/p/ajagadish0987 Resume PDF link :https://tryhackme.com/p/ajagadish0987 Email (optional) :jaga307aj@gmail.com Phone (optional) :7305287851) | [Portfolio](https://https://jagadish-prof.netlify.app)

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Prowler](https://github.com/prowler-cloud/prowler) - AWS Security Assessment
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite) - Multi-cloud Auditing
- AWS Security Best Practices Documentation

## 📫 Contact

For questions or collaboration:
- Email: your.email@example.com
- GitHub Issues: [Report Issues](https://github.com/yourusername/CloudSecAudit/issues)🛡️ Security & Best Practices

    Least Privilege: Use read-only IAM roles (CloudFormation template in config/).

    No Data Exfil: Local-only processing; no cloud uploads.

    Compliance: Maps to CIS Benchmarks 1.5.0, NIST 800-53.

    Rate Limiting: Built-in throttles to avoid API bans.

🐛 Troubleshooting

    Prowler Python Error: Use Python 3.10-3.13; recreate venv.

Permission Denied: chmod +x tools/*; aws sts get-caller-identity.

Dependencies Fail: pip install --upgrade pip setuptools wheel.

- 🏗️ ARCHITECTURE
-
- ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Cloud APIs    │───▶│   Scanner Core   │───▶│   Report Engine │
│ AWS/Azure/GCP   │    │ Prowler+ScoutSuite│    │ HTML/PDF/JSON   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                 │
                          ┌──────────────┐
                          │  API Server  │──▶ CI/CD / Slack / Email
                          └──────────────┘e Overview
  🔧 ADVANCED USAGE
  DOCKER (Production)
  # docker-compose up -d
   services: 
         cloudscan:
           image: jagadish/cloudsecaudit:latest
         volumes:
           - ./reports:/app/reports
         environment:
              - AWS_PROFILE=scanner

API Usage
     
   curl -X POST http://localhost:8000/scan \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"clouds": ["aws"], "profile": "scanner"}'
   
     🔍 Detected Vulnerabilities (Examples) 
         1. S3: Public bucket 'prod-backup-2025' (HIGH)
2. IAM: Admin role accepts '*' (CRITICAL)
3. RDS: Unencrypted instance (MEDIUM)
4. VPC: Internet-facing subnet (HIGH)
5. KMS: Shared customer keys (LOW)

    
- 
