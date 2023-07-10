from odoo import fields,models
from datetime import datetime

class openacademy_session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session Academy'
    
    name=fields.Char(string='Session Name' ,required=True)
    start_date=fields.Date(string='Start Date')
    duration=fields.Float(string ='Duration(hour)',help='Duration in days')
    number_of_seats=fields.Integer(String='Number of Seats')
    
    
    # Nguoi huong dan
    instructor_id=fields.Many2one('res.partner',string='Instructor',required=True)
    course_id=fields.Many2one('openacademy.course',string='Course',required=True)
    attendee_ids=fields.Many2many('res.partner',string='Attendees')