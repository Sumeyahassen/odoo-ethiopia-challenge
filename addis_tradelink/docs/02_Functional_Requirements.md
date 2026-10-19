# Functional Requirements Document (FRD)

**Project Name:** Addis TradeLink – Import-Export & Trading Company ERP  
**Version:** 1.0  
**Odoo Version:** Community Edition 17 / 18  
**Related Document:** 01_Business_Requirements.md

---

## 1. Introduction

This document describes all the functional requirements of the Addis TradeLink system. It explains **what** the system must do (not how it will be coded).

---

## 2. Master Data Requirements

### 2.1 Company Setup
- System must allow setting company name, logo, address (Addis Ababa), phone, email, and website
- Main currency must be Ethiopian Birr (ETB)
- System must support multiple currencies (USD, EUR, CNY)

### 2.2 Chart of Accounts
- System must have a suitable Chart of Accounts for a trading company in Ethiopia
- Main account types needed: Assets, Liabilities, Equity, Income, Expenses

### 2.3 Taxes
- System must support VAT 15%
- System must support Withholding Tax
- Taxes must be automatically calculated on vendor bills and customer invoices

### 2.4 Products
- System must allow creation of products with:
  - Product Name
  - Internal Reference (SKU)
  - Product Category
  - Unit of Measure
  - Purchase Cost
  - Sales Price
  - Can be Purchased / Can be Sold
- System should support product variants if needed (optional)

### 2.5 Partners (Customers & Suppliers)
- System must manage both Customers and Suppliers
- Foreign suppliers must support different currencies
- Local customers must support credit limit
- Full address, phone, email, and Tax ID (TIN) must be recorded

### 2.6 Payment Terms
- System must support common payment terms:
  - Immediate Payment
  - 15 Days
  - 30 Days
  - 45 Days

### 2.7 Warehouses and Locations
- System must support at least one main warehouse in Addis Ababa
- System should allow multiple locations (Storage, Input, Output, Quality Control)

---

## 3. Purchase Management Requirements

### 3.1 Request for Quotation (RFQ)
- User must be able to create RFQ for foreign suppliers
- RFQ must support multi-currency
- User must be able to send RFQ by email (optional)

### 3.2 Purchase Order
- User must be able to convert RFQ to Purchase Order
- Purchase Order must show currency, payment terms, and expected arrival date
- User must be able to attach documents (Commercial Invoice, Packing List, Bill of Lading)

### 3.3 Special Fields for Import (Custom)
- Purchase Order should have extra fields:
  - Bill of Lading Number
  - Container Number
  - Customs Declaration Number
  - Port of Loading
  - Port of Discharge
  - Expected Arrival Date in Addis

### 3.4 Vendor Bills and Payments
- System must allow creation of Vendor Bills from Purchase Order
- System must support partial payments and advance payments
- System must support multi-currency payments

---

## 4. Landed Cost Requirements (Critical)

### 4.1 Landed Cost Creation
- User must be able to create Landed Cost document linked to one or more receipts
- User must be able to add extra costs such as:
  - Ocean Freight
  - Marine Insurance
  - Customs Duty
  - Inland Transport (Djibouti to Addis)
  - Port Handling Charges
  - Bank Charges
  - Other miscellaneous costs

### 4.2 Cost Distribution
- System must distribute the extra costs to products automatically
- Distribution methods supported: By quantity, By current cost, By weight, By volume
- After validation, product cost must be updated correctly

---

## 5. Inventory Management Requirements

### 5.1 Receiving Goods
- User must be able to receive products against Purchase Order
- System must support partial receipt
- User should be able to record Quality Control notes (optional)

### 5.2 Stock Operations
- System must support:
  - Internal Transfers
  - Stock Adjustments
  - Scrap
- Real-time stock quantity must be visible

### 5.3 Reordering
- System must allow setting minimum and maximum stock levels
- System should generate reordering suggestions

### 5.4 Inventory Reports
- System must provide:
  - Stock on Hand
  - Product Moves
  - Inventory Valuation
  - Aged Stock (optional)

---

## 6. Sales Management Requirements

### 6.1 Customer Quotation
- User must be able to create professional quotations
- Quotation must show product, quantity, price, tax, and total

### 6.2 Sales Order
- User must be able to confirm quotation into Sales Order
- System must check customer credit limit before confirmation
- If credit limit is exceeded, system must block or warn the user

### 6.3 Delivery
- System must create Delivery Order from Sales Order
- User must validate delivery (partial delivery allowed)
- Stock must be reduced automatically

### 6.4 Customer Invoice and Payment
- System must create invoice from Sales Order or Delivery
- System must support partial payments
- System must show outstanding balance of each customer

### 6.5 Credit Limit Control
- Each customer must have a Credit Limit field
- System must prevent confirming Sales Order if outstanding amount + new order exceeds the limit
- Authorized users should be able to override (optional)

---

## 7. Accounting Requirements

### 7.1 Automatic Accounting
- Every Purchase, Sales, Inventory, and Payment transaction must create correct journal entries automatically

### 7.2 Multi-currency Accounting
- System must handle exchange rate differences correctly

### 7.3 Financial Reports
- System must provide:
  - Profit and Loss
  - Balance Sheet
  - Partner Ledger
  - Aged Receivable
  - Aged Payable
  - Tax Report

---

## 8. Reporting and Dashboard Requirements

- Management must be able to see:
  - Current Stock Value
  - Total Outstanding Customer Receivables
  - Total Outstanding Supplier Payables
  - Sales performance (daily, monthly)
  - Purchase performance

---

## 9. Security and Access Rights

| User Role              | Access Level                          |
|------------------------|---------------------------------------|
| General Manager        | Full access + Reports                 |
| Purchase Manager       | Purchase, Inventory (read), Accounting (limited) |
| Sales Manager          | Sales, Inventory (read), Accounting (limited) |
| Warehouse Keeper       | Inventory only                        |
| Accountant             | Accounting + Invoicing                |
| System Administrator   | Full technical access                 |

---

## 10. Non-Functional Requirements

- System must be fast enough for daily use
- All important documents must be printable in PDF
- System must allow attaching files (PDF, images)
- Data must be secure and backed up regularly
- Interface should be clean and easy to learn

---

**End of Functional Requirements Document**