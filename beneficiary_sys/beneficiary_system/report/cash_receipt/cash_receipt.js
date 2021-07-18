// Copyright (c) 2016, s97 and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Cash receipt"] = {
	"filters": [{
		"fieldname":"naming_series",
		"label": __("Receipt No."),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"reciept_date",
		"label": __("Reciept Date"),
		"fieldtype": "Date",
		"options": "",
		"default":""
	},
	{
		"fieldname":"description",
		"label": __("Description"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"amount",
		"label": __("Amount"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"partner_name",
		"label": __("Partner Name"),
		"fieldtype": "Select",
		"options": "",
		"default":""
	},
	{
		"fieldname":"branch",
		"label": __("Branch"),
		"fieldtype": "Link",
		"options": "",
		"default":""
	},
	{
		"fieldname":"record_status",
		"label": __("Record status"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"cash_classification",
		"label": __("Cash classification"),
		"fieldtype": "Link",
		"options": "",
		"default":""
	},
	{
		"fieldname":"project_name",
		"label": __("Project Name"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"delegate_name",
		"label": __("Delegate name"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	}
	]
};
