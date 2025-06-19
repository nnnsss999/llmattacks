---
title: "Anthropic RSP Supply Chain Controls"
category: "Supply Chain"
source_url: "https://www.anthropic.com/rsp-updates"
date_collected: 2025-06-19
license: "Fair Use"
---

The Responsible Scaling Policy (RSP) describes how Anthropic secures its model-building pipeline. It states:

> Monitor publicly known critical security issues in third-party dependencies. Conduct consistent scanning of all third-party dependencies and maintain a comprehensive vulnerability data repository. Proactively scan all incoming packages to enable download of only secure packages and reduce risk of introducing vulnerabilities. Leverage frameworks (e.g., SLSA) to improve security controls for software build and deployment. Require packages to have provenance metadata.

These controls show a commitment to verifying component integrity and tracking provenance to prevent compromised artifacts from entering production models.
