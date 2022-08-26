# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api


class ProjectTaskTimeSheet(models.Model):
    _inherit = 'account.analytic.line'

    date_start = fields.Datetime(string='Start Date')
    date_end = fields.Datetime(string='End Date', readonly=1)
    timer_duration = fields.Float(string='Time Duration', invisible=1)


class ProjectTaskTimer(models.Model):
    _inherit = 'project.task'

    def _compute_is_user_working(self):
        for order in self:
            if order.timesheet_ids.filtered(lambda x: (x.user_id.id == self.env.user.id) and (not x.date_end)):
                order.is_user_working = True
            else:
                order.is_user_working = False

    @api.depends('timesheet_ids.timer_duration')
    def _compute_duration(self):
        for each in self:
            each.duration = 0
            each.duration = sum(each.timesheet_ids.mapped('timer_duration'))

    def toggle_start(self):
        self.write({'task_timer': True, 'is_user_working': True})
        time_line = self.env['account.analytic.line']
        for time_sheet in self:
            time_line.create({
                'name': self.env.user.name + ': ' + time_sheet.name,
                'task_id': time_sheet.id,
                'user_id': self.env.user.id,
                'project_id': time_sheet.project_id.id,
                'date_start': datetime.now(),
            })

    def toggle_end(self):
        self.write({'task_timer': False, 'is_user_working': False})
        time_line_obj = self.env['account.analytic.line']
        domain = [('task_id', 'in', self.ids), ('date_end', '=', False), ('user_id', '=', self.env.user.id)]
        for time_line in time_line_obj.search(domain):
            time_line.write({'date_end': fields.Datetime.now()})
            if time_line.date_end:
                diff = fields.Datetime.from_string(time_line.date_end) - fields.Datetime.from_string(time_line.date_start)
                time_line.timer_duration = round(diff.total_seconds() / 60.0, 2)
                time_line.unit_amount = round(diff.total_seconds() / (60.0 * 60.0), 2)
            else:
                time_line.unit_amount = 0.0
                time_line.timer_duration = 0.0

    task_timer = fields.Boolean('Timer', default=False)
    is_user_working = fields.Boolean(
        'Is Current User Working', compute='_compute_is_user_working',
        help="Technical field indicating whether the current user is working")
    duration = fields.Float('Real Duration', compute='_compute_duration', store=True)
