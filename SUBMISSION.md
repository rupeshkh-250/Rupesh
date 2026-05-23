# Submission — DevOps Engineer Assignment

**Candidate name:** Moses A  
**Email:** mosessmos08@gmail.com  
**Date submitted:** 2026-05-23  
**Hours spent (approximate):** 8–10 hours  

## Deliverables checklist

- [x] Part A: Terraform code under /terraform applies cleanly on LocalStack
- [x] Part A: `terraform validate` and `terraform fmt -check` both pass
- [x] Part B: Janitor script runs in --dry-run mode and produces report.json
- [x] Part B: GitHub Actions workflow runs green on a fresh PR
- [x] Part B: --delete mode respects Protected=true tag
- [x] Part C: DESIGN.md is present and within 2 pages
- [x] Walkthrough video link below is accessible (unlisted is fine)

## Walkthrough video

Link ( Google Drive):  
https://drive.google.com/file/d/1AOSXvPZOLajDYEX0jJANRs2i979cZEot/view?usp=drivesdk

Length: ~3–4 minutes  

## Sample report

Path to a sample report.json produced by your script:  
 samples/report.example.json  

## Known limitations

- Cost estimation uses static pricing (not real-time AWS pricing)
- Only limited AWS resources are scanned (EBS, EC2, S3)
- LocalStack does not fully simulate all AWS edge cases
- No multi-region or multi-account support
- No alerting/notification system implemented

## AI usage disclosure

AI tools such as ChatGPT were used for:
- Initial guidance on Terraform + LocalStack setup
- Debugging GitHub Actions issues
- Structuring the janitor script

One issue encountered:
- AI suggested incorrect endpoint configuration for LocalStack, which caused connection errors. This was fixed by manually verifying endpoint URLs.

Manual work:
- Core janitor logic (resource filtering, cost calculation)
- Debugging CI/CD workflow errors
- Understanding and fixing LocalStack connectivity issues
