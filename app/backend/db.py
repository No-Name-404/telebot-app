import json
class database:
    def __init__(self, file):
        self.path = 'app/db/'+file+'.json'

    def read(self):
        with open(self.path,'r')as f:
            return json.loads(f.read())

    def add(self,dictionary):
        with open(self.path,'w')as f:
            f.write(json.dumps(dictionary,indent=4))

    def delete(self,key):
        db = self.read()
        del db[key]
        with open(self.path,'w')as f:
            f.write(json.dumps(db,indent=4))
