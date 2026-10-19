# Process Flows Document

**Project Name:** Addis TradeLink – Import-Export & Trading Company ERP  
**Version:** 1.0  
**Odoo Version:** Community Edition 17 / 18  
**Related Documents:** 01_Business_Requirements.md , 02_Functional_Requirements.md

---

## 1. Introduction

This document describes the main business processes that the system must support.  
Each process is written in clear numbered steps so that both business users and developers can understand the flow.

---

## 2. Process 1: Import Purchase Process (Foreign Supplier)

**Goal:** Buy goods from a foreign supplier and bring them to the Addis Ababa warehouse.

### Happy Path (Normal Flow)

1. Purchase Manager creates a **Request for Quotation (RFQ)** for a foreign supplier.
2. Supplier sends prices and conditions.
3. Purchase Manager reviews the prices and converts the RFQ into a **Purchase Order**.
4. Purchase Manager fills extra import information:
   - Bill of Lading Number
   - Container Number
   - Customs Declaration Number
   - Expected Arrival Date
5. Purchase Order is confirmed.
6. Company makes payment to the supplier (full or partial / advance).
7. Goods are shipped from the foreign country.
8. Goods arrive at Djibouti Port and are cleared by customs.
9. Goods are transported by truck from Djibouti to Addis Ababa.
10. Warehouse Keeper creates a **Receipt** (Incoming Shipment) against the Purchase Order.
11. Warehouse Keeper validates the Receipt (goods enter the warehouse).
12. Purchase Manager creates a **Landed Cost** document and adds all extra costs:
    - Ocean Freight
    - Insurance
    - Customs Duty
    - Inland Transport (Djibouti → Addis)
    - Port Charges
    - Bank Charges
13. Landed Cost is validated → Product costs are automatically updated.
14. Accountant creates **Vendor Bill** from the Purchase Order.
15. Accountant registers the supplier payment.

### Alternative / Exception Flows
- Partial receipt (some products arrive later)
- Price difference between Purchase Order and actual Vendor Bill
- Damaged or missing goods during transport
- Additional unexpected costs after arrival

---

## 3. Process 2: Landed Cost Process (Detail)

**Goal:** Calculate the true cost of imported products.

1. After goods are received, go to Inventory → Landed Costs.
2. Create new Landed Cost.
3. Select the Incoming Shipment(s) that just arrived.
4. Add cost lines (Freight, Duty, Transport, etc.).
5. Choose distribution method (usually By Quantity or By Current Cost).
6. Click “Compute” to see how costs are distributed to each product.
7. Validate the Landed Cost.
8. System automatically updates the cost price of the products.

---

## 4. Process 3: Local Sales Process

**Goal:** Sell goods from the Addis warehouse to local customers.

### Happy Path

1. Salesperson creates a **Quotation** for a local customer.
2. Customer accepts the quotation (by phone, email, or in person).
3. Salesperson confirms the Quotation → it becomes a **Sales Order**.
4. System automatically checks the customer’s **Credit Limit**.
5. If credit limit is OK → Sales Order is confirmed.
6. System creates a **Delivery Order**.
7. Warehouse Keeper prepares the goods and validates the Delivery.
8. Stock quantity is reduced automatically.
9. Salesperson or Accountant creates the **Customer Invoice**.
10. Customer makes payment (cash, bank transfer, cheque, etc.).
11. Accountant registers the payment against the invoice.
12. If the invoice is fully paid, it is marked as Paid.

### Credit Limit Exception
- If the new Sales Order will exceed the customer’s credit limit:
  - System blocks confirmation (or shows a strong warning).
  - Salesperson must ask for approval from Sales Manager or General Manager.
  - Only authorized users can override the credit limit.

### Other Exceptions
- Partial delivery
- Customer returns goods
- Price change after quotation
- Customer requests extra discount

---

## 5. Process 4: Customer Credit Control Process

1. Accountant or Sales Manager sets a Credit Limit on the customer form.
2. Every time a Sales Order is confirmed, the system calculates:
   - Current Outstanding Amount (unpaid invoices)
   - + Amount of the new Sales Order
3. If Total > Credit Limit → System blocks or warns.
4. Management can see Aged Receivable report at any time.
5. Follow-up actions (call customer, send statement, stop new sales) are taken manually.

---

## 6. Process 5: Stock Adjustment & Internal Transfer

**When to use:**
- Stock counting difference
- Damaged goods
- Moving goods between locations

**Steps:**
1. Warehouse Keeper creates Inventory Adjustment or Internal Transfer.
2. Selects products and quantities.
3. Validates the operation.
4. Stock quantities are updated.
5. Accounting entries are created automatically (if configured).

---

## 7. Process 6: Basic Financial Closing (Monthly)

1. Accountant checks all Vendor Bills and Customer Invoices are created.
2. Registers all bank and cash payments.
3. Performs Bank Reconciliation.
4. Reviews Aged Receivable and Aged Payable.
5. Generates Profit & Loss and Balance Sheet.
6. Management reviews the reports.

---

## 8. Summary of Main Document Flow
