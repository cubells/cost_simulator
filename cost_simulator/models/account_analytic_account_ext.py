# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class AccountAnalyticAccountaccount(models.Model):
    _inherit = 'account.analytic.account'

    @api.multi
    @api.depends('name')
    def name_get(self):
        if not self.ids:
            return []
        res = []
        for account in self:
            data = []
            data.insert(0, account.name)
            data = ' / '.join(data)
            res.append((account.id, data))
        return res

    estimated_balance = fields.Float(
        'Estimated Balance', readonly=True, digits_compute=dp.get_precision(
            'Account'
        )
    )
    estimated_cost = fields.Float(
        'Estimated Cost', readonly=True, digits_compute=dp.get_precision(
            'Purchase Price'
        )
    )
    estimated_sale = fields.Float(
        'Estimated Sale', readonly=True, digits_compute=dp.get_precision(
            'Sale Price'
        )
    )
