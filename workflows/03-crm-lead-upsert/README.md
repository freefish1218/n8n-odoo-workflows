# Odoo CRM lead intake with deduplicated upsert

A webhook validates and normalizes a lead before any write, finds or creates the contact by email, then finds or creates a CRM opportunity. Repeat submissions enrich the existing opportunity instead of opening duplicates.

## Setup

1. Import `workflow.json` into n8n 2.38.7 or newer.
2. Attach an Odoo API-key credential to all Odoo nodes.
3. Confirm CRM is installed and the integration user can read/write `res.partner` and `crm.lead`.
4. Review field names against custom modules in your database.
5. Send a staging webhook with `name`, `email`, and optional `phone`, `company`, `need`, and `source`. Submit the same email twice to verify deduplication.

The sample rejects malformed email before Odoo writes and contains no credential, real lead, or affiliate link. Add consent and retention controls required by your market before connecting a public form.
