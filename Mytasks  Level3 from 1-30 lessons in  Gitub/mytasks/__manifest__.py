{
  		'name': 'My Tasks',
  		'depends': ['base', 'mail'],
		'data':[
			'security/ir.model.access.csv',
			'views/mytask_view.xml',
			'reports/mytask_report.xml'
		],
 		'application': True,
}