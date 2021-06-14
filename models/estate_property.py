from odoo import models, fields
from datetime import date
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"  # . will be automatically converted into _
    _description = "Info about property"

    title = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(size=10)
    # copy attribute whether the field value should be copied when the record is duplicated (default: True)
    date_availability = fields.Date(
        copy=False, default=date.today() + relativedelta(months=+3))
    expected_price = fields.Float(required=True)
    # default value of readonly is False
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[(
        "north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])
    active = fields.Boolean(default=False)
    state = fields.Selection(selection=[("new", "New"), ("offer_received", "Offer Received"), (
        "offer_accepted", "Offer Accepted"), ("sold", "Sold"), ("cancelled", "Cancelled")])
