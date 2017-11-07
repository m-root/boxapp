from rolepermissions.roles import AbstractUserRole

class MiniCoaches(AbstractUserRole):
    available_permissions = {
		'create_membership_registration':True,
		'edit_membership_registration':True,
		'remove_membership_registration':True,
		'create_attendance':True,
		'edit_attendance':True,
		'remove_attendance':True,
		'create_schedule_and_calendar':True,
		'edit_schedule_and_calendar':True,
		'remove_schedule_and_calendar':True,
		'create_category':True,
		'edit_category':True,
		'remove_category':True,		
		'create_notification':True,
		'edit_notification':True,
		'remove_notification':True,
    }

class ProgramHeads(AbstractUserRole):
    available_permissions = {
		'create_membership_registration':False,
		'edit_membership_registration':False,
		'remove_membership_registration':False,
		'create_attendance':False,
		'edit_attendance':False,
		'remove_attendance':False,
		'create_schedule_and_calendar':True,
		'edit_schedule_and_calendar':True,
		'remove_schedule_and_calendar':True,
		'create_category':False,
		'edit_category':False,
		'remove_category':False,		
		'create_notification':True,
		'edit_notification':True,
		'remove_notification':True,
    }

class ME(AbstractUserRole):
    available_permissions = {
		'create_membership_registration':True,
		'edit_membership_registration':True,
		'remove_membership_registration':True,
		'create_attendance':False,
		'edit_attendance':False,
		'remove_attendance':False,
		'create_schedule_and_calendar':True,
		'edit_schedule_and_calendar':True,
		'remove_schedule_and_calendar':True,
		'create_category':False,
		'edit_category':False,
		'remove_category':False,		
		'create_notification':True,
		'edit_notification':True,
		'remove_notification':True,
    }

class Management(AbstractUserRole):
    available_permissions = {
		'create_membership_registration':True,
		'edit_membership_registration':True,
		'remove_membership_registration':True,
		'create_attendance':False,
		'edit_attendance':False,
		'remove_attendance':False,
		'create_schedule_and_calendar':False,
		'edit_schedule_and_calendar':False,
		'remove_schedule_and_calendar':False,
		'create_category':False,
		'edit_category':False,
		'remove_category':False,		
		'create_notification':False,
		'edit_notification':False,
		'remove_notification':False,
    }