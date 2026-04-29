# DevOps Delivery Diagnostics

Use this reference when a proposal concerns software delivery, SaaS operations, digital platforms, cloud migration, PHP/LAMP modernisation, CI/CD, DevSecOps, observability, incident response, or production reliability.

Source set: *Strategic DevOps*, *DevOps for PHP Developers*, *The DevOps Handbook, Second Edition*, and *Modern DevOps Practices*.

## Diagnostic Domains

| Domain | What to assess | Typical evidence |
|---|---|---|
| Value stream flow | Time from idea, ticket, or code commit to production feedback | Lead time, WIP, branch age, deployment calendar, approval queues |
| Pipeline and release | CI/CD stages, artifact promotion, gates, rollback, release evidence | Pipeline configs, build logs, release notes, deployment scripts |
| Branching and integration | Trunk readiness, branch age, merge conflict rate, release branch pattern | Git history, PR age, branch policy, failed merge records |
| Testing and quality | Unit, integration, contract, acceptance, performance, resilience, and security checks | Test reports, coverage, flaky test list, defect trends |
| Observability | Logs, metrics, traces, dashboards, release markers, actionable alerts | Monitoring dashboards, alert rules, log samples, incident timelines |
| Incident response | Severity model, on-call, escalation, status communication, post-incident learning | Incident reports, runbooks, on-call rota, action-item closure |
| Infrastructure and GitOps | IaC, configuration drift, containerisation, Kubernetes, desired-state management | Terraform/Ansible, manifests, cluster state, drift reports |
| PHP/LAMP operations | Composer, PHP-FPM, OPcache, web server, migrations, queues, file storage, patching | Server configs, deployment guide, backups, queue workers, `.env` handling |
| DevSecOps | Dependency scanning, secret scanning, IaC policy, image scanning, least privilege | Security pipeline results, IAM rules, vulnerability backlog |
| Cost and capacity | Cloud cost, utilisation, scaling, environment sprawl, CI runner cost | Cloud bills, tags, utilisation, autoscaling policy, runner metrics |

## Methodology Building Blocks

### Current-State Delivery Assessment

- Map the technology value stream from demand intake to production feedback.
- Measure lead time, deployment frequency, change failure rate, and time to restore.
- Identify where work waits: review, test, environment, approval, deployment, or verification.
- Separate tooling gaps from operating-model gaps: ownership, incentives, handoffs, and decision rights.

### Pipeline and Release Review

- Confirm that the pipeline is the normal route to production.
- Check whether artifacts are built once and promoted through environments.
- Review branch strategy and integration delay.
- Classify release risk by schema changes, auth, workflow-critical logic, infrastructure, data side effects, or feature exposure.
- Test rollback realism across code, database, caches, queues, files, and external integrations.

### Observability and Incident Review

- Define service-level indicators and service-level objectives.
- Check RED metrics for services and USE metrics for infrastructure.
- Verify that release markers appear in telemetry.
- Review whether alerts are actionable and routed to the right owner.
- Check whether incidents produce system improvements, not blame-only reports.

### PHP and Cloud-Native Review

For PHP systems, inspect Composer discipline, environment config, PHP-FPM, OPcache, queues, migrations, web server config, backups, file permissions, and patching.

For cloud-native systems, inspect container build quality, image scanning, readiness/liveness probes, resource limits, rollout strategy, GitOps workflow, namespace isolation, network policy, and drift monitoring.

## Proposal Language

"Our methodology will assess the client's software delivery operating model across value-stream flow, CI/CD pipeline design, release governance, observability, incident response, infrastructure automation, security controls, and runtime operations. This allows us to distinguish tooling gaps from process, architecture, ownership, and reliability gaps before recommending a practical delivery improvement roadmap."

## Deliverable Options

- DevOps maturity assessment
- CI/CD pipeline and release governance review
- PHP/LAMP deployment hardening plan
- Cloud-native or Kubernetes readiness assessment
- DevSecOps controls roadmap
- Observability and incident response improvement plan
- GitOps and Infrastructure-as-Code implementation plan
- Software delivery KPI dashboard
