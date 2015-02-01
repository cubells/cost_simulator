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


class SimulationTemplate(models.Model):
    _name = 'simulation.template'
    _description = 'Simulation Template'

    name = fields.Char('Name', required="True", select=True)
    template_product_id = fields.Many2one('product.product',
                                          'Product for sale')
    others_template_lines_ids = fields.One2many('simulation.template.line',
                                                'template_id',
                                                'Others Lines')


class SimulationTemplateLine(models.Model):
    _name = 'simulation.template.line'
    _description = 'Simulation Template Line'

    template_id = fields.Many2one('simulation.template', 'Template')
    product_id = fields.Many2one('product.product', 'Product', required=True)
    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    amortization_rate = fields.Float('Amortization Rate', digits=(3, 2))
    indirect_cost_rate = fields.Float('Indirect Cost Rate', digits=(3, 2))
    amount = fields.Float('Amount',
                          digits_compute=dp.get_precision('Product UoM'))
    uom_id = fields.Many2one('product.uom', 'Default Unit Of Measure',
                             required=True)
    type_cost = fields.Selection([('Others', 'Others')], 'Type of Cost')
    type2 = fields.Selection([('fixed', 'Fixed'),
                              ('variable', 'Variable')],
                             'Fixed/Variable')
    type3 = fields.Selection([('marketing', 'Marketing'),
                              ('sale', 'Sale'),
                              ('production', 'Production'),
                              ('generalexpenses', 'General Expenses'),
                              ('structureexpenses', 'Structure Expenses'),
                              ('amortizationexpenses',
                               'Amortization Expenses')],
                             'Cost Category')
    _defaults = {
        'type_cost': lambda self, cr, uid, c: c.get('type_cost', False),
        'amount': 1.0,
    }

    @api.v7
    def onchange_product(self, cr, uid, ids, product_id, type, context=None):
        product_obj = self.pool['product.product']
        if product_id and type:
            product = product_obj.browse(cr, uid, product_id, context=context)
            res = {'name': (product.name or ''),
                   'description': (product.description or ''),
                   'uom_id': product.uom_id.id,
                   'amortization_rate': product.amortization_rate,
                   'indirect_cost_rate': product.indirect_cost_rate,
                   }
            return {'value': res}

    @api.v7
    def onchange_type_cost(self, cr, uid, ids, type, context=None):
        res = {'product_id': '',
               'name': '',
               'description': '',
               'uom_id': '',
               'amount': 0
               }
        return {'value': res}
