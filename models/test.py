# -*- coding: utf-8 -*-
from odoo import models, fields, api


class test(models.Model):
    _name = 'vocabulary.test'
    _description = 'Model kiểm tra'

    name = fields.Char('Tên')
    quiz = fields.One2many('vocabulary.quiz', string='Câu hỏi', inverse_name='test_id')
    word_id = fields.Many2one('vocabulary.words', string='Từ vựng')
    quiz_count = fields.Integer(compute='_count_quiz', string='Số câu hỏi')

    @api.depends('quiz')
    def _count_quiz(self):
        for record in self:
            record.quiz_count = len(record.quiz)
