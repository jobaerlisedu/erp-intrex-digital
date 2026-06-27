# System Modules & Sections Reference

This runbook catalog provides system administrators with an overview of all functional modules and sections present in the Intrex ERP/CRM platform. It outlines the interface navigation structure and corresponding access control scopes.

---

## Access Scopes & Modules Catalog

Each module requires specific user permissions, typically controlled by the group names mapping to `{module_name}_access` or administrative status flags (`is_staff` or `is_superuser`).

| Module Display Name | Tech Identifier | Access Requirement | Description |
| :--- | :--- | :--- | :--- |
| **HR Management** | `hrm` | `hrm_access` Group / Admin | Personnel directory, rosters, payroll, leaves. |
| **Procurement & Stock** | `inventory` | `inventory_access` Group / Admin | Vendor bids, RFQs, purchase orders, warehouses. |
| **Investment** | `investment` | `investment_access` Group / Admin | Capital tracking, loans, amortization, outbound. |
| **Accounts & Billing** | `billing` | `billing_access` Group / Admin | Chart of Accounts, ledger, invoicing, AP. |
| **Solutions & Projects** | `solutions` | `solutions_access` Group / Admin | Project planning, Kanban task tracking, licensing. |
| **Training Module** | `training` | `training_access` Group / Admin | Student admissions, classes, grading, installments. |
| **System Audit Logs** | `audit_logs` | `audit_logs` permission / Superuser | Crypto-linked system execution audits. |
| **User Management** | `accounts` | `is_staff` / `is_superuser` flag | User profiles, database state management. |

---

## Detailed Navigation & Section Directory

### 1. HR Management (`hrm`)
*   **Overview**: Executive dashboard showing employee headcount, active roster summary, and leave statistics.
*   **Recruitment**: Job posting manager, application tracker, and candidate pipeline logs.
*   **Onboarding & Offboarding**: Administrative checklists for employee intakes and clearance procedures.
*   **Department**: Departmental hierarchy configurer (includes sub-departments).
*   **Employee Database**: General directory containing profile details, roles, salaries, and contract dates.
*   **Attendance Management**: Clock-in and clock-out event tracking.
*   **Shift Roster**: Rotational roster assignments and scheduling calendars.
*   **Leave Management**: Holiday tracking and employee leave request processing.
*   **Payroll Management**: Monthly payroll runs, salary calculations, advance repayments, and payslips.
*   **Expense Claims**: Claims submissions, receipts tracking, and authorization workflows.
*   **Document & Asset Vault**: Repository for scanning employee documents and tracking assigned hardware assets (laptops, phones).
*   **Report Generator**: Exportable HR dashboards and compliance metrics.

---

### 2. Procurement & Stock (`inventory`)
*   **Dashboard**: Inventory valuation charts, low stock alerts, active POs, and pending requisitions.
*   **Client Requisitions**: Consolidated registry of material and sourcing requests.
*   **Vendor Directory**: Supplier profile directories including rating benchmarks and payment agreements.
*   **RFQ & Bidding**: Request for Quotation logs, bidding windows, and supplier quotation lists.
*   **Purchase Orders**: Procurement contract builder, draft PO approvals, and dispatch statuses.
*   **Goods Receipt Notes (GRN)**: Quality assurance inspection records, stock intakes, and storage locations.
*   **Warehouse Stock**: Real-time physical inventory quantities and sku directories.
*   **Dispatch & Challan**: Client handovers, dispatch logs, and delivery receipts (Challans).

---

### 3. Investment (`investment`)
*   **Dashboard**: Managed inbound capital tracking, outbound investment yields, and due interest.
*   **Investors (CRM)**: Investor directory tracking KYC verifications and profiles.
*   **Inbound Capital**: Capital influx transaction registry.
*   **Investor Loans**: Loan registries calculating amortization schemes.
*   **Outbound Placements**: Allocations to third-party assets and valuations tracking.
*   **Securities Registry**: Registry for shares, bonds, and financial instruments.
*   **Profit & Loss**: Real-time tracking of operational profitability.
*   **Liabilities & Payables**: Amortization payout scheduling and repayment clearances.

---

### 4. Accounts & Billing (`billing`)
*   **Dashboard**: Bank/cash levels, overdue receivables, payables due, and maker-checker validation queues.
*   **Chart of Accounts**: Core Ledger classification (Assets, Liabilities, Equity, Revenue, Expenses).
*   **General Journal**: Standard journal creation, double-entry balancing validation, and ledger posting.
*   **AR Invoices**: Sales invoices, receivables tracking, and payments clearing.
*   **AP Bills**: Supplier bill matching, liability generation, and cash payout settlements.
*   **Tax Center**: Tax code setup and National Revenue Authority liabilities.
*   **Financial Statements**: Real-time statements generation (Trial Balance, Balance Sheet, Income Statement).
*   **Audit Trail**: System audit trail capturing edits made to financial documents.

---

### 5. Solutions & Projects (`solutions`)
*   **Dashboard**: Delivery stats and active project status maps.
*   **Projects Scoping**: Milestone mapping, phases configuration, and cost tracking.
*   **Kanban Board**: Multi-stage task boards.
*   **Project Sourcing**: Hardware/software requisitions linked to Procurement.
*   **Licensing & Assets**: Subscription licensing keys and handover records.
*   **Client Stakeholders**: Business partner directory.
*   **Global Contacts (MDM)**: Single master contact registry.
*   **Meeting Scheduler**: Coordination calendar for client meetings.

---

### 6. Training Module (`training`)
*   **Lobby & Admissions**
    *   *Overview*: Admissions statistics.
    *   *Inquiries*: General inquiry leads.
    *   *Sales Management*: Target tracking and sales pipelines.
    *   *Student List*: Active learner database.
*   **Academic Operations**
    *   *Course Creation*: Syllabus and curriculum configuration.
    *   *Batch Management*: Schedules and student assignments.
    *   *Class Calendar*: Room allocations and session logs.
*   **Evaluation & Completion**
    *   *Course Assessments*: Theory/practical exam grades.
    *   *Certificates*: Online verifiable diploma registries.
    *   *Job Placement*: Alumni career tracking.
*   **Directories**
    *   *Employee Database*: Academic personnel.
    *   *Trainer Database*: Profiles of active teaching staff.
    *   *Brand Ambassadors*: Ambassador profiles and performance logs.
    *   *Contact Directory*: Local training contacts.
*   **Financial Control**
    *   *Installment Plan*: Due dates, collections, and balance records.
    *   *Revenue Tracker*: Earned tuition tracking.
    *   *Expense Tracker*: Class expenses logs.
*   **Analytics**
    *   *Reports*: Batch performance and admissions charts.

---

### 7. Core Security & Audit Logs
*   **User Management**: User access controls, permissions, and group groupings.
*   **Audit Logs**: Immutable cryptographic system log trail.
*   **Documentation Portal**: Developers and users documentation.
