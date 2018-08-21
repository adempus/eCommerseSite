from data.shopdatabase import ShopDatabase


class Validate(object):
    def __init__(self, dao):
        self.dao = dao

    def newUser(self, userModel):
        shit = userModel['email']
        userExists = self.dao.retrieveUser(shit, 'email')
        print(userExists)



