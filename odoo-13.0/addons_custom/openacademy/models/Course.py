# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy'

    title = fields.Char(required=True)
    description = fields.Char()
    
    # Người chịu trahc nhiem
    responsible_id=fields.Many2one('res.users',string='Responsible',required=True)
    session_id=fields.One2many('openacademy.session','course_id',string='Session')