# n8n + Odoo: three production-minded workflow patterns

**Review page:** https://mybots.vip/workflows/ · **Source:** https://github.com/freefish1218/n8n-odoo-workflows

These workflows come from practical AI-agent and Odoo ERP delivery work for small and midsize businesses. They focus on the failure modes that matter in real projects: duplicate writes, weak validation, silent collection automation, and missing audit trails.

| Workflow | Odoo models | Production concern addressed |
|---|---|---|
| [Sales-order upsert](workflows/01-sales-order-upsert/) | `res.partner`, `sale.order` | External idempotency key; create/update split; audit response |
| [Invoice dunning audit](workflows/02-invoice-dunning-audit/) | `account.move`, `mail.activity` | Staged escalation; duplicate-activity guard; human review before customer email |
| [CRM lead upsert](workflows/03-crm-lead-upsert/) | `res.partner`, `crm.lead` | Input validation; contact and opportunity deduplication |

## What was verified

- JSON structure and graph references are checked by `validate.py`.
- All three files are imported with the n8n 2.38.7 CLI before release.
- The node configuration follows n8n's built-in Odoo v2 implementation (`n8n-nodes-base.odoo`).
- There are no credentials, client names, private endpoints, analytics, or affiliate links.

A live Odoo execution is intentionally not claimed here: each Odoo database can have different installed modules, custom fields, record rules, and model IDs. Use a staging database, attach your own API-key credential, and follow each workflow's setup notes. Odoo external API access requires a Custom plan.

## Maintainer context

MyBots is operated by the founder of a China-based AI and Odoo consultancy. The work combines ERP implementation, automation design, and AI-agent delivery. We are publishing a small set of reviewable workflows first and will improve them from import and user feedback.

## License

MIT. No affiliate link is present. If an n8n affiliate application is approved later, any referral link added in the future will be clearly disclosed.
