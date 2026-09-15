# Odoo overdue-invoice dunning with an audit trail

A weekday schedule reads posted customer invoices with an outstanding balance, assigns a gentle/firm/final escalation stage from days overdue, and creates a tagged `mail.activity` in Odoo only when that invoice/stage has not already been recorded.

## Setup

1. Import `workflow.json` into n8n 2.38.7 or newer and attach an Odoo API-key credential.
2. Confirm the Accounting and Activities models are installed.
3. Replace the documented `res_model_id` placeholder with the `ir.model` ID for `account.move` in your database. This value is database-specific, so publishing a guessed value would be unsafe.
4. Review the 3/14/30-day policy in **Compute escalation stage**.
5. Run against a staging database and inspect the created activities before activating the schedule.

The sample intentionally creates internal follow-up activities rather than emailing customers automatically. A human can review wording, local collection rules, and disputed invoices first. No credentials, customer records, or affiliate links are included.
