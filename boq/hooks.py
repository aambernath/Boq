# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "boq"
app_title = "Boq"
app_publisher = "vivek@quarkcs"
app_description = "Bill of Quantity"
app_icon = "octicon octicon-file-binary"
app_color = "green"
app_email = "vivek@digmabernath.org"
app_license = "MIT"


fixtures = ["Custom Field"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/boq/css/boq.css"
# app_include_js = "/assets/boq/js/boq.js"

# include js, css files in header of web template
# web_include_css = "/assets/boq/css/boq.css"
# web_include_js = "/assets/boq/js/boq.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "boq.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "boq.install.before_install"
# after_install = "boq.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "boq.notifications.get_notification_config"

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
# 		"boq.tasks.all"
# 	],
# 	"daily": [
# 		"boq.tasks.daily"
# 	],
# 	"hourly": [
# 		"boq.tasks.hourly"
# 	],
# 	"weekly": [
# 		"boq.tasks.weekly"
# 	]
# 	"monthly": [
# 		"boq.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "boq.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "boq.event.get_events"
# }
