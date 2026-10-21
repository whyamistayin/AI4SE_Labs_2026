# Software Requirements Specification

Generated from 20 source documents.

## Priority scale

- **Must** — Essential or explicitly mandatory for the system.
- **Should** — Important, but a viable workaround exists.
- **Could** — Desirable or explicitly optional.

## Requirements

### REQ-001: (Could) Notify users about delayed or problematic transfers

**Priority:** Could

The transfer utility could notify users when a transfer is delayed or has issues.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R016) - > If an item transfer is delayed or has issues, notify me
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R034) - > If an item transfer is delayed or has issues, notify me

### REQ-002: (Could) Schedule purging utility runs

**Priority:** Could

The purging utility could support scheduled automatic runs, such as running at the end of each year.

**Derived from:**
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R014) - > can the purging utility be scheduled

### REQ-003: (Could) Track denied deletion attempts and capture deletion reason/prior status

**Priority:** Could

The system could track deletion attempts that were denied to support compliance and troubleshooting. It could also capture a reason and/or the prior status for a deletion alongside the deletion audit information.

**Derived from:**
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R008) - > track attempted deletions that were denied
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R009) - > Possibly why (status before deletion

### REQ-004: (Optional) Filter shelf-space share reports by date range

**Priority:** Could

The shelf-space report could support filtering by a date range to examine shelf-space utilization across different periods (such as quarters).

**Derived from:**
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R005) - > Can we also filter by date range
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R011) - > Can we also filter by date range

### REQ-005: (Optional) Provide comparison view of library breakdowns side by side

**Priority:** Could

The shelf-space report could offer a comparison view that presents each library’s breakdown side by side to make differences between libraries easier to identify.

**Derived from:**
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R006) - > a "comparison" view that shows each library's breakdown side by side
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R012) - > include a "comparison" view that shows each library's breakdown side by side

### REQ-006: (Optional) Show volume for recent acquisition windows (e.g., last 30/60/90 days)

**Priority:** Could

The system should allow users to see how much volume was added during recent periods such as the last 30, 60, or 90 days.

**Derived from:**
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R008) - > It would be helpful to see how much volume has been added in the last 30/60/90 days

### REQ-007: (Optional) Use color coding for capacity status (under-capacity / nearing-full / at-or-over-capacity)

**Priority:** Could

The capacity interface could use color coding (for example green/yellow/red) to indicate under-capacity, nearing-full, and at-or-over-capacity status.

**Derived from:**
- `conversations/conv_pines015_capacity_interface.eml` (lines 1-102; DOC-4acf2fdb375b, DOC-4acf2fdb375b-C001, DOC-4acf2fdb375b-C001-R007) - > Maybe color-coding - green for under capacity, yellow for getting full,    red for at/over capacity

### REQ-008: (Required) Provide hierarchical online help and context/administrative query-specific feedback

**Priority:** Must

The system must provide an online hierarchical, cross-linked help system in HTML. It must also allow Local and Global System Administrators to receive low-level, query-specific feedback from the front-end interface when queries/reports fail.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R024) - > an online, hierarchical, and cross-linked help       system in HTML that describes and illustrates all system functions
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R026) - > shall allow low-level query-specific feedback for Local and Global       System Administrators from the front-end interface
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R006) - > Admin controls access
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R013) - > shall allow low-level query-specific feedback for administrators

### REQ-009: (Should) Confirm changes with a transfer preview before applying; support undo of transfers

**Priority:** Should

Before applying changes, the transfer utility should show a preview of the transfer (including the number of items and the source and destination locations) and ask the user to confirm. The utility should also provide a way to undo a transfer if it was initiated by mistake.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R012) - > show a preview before making changes
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R013) - > And we need an undo function
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R028) - > the utility should show a preview before making changes
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R029) - > And we need an undo function

### REQ-010: (Should) Generate printable pull lists and/or printable transit labels for transferred items

**Priority:** Should

The transfer utility should generate printable pull lists of items to be moved. It should be able to generate printable transit labels for transferred items, including barcodes.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R006) - > create a printable list of items to be moved
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R015) - > can we generate transit labels? Like, printable barcodes for the items being transferred
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R033) - > generate transit labels? Like, printable barcodes for the items being transferred

### REQ-011: (Should) Provide a last-copy report with library and system scope and flag last copies within the selected scope

**Priority:** Must

The system must provide a last-copy report that identifies last copies both at an individual library scope and across the system. For each item record, the last-copy report must determine whether it is the only copy in the specified library or system scope and flag it when it is.

**Derived from:**
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R007) - > I think we need both views
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R008) - > is this the only copy in the specified scope (library or system)? If yes, flag it

### REQ-012: (Should) Provide audit logging and track item-level transfer history; process transfer updates in smaller batches with transaction safety

**Priority:** Should

The system should record transfers for audit purposes and provide item-level transfer history so users can see how many times an item has been transferred over a period. To reduce database locking for large transfers, batch updates should be processed in smaller groups. Location updates should be performed with transaction safety.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R010) - > track all transfers for audit purposes
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R011) - > this item has been transferred 5 times in the past year
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R009) - > We should process in smaller batches to avoid locking the database
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R023) - > Batch update of location field - straightforward database update with    transaction safety
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R035) - > We should process in smaller batches to avoid locking the database

### REQ-013: (Should) Purge utility support for batch status conversion and optional deletion behaviors (delete volume with copy entries; delete records with no attached items)

**Priority:** Should

The system should provide a report to assist users in converting items from one status to another in batch rather than handling each item individually. The system should also support optional deletion behaviors such as deleting volume entries together with associated copy entries and deleting records that have no items attached.

**Derived from:**
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R006) - > I need a report to help convert items from one status to another in batch
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R009) - > deleting volume entries along with copy entries
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R010) - > records with no items attached

### REQ-014: (Should) Restrict transfer utility permissions to authorized roles

**Priority:** Should

The transfer utility should restrict transfer capabilities to authorized roles (for example managers, administrators, or transfer coordinators) rather than making transfers available to all staff.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R014) - > This should be limited to certain roles (managers, administrators, transfer coordinators
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R030) - > This should be limited to certain roles (managers, administrators, transfer coordinators

### REQ-015: (Should) Support automatic reversion of transfers after time-based and non-time criteria (including event/program)

**Priority:** Should

The transfer utility should support returning transferred items to their original location after a specified period of time. It should also support automatically reverting transferred items based on criteria other than elapsed time, including status-based or event-based criteria. In addition, it should support moving items to a temporary location for a specific event/program and returning them after that event/program.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R007) - > Revert items to original location after a set period of time
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R026) - > reverts them based on time or status criteria
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R027) - > transfer items to a temporary location for a specific event or program? Like, move 20 biographies to the community center for their genealogy workshop, then revert them after the event
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R025) - > Revert items to original location after a set period of time

### REQ-016: (Supplemental) Email and accessibility-ready reporting outputs (as required by platform-level constraints)

**Priority:** Must

The system must support report interfaces and outputs consistent with accessibility and output standards; it must deliver standards-compliant HTML for web and help/report outputs and provide accessible experiences for users relying on assistive technology.

**Derived from:**
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R043) - > Excel, HTML, and CSV formats are required
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R002) - > all HTML output validates against W3C standards
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R006) - > The system needs to work with:   - Screen readers like JAWS and NVDA   - Screen magnification software like ZoomText   - Other assistive technology programs

### REQ-017: Access control model: control rights and privileges through security groups/roles

**Priority:** Must

The system must use security groups and/or roles to control user rights and privileges for individuals, workgroups, and arbitrary staff groups.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R018) - > User rights and privileges will be controlled through security groups and       or "roles" that allow access control for individuals, workgroups, and       arbitrary staff groups
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R011) - > The permission system needs to be controlled through security groups and/or "roles." This allows access control for individuals, workgroups, and arbitrary staff groups
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R011) - > User rights and privileges will be controlled through security groups       and/or "roles" that allow access control for individuals, workgroups,       and arbitrary staff groups

### REQ-018: Appendix A report families: support circulation report types and item report types as defined

**Priority:** Must

The system must support Appendix A circulation report types and item report types, including the defined counts/breakdowns for check-ins/check-outs/renewals and the defined item report families such as items added/deleted/edited, overdue/long-overdue, missing, claims-returned, transit, weeding, last-copy, and collection age reports.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R060) - > CIRCULATION REPORTS
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R061) - > ITEMS REPORTS

### REQ-019: Architecture: centralized multi-location operation and read-only integration with enterprise library automation data; query OPAC-created holds/circulation transactions without modifying them

**Priority:** Must

Management/reporting processes must be consolidated at a central location and accept input from and provide services to multiple library locations. The reporting system must rely on and read data from the enterprise Library Automation System (including acquisitions and cataloging modules) rather than managing acquisitions or cataloging itself. It must be able to query OPAC-created holds and circulation transactions without modifying that data.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R006) - > consolidated at a central location and accept input from and provide services to multiple library locations
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R019) - > Management Processes are consolidated at a central location, and accept       input and provide services to multiple locations
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R014) - > Management Processes are consolidated at a central location, and accept input and provide services to multiple locations
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R016) - > The reporting system doesn't manage acquisitions or cataloging - it just reads the data
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R017) - > The reporting system queries this data, but doesn't modify it
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R042) - > The reporting system queries this data, but doesn't modify it

### REQ-020: Batch transfer utility between branches (including temporary/program transfers and moving items to a new location)

**Priority:** Must

The system shall provide a utility to transfer batches of items from one branch to another, including temporary/program-related transfers. The workflow shall support transferring selected items to a destination/new location.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R001) - > utility for transferring batches of items between branches
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R017) - > utility for transferring batches of items between branches
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R025) - > Revert items to original location after a set period of time

### REQ-021: Break down material volume by customizable categories and show holds counts per category

**Priority:** Should

The material-volume report shall allow users to view volume broken down by categories (such as fiction/non-fiction and formats). The report shall include hold counts per category in its category breakdown. Category definitions used for breakdowns shall be customizable so different libraries can select the breakdowns they need.

**Derived from:**
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R004) - > Groups by categories (fiction/non-fiction, format, etc
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R006) - > Shows breakdowns with holds count per category
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R005) - > Can we make the categories customizable

### REQ-022: Capacity interface: show a system-wide (all-branch) capacity overview with drill-down to individual branches

**Priority:** Must

The capacity interface shall provide a high-level overview of capacity across all branches at once. Users shall be able to drill down from the system-wide overview to view individual branch capacity.

**Derived from:**
- `conversations/conv_pines015_capacity_interface.eml` (lines 1-102; DOC-4acf2fdb375b, DOC-4acf2fdb375b-C001, DOC-4acf2fdb375b-C001-R001) - > High-level overview of all branches' capacity at once
- `conversations/conv_pines015_capacity_interface.eml` (lines 1-102; DOC-4acf2fdb375b, DOC-4acf2fdb375b-C001, DOC-4acf2fdb375b-C001-R002) - > Ability to drill down into individual branches

### REQ-023: Capacity interface: support sorting, filtering (region/library type/current load), and show capacity trends; allow CSV export

**Priority:** Should

The capacity interface shall allow users to sort and filter branch capacity information. Filtering shall support criteria including region, library type, and current load. The interface shall show trend data indicating whether branch capacity is growing or shrinking. Users shall be able to export capacity data in CSV format.

**Derived from:**
- `conversations/conv_pines015_capacity_interface.eml` (lines 1-102; DOC-4acf2fdb375b, DOC-4acf2fdb375b-C001, DOC-4acf2fdb375b-C001-R003) - > I'd want to be able to sort and filter
- `conversations/conv_pines015_capacity_interface.eml` (lines 1-102; DOC-4acf2fdb375b, DOC-4acf2fdb375b-C001, DOC-4acf2fdb375b-C001-R004) - > By region, by library type, by current load
- `conversations/conv_pines015_capacity_interface.eml` (lines 1-102; DOC-4acf2fdb375b, DOC-4acf2fdb375b-C001, DOC-4acf2fdb375b-C001-R005) - > Trend data (growth/shrink patterns
- `conversations/conv_pines015_capacity_interface.eml` (lines 1-102; DOC-4acf2fdb375b, DOC-4acf2fdb375b-C001, DOC-4acf2fdb375b-C001-R006) - > export to CSV

### REQ-024: Combine patron filters with AND/OR; include null patron values in results; support configurable age ranges and compute age range from birth date at query time

**Priority:** Should

The system should allow multiple report filters to be combined using AND and OR logic. It should include records with null optional patron values in results rather than silently excluding them. The system should allow users to configure age brackets used for reports, and it should calculate a patron’s age range from the birth_date field at query time so the configured brackets are applied during query execution.

**Derived from:**
- `conversations/conv_pines023_patron_characteristics.eml` (lines 1-133; DOC-d2b26a6e7678, DOC-d2b26a6e7678-C001, DOC-d2b26a6e7678-C001-R003) - > Filters can be combined with AND/OR logic
- `conversations/conv_pines023_patron_characteristics.eml` (lines 1-133; DOC-d2b26a6e7678, DOC-d2b26a6e7678-C001, DOC-d2b26a6e7678-C001-R004) - > We should include them in the report (with null values) rather than excluding them
- `conversations/conv_pines023_patron_characteristics.eml` (lines 1-133; DOC-d2b26a6e7678, DOC-d2b26a6e7678-C001, DOC-d2b26a6e7678-C001-R005) - > Age ranges should be configurable per report
- `conversations/conv_pines023_patron_characteristics.eml` (lines 1-133; DOC-d2b26a6e7678, DOC-d2b26a6e7678-C001, DOC-d2b26a6e7678-C001-R006) - > The "age range" is calculated from the birth_date field, which means we need to compute it at query time

### REQ-025: Database and data model constraints: use a fully relational database backend and provide complete data specifications and documentation of major processes

**Priority:** Must

The system must use a fully relational database back-end and work with relational database structures. The developer must provide complete data specifications for authority, bibliographic, order, item, hold/request, and other records maintained or accessed by the management/reporting processes. The developer must also provide thorough high-level descriptions of major processes, including bibliographic record import/export, validation against internal/external authority sources, and standard reports.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R015) - > The system must use a fully relational database back-end
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R009) - > The reporting system needs to work with the relational structure, not fight against it
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R001) - > the system must use a fully relational database back-end
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R020) - > complete data specifications for authority       records, bibliographic records, order records, item records, hold/request       records, and other records maintained or accessed by the Management       Processes
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R013) - > The software developer shall provide complete data specifications for       authority records, bibliographic records, order records, item records,       hold/request records, and other records maintained or accessed by       Management Processes
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R033) - > The developer must provide complete data specifications for
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R021) - > bibliographic record import and export
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R014) - > The software developer shall provide a thorough high-level description       of major processes, including bibliographic record import and export,       validation of bibliographic records against internal and external       authority sources, and standard reports
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R034) - > The developer must provide a thorough high-level description of major processes

### REQ-026: Deletion auditing analytics: count and track deletions by location and system; provide an interface and aggregated reports for deletion audits

**Priority:** Should

The system should count and track record deletions, including item and patron records, per location and per system. It should provide an interface for querying the audit log of deletion records. The system should support aggregated deletion reporting by date range, by user, and by record type, including totals by period and breakdowns by record type and location, and it should provide reports identifying the users with the most deletions.

**Derived from:**
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R002) - > count and track record deletions (e.g., item records, patron records) per location and per system
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R003) - > A report interface to query this audit table
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R004) - > We can aggregate by date range, by user, by record type
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R005) - > Total deletions per period (month, quarter, year
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R006) - > Deletions by type (item vs patron vs other) - Deletions by location
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R007) - > Top users who delete the most records

### REQ-027: Deletion auditing: record details when records are deleted

**Priority:** Should

When a record is deleted, the system should create an audit entry containing the record type, record ID, deleting user, deletion timestamp, and location.

**Derived from:**
- `conversations/conv_pines022_deletions.eml` (lines 1-124; DOC-7b8da7c05931, DOC-7b8da7c05931-C001, DOC-7b8da7c05931-C001-R001) - > Fields: record_type, record_id, deleted_by, deleted_at, location

### REQ-028: Development and training environments with safe configuration migration to production

**Priority:** Must

The system must provide separate development and training environments. Configurations created in development/training must be migratable to production. The training environment must allow staff to experiment without risking production data.

**Derived from:**
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R014) - > We definitely need separate environments
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R015) - > Developers need a place to test new reports without affecting production
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R016) - > new staff members need a training environment where they can practice running reports without worrying about making mistakes
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R017) - > We need export/import functionality for report templates, permission settings, and other configuration
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R004) - > staff should be able to experiment without risking production data

### REQ-029: In the material-volume report, show separate counts by circulation status (new acquisitions, on shelf, out in circulation) plus a total; support historical date filters

**Priority:** Should

For the selected library and point in time (including historical comparisons), the material-volume report shall separately show counts for new acquisitions, items on the shelf, and items out in circulation, and also show a total across those counts. The report shall support date filtering so users can view volume for historical periods and compare over time.

**Derived from:**
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R003) - > all three counts separately plus a total
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R007) - > We can also add date filters - volume at any point in time, not just current. This would be useful for historical comparisons
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R020) - > Ability to report on the volume of material in a given library at any point in time, based on new acquisitions, items on the shelf, and items out in circulation

### REQ-030: In-transit report: list items exceeding a configurable transit age threshold; scope by branch and system; combine transit-to and transit-from

**Priority:** Must

The system shall generate a list of items that have been in transit for more than a configurable number of days. The in-transit report shall allow viewing items per branch and per system, and it shall combine transit-to and transit-from items into one report for front-line staff.

**Derived from:**
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R004) - > items that have been in-transit for more than    X days (X configurable
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R005) - > per branch and per system
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R006) - > report merges    transit-to and transit-from into one report

### REQ-031: In-transit report: sorting by due date and identification of items with null arrival dates (when departure is older than threshold)

**Priority:** Should

The in-transit report should allow sorting by due date so staff can follow up on the oldest items first. The report should also identify in-transit items with no arrival date (null arrival) where the departure date is older than the configured threshold.

**Derived from:**
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R007) - > can we sort by due date
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R008) - > items where the arrival date is null and the departure date is more than X days ago

### REQ-032: Inactive patrons report enhancements: CSV export; run in background; cache report results for performance

**Priority:** Should

The inactive-patrons report should be exportable as CSV. The system should support background processing of the report and should cache report results to handle performance impact when processing large patron databases.

**Derived from:**
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R008) - > Exportable format (CSV
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R009) - > Background processing for performance
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R010) - > run it as a background report and cache results

### REQ-033: Inactive patrons report generation (configurable lookback) with required definitions of electronic activity and configurable organizational scope levels

**Priority:** Must

The system must generate an inactive-patrons report listing patrons who have had no circulation or electronic activity during a configured lookback period. The inactivity period (number of days) must be configurable, and electronic activity shall include OPAC or patron-account logins, online hold placements, and online renewals, with access to digital collections included when integrated and logged. The report must support configurable organizational scope/levels, including System, Home Library, and County (and other levels as needed).

**Derived from:**
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R001) - > generate a list of patrons with no circulation or electronic activity in the last X days
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R002) - > X configurable
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R003) - > Electronic activity includes OPAC login, online hold placement, online renewals
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R004) - > System - Home Library - County - (Other levels as needed

### REQ-034: Inactive patrons report outreach and handling options: include current mailing addresses; track inactive patrons with outstanding fines separately; exclude selected patron types

**Priority:** Should

The inactive-patrons report should include patrons’ current mailing addresses to support outreach. The system should identify inactive patrons with outstanding fines separately from other inactive patrons. The system should allow users to exclude selected patron types from the inactive-patrons report, including examples such as do-not-disturb flags, VIP patrons, staff members, and patrons who opted out of communications.

**Derived from:**
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R005) - > Include current mailing addresses for outreach
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R006) - > Track inactive patrons with outstanding fines separately
- `conversations/conv_pines024_inactive_patrons.eml` (lines 1-154; DOC-705ab8a51bf2, DOC-705ab8a51bf2-C001, DOC-705ab8a51bf2-C001-R007) - > Allow exclusion of certain patron types

### REQ-035: Missing and damaged items report organized per branch

**Priority:** Must

The system shall provide a report of missing and damaged items organized per branch so staff can review them for inventory and collection-management purposes.

**Derived from:**
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R001) - > System provides reports of missing and damaged items per branch

### REQ-036: Missing and damaged items report: include item condition notes (optional) and support date-range filtering (optional)

**Priority:** Could

The missing and damaged items report should be able to include condition notes (for example descriptions of water damage or vandalism) to help staff understand likely causes. The report could also support filtering by date range (for example last 30 days or last quarter) to support trending.

**Derived from:**
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R002) - > can the report include item condition notes
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R003) - > The missing/damaged report can include date ranges

### REQ-037: Patron characteristic filtering and grouping for queries/reports

**Priority:** Must

The system shall allow patron queries and reports to be restricted using patron characteristics including age range, zip code, county of residence, home branch, patron type, and preferred language. The system shall support grouping report results by these same patron characteristics and presenting aggregate measures (such as circulation or patron counts) for each group.

**Derived from:**
- `conversations/conv_pines023_patron_characteristics.eml` (lines 1-133; DOC-d2b26a6e7678, DOC-d2b26a6e7678-C001, DOC-d2b26a6e7678-C001-R001) - > limited or grouped by various patron characteristics, including: - Age range - Zip code - County of residence - Home branch - Patron type - Preferred language
- `conversations/conv_pines023_patron_characteristics.eml` (lines 1-133; DOC-d2b26a6e7678, DOC-d2b26a6e7678-C001, DOC-d2b26a6e7678-C001-R002) - > Both LIMIT (filter) and GROUP BY (aggregate) should be supported

### REQ-038: Performance/queueing: process reports in the background or via queuing, and support cancellation of scheduled/running reports with cancellation signals

**Priority:** Should

The system should provide background processing or queuing for report execution so that report generation does not slow down core clients. The system should allow users to cancel a report that is scheduled or already running, and during report processing it must check for cancellation signals so cancellation can take effect.

**Derived from:**
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R003) - > We need       background processing/queuing to prevent report generation from slowing       down the circulation client
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R033) - > Ability to cancel a report that has already been scheduled to run or is   currently running
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R046) - > The ability to cancel a scheduled or running report is technically feasible

### REQ-039: Platform and accessibility: operate on Linux or Solaris; support web and Windows client access; supported browsers; work with assistive technologies and comply with Section 508

**Priority:** Must

The system must operate on Linux or Solaris server environments. It must be accessible through a web browser or a Windows-compatible client, and if web-browser based it must support Microsoft Internet Explorer 6.0 or later and Mozilla Firefox 2.0 or later. The system must be accessible using assistive technologies such as screen readers and screen magnification software and must comply with Section 508 accessibility requirements.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R011) - > The system must operate on a Linux or Solaris server environment
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R012) - > The system must be accessible through a web browser or a Windows-compatible       client
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R013) - > If web-browser based, the system must be accessible through Microsoft       Internet Explorer (version 6.0 and later) and Mozilla Firefox (version       2.0 and later
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R014) - > The system must be accessible with screen-reading software, screen-       magnification software, and other assistive technology programs designed       to increase accessibility
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R004) - > So we need to support IE 6.0+ and Firefox 2.0
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R005) - > As a public institution, we MUST comply with Section 508 accessibility requirements
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R006) - > The system needs to work with:   - Screen readers like JAWS and NVDA   - Screen magnification software like ZoomText   - Other assistive technology programs

### REQ-040: Provide a material-volume report for a selected library at any point in time (historical), scoped to items at that library

**Priority:** Should

The system shall provide a material-volume report for a specified library that can show the library’s material volume at any point in time (not only current volume). The report results shall be scoped to items assigned to the selected library/location.

**Derived from:**
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R001) - > The system should provide the ability to report on the volume of material in a given library at any point in time
- `conversations/conv_pines014_material_volume.eml` (lines 1-113; DOC-f10d64601647, DOC-f10d64601647-C001, DOC-f10d64601647-C001-R002) - > Counts all items with a location = your library
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R020) - > Ability to report on the volume of material in a given library at any point in time, based on new acquisitions, items on the shelf, and items out in circulation

### REQ-041: Purge-candidate reports must be read-only; require confirmation before deletion; maintain purge audit trail

**Priority:** Must

Reports that identify purge candidates shall be read-only and must not carry out deletions themselves. The system must require a separate confirmation step before actual deletions of purge candidates. The system must maintain an audit trail for purges, including who purged what and when.

**Derived from:**
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R011) - > Reports show candidates for purging (read-only
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R012) - > A separate confirmation step for actual deletions
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R013) - > We need to track who purged what and when

### REQ-042: Purging support: identify purge candidates using customizable criteria (status, time-in-status, circulation activity, and combined conditions)

**Priority:** Should

The system should provide a utility and reports that identify item records as purge candidates according to user-customizable criteria. Criteria shall include using item status (including statuses such as missing, discard/weed, and damaged), time-based criteria (duration in a status, configurable in months/years), and circulation-activity criteria (how long ago an item last circulated, configurable in days/months/years). Users should be able to combine criteria so multiple conditions can be met.

**Derived from:**
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R001) - > identify item records to purge based on customizable criteria
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R002) - > Status-based criteria (missing, discard/weed, damaged
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R003) - > Time-based criteria (in status for X months/years
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R004) - > Activity-based criteria (last circulated X days/months/years ago
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R005) - > The system should let us combine criteria

### REQ-043: Query/reporting interface: provide a user-friendly query-design interface across record types with field/value/regex/Boolean selection

**Priority:** Should

The system should provide a user-friendly interface for designing queries across bibliographic, item, patron, transaction, and financial record types. The interface should allow staff to select query fields and values (including from picklists), select regular expressions from a menu, and use Boolean query operators.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R038) - > a user-friendly interface for designing queries against all record types (bibliographic, item, patron, transaction, financial
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R039) - > Select fields to query
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R040) - > Select values from a picklist of possible values
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R041) - > Select regular expressions from a drop-down menu
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R042) - > Use a full range of Boolean operators
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R002) - > Staff should be able to select fields to query
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R003) - > select    values from picklists
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R004) - > use regular expressions from a dropdown
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R005) - > use    Boolean operators

### REQ-044: Report execution must not constrain OPAC functionality or slow OPAC during report execution

**Priority:** Must

Management/reporting functionality must not constrain the functionality or features of the Online Public Access Catalog (OPAC). When a report is running, it must not slow down or otherwise constrain OPAC access/performance.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R019) - > These requirements must not constrain functionality or features of the       Online Public Access Catalog (OPAC) module
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R032) - > If a report is running, it should not slow down the OPAC
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R012) - > These requirements shall not constrain functionality or features of the       Online Public Access Catalog (OPAC) module
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R007) - > If a report is running, it should not slow down the OPAC

### REQ-045: Report interfaces must support historical as-of-date reporting and real-time where needed (high-level capability)

**Priority:** Should

The system should support both real-time and historical reporting capabilities, such that some reports can reflect current conditions (real-time/overdue today) and other reports can retrieve information as of a past date (historical snapshots).

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R035) - > Ability to have real time reporting
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R036) - > Ability to have historical reporting - a reporting warehouse such that data   can be acquired on a given date or date range
- `survey_results_2009.txt` (lines 1-143; DOC-aac7bceef7a8, DOC-aac7bceef7a8-C001, DOC-aac7bceef7a8-C001-R023) - > Historical reporting - I want to see what the data looked like on a     specific date in the past, even if the shelving location has changed
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R044) - > Some reports need to be real-time
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R045) - > Others are historical

### REQ-046: Report queue visibility: show queue position/status and allow prioritization of certain report types

**Priority:** Should

The system should provide visibility into report queue position/status (including waiting/running/completed/failed and how many reports are ahead). It should also allow selected reports to be prioritized so they move ahead of other queued reports.

**Derived from:**
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R022) - > How many reports are ahead of theirs
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R024) - > Status (waiting, running, completed, failed
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R025) - > A director's board report should be able to jump ahead of a staff member's ad-hoc query

### REQ-047: Report templates and three reporting interfaces (canned, noncanned/on-demand editable, and open-template)

**Priority:** Must

The reporting functionality must provide three reporting interfaces: canned reports that can be run ASAP or on a recurring basis; noncanned/on-demand reports with preset criteria that users can edit; and open-template reporting where users select attributes to filter and display. The system should also allow administrators to create report templates that staff can run, with staff able to run templates as-is or modify them within admin-configured limits without compromising accuracy.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R008) - > Three interfaces are needed
- `evergreen_reference_2009.txt` (lines 1-228; DOC-e6aa9f8c6308, DOC-e6aa9f8c6308-C001, DOC-e6aa9f8c6308-C001-R051) - > Three interfaces (canned, on-demand, open template
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R030) - > System administrators should be able to create report templates that are available to staff
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R031) - > These templates should be runnable as-is or modifiable for individual needs
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R032) - > Changes to templates should not compromise the accuracy of results
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R033) - > Administrators should be able to limit which filters and display fields can be altered, to certify a dependable output
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R009) - > Admins should be able to limit which filters and display    fields can be altered

### REQ-048: Reporting output and execution controls: support Excel/HTML/CSV output; scheduling; email delivery; include null/blank fields in results

**Priority:** Must

The system must provide report output in Excel, HTML, and CSV formats. It must support scheduled report execution. It should allow sending reports by email to specified email addresses. Report results must include all null and blank fields regardless of filtering/display selections.

**Derived from:**
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R043) - > Excel, HTML, and CSV formats are required
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R017) - > Ability to select Run ASAP, Hourly, Daily, Weekly, Monthly, Yearly
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R018) - > Excel, HTML, and CSV formats are required
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R019) - > Ability to enter email addresses for report to be sent to
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R020) - > All nulls and blank fields must be included in the results
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R043) - > Excel, HTML, and CSV formats are required

### REQ-049: Run shelf-space share reporting at both library and system scopes

**Priority:** Should

The shelf-space report shall be runnable/viewable at both the individual-library level and the system level.

**Derived from:**
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R004) - > The report should be able to run per library
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R010) - > The report should be available per library and per system

### REQ-050: Scalability: support consortium-scale operations (286 locations, 17M annual circulations, 900k+ items/year)

**Priority:** Must

The system must support a library consortium with 286 locations, 17 million annual circulations, and purchasing and processing over 900,000 items per year.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R009) - > The system must support a library consortium with 286 locations, 17 million       annual circulations, and purchasing/processing over 900,000 items per year
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R001) - > the system must support a library       consortium with 286 locations, 17 million annual circulations,       purchasing and processing over 900,000 items per year

### REQ-051: Security and staff login: support streamlined login (optional) and traditional username/password fallback; track authenticated staff member; determine permissions from security groups/roles

**Priority:** Must

The system must support streamlined staff login methods (such as card swipe), but streamlined login must remain optional (i.e., the system must not require it). The system must provide a traditional username-and-password login as a fallback. The system must identify which individual staff member is logged in (including when streamlined login is used) for auditability. Whenever a staff member logs in, the system should determine their permissions from their assigned security group or role.

**Derived from:**
- `email_staff_login.eml` (lines 1-98; DOC-64b10e94c425, DOC-64b10e94c425-C001, DOC-64b10e94c425-C001-R001) - > The system should support BOTH methods - streamlined login (e.g. card swipe) AND traditional login (individual login and password
- `email_staff_login.eml` (lines 1-98; DOC-64b10e94c425, DOC-64b10e94c425-C001, DOC-64b10e94c425-C001-R002) - > The system supports (but does not require) streamlined staff login methods
- `email_staff_login.eml` (lines 1-98; DOC-64b10e94c425, DOC-64b10e94c425-C001, DOC-64b10e94c425-C001-R003) - > The system must track WHICH staff member is logged in for audit purposes
- `email_staff_login.eml` (lines 1-98; DOC-64b10e94c425, DOC-64b10e94c425-C001, DOC-64b10e94c425-C001-R004) - > when a staff member logs in (by any method), their permissions should be determined by their assigned security group/role
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R011) - > The help system needs to work with screen readers

### REQ-052: Shelf-space/circulation/collection share report by genre and format, including shelf-space percentage estimation

**Priority:** Should

The shelf-space report shall show, for each genre and format, the percentage of total circulations attributable to that genre/format and the percentage of the collection represented by that genre/format. It shall also show the percentage of total shelf space occupied by that genre/format; since shelf space is not directly tracked, shelf-space percentage shall be estimated using available item attributes (e.g., item dimensions or item count as a proxy).

**Derived from:**
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R001) - > percentage of total circulations
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R002) - > percentage of the collection
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R003) - > Estimate shelf space per genre/format (this is the "percentage of shelf space

### REQ-053: Show query selections/criteria with report results; include report selection dates and report name

**Priority:** Should

When presenting report results, the system should also display the query selections/criteria used so users can see what generated the results. Report results should show the selected date criteria and report name so users can quickly identify the selected date range and report.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R013) - > provide the query selections along with the results, so users can see what criteria were used to generate the report
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R021) - > System provides query selections along with results
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R038) - > Report results would include the date selection criteria at the top or bottom   to quickly see date range selected along with the name of the report

### REQ-054: Standards-compliant HTML and accessible help plus high-level error reporting

**Priority:** Must

The system must produce standards-compliant HTML output (including semantics suitable for accessibility). It must provide an online hierarchical, cross-linked help system in HTML describing and illustrating all system functions, and the help system must work with screen readers. The system must provide thorough high-level error reporting and feedback.

**Derived from:**
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R002) - > all HTML output validates against W3C standards
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R016) - > The system must produce standards-compliant HTML output for web-based       components
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R024) - > an online, hierarchical, and cross-linked help       system in HTML that describes and illustrates all system functions
- `evergreen_reference_2009.txt` (lines 1-228; DOC-e6aa9f8c6308, DOC-e6aa9f8c6308-C001, DOC-e6aa9f8c6308-C001-R007) - > List of Items by Fines Stopped Reason (not available
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R007) - > If a report is running, it should not slow down the OPAC
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R025) - > The system must provide thorough high-level error reporting and feedback
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R007) - > The HTML output needs to be properly structured with alt tags, ARIA labels, and proper semantic HTML

### REQ-055: Support in-transit, missing/damaged, last-copy, and purge-related operational workflows as part of the reporting suite

**Priority:** Must

The system’s reporting suite must include operational reporting for in-transit items, missing/damaged items, last copies, and purge-candidate identification and conversion operations that support collection and inventory management workflows.

**Derived from:**
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R001) - > System provides reports of missing and damaged items per branch
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R004) - > items that have been in-transit for more than    X days (X configurable
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R007) - > I think we need both views
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R006) - > I need a report to help convert items from one status to another in batch

### REQ-056: Support output fields completeness: include null and blank fields in results

**Priority:** Must

The system must include null values and blank fields in report results, regardless of what fields are filtered or displayed.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R034) - > All nulls and blank fields must be included in the results no matter what is   being filtered or displayed
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R020) - > All nulls and blank fields must be included in the results
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R047) - > All nulls and blank fields must be included in the results

### REQ-057: Support searches and reports during open hours without disrupting other system functions

**Priority:** Could

The system should be able to process searches and reports during open hours without disrupting other system functions.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R010) - > highly desirable that searches and reports can be processed during       open hours without disrupting other system functions
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R002) - > It is highly       desirable that searches and reports can be processed during open hours       without disrupting other system functions

### REQ-058: Transfer execution: update selected items’ location/destination

**Priority:** Must

The transfer utility shall update the records of selected items to reflect their new location/destination.

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R005) - > Change records of selected items to new location
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R022) - > Change records of selected items to new location

### REQ-059: Transfer query workflow: query candidate materials, save queries for reuse, and manually select items from results

**Priority:** Must

The transfer utility shall allow users to query for candidate materials for transfer. Users shall be able to save queries so they can run them again for recurring transfer tasks. The workflow shall allow users to manually select which items from query results to include in the transfer (rather than transferring every candidate returned).

**Derived from:**
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R002) - > Query for candidate materials
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R003) - > Save queries for repeated use
- `conversations/conv_pines018_item_transfer.eml` (lines 1-179; DOC-a47eb1f11286, DOC-a47eb1f11286-C001, DOC-a47eb1f11286-C001-R004) - > Manually select titles from query results

## Discarded or conflicting candidates

### Show circulation percentage report (duplicative of shelf-space share requirement)

A requirement to show circulation percentage report by genre and format was treated as redundant because the consolidated shelf-space/circulation/collection share reporting already covers circulation percentage by genre and format.

**Disposition:** Duplicate/overlapping functionality with the accepted “shelf-space/circulation/collection share report by genre and format” requirement.

**Derived from:**
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R001) - > percentage of total circulations
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R023) - > For each genre and format of material, ability to compare

### Show collection percentage report (duplicative of shelf-space share requirement)

A requirement to show collection percentage report by genre and format was treated as redundant because the consolidated shelf-space/circulation/collection share reporting already covers collection percentage by genre and format.

**Disposition:** Duplicate/overlapping functionality with the accepted “shelf-space/circulation/collection share report by genre and format” requirement.

**Derived from:**
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R002) - > percentage of the collection
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R023) - > For each genre and format of material, ability to compare

### Show shelf-space percentage report (duplicative of shelf-space share requirement)

A requirement to show shelf-space percentage by genre and format was treated as redundant because the consolidated shelf-space/circulation/collection share reporting already covers shelf-space percentage by genre and format via estimation.

**Disposition:** Duplicate/overlapping functionality with the accepted “shelf-space/circulation/collection share report by genre and format” requirement.

**Derived from:**
- `conversations/conv_pines016_shelf_space.eml` (lines 1-119; DOC-b507e8abe1ba, DOC-b507e8abe1ba-C001, DOC-b507e8abe1ba-C001-R003) - > Estimate shelf space per genre/format (this is the "percentage of shelf space
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R023) - > For each genre and format of material, ability to compare

### Pivot-table output

An extracted requirement for pivot-table output was not included as a standalone accepted requirement because no controlling requirement established it as mandatory or prioritized above other reporting features within the accepted set.

**Disposition:** Not established as a controlling standalone requirement in the accepted set; treated as optional enhancement and therefore not accepted as a traceable requirement in this consolidation.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R032) - > Pivot table output

### Development/training environments with migration and protection from production risk (mis-cited evidence candidate)

A previously normalized requirement blended development/training environment details but incorrectly cited evidence unrelated to those environment constraints.

**Disposition:** Unsupported/misleading provenance: evidence cited does not support the stated environment-related behavior (per review findings).

**Derived from:**
- `evergreen_reference_2009.txt` (lines 1-228; DOC-e6aa9f8c6308, DOC-e6aa9f8c6308-C001, DOC-e6aa9f8c6308-C001-R004) - > Circulation Count by Circ Location broken down by Patron County (not available

### Web output and help must be standards-compliant and accessible (incorrect provenance candidate)

A previously normalized requirement combined web standards/accessibility/help/error-feedback but referenced purge-candidate read-only behavior as one of its sources.

**Disposition:** Direct provenance defect: referenced source candidate does not support HTML standards/accessibility/help/error-feedback (per review findings).

**Derived from:**
- `conversations/conv_pines021_item_purging.eml` (lines 1-149; DOC-74ccbb6ac771, DOC-74ccbb6ac771-C001, DOC-74ccbb6ac771-C001-R011) - > Reports show candidates for purging (read-only

### Report output formats, scheduling, delivery, and inclusion of null/blank fields (bundled Must evidence mixed with unrelated login candidate)

A previously normalized requirement bundled output/scheduling/email/null-field inclusion with an unrelated staff login requirement used as evidence.

**Disposition:** Direct provenance defect for at least one clause: login evidence does not support report output/scheduling/delivery/null-field behavior (per review findings).

**Derived from:**
- `email_staff_login.eml` (lines 1-98; DOC-64b10e94c425, DOC-64b10e94c425-C001, DOC-64b10e94c425-C001-R002) - > The system supports (but does not require) streamlined staff login methods

### Transaction archive privacy/anonymization and retention policies (included accounting compliance candidate as privacy evidence)

A previously normalized requirement bundled privacy/anonymization and retention policies but included an accounting/auditing compliance candidate as evidence for those privacy behaviors.

**Disposition:** Direct clause-level provenance defect: the cited candidate does not support transaction privacy/anonymization/retention (per review findings).

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R053) - > All reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements

### Report generation during open hours without disrupting other system functions / background queue performance (priority inconsistency candidate set)

A previously normalized set treated open-hours disruption behavior and background queue behavior as separate but inconsistently prioritized, losing the strongest source priority for each behavior.

**Disposition:** Priority normalization inconsistency: combined or compared Must vs Should evidence without preserving controlling priority boundaries (per review findings).

**Derived from:**
- `interview_sysadmin_2009-05-10.txt` (lines 1-123; DOC-b1738fd7a6de, DOC-b1738fd7a6de-C001, DOC-b1738fd7a6de-C001-R003) - > searches and reports can be processed during open hours without disrupting other system functions
- `meeting_minutes/meeting_2009-07-20_minutes.txt` (lines 1-219; DOC-5ab1dd8bc97a, DOC-5ab1dd8bc97a-C001, DOC-5ab1dd8bc97a-C001-R003) - > We need       background processing/queuing to prevent report generation from slowing       down the circulation client

### In-transit report combine transit-to and transit-from (duplicative candidate)

Candidate describing combining transit directions was treated as redundant given the accepted in-transit combined-transit requirement.

**Disposition:** Duplicate/overlapping functionality with accepted combined in-transit requirement.

**Derived from:**
- `conversations/conv_pines019_020_missing_intransit.eml` (lines 1-126; DOC-b233b12122ca, DOC-b233b12122ca-C001, DOC-b233b12122ca-C001-R006) - > report merges    transit-to and transit-from into one report
- `early_draft_srs_galecia.txt` (lines 246-531; DOC-091180de9b2d, DOC-091180de9b2d-C002, DOC-091180de9b2d-C002-R036) - > The report should merge the transit-to and transit-from into one report for ease of front-line staff use

### Restrict editable template options (duplicative candidate)

A candidate about restricting editable template options was treated as redundant with the accepted admin-configured template modification limits requirement.

**Disposition:** Duplicate/overlapping with accepted template modification within admin-configured limits.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 1-265; DOC-091180de9b2d, DOC-091180de9b2d-C001, DOC-091180de9b2d-C001-R033) - > Administrators should be able to limit which filters and display fields can be altered, to certify a dependable output
- `email_report_features.eml` (lines 1-128; DOC-d9e168e0c039, DOC-d9e168e0c039-C001, DOC-d9e168e0c039-C001-R009) - > Admins should be able to limit which filters and display    fields can be altered

### Pivot Table Output (survey/early draft overlap omission)

Candidate pivot-table output was not carried as accepted due to insufficient controlling requirement evidence in this consolidation.

**Disposition:** Not promoted to accepted requirement; treated as optional enhancement.

**Derived from:**
- `evergreen_reference_2009.txt` (lines 1-228; DOC-e6aa9f8c6308, DOC-e6aa9f8c6308-C001, DOC-e6aa9f8c6308-C001-R032) - > No pivot table output

### Canned, on-demand, and open-template reporting interfaces (duplicate across evidence sets)

An extracted reporting interface candidate was treated as redundant because the consolidated “Report templates and three reporting interfaces” requirement already covers the three-interface behavior.

**Disposition:** Duplicate/overlapping with accepted three reporting interfaces requirement.

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R008) - > Three interfaces are needed
- `evergreen_reference_2009.txt` (lines 1-228; DOC-e6aa9f8c6308, DOC-e6aa9f8c6308-C001, DOC-e6aa9f8c6308-C001-R051) - > Three interfaces (canned, on-demand, open template

### Filter surveys by name (not accepted separately)

An extracted candidate required filtering by survey name rather than survey ID.

**Disposition:** Omitted from accepted set because no accepted consolidated requirement established it as a traceable controlling behavior for the scope of this consolidation (traceability coverage omission per review findings, but not accepted here).

**Derived from:**
- `early_draft_srs_galecia.txt` (lines 511-678; DOC-091180de9b2d, DOC-091180de9b2d-C003, DOC-091180de9b2d-C003-R039) - > Ability to select the survey name and not have to enter the survey id for   filtering
- `meeting_tech_subcommittee_2009-06-30.txt` (lines 1-198; DOC-e081aa7bd57b, DOC-e081aa7bd57b-C001, DOC-e081aa7bd57b-C001-R021) - > filter by survey name rather than survey ID requires the system to resolve names to IDs internally

### Avoid duplicate rows in Excel exports

An extracted usability/export quality candidate stated Excel exports should not contain excessive duplicate rows.

**Disposition:** Not accepted as a controlling standalone requirement within this consolidation because it does not establish a clear mandatory behavior independent of broader output/format requirements.

**Derived from:**
- `survey_results_2009.txt` (lines 1-143; DOC-aac7bceef7a8, DOC-aac7bceef7a8-C001, DOC-aac7bceef7a8-C001-R033) - > I need to export to Excel but the data has too many duplicate rows

### Make reports easy to locate

An extracted usability candidate requested improved discoverability/navigation for reports.

**Disposition:** Not accepted as a controlling standalone requirement in this consolidation; treated as a generic UX improvement without an independently specified acceptance criterion beyond discoverability.

**Derived from:**
- `survey_results_2009.txt` (lines 1-143; DOC-aac7bceef7a8, DOC-aac7bceef7a8-C001, DOC-aac7bceef7a8-C001-R036) - > The interface is confusing - I can't find the reports I need

## Extraction gaps

_No extraction evidence gaps were reported._

## Review status

Not fully approved; the bounded review loop ended with findings. Unresolved findings are recorded below.

### Unresolved findings

- **High - Standards-compliant HTML and accessible help plus high-level error reporting:** The requirement cites DOC-e6aa9f8c6308-C001-R007, which concerns items grouped by fines-stopped reason and provides no evidence for HTML standards, accessibility, help, or error reporting. This is a direct provenance defect. **Recommended action:** Remove the unrelated source citation and retain only candidates that support the stated clauses, such as DOC-091180de9b2d-C001-R016/R024/R025, DOC-e081aa7bd57b-C001-R002/R007, and DOC-b1738fd7a6de-C001-R007.
- **High - Batch transfer utility between branches (including temporary/program transfers and moving items to a new location), (Should) Support automatic reversion of transfers after time-based and non-time criteria (including event/program):** The batch-transfer requirement cites DOC-a47eb1f11286-C001-R025, but that candidate is specifically about reverting items after a specified period, not about transferring batches or temporary/program transfers. The reversion requirement also mixes a source marked Must (R025) into a consolidated requirement marked Should, losing priority evidence. **Recommended action:** Remove R025 from the batch-transfer requirement. Use R017 for batch transfers and R027 for event/program transfers. Separately decide whether the time-based reversion behavior remains Must, and preserve that priority rather than downgrading it without an explicit decision.
- **High - Report execution must not constrain OPAC functionality or slow OPAC during report execution, Support searches and reports during open hours without disrupting other system functions:** The first requirement correctly treats OPAC protection as Must, but the second covers substantially the same non-disruption behavior and is marked Could even though source candidates include Must-level evidence (DOC-b1738fd7a6de-C001-R003 and DOC-5ab1dd8bc97a-C001-R003). The result is an inconsistent priority model for materially overlapping behavior. **Recommended action:** Merge the overlapping performance/non-disruption requirements or define their boundaries. Preserve the strongest applicable priority for the shared behavior and specify measurable acceptance criteria, such as permitted OPAC latency impact and report concurrency conditions.
- **High - Reporting output and execution controls: support Excel/HTML/CSV output; scheduling; email delivery; include null/blank fields in results, (Supplemental) Email and accessibility-ready reporting outputs (as required by platform-level constraints):** The supplemental requirement claims email delivery, but its cited sources only support HTML standards/accessibility and report output formats; they do not support email delivery. The output requirement also cites DOC-e081aa7bd57b-C001-R043 twice, indicating weak source normalization. In addition, the two requirements substantially overlap on output and accessibility concerns. **Recommended action:** Remove the email clause or add the actual email-delivery candidates (for example DOC-091180de9b2d-C003-R019 and DOC-e6aa9f8c6308-C001-R036). Deduplicate the repeated source citation and merge or clearly separate the output-format, email, and accessibility requirements.
- **High - Database and data model constraints: use a fully relational database backend and provide complete data specifications and documentation of major processes, Performance/queueing: process reports in the background or via queuing, and support cancellation of scheduled/running reports with cancellation signals:** The sources contain Must requirements to separate reporting from production operations or use a separate reporting database/replica (DOC-e6aa9f8c6308-C001-R043 and R060), while another source expresses a preference for keeping reporting in the main relational database (DOC-b1738fd7a6de-C001-R010). The accepted requirements omit the separate-reporting-architecture requirement and do not resolve this direct architectural tension. **Recommended action:** Add an explicit architecture decision: either require a separate reporting database/replica, permit either a replica or background queue subject to measurable performance limits, or reject the separate-replica requirement with documented rationale. Ensure the relational-database requirement does not imply that reporting must run on production.
- **High - Appendix A report families: support circulation report types and item report types as defined, Support in-transit, missing/damaged, last-copy, and purge-related operational workflows as part of the reporting suite:** A Must source candidate explicitly requires support for Appendix B fine-grained reports (DOC-091180de9b2d-C002-R016), but no accepted requirement cites or describes Appendix B. The Appendix A requirement also summarizes only circulation and item report families, while source candidates contain additional bibliographic, patron, holds, in-house-use, transit, and bills report families whose detailed coverage is not demonstrably preserved. **Recommended action:** Add a traceable Must requirement for Appendix B and enumerate or explicitly reference its report definitions. Map every Appendix A/C003 report family to an accepted requirement or document which source statements were intentionally excluded.
- **Medium - (Should) Provide a last-copy report with library and system scope and flag last copies within the selected scope:** The requirement name says “(Should)” while the priority field is Must. Similar name/priority mismatches occur where consolidated requirements include source candidates with different priorities. This makes the governing priority ambiguous for implementation and review. **Recommended action:** Make the name and priority consistent, preferably by removing priority labels from names and retaining a single authoritative priority field. Reconcile the source priorities explicitly when combining candidates.
- **Medium - Support output fields completeness: include null and blank fields in results, Combine patron filters with AND/OR; include null patron values in results; support configurable age ranges and compute age range from birth date at query time:** The general null/blank-field requirement and the patron-specific null-value behavior overlap but use different scope and wording. It is unclear whether the general rule applies to filtered-out records, displayed fields, optional patron attributes, or all result rows. This can produce conflicting interpretations. **Recommended action:** Define one authoritative null/blank semantics requirement, stating whether null-valued records remain in result sets and how nulls are rendered for filtered versus displayed fields. Reference the patron-specific behavior as a scoped application of that rule.
- **Medium - Provide hierarchical online help and context/administrative query-specific feedback, Standards-compliant HTML and accessible help plus high-level error reporting, (Supplemental) Email and accessibility-ready reporting outputs (as required by platform-level constraints):** Help, HTML accessibility, and error feedback are repeated across three accepted requirements, with overlapping obligations and different source sets. This is not merely stylistic duplication: a future change could update one requirement while leaving contradictory or incomplete copies elsewhere. **Recommended action:** Consolidate help and accessibility obligations into one requirement, keep high-level and query-specific error feedback separate if their audiences differ, and reference the consolidated accessibility requirement from report-output requirements rather than repeating it.
- **Medium - Filter surveys by name (not accepted separately), Support Appendix A report families: support circulation report types and item report types as defined:** Filtering by survey name is supported by multiple source candidates, including a technical-subcommittee candidate, but was discarded without a substantive scope rationale. It is an actionable, testable query capability and is not covered by the accepted query-interface requirement, which does not mention survey-name resolution. **Recommended action:** Either add a requirement requiring survey-name selection with internal name-to-ID resolution, or document an explicit scope decision that survey reporting is excluded. Do not discard it solely because it lacks controlling evidence; the source evidence is repeated and actionable.
