# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HmsSection(models.Model):
    _name = 'hms.section'

    name = fields.Char('Section')


class HmsFloors(models.Model):
    _name = 'hms.floors'
    _rec_name = 'name'
    _description = 'hospital floors'

    name = fields.Char('Floor Name')
    section_id = fields.Many2one('hms.section', string='Section Name')


class HmsRooms(models.Model):
    _name = 'hms.rooms'
    _rec_name = 'name'
    _description = 'hospital rooms'

    name = fields.Char('Room Name', required=True)
    floor_id = fields.Many2one('hms.floors', string='Floor Name')
    state = fields.Selection([('free', 'Free'), ('busy', 'Busy')], default='free')
