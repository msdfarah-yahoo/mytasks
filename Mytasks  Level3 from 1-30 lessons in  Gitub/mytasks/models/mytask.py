from odoo import models,fields,api
from odoo.exceptions import ValidationError


class MyTask(models.Model):
    _name = 'mytask'
    _order = 'tdate asc, tstatus asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
        
    name=fields.Char(string="Task", tracking=True)
    tdate=fields.Date(string="Task Date", default=fields.Date.today, required=True, tracking=True)
    tstatus = fields.Selection(
            [
                ('pending', 'Pending'),
                ('done', 'Done'),
            ],
            string="Status", default='pending', required=True ,
    tracking=True)
    active = fields.Boolean(string="Active", default=True ,
    tracking=True)   
    
    task_info = fields.Char(
        string="Task Info", default="MyTask ", 
        compute="_compute_task_info"
    )

    @api.depends('name')
    def _compute_task_info(self):
        for task in self:
            task.task_info = task.tstatus +" - "+ task.name

    _sql_constraints = [
            (
                'mytask_name_unique',
                'unique(name)',
                'Task name must be unique'
            )
        ]

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if not record.name:
                raise ValidationError("Task name cannot be empty.")

    def action_done(self):
        for task in self:
            task.tstatus = 'done'   
            
    def action_pending(self):
        for task in self:
            task.tstatus = 'pending'   