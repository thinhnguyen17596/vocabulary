# -*- coding: utf-8 -*-
from odoo import models, fields, api


class example(models.Model):
    _name = 'vocabulary.example'
    _description = 'Model Ví dụ'

    id = fields.Char()
    example = fields.Text('Ví dụ')
    word_ids = fields.Many2many('vocabulary.words', string='Từ vựng')
