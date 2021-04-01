# -*- coding: utf-8 -*-
from odoo import models, fields, api


class student(models.Model):
    _inherit = 'res.users'

    title = fields.Char(compute='_title', string='Danh hiệu', store=True)
    learn_section = fields.One2many('vocabulary.learn_section', string='Các phiên học', inverse_name='learner')
    word_count = fields.Integer(compute='_count_words', string='Số từ vựng', store=True)

    @api.depends('learn_section')
    def _count_words(self):
        for record in self:
            record.word_count = 0
            for each in record.learn_section:
                record.word_count += each.word_count

    @api.depends('word_count')
    def _title(self):
        for record in self:
            if record.word_count <= 10:
                record.title = 'Mẫu giáo'
            if record.word_count <= 50 and record.word_count > 10:
                record.title = 'Tiểu học'
            if record.word_count <= 1000 and record.word_count > 50:
                record.title = 'Trung học cơ sở'
            if record.word_count <= 2000 and record.word_count > 1000:
                record.title = 'Trung học phổ thông'
            if record.word_count <= 5000 and record.word_count > 2000:
                record.title = 'Đại học'