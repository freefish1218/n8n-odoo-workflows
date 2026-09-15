# Idempotent Odoo sales-order upsert

A webhook accepts a paid order, validates the payload, resolves or creates the customer, and upserts a draft `sale.order` using `client_order_ref` as the idempotency key. Existing records are updated rather than duplicated, and the response contains an audit identifier.

## Setup

1. Import `workflow.json` into n8n 2.38.7 or newer.
2. Create one Odoo API-key credential and attach it to every Odoo node. Odoo external API access requires a Custom plan.
3. Confirm your Odoo database exposes `res.partner` and `sale.order`.
4. Map product SKUs to `sale.order.line` for your own catalog before production; the public sample deliberately creates only the order header.
5. Post a staging payload containing `external_id`, `customer_email`, `total`, and optional currency/date fields.

The workflow contains no endpoint, credential, customer data, or affiliate link. Test it against an Odoo staging database before enabling it.
