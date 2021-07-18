# Copyright (c) 2013, s97 and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = get_data(filters)

	return columns, data


def get_columns():
	return [
		_("Cash No.") + ":Select:120",
		_("Cash Date") + ":date:100",
		_("Description") + ":Text:100",
		_("Amount") + ":Float:100",
		_("Partner Name") + ":Link/Partners",
		_("Branch") + ":Link/Branch:100",
		_("Record status") + ":Select:60",
		_("Cash classification") + ":Link/Cash classification:100",
		_("Project Name") + ":Link/Project:100",
		_("Delegate name") + ":Link/Employee:100"
	]


def get_data(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select naming_series, cash_date, description,
	amount, partner_name, branch,
	record_status, cash_classification ,project_name ,delegate_name 
	from `tabCash receipt` where  record_status = 'Active' %s""" % conditions, as_list=1)


def get_conditions(filters):
	conditions = ""
	if filters.get("naming_series"): conditions += " and naming_series = '%s'" % \
												   filters["naming_series"].replace("'", "\\'")

	if filters.get("cash_date"): conditions += " and cash_date = '%s'" % \
													 filters["cash_date"].replace("'", "\\'")

	if filters.get("description"): conditions += " and description = '%s'" % \
											   filters["description"].replace("'", "\\'")

	if filters.get("amount"): conditions += " and amount = '%s'" % \
														filters["amount"].replace("'", "\\'")

	if filters.get("partner_name"): conditions += " and partner_name = '%s'" % \
												  filters["partner_name"].replace("'", "\\'")

	if filters.get("branch"): conditions += " and branch = '%s'" % \
												filters["branch"].replace("'", "\\'")

	if filters.get("record_status"): conditions += " and record_status = '%s'" % \
											filters["record_status"].replace("'", "\\'")
	if filters.get("cash_classification"): conditions += " and cash_classification = '%s'" % \
															 filters["cash_classification"].replace("'", "\\'")

	if filters.get("project_name"): conditions += " and project_name = '%s'" % \
												   filters["project_name"].replace("'", "\\'")

	if filters.get("delegate_name"): conditions += " and delegate_name = '%s'" % \
													filters["delegate_name"].replace("'", "\\'")

	return conditions