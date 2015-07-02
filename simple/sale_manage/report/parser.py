from openerp.report import report_sxw


class Parser(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):

        print "Inside The Parser Class..."

        super(Parser, self).__init__(cr, uid, name=name, context=context)

        self.localcontext.update({

            'get_serial':self._get_serial,

        })


    def _get_serial(self, sl_ids):

        serial = []
        counter = 1

        for line in sl_ids:

            serial.append(counter)

            counter +=1

        return serial