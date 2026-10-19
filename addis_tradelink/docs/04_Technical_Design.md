# Technical Design Document

**Project Name:** Addis TradeLink – Import-Export & Trading Company ERP  
**Version:** 1.0  
**Odoo Version:** Community Edition 17 / 18  
**Related Documents:** 01_BRD, 02_FRD, 03_Process_Flows

---

## 1. Technology Stack

- **Odoo Version:** Community 17 or 18
- **Edition:** Community only (no Enterprise features)
- **Database:** PostgreSQL
- **Language:** Python 3.10+
- **Frontend:** Odoo standard views (XML) + QWeb reports
- **Version Control:** Git + GitHub

---

## 2. Standard Odoo Modules to Install

Install these modules first (in this order):

1. Contacts
2. Sales Management (`sale_management`)
3. Purchase (`purchase`)
4. Inventory (`stock`)
5. Invoicing / Accounting (`account`)
6. Landed Costs (included in Inventory / Account)

Optional but useful:
- Discuss (for internal communication)
- Document Management (attachments)

---

## 3. Custom Module Design

**Module Technical Name:** `addis_tradelink`  
**Module Display Name:** Addis TradeLink – Import Export Extensions

### 3.1 Module Structure

```text
custom_addons/
└── addis_tradelink/
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    │   ├── __init__.py
    │   ├── purchase_order.py
    │   └── res_partner.py
    ├── views/
    │   ├── purchase_order_views.xml
    │   └── res_partner_views.xml
    ├── security/
    │   └── ir.model.access.csv
    ├── report/
    │   └── (optional custom reports later)
    └── static/
        └── description/
            └── icon.png