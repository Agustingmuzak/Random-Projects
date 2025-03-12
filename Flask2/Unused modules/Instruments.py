class Instrument:
    def __init__(self, instrument_type, sub_category):
        self.instrument_type = instrument_type
        self.sub_category = sub_category
    def getDetail(self):
        return 'The instrument is: {} {}'.format(self.sub_category, self.instrument_type)