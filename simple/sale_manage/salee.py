from openerp.osv import osv , fields

class saleorder(osv.Model):
    _name = "saleorder.saleorder"
        
    _columns = {
                'name' : fields.char('Name',size = 30),
                'ocode' : fields.char('Order Code',size = 30),
                'sl_ids':fields.one2many('saleline.saleline','so_id','Sale Line Orders')
                }

class invoice(osv.Model):
    _name = "invoice.invoice"
    
    _columns = {
                'name' : fields.char('Name',size = 30),
                'icode' : fields.char('invoice Code',size = 30),
                'al_ids': fields.one2many('activeline.activeline','invo_id','Active Order Lines'),
                'iso_id': fields.many2one('saleorder.saleorder','Saleorder')
                
                }
    
    
        

class saleline(osv.Model):
    _name = "saleline.saleline"
        
    _columns = {
                'name' : fields.char('Name',size = 30),
                'slcode' : fields.char('sale line Code',size = 30),
                'so_id': fields.many2one('saleorder.saleorder','Saleorder'),
                'number': fields.integer('Number'),
                'pin':fields.integer('pin')
                } 

    _sql_constraints = [
        ('mynum','CHECK(number<10)','Please Check Your Number'),
        ('mypin','CHECK(pin>10)','Please Check Your pin'),
        ('myunique','unique(name)','please enter another name')
      ]
class activeline(osv.Model):
    _name = "activeline.activeline"
        
    _columns = {
                'name' : fields.char('Name',size = 30),
                'alcode' : fields.char('active line Code',size = 30),
                'invo_id':fields.many2one('invoice.invoice','Invoice')
                
                }         
