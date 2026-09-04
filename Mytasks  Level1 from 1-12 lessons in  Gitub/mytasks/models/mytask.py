from odoo import models,fields

class MyTask(models.Model):
    _name = 'mytask'
    
    name=fields.Char(string="Task", required=True)
    tdate=fields.Date(string="Task Date", default=fields.Date.today, required=True)
    tstatus = fields.Selection(
            [
                ('pending', 'Pending'),
                ('done', 'Done'),
            ],
            string="Status", default='pending', required=True )
    active = fields.Boolean(string="Active", default=True )   

    
    

   