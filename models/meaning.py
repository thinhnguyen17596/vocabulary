# -*- coding: utf-8 -*-
from odoo import models, fields, api


class meaning(models.Model):
    _name = 'vocabulary.meaning'
    _description = 'Model ý nghĩa từ vựng'

    type = fields.Selection(
        [('noun', 'Danh từ'), ('verb', 'Động từ'), ('adj', 'Tính từ'), ('adv', 'Trạng từ'), ('preposition', 'Giới từ'),
         ('pronoun', 'Đại từ'), ('conjunction', 'Liên từ')],
        string="Loại từ")
    meaning = fields.Text('Ý nghĩa')
    related_words = fields.One2many('vocabulary.words',  string='Từ tương tự', inverse_name='related_ids')
    word_id = fields.Many2one('vocabulary.words', string='Từ')
