import sqlite3

class ShopDatabase(object):
    def __init__(self):
        self.schema = self.ShopDBSchema()

    def cursor(self):
        return self.schema.getCursor()

    def connection(self):
        return self.schema.getConnection()

    class ShopDBSchema(object):
        def __init__(self):
            self.__connection = sqlite3.connect('./data/db/shop.db')
            self.__cursor = self.__connection.cursor()
            self()

        def initUsersTable(self):
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname   TEXT NOT NULL,
                lastname    TEXT NOT NULL,
                email       TEXT NOT NULL,
                password    TEXT NOT NULL,
                address     INTEGER REFERENCES address(id));
            ''')

        def initAddressTable(self):
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS address(
                id          INTEGER PRIMARY KEY,
                country     TEXT NOT NULL,
                state       TEXT NOT NULL,
                city        TEXT NOT NULL,
                streetname  TEXT NOT NULL,
                zip         INTEGER NOT NULL,
                apt         TEXT);
            ''')

        def initCartTable(self):
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS cart(
                id          INTEGER PRIMARY KEY,
                item        TEXT NOT NULL,
                price       DOUBLE PRECISION
                category    INTEGER REFERENCES categories(id),
                quantity    INTEGER NOT NULL);
            ''')

        def initCategoriesTable(self):
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
                id      INTEGER PRIMARY KEY,
                name    TEXT NOT NULL);
            ''')

        def initCatalogTable(self):
            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS products(
                id       INTEGER PRIMARY KEY,
                product  TEXT NOT NULL,
                category INTEGER REFERENCES categories(id),
                price    DOUBLE PRECISION);
            ''')

        def getCursor(self):
            return self.__cursor

        def getConnection(self):
            return self.__connection

        def __call__(self):
            self.initUsersTable()
            self.initAddressTable()
            self.initCartTable()
            self.initCategoriesTable()
            self.initCatalogTable()
            self.__connection.commit()