# -*- coding: utf-8 -*-
# Copyright 2017 Alex Comba
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    odoo_sh = fields.Boolean(string='Odoo sh')
