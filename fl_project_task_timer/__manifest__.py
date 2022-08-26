# -*- coding: utf-8 -*-
{
    'name': 'Project Task Timer - Multiple Users',
    'version': '13.0.1.0.0',
    'category': 'Project',
    'summary': 'Task Timer With Start & Stop for Multiple Users, Timer for Project Task, Task Timer, Project Timer',
    'description': """
        This module allow to track time and add timesheet in project automatically. 
        It's allow multiple user to track timesheet.
    """,
    'sequence': 1,
    'author': 'Futurelens',
    'website': 'http://thefuturelens.com',
    'depends': ['base', 'project', 'hr_timesheet'],
    'data': [
        'views/project_task_timer_view.xml',
        'views/backend_assets.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    'images': [
        'static/description/banner_project_task_timer.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
    'price': 10,
    'currency': 'EUR',
}
