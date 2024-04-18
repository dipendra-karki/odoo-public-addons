from odoo import api, models
import odoo
import re


class BaseImport(models.TransientModel):
    _inherit = 'base_import.import'

    def clean_value(self, value):
        if not value:
            return None
        return re.sub(r'\s+', ' ', value.strip())

    @api.model
    def _convert_import_data(self, fields, options):
        data, fields = super(BaseImport, self)._convert_import_data(fields, options)
        final_data = [[self.clean_value(val) if type(val) == str else val for val in d] for d in data]
        return final_data, fields