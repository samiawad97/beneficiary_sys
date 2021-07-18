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
		_("Receipt No.") + ":Select:120",
		_("Reciept Date") + ":date:100",
		_("Description") + ":Text:100",
		_("Amount") + ":Float:100",
		_("Partner Name") + ":Link/Partners",
		_("Branch") + ":Link/Branch:100",
		_("Record status") + ":Select:60",
		_("Donation classification") + ":Link/Donation classification:100",
		_("Project Name") + ":Link/Project:100",
		_("Affiliate name") + ":Link/Affiliate:100"
	]


def get_data(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select naming_series, reciept_date, description,
	amount, partner_name, branch,
	record_status, donation_classification ,project_name ,affiliate_name 
	from `tabReceipt` where  record_status = 'Active' %s""" % conditions, as_list=1)


def get_conditions(filters):
	conditions = ""
	if filters.get("naming_series"): conditions += " and naming_series = '%s'" % \
												   filters["naming_series"].replace("'", "\\'")

	if filters.get("reciept_date"): conditions += " and reciept_date = '%s'" % \
													 filters["reciept_date"].replace("'", "\\'")

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
	if filters.get("donation_classification"): conditions += " and donation_classification = '%s'" % \
															 filters["donation_classification"].replace("'", "\\'")

	if filters.get("project_name"): conditions += " and project_name = '%s'" % \
												   filters["project_name"].replace("'", "\\'")

	if filters.get("affiliate_name"): conditions += " and affiliate_name = '%s'" % \
													filters["affiliate_name"].replace("'", "\\'")

	return conditions