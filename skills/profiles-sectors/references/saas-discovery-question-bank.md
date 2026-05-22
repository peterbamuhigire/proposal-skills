# SaaS Discovery Question Bank

Reusable discovery question set for SaaS implementation and SaaS product-development engagements. Use these questions to:

- Stress-test an incomplete brief or RFP before drafting.
- Build the Understanding of the Assignment section.
- Populate the Pain Chain, Impact, and Decision Process blocks in the methodology.
- Generate clarification requests for the procurement team or sponsor.

Translate into evaluator-facing assumptions and discovery summaries; never submit the raw question list inside the proposal body.

## A. Ideal Customer Profile and Critical Event

- Which segment of customers, employees, or beneficiaries does this SaaS serve, and what defines a "fit" customer for the proposed solution?
- What event made this assignment urgent now rather than six months ago: regulatory deadline, system end-of-life, audit finding, M&A integration, growth ceiling, competitor move, customer-experience failure, or board mandate?
- What changes for the organisation if this assignment slips by six months? What changes if it slips by two years?
- Is the client buying SaaS for internal use, or buying SaaS-readiness to deliver a SaaS product to its own customers?

## B. Pain Chain

- What is the surface-level pain everyone currently complains about?
- What operational pain does that surface-pain cause (delays, rework, overtime, error rates, complaints, manual workarounds)?
- What financial pain does the operational pain cause (cost, lost revenue, penalty, write-off, working-capital tied up)?
- What strategic pain does the financial pain cause (investor confidence, regulator attention, customer attrition, reputation, succession planning)?
- For each pain link, what evidence already exists (analytics, audit, complaint logs, support tickets, interviews, observation)?

## C. Impact per Role

For each of the roles below, ask: what metric improves, by how much, on what baseline, and worth what to the client?

- Executive sponsor (CEO, MD, board chair).
- Finance owner (CFO, finance director).
- Operations owner (COO, head of operations).
- Technology owner (CIO, CTO, head of digital).
- Security owner (CISO, risk officer, compliance officer).
- Frontline user (the person who uses the SaaS daily).
- Customer or beneficiary (the end consumer of the service the SaaS enables).
- Procurement owner (procurement director, head of supplier management).

## D. Decision Process

- Is this decision a *consensus* decision (multiple veto holders, each able to block) or a *hierarchy* decision (a single executive owns the call)?
- Name every individual who can say yes; name every individual who can say no.
- What previous procurement experiences shape current expectations?
- Who must defend the award decision internally, and to whom?
- Which evaluation criteria are mandatory-compliance, which are scored, and which are personal-confidence?
- What is the path from shortlist to signature, in named steps with named owners and target dates?

## E. Decision Criteria

- What evaluation criteria are mandatory by procurement rule?
- What evaluation criteria are scored by the technical evaluators?
- What confidence factors (not in the scoring sheet) will actually influence the award: senior team availability, comparable-vertical experience, reference reachability, after-go-live commitment, exit clauses?
- Which criteria carry the highest weight, and which is the buyer secretly most worried about?
- How will the buyer's executive sponsor justify a premium price to their CFO?

## F. Current State Architecture and Data

- Which existing systems must the SaaS integrate with: core banking, policy admin, HMIS, ERP, CRM, identity provider, data warehouse, regulatory reporting, payment gateway?
- Which systems must the SaaS replace? Which must it co-exist with for how long?
- Where does customer/citizen data currently live, and what is its quality?
- What are the data residency, privacy, retention, and audit obligations?
- What identity model exists (corporate SSO, federated IdP, government digital ID, customer-facing auth)?

## G. Tenant Model and Architecture (where the client is or becomes a SaaS provider)

- How many tenants does the platform need to support at year 1, year 3, year 5?
- What variation across tenants is mandatory: branding, workflows, data schema, regulators, languages, currencies?
- What is the desired isolation model: silo, pool, bridged? Is the answer different for compute vs storage?
- Which tenants demand dedicated infrastructure for contractual or regulatory reasons?
- What is the noisy-neighbour tolerance, and how is it monitored today?
- What is the desired onboarding pattern: fully self-serve, sales-assisted, or operations-assisted?

## H. Commercial Model (where the client owns SaaS revenue)

- Subscription, usage-based, hybrid, or enterprise tier?
- Per-seat, per-volume, per-feature, per-outcome?
- Free tier, freemium, paid trial, or paid POC?
- Expected ACV by segment? Expected payback period? Target gross retention? Target net retention?
- Is the commercial model expected to evolve, and over what horizon?

## I. Implementation Constraints

- Fixed dates: contract start, mid-term review, go-live, end of warranty, end of support.
- Hard procurement constraints: validity period, currency, withholding tax, VAT, evaluation method.
- Hard delivery constraints: on-site requirements, security clearance, country-of-residence, language.
- Approval cadence and review windows on the client side.
- Public holidays, election periods, rainy seasons, exam periods (for education clients).

## J. Risk and Support

- What contractual exits, data-return, escrow, and termination protections must the proposal address?
- What SLA penalties, credits, or remedies are expected?
- What support window, channels, hours, and severity model is expected?
- What is the regulator's view on outsourced or cloud-hosted SaaS for this vertical?
- What sub-processors must be disclosed, and what residency must they meet?

## K. Adoption and Change

- Who owns the SaaS after go-live: an internal team, a managed-service provider, or a hybrid?
- What is the operating model change required (release cadence, support model, customer-success function)?
- What is the readiness of leadership, middle management, and frontline users?
- What previous transformation attempts failed, and why?
- What is the change-management budget and capacity?

## L. Measurement and Value Realisation

- What baseline metrics exist and have been verified?
- Which metrics will move first, and by when, after go-live?
- What is the agreed value-realisation review cadence (30/60/90, quarterly business review)?
- What internal-control measurement is expected (A/B, holdout, propensity matching) vs benchmark comparison?
- Who in the client organisation will own the value-realisation report?

## How to Use This Bank in a Proposal Workflow

1. Skim the ToR/RFP and mark which questions are already answered.
2. List the unanswered questions and decide which must be answered before submission (write a clarification request) and which can be addressed through declared assumptions in the proposal.
3. Populate Pain Chain, Impact-per-Role, and Decision Process blocks for the Understanding of the Assignment and Methodology sections.
4. Use answers to size the POC/pilot, design the MAP, and structure the business case.
5. Keep a per-engagement copy of the answered question set in the proposal's `research/` folder.
