# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cint, flt, round_based_on_smallest_currency_fraction


form_grid_templates = {
	"items": "templates/form_grid/boq_grid.html"
}

class Boq(Document):
	def validate(self):
		self.item_total()
		self.total()

	def item_total(self):
		for item in self.get("items"):
			item.cost_amount = flt(item.current_cost * item.qty, item.precision("sale_amount"))
			item.sale_amount = flt(item.selling_price * item.qty, item.precision("sale_amount"))
			item.margin = item.sale_amount - item.cost_amount


	def total(self):
		self.total_cost = 0.0
		self.total_sale = 0.0
		for item in self.get("items"):
			self.total_cost += item.cost_amount
			self.total_sale += item.sale_amount



@frappe.whitelist()
def make_quotation(source_name, target_doc=None):
	boq = frappe.get_doc("Boq", source_name)
	frappe.db.set_value("Opportunity", boq.opportunity, "status", "Quotation")

	doclist = get_mapped_doc("Boq", source_name, {
		"Boq": {
			"doctype": "Quotation",
			"field_map": {
				"account_manager": "tablix_rep",
				"name": "enq_no",
			}
		},
		"Boq Item": {
			"doctype": "Quotation Item",
			"field_map": {

				"uom": "stock_uom",
				"selling_price": "rate",
				"sale_amount": "total",
			}
		}
	})

	return doclist
