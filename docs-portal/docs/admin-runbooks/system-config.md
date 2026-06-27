# System Configuration Guide

This runbook documents the global environment settings, security flags, and backend integrations required to configure the Intrex ERP application.

---

## 1. Environment Variables Configuration

The application loads its configuration settings dynamically from the `.env` file in the root workspace directory. Ensure these variables are set correctly for your target deployment environment.

| Environment Variable | Recommended Value (Prod) | Default Fallback (Dev) | Description |
| :--- | :--- | :--- | :--- |
| `DJANGO_SECRET_KEY` | *Generated 50-character key* | *Insecure local key* | Security salt for cryptographic signatures and session tokens. |
| `DJANGO_DEBUG` | `False` | `True` | Toggles detailed traceback pages. Must be `False` in production. |
| `DJANGO_ALLOWED_HOSTS` | `erp.intrex.digital` | `*` or `localhost` | Comma-separated list of host/domain names that this Django site can serve. |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://erp.intrex.digital` | `http://localhost:8000` | Comma-separated list of trusted origins for safe cross-site requests. |
| `FIREBASE_CREDENTIALS_PATH` | `firebase-credentials.json` | `firebase-credentials.json` | File path to Google Cloud service account keys. |
| `FIREBASE_CREDENTIALS_JSON` | *Minified JSON key string* | *None* | Alternative method (specifically for Render cloud deployments) to inject credentials as an environment variable without storing key files. |

---

## 2. Database Configuration

The application implements a hybrid data layer:

### A. Local Relational Engine (SQLite3)
Manages django sessions, user groups, and compliance logs.
*   **Engine**: `django.db.backends.sqlite3`
*   **Path**: `BASE_DIR / 'db.sqlite3'`
*   **Configuration Location**: `config/settings.py` -> `DATABASES` settings block.

### B. Cloud NoSQL Engine (Google Firestore)
Manages ERP transactional and master business entities.
*   **Initialization**: Configured inside `config/firebase.py`.
*   **Connection Logic**:
    1. Looks for the `FIREBASE_CREDENTIALS_JSON` environment string. If found, initializes connections directly from the JSON payload.
    2. Otherwise, looks for the physical file specified by `FIREBASE_CREDENTIALS_PATH` in the root directory.
    3. If neither is present, falls back to Google Application Default Credentials (ADC) if running inside Google Cloud (GAE/GKE).

---

## 3. Security & CSRF Origins Validation

To protect against Cross-Site Request Forgery (CSRF) attacks, Django validates HTTP Origin request headers.

To simplify deployments, the application automatically computes safe origins using the following mechanisms:
1. **Host-to-Origin Parsing**: The application loops through all hostnames configured in `DJANGO_ALLOWED_HOSTS` and prepends both `https://` and `http://` variants to the CSRF trust list.
2. **Render Cloud Platform Detection**: If the environment variable `RENDER_EXTERNAL_URL` is set, the system automatically appends the target deployment URL to allow immediate operations on Render subdomains.
3. **Hardcoded Secure Fallbacks**: The URLs `https://erp-intrex-digital.onrender.com` and its `http` counterpart are registered by default to guarantee standard sandbox deployments pass origin validation checks.

---

## 4. Production Deployment Checklist

Before deploying the platform instance to production:
1. Set `DJANGO_DEBUG=False`.
2. Generate a secure `DJANGO_SECRET_KEY` and store it inside environment variables (never hardcode in settings files).
3. Specify exact, restricted hostnames in `DJANGO_ALLOWED_HOSTS`.
4. Ensure `firebase-credentials.json` is excluded from git commits and is securely hosted or injected via variables.
5. Verify that SQLite files are placed on a persistent disk volume (if using container services like Docker or Render) so that audit logs and user accounts are not wiped on service redeployments.