# -*- coding: utf-8 -*-
from odoo import models, fields, api


class words(models.Model):
    _name = 'vocabulary.words'
    _description = 'Model từ vựng'
    _sql_constraints = [('name',
                         'UNIQUE (name)',
                         'Đã có từ vựng này'), ]

    name = fields.Char('Từ', required=True)
    id = fields.Integer()
    pronunciation = fields.Char('Phát âm')
    category_ids = fields.Many2one('vocabulary.category', string='Danh mục')
    meaning = fields.One2many('vocabulary.meaning', string='Ý nghĩa', inverse_name='word_id')
    related_ids = fields.Many2one('vocabulary.meaning')
    example = fields.Many2many('vocabulary.example', string='Ví dụ')
    test_id = fields.One2many('vocabulary.test', string='Bải kiểm tra', inverse_name='word_id')
    learn_section_ids = fields.Many2many('vocabulary.learn_section', string='Phiên học')
    learn_section_count = fields.Integer(compute='_count_section', string='Số phiên học', store=True)

    @api.depends('learn_section_ids')
    def _count_section(self):
        for record in self:
            record.learn_section_count = len(record.learn_section_ids)