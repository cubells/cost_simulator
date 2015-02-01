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

from openerp import models, fields


class Project(models.Model):
    _inherit = 'project.project'

    purchase_order_ids = fields.One2many('purchase.order', 'project2_id',
                                         'Project Purchase Orders')
    sale_order_ids = fields.One2many('sale.order', 'project2_id',
                                     'Project tasks')
    simulation_cost_id = fields.Many2one('simulation.cost', 'Simulation Cost')
    simulation_cost_id2 = fields.Many2one('simulation.cost', 'Simulation Cost')
    is_project = fields.Boolean('Is Project')
    purchase_order_ids2 = fields.One2many('purchase.order', 'project3_id',
                                          'Project Purchase Orders')
    task_ids2 = fields.One2many('project.task', 'project3_id', 'Project Task')
    is_subproject = fields.Boolean('Is Subproject')

    def button_analytical_structure_update_costs(self, cr, uid, ids, *args):
        return True

    def onchange_purchase_ids(self, cr, uid, ids, purchase_list, context=None):
        res = {}
        return {'value': res}


class ProjectTask(models.Model):
    _inherit = 'project.task'

    cost_product_name = fields.Char('Cost Product', size=64, readonly=True)
    sale_product_name = fields.Char('Sale Product', size=64, readonly=True)
    project3_id = fields.Many2one('project.project', 'Project')
