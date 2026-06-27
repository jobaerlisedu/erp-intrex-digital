# Accounts & Billing Guide

The Accounts & Billing module manages the financial books of the enterprise. It features a complete double-entry general ledger, AR invoicing, AP billing, tax configurations, and financial statements compilation.

---

## 1. Accounting Structure

All financial transactions flow through the Chart of Accounts into double-entry journal books:

```
                  ┌────────────────────────┐
                  │   Chart of Accounts    │
                  └───────────┬────────────┘
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
       [Accounts Receivable]         [Accounts Payable]
       Customer Invoices (AR)        Vendor Bills (AP)
               │                             │
               └──────────────┬──────────────┘
                              ▼
                  ┌────────────────────────┐
                  │    General Journal     │
                  │ (Debits = Credits)     │
                  └───────────┬────────────┘
                              ▼
                  ┌────────────────────────┐
                  │  Financial Statements  │
                  │  (Balance Sheet, P&L)  │
                  └────────────────────────┘
```

---

## 2. Operating the General Ledger

### A. Chart of Accounts (COA)
Navigate to **Billing** -> **Chart of Accounts** to review the account ledger. Accounts are categorized into five types:
1. **Assets** (e.g. Cash, Accounts Receivable, Inventory)
2. **Liabilities** (e.g. Accounts Payable, Accrued Taxes)
3. **Equity** (e.g. Retained Earnings, Capital Influx)
4. **Revenue** (e.g. Course Tuition Fees, Project Contract Sales)
5. **Expenses** (e.g. Employee Salaries, Vendor Procurement costs)

### B. Posting Journal Entries
1. Navigate to **Billing** -> **General Journal**.
2. Click **Create Journal Entry**.
3. Input the Posting Date and a descriptive narration.
4. Add journal lines (at least two lines are required):
    *   Select the target Account.
    *   Input either a **Debit** or **Credit** amount.
5. Click **Post Entry**.
> [!IMPORTANT]
> The system enforces strict double-entry integrity. You cannot post a journal entry if the sum of Debits does not equal the sum of Credits.

---

## 3. AR Invoices & AP Bills

### A. Accounts Receivable (AR) - Invoicing Customers
To invoice clients for IT projects, training enrollments, or services:
1. Navigate to **Billing** -> **Invoices (AR)**.
2. Click **Create Invoice**.
3. Select the customer contact, tax rate (from the **Tax Center**), and due date.
4. Add line items, specifying quantities and unit prices.
5. Save and send the invoice. When payments arrive, click **Record Payment** to clear the invoice balance.

### B. Accounts Payable (AP) - Logging Vendor Bills
To log vendor charges from purchase orders or utility expenses:
1. Navigate to **Billing** -> **Bills (AP)**.
2. Click **Record Vendor Bill**.
3. Select the vendor, input the bill reference number, and record the debit accounts.
4. Post the bill. When paid, mark the bill as *Paid* to clear the AP liability account.

---

## 4. Financial Reporting

Administrators can compile standard statements in real-time under **Billing** -> **Financial Reports**:
*   **Income Statement (Profit & Loss)**: Sums revenue accounts and subtracts expense accounts over a date range to determine net profit.
*   **Balance Sheet**: Summarizes the accounting equation: $\text{Assets} = \text{Liabilities} + \text{Equity}$ at a specific point in time.
*   **Tax Center**: Consolidates VAT/Sales Tax collection and payments to assist with government filings.