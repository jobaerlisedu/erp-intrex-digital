import os

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs-portal', 'docs')

structure = {
    'index.md': '# Welcome to Intrex ERP Documentation\n\nPlease select your role from the top navigation menu to get started.',
    'user-guides': {
        'getting-started.md': '# Getting Started\n\nWelcome to Intrex ERP. Here is your day-one onboarding guide.',
        'hrm.md': '# HR Management Guide\n\nHow to manage employees, payroll, and attendance.',
        'inventory.md': '# Procurement & Inventory Guide\n\nHow to manage RFQs, POs, and stock.',
        'billing.md': '# Accounts & Billing Guide\n\nHow to manage ledgers, taxes, and invoicing.',
        'solutions.md': '# Service Solutions Guide\n\nHow to manage projects, tasks, and IT delivery.',
        'training.md': '# Training & EdTech Guide\n\nHow to manage courses, enrollments, and classes.',
    },
    'admin-runbooks': {
        'access-control.md': '# Access Control (RBAC)\n\nConfiguring roles and permissions.',
        'audit-compliance.md': '# Audit & Compliance\n\nMonitoring system logs and exporting compliance reports.',
        'disaster-recovery.md': '# Disaster Recovery\n\nBackup and restore procedures.',
        'system-config.md': '# System Configuration\n\nGlobal settings and overarching rules.',
    },
    'developer': {
        'architecture.md': '# Architecture & Logic\n\nCross-module automated workflows.',
        'database-schema.md': '# Database Schema\n\nER Diagrams and MDM rules.',
        'api-reference.md': '# API Reference\n\nREST and GraphQL endpoint specifications.',
        'local-setup.md': '# Local Setup\n\nEnvironment and Docker setup guidelines.',
    },
    'assets': {
        # Just create the dir
    }
}

def create_structure(base, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

os.makedirs(base_dir, exist_ok=True)
create_structure(base_dir, structure)
print("Documentation structure scaffolded successfully.")
