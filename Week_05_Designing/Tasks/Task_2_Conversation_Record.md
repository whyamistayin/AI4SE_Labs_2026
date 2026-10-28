# Teamify ADR Discussion Record

This is a concise record of the design discussion and review, not a word-for-word transcript. It accompanies the final [Teamify ADR](./Task_2_Teamify_ADR.md) and builds on the [Task 1 architecture proposals](./Task_1_Architecture_Notes.md).

## Discussion notes

### 1. Selecting the architecture for the ADR

**User:** Create an architecture decision record for the second architecture design from Task 1, and create another conversation record like the previous task.

**Assistant:** The second proposal is a domain-oriented service architecture: Identity, Collaboration, Chat, Polls, and Notifications are independently deployed services; each owns its data. A gateway handles client-facing routing, synchronous APIs handle immediate decisions, and a durable broker carries asynchronous domain events.

**Note:** Task 1 recommended a modular monolith as the lower-risk starting point because scale and operational needs are unspecified. The requested ADR records the second option as the selected target for this design exercise, without presenting it as a production commitment supported by unprovided scale evidence.

### 2. First review: what should an informative ADR explain?

**Assistant review:** A service list alone would not explain how Teamify actually works. The ADR needs to show who owns membership and roles, how services authorize shared actions, how events and notifications survive failure, and what happens when deleting a team or account spans multiple services.

**Revision made:** Added service ownership and exclusions, a logical architecture diagram, synchronous-versus-asynchronous communication guidance, and an event/outbox/idempotency model.

### 3. Second review: identify the painful consistency boundary

**Assistant review:** Chat needs current team membership, but membership is owned by Collaboration. Copying roles into Chat through asynchronous events can leave stale authorization after a member is removed. A synchronous check reduces that risk but adds latency and a dependency; it still cannot make membership validation and message persistence one atomic cross-service transaction.

**Revision made:** Made Collaboration the membership authority, required an authenticated synchronous authorization check before a chat send, prohibited fail-open behavior, and documented the remaining race and the option to change the boundary if strict revocation is required.

### 4. Final review: make the decision and its limits clear

**Assistant review:** The ADR should distinguish a design-exercise decision from an approved production commitment. It should also compare the alternatives, name the costs of independent services, and list evidence needed before rollout.

**Revision made:** Marked the ADR “Accepted for the design exercise; production commitment requires validation,” added an alternative comparison, consequences, rollout checks, operational/security requirements, and unresolved product questions.

## Result

The final ADR records the domain-oriented services design and makes the main implementation trade-offs inspectable: service-owned data, no cross-service transactions, eventual consistency, idempotent event processing, synchronous membership authorization, lifecycle sagas, observability, and operational overhead. It intentionally leaves provider, language, and broker choices open because the requirements do not establish them.

### 5. User preference: data isolation and testability

**User:** The second architecture is preferred because it restricts data leakage and can be tested more easily, while acknowledging that handling many services is more challenging.

**Assistant:** Agreed that explicit service ownership can limit accidental exposure and support focused testing. These are benefits only when the boundaries are enforced: per-service credentials and datastore permissions, narrow APIs, resource-level authorization, and tests at service and integration boundaries. Multiple services also add contract, integration, and end-to-end testing work, so the architecture does not inherently make the whole system easier to test.

**Revision made:** Added these points to the ADR decision drivers and a dedicated rationale section, including the safeguards and trade-offs needed for data isolation and testability to be real rather than assumed.
