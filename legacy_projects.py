from openerp.osv import fields, osv

class legacy_projects(osv.osv):

  _inherit = "project.project"

  _columns = {
    'legacy_projects_id': fields.integer('Legacy project ID', size=11)
  }

  _defaults ={
    'legacy_projects_id': 0
  }

legacy_projects();
