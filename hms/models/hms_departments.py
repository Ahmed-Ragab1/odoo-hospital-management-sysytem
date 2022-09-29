from odoo import fields,models

class HmsDepartments(models.Model):
    _name = 'hms.departments'

    name=fields.Char()
    capacity=fields.Integer()
    is_opened=fields.Boolean()
    patients=fields.One2many('hms.patient','department_ids')


