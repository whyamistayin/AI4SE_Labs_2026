---
name: architecture-decision-workflow
description: "Use when analyzing software requirements to propose and compare architecture alternatives, discussing trade-offs, selecting an architecture, or creating and refining an Architecture Decision Record (ADR)."
argument-hint: "Requirements source, architecture options or ADR scope"
---

# Architecture Decision Workflow

Help stakeholders move from software requirements to a reasoned architecture choice and a useful ADR. Keep architecture analysis grounded in the actual requirements; distinguish user decisions from assistant recommendations and facts from assumptions.

## 1. Inspect the requirements and context

1. Read the supplied requirements, user stories, constraints, and relevant existing architecture documents before proposing a design. Inspect enough of the repository to find established documentation conventions and the correct output location.
2. Summarize the system's capabilities, actors, important data, authorization rules, and quality attributes implied by the requirements. Identify conflicts, omissions, and unclear terms.
3. Separate:
   - stated requirements;
   - reasonable assumptions, labeled as assumptions;
   - open questions that could change the decision.
4. Do not invent traffic, availability, latency, hosting, compliance, budget, or team-size targets. Ask focused questions when an unresolved choice materially changes the architecture. If the stakeholder cannot answer, proceed with explicit assumptions and explain their effect.
5. Agree on deliverables and locations when not already clear. If the user asks for notes or the assignment requires a discussion record, maintain concise notes as the work progresses. Do not fabricate dialogue or claim the user approved a decision they did not make.

## 2. Propose distinct architecture alternatives

When asked for alternatives, provide the requested number of genuinely different options. For a typical product, useful starting points may include:

- a modular monolith with clear in-process domain boundaries;
- independently deployed domain-oriented services with service-owned data;
- a managed serverless/event-driven deployment.

Treat these as candidates, not a fixed menu. Select options appropriate to the requirements and explain when a difference is about domain decomposition versus deployment model. Do not present multiple names for essentially the same design as distinct choices.

For each alternative, explain:

1. **Shape and boundaries:** clients, application components, service/module responsibilities, data ownership, and major integrations.
2. **Concrete behavior:** walk through at least one important user workflow end-to-end, including authorization and persistence.
3. **Data and consistency:** source of truth, transaction boundaries, synchronous calls, events, eventual consistency, retries, deduplication, and recovery where relevant.
4. **Security and privacy:** identity, resource/tenant authorization, data isolation, sensitive data movement, and revocation behavior.
5. **Testing:** unit/component tests, API or event contract tests, integration tests, and end-to-end tests needed by that topology.
6. **Benefits, costs, and painful implementation details:** operations, deployment, observability, failure handling, performance, cost, team skills, and likely coupling or lock-in.
7. **Fit:** conditions under which the option is a good or poor choice.

Compare alternatives in a compact table using criteria that matter to the requirements. State a recommendation and its assumptions, but do not override the user's selection. If the user prefers an option for a particular reason, record that rationale faithfully and explain the safeguards and trade-offs; for example, service boundaries can reduce accidental data access and enable focused testing, but do not automatically guarantee security or make cross-service tests easier.

Keep the discussion interactive when requested: invite critique or selection, explain low-level consequences in plain language, and refine the proposal when the user points out missing information.

## 3. Record the decision

Once an option is selected, or the user asks directly for an ADR, create a Markdown ADR in the requested or repository-appropriate location. Use a concise, recognizable structure:

- Title and metadata: status, date, decision owners if known, and related documents.
- **Context:** system scope, requirements, constraints, and relevant uncertainty.
- **Decision drivers:** prioritized requirements and user-stated reasons.
- **Decision:** the chosen architecture, boundaries, and consequential design rules.
- **Architecture overview:** diagram when it clarifies components, ownership, and communication; Mermaid is suitable when supported.
- **Responsibilities and data ownership:** what each component owns and explicitly does not own.
- **Key flows and technical behavior:** representative workflows, authorization, persistence, consistency, events, retries, and lifecycle operations as applicable.
- **Security, privacy, and testing implications:** explain what the architecture enables and what must still be enforced or tested.
- **Consequences:** benefits, costs, risks, and operational burden.
- **Alternatives considered:** why each was not selected and what evidence would justify revisiting it.
- **Rollout/validation and open questions:** measurable checks, unresolved requirements, and decision triggers where useful.

Tailor the ADR to the system. Do not pad it with irrelevant sections or lock in a cloud vendor, language, database, broker, or numerical target without evidence or stakeholder direction. Do not label an architecture “accepted” as an organizational fact unless the user has authority and has explicitly said so.

## 4. Review and refine

1. Inspect the resulting ADR from the reader's perspective: Can they understand what was chosen, why, how important flows work, what alternatives were rejected, and what remains uncertain?
2. Check that the diagram agrees with the written boundaries and that no service reads another service's private datastore unless explicitly justified.
3. Look for unsupported requirements, hidden assumptions, vague security claims, unjustified precision, missing failure paths, and consequences omitted from the comparison.
4. Refine the ADR based on stakeholder feedback. Preserve previous decisions unless the user changes them; explain meaningful changes in discussion notes when requested.
5. If a conversation record is requested, summarize the real decision points, questions, user preferences, revisions, and final outcome—not an invented verbatim transcript.
6. Verify links, file placement, Markdown structure, and repository documentation checks when available. Report created files and any unresolved questions.

## Quality bar

- Be specific to the stated system and trace architectural claims back to requirements or labeled assumptions.
- Explain trade-offs symmetrically; every option should have realistic drawbacks.
- Treat authorization, data privacy, retries, and failure handling as design concerns, not diagram annotations.
- Distinguish focused component testing from whole-system integration/testing effort.
- Prefer the simplest architecture that meets known needs, while fairly documenting a user-selected alternative.
- Write for both technical and non-technical stakeholders: define jargon at first use and explain operational consequences plainly.
