class Duck:
    phylum = 'chordata'

    def __init__(self, loc):
        self.location = loc
    
    def __str__(self):
        return 'quacking in the ' + self.location

    