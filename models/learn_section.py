# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api, exceptions


class learn_section(models.Model):
    _name = 'vocabulary.learn_section'
    _description = 'Model phiên học'

    id = fields.Integer()
    learner = fields.Many2one('res.users', string='Người học')
    start_date = fields.Datetime('Bắt đầu')
    end_date = fields.Datetime('Kết thúc')
    state = fields.Selection([('init', 'Khởi tạo'), ('learning', 'Đang học'), ('learned', 'Đã học'), ('review', 'Ôn tập')],
                             string="Trạng thái", readonly=True, required=True, tracking=True, copy=False,
                             default='init')
    word_ids = fields.Many2many('vocabulary.words', string='Từ vựng')
    word_count = fields.Integer(compute='_count_words', string='Số từ vựng')

    def name_get(self):
        names = []
        for rec in self:
            name = '%s phiên học %s' % (rec.learner.name, rec.start_date)
            names.append((rec.id, name))
        return names

    @api.depends('word_ids')
    def _count_words(self):
        for record in self:
            record.word_count = len(record.word_ids)

    def set_open(self):
        return self.write({
            'state': 'learning',
            'start_date': fields.datetime.now(),
            'end_date': fields.datetime.now() + datetime.timedelta(days=7),
        })

    def set_close(self):
        return self.write({
            'state': 'learned',
            'end_date': fields.datetime.now(),
        })

    def set_review(self):
        return self.write({
            'state': 'review'
        })

    def reset_state(self):
        return self.write({
            'state': 'init'
        })
