<img src="profile.jpg" class="profile-photo" alt="Yu Hsuan Chen (Tina)" />

# Yu Hsuan Chen (Tina)
**Solution Architect / SRE / DevOps**

📧 tinachen1996121@gmail.com · 📱 0917-577-377 · 📍 New Taipei City, Taiwan
🔗 [cake.me/tinachen1996121](https://www.cake.me/resumes/tinachen1996121) · 💼 [LinkedIn](https://www.linkedin.com/in/yu-hsuan-chen-1a08b1203/)

---

## Profile

7-year cross-cloud SRE / DevOps engineer with hands-on production experience
across **AWS, GCP, and on-premise** environments. Background spans crypto
exchange (high regulatory bar), martech SaaS, hardware / IoT, and education
tech — covering **SOC 2 / ISO 27001 compliance**, **org-scale cloud migration**,
**security incident response**, **cost optimization**, and **AI-powered SRE
tooling**. Currently driving SOC 2 readiness, pre-production environment
design, and an LLM-based SRE agent at ViewSonic.

---

## Highlights

- **Multi-cloud** — AWS (~5 yrs) + GCP (2 yrs); 11+ AWS accounts, multi-region production
- **Compliance** — SOC 2 audit readiness · ISO 27001 monitoring
- **Migration scale** — GCP Org migration (Shared VPC, PSC, DMS) · GitHub org migration (69 repos)
- **Security** — Drove breach response & full EKS rebuild · Secret Manager + ESO + key rotation · WAF / GuardDuty / SCC
- **Cost** — AWS Savings Plans + RI (RDS / Redis / OpenSearch + Compute SP) · GCP CUD · 100% Spot GKE · KubeCost
- **AI / automation** — Built OpenClaw (LLM-based SRE agent) · 30+ Claude Code skills + hook-driven automation adopted by infra team

---

## Experience

### DevOps Engineer · ViewSonic Corporation
*New Taipei · 2025 – Present · DEV Department*

#### 🛡️ SOC 2 Audit Readiness
- Drove SOC 2 documentation preparation (PBC mapping) across RD / SRE / QA,
  coordinating evidence collection from 3 functions.
- Implemented strict IAM policies, MFA enforcement, and automated account
  review workflows.
- Enforced Dev / Test / Prod environment isolation and secure SDLC practices
  with mandatory code reviews.
- Managed cloud asset inventory and automated data encryption via AWS KMS /
  Azure Key Vault.
- Authored Business Continuity (BCP) and Disaster Recovery (DR) plans
  meeting RTO / RPO targets.
- Configured centralized audit logging, vulnerability scanning, and
  automated alerting systems.

#### 🚀 Pre-Production (RC) Environment
- Stood up release-candidate environment **inside the production AWS account**,
  sharing EKS cluster / VPC / ACM while isolating data and compute — cuts
  infra spend versus full prd-duplicate setup.
- Separated RDS / Redis / S3 with `-rc` suffix, including data migration,
  firewall rules, and dedicated DB credentials.
- Created dedicated CloudFront distributions for `*rc.classswift.com` with
  Lambda@Edge, reusing the same WAF and Istio NLB.
- Split EKS node pools and namespaces via ArgoCD `value.rc.yaml` with RC
  node selectors.
- Isolated Parameter Store keys under `/rc/` path for both infra and app config.
- Extended Grafana dashboards and Kibana indices to cover RC alongside prd.

#### 🦞 OpenClaw — AI SRE Agent
- Built LLM-based SRE assistant that runs AWS CLI / kubectl across
  dev / stg / prd accounts; designed **3-layer Terraform state architecture**
  with S3 backend and cross-account assume-role.
- Deployed on a single EC2 running k3s, connected via SSM through VPC
  Endpoints (no public IP, no inbound exposure).
- Slack integration via API Gateway + Lambda with DynamoDB-backed
  conversation memory.
- Designed modular **skill system (8 skills)** loaded on demand via K8s
  ConfigMap.
- Packed internal repos into searchable XML references so the LLM can look
  up infra configs during incidents.
- Wrote custom system prompts with incident triage SOP and guardrails to
  keep the bot action-oriented.

#### 🔀 GitHub Organization Migration & Governance
- Drove migration of **69 repositories** from VSX-ViewSonic to Viewsonic-EDU
  (Apr 2026), standardizing branch protection, ruleset, and
  `delete_branch_on_merge` baseline via gh API automation. Zero downtime,
  zero broken CI pipelines.
- Established org-wide governance baseline: ruleset templates, bypass
  approval rules, PR auto-delete-branch — applied uniformly across all
  migrated repos.

#### 🤖 Multi-Agent Automation Platform *(internal DevTool)*
- Built Claude Code-based automation framework: **30+ custom skills**
  covering AWS infrastructure, Kubernetes, GitHub, CI/CD, and security
  workflows; hook system for event-driven actions (pre-commit / post-edit
  / on-PR); 3 parallel execution modes (team-mode / parallel-research /
  parallel-dev).
- Packed internal AWS / Terraform / K8s reference docs into searchable XML
  knowledge bases for LLM lookup during incident response and IaC review.
- Hook-driven event automation: PR open / merge triggers, post-edit
  linting, pre-commit validation pipelines — eliminated manual hand-offs
  in daily ops.
- Adopted by infra team as daily-driver tooling.

#### 🌐 Cross-Account Networking & Alerting
- Designed VPC peering (vsx-dev ↔ sss-ai-dev) including TGW attachment
  cleanup, RAM share, and route table propagation — unblocked AI team's
  cross-account service access in 1 sprint.
- Built reusable Terraform module (`aws-alert` repo) for RDS / ElastiCache
  / EKS health → SNS → on-call rotation; consolidated 20+ ad-hoc CloudWatch
  alarms into one declarative source of truth.
- Operate AWS Client VPN (dev / prd endpoints) with SNAT routing for
  engineer access to internal resources (EKS, RDS, ElastiCache).

#### 💰 AWS Cost & IAM Identity Center Governance
- Integrated AWS Cost Explorer at **Org payer level** (admin account,
  us-east-1) for cross-account **NetAmortizedCost** reporting with RI /
  Savings Plan amortization across 11 accounts; replaced per-account
  UnblendedCost guesswork that understated true monthly cost by **20–35%**.
- Centralized IAM Identity Center governance (us-east-1): standardized
  shared permission sets (`vsx-fullstack-v1` / `vsx-ro-v1` /
  `vsx-admin-v1` / `vsx-vendor-v1`) across all subaccount families
  instead of per-app proliferation — prevents policy drift and simplifies
  audit.
- Automated user / group / permission-set provisioning via aws-cli +
  Identity Store + SSO-Admin APIs (modular bash workflow).

#### 🔒 Security Scan Automation *(SCA / SAST)*
- Integrated central reusable GitHub Actions workflow
  (`edu-security-lab-va`) with **DefectDojo + Dependency-Track** for SBOM
  generation and vulnerability scanning across all migrated repos.
- OIDC-based AWS role assumption (`DevSecOps-Github-OIDC-bot`) for secure
  cross-account scan access; standardized `BU/product/repo-name` taxonomy
  for portfolio classification.
- Authored integration playbook covering common gotchas (workflow
  permissions, OIDC token scope, DT project ACL setup) — reduced
  first-time integration failures across BU teams.

---

### SRE · BitoPro Technology
*Taipei · 2023 – 2025 · O&M Department · (Taiwan's largest crypto exchange)*

#### 🔥 Security Breach Response
- Rebuilt EKS cluster from scratch and migrated all applications post-incident.
- Rotated all secrets: Secret Manager entries, EC2 user passwords, K8s Secrets.
- Re-deployed K8s resources through Jenkins pipeline; reviewed every Network
  Policy / Security Group inbound & outbound rule.
- Isolated payment systems onto stand-alone EC2 instances.
- Hardened with AWS Config / Security Hub / GuardDuty; restricted SRE IAM
  permissions to least-privilege; reviewed all WAF rules.

#### ☁️ AWS Infrastructure as Code
- Owned production AWS CDK codebase (TypeScript).

#### 💰 Cost Optimization
- AWS Savings Plans + RIs across RDS / Redis / OpenSearch + Compute SP;
  daily budget alerts; KubeCost rollout with per-deployment CPU/mem
  requests / limits tuning.

#### 📈 Observability & Monitoring
- AWS service monitoring · PMM DB query insights · Grafana OnCall
  notifications · OpenTelemetry tracing · Thanos central monitoring ·
  ELK / OpenSearch logging architecture.

#### 🛡️ Security Hardening
- Architected Secret Manager + External Secrets Operator pipeline with
  automatic key rotation; routed VPC Flow Logs + WAF logs to S3 for Athena
  reporting.
- Deployed cert-manager for TLS lifecycle; tightened Network Policies,
  Security Policies, NACLs; ran Chaos Monkey drills; tuned WAF rules.

#### 🔧 CI/CD Pipelines
- Built Jenkins pipeline with dynamic pod templates (JNLP + Kaniko
  containers, S3 cache, EFS-mounted Go build cache, ECR-refresher helper
  for credential rotation).
- Mirrored architecture on GitLab Runner.

#### 📊 Reliability & Stability
- Pod HPA / VPA · Node ASG · JMeter stress testing · daily Velero backups
  (RDS / Redis / EBS / PVC) · operated multi-broker, partitioned, replicated
  Kafka clusters.

#### 🔄 Operational Maintenance
- Helm chart upgrades · SSM Agent updates · EKS version upgrade workflow ·
  routine release deploys.

---

### SRE · awoo Intelligence
*Taipei · 2021 – 2023 · Cloud Infra Department*

#### 🌏 GCP Organization Migration
- Designed and executed GCP organization migration end-to-end: Shared VPC,
  VPC peering, GKE / Cloud SQL / Redis IP range planning, Private Service
  Connect (PSC), Database Migration Service (DMS).
- Built migration playbook: Terraform IaC, ArgoCD CI/CD, MongoDB dump /
  restore, continuous Cloud SQL migration, GCE migration, public IP
  migration with **minimized downtime traffic switch**.

#### 🏗️ On-Premise Data Center Operations
- NAS backup solution · Fortinet site-to-site VPN · VLAN environment
  isolation (Dev / Staging / Production).

#### 💾 Disaster Recovery
- Planned Tokyo subnet + GKE Pod / Service IP ranges · backup / restore
  procedures · DR rehearsals.

#### 🔧 GitOps CI/CD on GKE
- Terraform Infra Pipeline — GitLab + GKE runner + Helm + Terraform.
- ArgoCD Application Pipeline — GitLab + GKE ArgoCD + Kustomize + Helm.

#### 💰 GCP Cost Optimization
- KubeCost-driven deployment cost tuning; **100% Spot GKE**; Redis & MongoDB
  self-hosted on GKE; Nginx Ingress Controller replacing internal LB.
- Committed Use Discounts (CUD) for VM / Cloud SQL / Redis; BQ + GCS data
  lifecycle policies; daily BQ query quota limits; Cloud Logging exclusion
  rules; scheduled GCE stop / restart; auto-cleanup of unattached disks /
  external IPs.

#### 📈 Monitoring
- Thanos central monitoring · Cloud Monitoring central alerting · service
  uptime checks.

#### 🛡️ Security
- Security Command Center · VM patch / NTP / OS update automation · VM
  vulnerability scanner · Cloud SQL SSL enforcement · company-wide MFA ·
  Cloud Armor WAF for L7 DDoS mitigation · firewall hardening (removed
  `0.0.0.0/0` source on SSH / RDP ports).

---

### Cloud Engineer · Askey Computer Corp
*New Taipei · 2019 – 2021 · Cloud Dev Department · (ASUS subsidiary, hardware / IoT)*

Built cloud APIs and IoT services for smart home, smart bus, FOTA, and
firmware management products.

- **Smart Shuttle Bus IoT** — Node.js, Raspberry Pi GPIO, AWS IoT Core,
  MQTT, WebSocket; connected smart stations, shuttles, and cloud.
- **Smart Home Capability API** — Node.js, Cloud Functions, IoT Core, PubSub,
  DataStore, MQTT; appliance capability sync between devices and cloud.
- **WiFi 6 Router Management Report API** — Node.js, BigQuery, Cloud Functions,
  API Gateway; account registration + device onboarding analytics.
- **AI Search Service API** — Python, S3, Lambda, Rekognition, SNS, SQS,
  Elasticsearch, API Gateway; video analysis, search, and download for
  surveillance product.
- **FOTA / iDVR Billing Report API** — Node.js, CloudWatch, S3, Athena,
  Lambda, DynamoDB, API Gateway; firmware-over-the-air + fleet management
  billing.
- **Operations tooling** — automated email delivery (SES + S3 templates);
  CloudWatch alert configuration tool; cross-cloud monitoring → Google Chat
  webhook push (Lambda + SNS + Ansible).
- **ISO 27001 Service Monitor** — CloudWatch dashboard for compliance audit.

---

## Skills

| Category | Technologies |
|---|---|
| **AWS** | EKS · ECS · RDS · ElastiCache · VPC · IAM Identity Center · Cost Explorer · Organizations · ECR · SSM · Lambda · Route53 · ACM · CloudWatch · EventBridge · SNS · Secrets Manager · WAF · GuardDuty · Security Hub · Config · Athena · Client VPN · KMS · Rekognition |
| **GCP** | GKE · Cloud SQL · Cloud Functions · IoT Core · BigQuery · Cloud Armor · Security Command Center · Cloud Monitoring · PubSub · PSC · DMS |
| **IaC** | Terraform (3-layer state, S3 + DynamoDB lock) · AWS CDK (TypeScript / Python) · Helm · Kustomize |
| **Kubernetes** | EKS · GKE · k3s · ArgoCD · KEDA · HPA / VPA · Istio · External Secrets Operator · IRSA · Velero · cert-manager |
| **CI/CD** | GitLab + GitLab Runner · Jenkins (JNLP + Kaniko + S3 / EFS cache) · GitHub Actions (reusable workflows, OIDC) |
| **Observability** | Grafana · OpenTelemetry · Thanos · ELK / OpenSearch · PMM · CloudWatch · Cloud Monitoring · Sentry |
| **Security & Compliance** | SOC 2 · ISO 27001 · WAF · GuardDuty · Security Hub · Cloud Armor · cert-manager · Network Policy · Chaos Monkey · DefectDojo + Dependency-Track |
| **AI / DevTools** | LLM-based SRE automation (OpenClaw) · Claude Code multi-agent skill platform |
| **Languages** | Python · TypeScript · Node.js · Bash · HCL · YAML |
| **Other** | Fortinet VPN · IoT (MQTT, GPIO, Raspberry Pi) · AWS Client VPN |

