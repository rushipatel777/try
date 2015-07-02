from openerp.osv import osv, fields

class employee1(osv.Model):
    
    _name = 'employee1.employee1'
    
            
    
    _columns = {
        'name' : fields.char('Name', size=64),
        'work_address': fields.text('working address'),
        'work_phone_no': fields.char('Contact Number :' ,size=64),
        'address': fields.text('address :'),
        'nationality': fields.char('nationality :' ,size=64),
        'contact_no' : fields.integer('Phone No'),
        'birthdate' : fields.date('Date of Birth'),
        'gender' : fields.selection([('male','Male'), ('female', 'Female')], 'Gender'),
        'is_exp' : fields.boolean('Experienced?'),
        'year_of_exp' : fields.integer('Years of Experience'),
        'notes' : fields.text('Employee Notes'),
        'emp_resume' : fields.binary('Employee Resume'),
        'department_id' : fields.many2one('department1.department1', 'Department'),
        'salary_releted' : fields.related('department_id','salary',type='float', string="Salary"),
        'emp_signature' : fields.html(' '),
        'emp_company':fields.many2one('company1.company1','Company naame'),
    
         
    }
    
class department1(osv.Model):
    
    _name = 'department1.department1'
    
    
    _columns = {
        'name' : fields.char('Department Name', size=64),
        'employee_ids' : fields.one2many('employee1.employee1', 'department_id', 'Employees'),
        'salary' : fields.float('Salary'),
    
    }
    
    
class company1(osv.Model):
    
    _name = 'company1.company1'
    
    _columns = {
        'name' : fields.char('Company Name', size=64),
        'department_ids' : fields.many2many('department1.department1', 'company_department_rel', 
                                            'company_id', 'department_id', 'Departments')
    }