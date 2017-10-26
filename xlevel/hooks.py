# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "xlevel"
app_title = "Xlevel"
app_publisher = "openetech"
app_description = "Default Cost Center & Warehouse"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@openetech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/xlevel/css/xlevel.css"
# app_include_js = "/assets/xlevel/js/xlevel.js"

# include js, css files in header of web template
# web_include_css = "/assets/xlevel/css/xlevel.css"
# web_include_js = "/assets/xlevel/js/xlevel.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "xlevel.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "xlevel.install.before_install"
# after_install = "xlevel.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "xlevel.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"xlevel.tasks.all"
# 	],
# 	"daily": [
# 		"xlevel.tasks.daily"
# 	],
# 	"hourly": [
# 		"xlevel.tasks.hourly"
# 	],
# 	"weekly": [
# 		"xlevel.tasks.weekly"
# 	]
# 	"monthly": [
# 		"xlevel.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "xlevel.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "xlevel.event.get_events"
# }
fixtures = [{"dt":"Custom Script", "filters": [["name", "in", ["Sales Order-Client","Sales Invoice-Client","Purchase Receipt-Client","Purchase Invoice-Client"]]]},
{"dt":"Custom Field", "filters": [["name", "in", ["Sales Order-x_default_cost_center","Sales Order-x_default_warehouse","Sales Invoice-x_default_cost_center","Sales Invoice-x_default_warehouse","Purchase Receipt-x_default_cost_center","Purchase Receipt-x_default_warehouse","Purchase Invoice-x_default_cost_center","Purchase Invoice-x_default_warehouse"]]]}]
