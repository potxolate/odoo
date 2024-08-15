# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Prueba técnica",
    "category": "Uncategorized",
    "license": "AGPL-3",
    "author": "Rubén García Solís",
    "version": "16.0.1.0.0",
    "website": "https://github.com/potxolate",
    "summary": "Test module for job application.",
    "depends": [
        "website_blog",
        "sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
        "views/website_blog_templates.xml",
        "views/website_blog_views.xml",
        "views/crm_lead_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
}
