# Business Requirements Document (BRD)

**Project Name:** Addis TradeLink – Import-Export & Trading Company ERP  
**Version:** 1.0  
**Date:** October 2026  
**Odoo Version:** Community Edition 17 / 18  
**Prepared by:** [Your Name]  
**Purpose:** Portfolio project for Ethiopian ERP companies (ITA, Top Technology, etc.)

---

## 1. Project Overview

### 1.1 Purpose
The purpose of this project is to design and develop a complete Import-Export Trading management system using **Odoo Community Edition**. The system will help medium-sized trading companies in Addis Ababa manage their full business cycle — from foreign purchasing to local sales — in a modern, controlled, and transparent way.

### 1.2 Background
Most trading companies in Addis Ababa still use Excel sheets and paper documents to manage:
- Foreign purchases
- Customs and transport costs
- Warehouse stock
- Customer credit sales
- Financial reports

This creates many problems such as stock errors, wrong product costing, unpaid customer invoices, and lack of real-time information. This project aims to solve these problems using Odoo.

---

## 2. Company Profile (Fictional but Realistic)

**Company Name:** EthioLink Trading PLC  
**Legal Form:** Private Limited Company  
**Location:** Bole Sub-city, Addis Ababa, Ethiopia  
**Year Established:** 2018  
**Number of Employees:** 12  
**Main Business Activity:** Import and distribution of goods

### Main Product Categories:
- Construction Materials (Cement, Steel Bars, Tiles, Paints, Sanitary items)
- Electronics (Televisions, Mobile Phones, Laptops, Accessories)
- Fast Moving Consumer Goods (Cooking Oil, Rice, Pasta, Sugar, Canned food)

### Business Model:
- Import goods mainly from China, United Arab Emirates, Turkey, and India
- Goods arrive through Djibouti Port
- Stored in warehouse in Addis Ababa
- Sold to wholesalers, retailers, construction companies, and projects across Ethiopia

### Currencies Used:
- Ethiopian Birr (ETB) – Main currency
- US Dollar (USD)
- Euro (EUR)
- Chinese Yuan (CNY)

---

## 3. Current Problems (As-Is Situation)

| No. | Problem | Impact on Business |
|-----|--------|--------------------|
| 1 | Stock information is not accurate | Sales of non-existing products, overstocking |
| 2 | Real cost of imported goods is not clear | Wrong selling price and wrong profit calculation |
| 3 | Customer credit is not controlled | High amount of unpaid invoices (bad debts) |
| 4 | Heavy dependence on Excel and paper | Data loss, duplication, and human error |
| 5 | Multi-currency transactions are confusing | Accounting mistakes |
| 6 | No real-time reports for management | Slow and poor decision making |
| 7 | Difficult to track one shipment from start to end | Lack of transparency |

---

## 4. Project Goals (To-Be Situation)

1. Provide real-time and accurate stock information
2. Automatically calculate the true cost of imported products (Landed Cost)
3. Control customer credit limits strictly
4. Reduce use of Excel and paper documents
5. Support multi-currency purchasing and accounting
6. Give management clear and fast reports (stock, sales, profit, receivables)
7. Create full traceability from Purchase Order to Customer Payment

---

## 5. Scope of the Project

### 5.1 In Scope
- Purchase Management (Foreign suppliers)
- Landed Cost Management
- Inventory / Warehouse Management
- Sales Management
- Customer Credit Limit Control
- Basic Accounting and Financial Reports
- Multi-currency support
- Document attachment (Bill of Lading, Commercial Invoice, etc.)

### 5.2 Out of Scope
- Manufacturing
- Website / E-commerce
- Human Resources & Payroll
- Advanced Budgeting
- Mobile Application
- Point of Sale (POS)

---

## 6. Stakeholders

| Role | Responsibility |
|------|----------------|
| General Manager / Owner | Final decisions, views reports |
| Purchase Manager | Handles foreign suppliers and import process |
| Sales Manager | Handles local customers and sales |
| Warehouse Keeper | Receives and issues goods |
| Accountant | Handles invoices, payments, and reports |
| System Administrator | Manages Odoo system |

---

## 7. Success Criteria

The project will be considered successful when:
- Full import cycle (Purchase → Landed Cost → Receipt) works correctly
- Full sales cycle (Quotation → Delivery → Invoice → Payment) works correctly
- Credit limit blocks sales when exceeded
- Product cost is updated correctly after Landed Cost
- Management can see stock and receivable reports in real time
- The system can be demonstrated clearly in a 5–8 minute video

---

## 8. Assumptions and Constraints

**Assumptions:**
- Users have basic computer knowledge
- Internet connection is available
- Company will use Ethiopian Birr as main currency

**Constraints:**
- Only Odoo Community Edition will be used (no Enterprise features)
- Development must be completed as a portfolio project
- Customization should remain simple and clean

---

**End of Business Requirements Document**