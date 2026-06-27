# Disaster Recovery & Backup Runbook

This runbook outlines the disaster recovery procedures for the Intrex ERP/CRM platform. It details backup and restoration operations for both the local SQLite database (User Access, Sessions, & Audits) and the Google Firestore NoSQL database (ERP Business Ledger & Master Data).

---

## 1. Disaster Recovery Parameters

To meet business continuity compliance, system administrators must operate under the following parameters:
*   **Recovery Point Objective (RPO)**: 24 hours (maximum acceptable data loss).
*   **Recovery Time Objective (RTO)**: 1 hour (maximum acceptable downtime to restore services).

---

## 2. Local SQLite Backup & Restore (Auth, Sessions & Audits)

The file `db.sqlite3` is located in the root of the workspace directory. Because the system can write logs continuously, simple file copying can cause database write locks or corruption.

### A. SQLite Backup Procedure (Cron-ready)
Use SQLite's online backup tool to copy the database safely without stopping the Django web service:
```bash
sqlite3 db.sqlite3 ".backup '/var/backups/erp/sqlite/db_backup_$(date +%F_%H%M%S).sqlite3'"
```

### B. SQLite Restore Procedure
1. Stop the Django application server:
   ```bash
   pkill -f "manage.py runserver"
   ```
2. Rename the active compromised/corrupt database:
   ```bash
   mv db.sqlite3 db.sqlite3.corrupted
   ```
3. Copy the target backup file into place:
   ```bash
   cp /var/backups/erp/sqlite/db_backup_2026-06-27_120000.sqlite3 db.sqlite3
   ```
4. Restart the web service:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

---

## 3. Google Firestore Backup & Restore (ERP Core Data)

All business modules (HRM, Inventory, Investment, Billing, Solutions, Training) write to Google Firestore. 

### A. Firestore Export Procedure
Exports are dispatched to a secure Google Cloud Storage (GCS) bucket:
```bash
gcloud firestore export gs://intrex-erp-backups/firestore-exports/$(date +%F)
```
*To automate this, schedule it via Google Cloud Scheduler and Google Cloud Functions.*

### B. Firestore Import (Restoration) Procedure
> [!IMPORTANT]
> Firestore imports do not overwrite documents if the existing records are identical. If you need a clean rollback to a past state, you must first clear the existing collection records using the Firebase CLI or an admin script, then dispatch the import.

To import the database state:
```bash
gcloud firestore import gs://intrex-erp-backups/firestore-exports/2026-06-27/
```

---

## 4. Disaster Recovery Scenarios

### Scenario A: SQLite Database Corruption
*   **Symptom**: Django prints `sqlite3.DatabaseError: database disk image is malformed` or cryptographic log chain audits fail (`COMPROMISED`).
*   **Resolution**: 
    1. Immediately stop the Django server.
    2. Run the SQLite Restore Procedure using the latest clean daily backup.
    3. Run a manual cryptographic integrity check via the Admin Dashboard.

### Scenario B: Cloud Service Disruption or Firestore Loss
*   **Symptom**: Page loads return Firestore connectivity errors, or collection data is missing.
*   **Resolution**:
    1. Check the Google Cloud Status Dashboard for service outages.
    2. If data was accidentally deleted, authenticate the Google Cloud SDK CLI.
    3. Run `gcloud firestore import` pointing to the latest verified GCS export bucket folder.

### Scenario C: Key Compromise (`firebase-credentials.json`)
*   **Symptom**: Unauthorized read/write requests detected in Firebase audit trails.
*   **Resolution**:
    1. Log in to the Google Cloud Console (IAM & Admin -> Service Accounts).
    2. Locate the service account key for the ERP connection.
    3. Click **Actions** -> **Delete** to instantly revoke the compromised key.
    4. Click **Add Key** -> **Create New Key** (JSON).
    5. Download the key, upload it to the server, overwrite `/home/hsjb/Documents/Website/erp-intrex-digital/firebase-credentials.json` with the new file, and restart Django.

---

## 5. Automated Backup Script

Save the script below to `/usr/local/bin/erp-backup.sh` and set up a root cron job (`crontab -e`) to execute daily at 02:00:
`0 2 * * * /usr/local/bin/erp-backup.sh`

```bash
#!/bin/bash
# Backup Configuration
BACKUP_DIR="/var/backups/erp"
SQLITE_BACKUP_DIR="$BACKUP_DIR/sqlite"
DATE=$(date +%F_%H%M%S)

mkdir -p "$SQLITE_BACKUP_DIR"

# 1. SQLite Online Backup
sqlite3 /home/hsjb/Documents/Website/erp-intrex-digital/db.sqlite3 ".backup '$SQLITE_BACKUP_DIR/db_$DATE.sqlite3'"

# 2. Firestore Cloud Backup Trigger
gcloud firestore export gs://intrex-erp-backups/firestore-exports/$DATE

# 3. Clean up local backups older than 14 days
find "$SQLITE_BACKUP_DIR" -type f -name "*.sqlite3" -mtime +14 -delete

echo "Intrex ERP backup completed on $DATE"
```