# -*- coding: utf-8 -*-
from odoo import models, fields, api


class category(models.Model):
    _name = 'vocabulary.category'
    _description = 'Model danh mục từ vựng'

    name = fields.Char('Danh mục')
    image = fields.Binary('Ảnh')
    word_ids = fields.One2many('vocabulary.words', string='Các từ vựng', inverse_name='category_ids')
    word_count = fields.Integer(compute='_count_words', string='Số từ vựng', store=True)

    @api.depends('word_ids')
    def _count_words(self):
        for record in self:
            record.word_count = len(record.word_ids)
