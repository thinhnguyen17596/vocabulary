# -*- coding: utf-8 -*-
from odoo import models, fields, api


class quiz(models.Model):
    _name = 'vocabulary.quiz'
    _description = 'Model câu hỏi'

    name = fields.Char('Câu hỏi')
    show_answer = fields.Boolean('Hiện đáp án đúng', default='True')
    choice1 = fields.Text('Đáp an 1.')
    choice2 = fields.Text('Đáp an 2.')
    choice3 = fields.Text('Đáp an 3.')
    choice4 = fields.Text('Đáp an 4.')
    answer = fields.Integer('Đáp án đúng')
    test_id = fields.Many2one('vocabulary.test', string='Bài kiểm tra')
