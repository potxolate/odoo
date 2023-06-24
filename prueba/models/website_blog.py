# -*- coding: utf-8 -*-

from odoo import models, fields


class Blog(models.Model):
    _inherit = 'blog.blog'

    company_id = fields.Many2one(
        'res.company', string='Company', required=True)


class BlogPost(models.Model):
    _inherit = 'blog.post'

    company_id = fields.Many2one(
        'res.company', string='Company', related='blog_id.company_id', store=True)