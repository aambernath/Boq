// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt


frappe.provide("erpnext.boq");

frappe.ui.form.on('Boq', {
	refresh: function(doc, dt, dn) {
    var frm = cur_frm;
		if(frm.doc.status == "Complete"){
		cur_frm.add_custom_button(__('Quotation'),
				cur_frm.cscript['Make Quotation']);
    }
				cur_frm.add_custom_button(__('New Version'),
						cur_frm.cscript['New Version']);


	}
});



cur_frm.add_fetch("item_code", "description", "description");
cur_frm.add_fetch("item_code", "item_name", "item_name");
cur_frm.add_fetch("item_code", "part_no", "part_no");
cur_frm.add_fetch("item_code", "stock_uom", "stock_uom");
cur_frm.add_fetch("opportunity", "enquiry_from", "quotation_to");
cur_frm.add_fetch("opportunity", "customer", "customer")
cur_frm.add_fetch("opportunity", "lead", "lead")

cur_frm.cscript['Make Quotation'] = function() {
	frappe.model.open_mapped_doc({
		method: "boq.boq.doctype.boq.boq.make_quotation",
		frm: cur_frm
	})
}

cur_frm.cscript.qty = function(doc, cdt, cdn) {
	erpnext.boq.calculate_rm_cost(doc);
	erpnext.boq.calculate_margin(doc);

}

cur_frm.cscript.current_cost = function(doc, cdt, cdn) {
	erpnext.boq.calculate_rm_cost(doc);
  erpnext.boq.calculate_margin(doc);
	erpnext.boq.calculate_rm_margin(doc);
}

cur_frm.cscript.selling_price = function(doc, cdt, cdn) {
	erpnext.boq.calculate_rm_sale(doc);
  erpnext.boq.calculate_margin(doc);
	erpnext.boq.calculate_rm_margin(doc);
}

erpnext.boq.calculate_rm_sale = function(doc) {
	var rm = doc.items || [];
	total_rm_sale = 0;
	for(var i=0;i<rm.length;i++) {
		amt =	flt(rm[i].selling_price) * flt(rm[i].qty);
		set_multiple('Boq Item',rm[i].name, {'sale_amount': amt}, 'items');
		total_rm_sale += amt;

	}
	cur_frm.set_value("total_sale", total_rm_sale);
}

erpnext.boq.calculate_rm_margin = function(doc) {
	var rm = doc.items || [];

	for(var i=0;i<rm.length;i++) {
		margin =	flt(rm[i].sale_amount) - flt(rm[i].cost_amount);
		set_multiple('Boq Item',rm[i].name, {'margin': margin}, 'items');
	}
}



erpnext.boq.calculate_rm_cost = function(doc) {
	var rm = doc.items || [];
	total_rm_cost = 0;
	for(var i=0;i<rm.length;i++) {
		amt =	flt(rm[i].current_cost) * flt(rm[i].qty);
		set_multiple('Boq Item',rm[i].name, {'cost_amount': amt}, 'items');
		total_rm_cost += amt;
	}
	cur_frm.set_value("total_cost", total_rm_cost);
}

erpnext.boq.calculate_margin = function(doc) {
	margin = flt(doc.total_sale) - flt(doc.total_cost);
	m_per = flt(flt(margin) / flt(doc.total_sale) * 100, 2);
	frappe.model.set_value(doc.doctype, doc.name, "margin", margin);
	frappe.model.set_value(doc.doctype, doc.name, "margin_percent", m_per);
}
