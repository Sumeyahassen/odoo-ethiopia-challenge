# -*- coding: utf-8 -*-
{
    "name": "Project & Credential Vault (Vault18/20)",
    "version": "20.0.1.0.1",          # ← VERSION TOKEN
    "category": "Project",
    "summary": "Secure multi-tech-stack project registry and encrypted credential vault",
    "depends": ["base", "mail", "web"],
    "data": [
        "security/vault_security.xml",
        "security/ir.access.csv",
        "data/tech_stack_data.xml",
        "views/vault_technology_views.xml",
        "views/vault_credential_views.xml",
        "views/vault_project_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}