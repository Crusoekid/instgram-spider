from google.cloud import datastore
from ..spiders.constantant import G_SAVE_KIND

class gDataHandler:

    def getClient(self):
        return datastore.Client('hello-world-168008')

    def insertData(self,client,data):
        name = str(data['id_'])
        key = client.key(G_SAVE_KIND,name)
        task = datastore.Entity(key=key)
        task['id'] = name
        task['name'] = data['name_']
        task['portrait'] = data['portrait_url_']
        task['work'] = data['img_url_']
        client.put(task)
        pass

    def delData(self,id):
        client = self.getClient()
        key = client.key(G_SAVE_KIND,id)
        client.delete(key)
        pass
    
    def updateData(self,client,data,task):
        mid = str(data['id_'])
        task['id'] = mid
        task['name'] = data['name_']
        task['portrait'] = data['portrait_url_']
        task['work'] = data['img_url_']

        client.put(task)
        pass
    
    def searchData(self,data):
        client = self.getClient()
        name = str(data['id_'])
        key = client.key(G_SAVE_KIND,name)
        task = client.get(key)

        if task:
            self.updateData(client,data,task)
        else:
            self.insertData(client,data)
        pass