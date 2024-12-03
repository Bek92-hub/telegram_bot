import pymysql


class Database:
    def __init__(self, db_name, db_password, db_user, db_port, db_host):
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.db_port = db_port
        self.db_host = db_host

    def connect(self):
        return pymysql.Connection(
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute(self, sql: str, params: tuple = (), commit=False, fetchone=False, fetchall=False) -> dict | list:
        database = self.connect()
        cursor = database.cursor()

        cursor.execute(sql, params)
        data = None

        if fetchone:
            data = cursor.fetchone()

        elif fetchall:
            data = cursor.fetchall()

        if commit:
            database.commit()

        return data

    def create_users_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users(
                id INT PRIMARY KEY AUTO_INCREMENT,
                telegram_id BIGINT NOT NULL UNIQUE,
                fullname VARCHAR(100),
                username VARCHAR(100),
                address VARCHAR(255),
                is_subscribed INT DEFAULT 1
            )
        """
        self.execute(sql)

    def create_categories_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS categories(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE
            )
        """
        self.execute(sql)
    
    def create_products_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS products(
                id INT PRIMARY KEY AUTO_INCREMENT,
                category_id INT NOT NULL,
                name VARCHAR(100) NOT NULL UNIQUE,
                description VARCHAR(255),
                photo VARCHAR(255) NOT NULL,
                price DECIMAL(12, 2) NOT NULL
            )
        """
        self.execute(sql)

    def create_cart_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS cart(
                id INT PRIMARY KEY AUTO_INCREMENT,
                owner INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                total_price DECIMAL(12, 2)
            )    
        """
        self.execute(sql)

    def add_to_cart(self, user_id, product_id, quantity):
        product = self.get_product(product_id=product_id)

        total_price = float(product.get('price')) * int(quantity)

        sql = """
            INSERT INTO cart(owner, product_id, quantity, total_price)
            VALUES (%s, %s, %s, %s)
        """
        self.execute(sql, (user_id, product_id, quantity, total_price), commit=True)


    def register_user(self, telegram_id: int, fullname: str, username: str):
        sql = """
            INSERT INTO users (telegram_id, fullname, username)
            VALUES (%s, %s, %s)
        """
        self.execute(sql, (telegram_id, fullname, username), commit=True)

    def get_categories(self):
        sql = """
            SELECT * FROM categories
        """
        return self.execute(sql, fetchall=True)

    def get_products(self, category_id):
        sql = """
            SELECT * FROM products WHERE category_id = %s
        """
        return self.execute(sql, (category_id,), fetchall=True)

    def get_product(self, product_id):
        sql = """
            SELECT * FROM products WHERE id = %s
        """
        return self.execute(sql, (product_id,), fetchone=True)

    def get_user(self, telegram_id):
        sql = """
            SELECT * FROM users WHERE telegram_id = %s
        """
        return self.execute(sql, (telegram_id,), fetchone=True)

    def get_cart_products(self, user_id):
        sql = """
            SELECT * FROM cart WHERE owner = %s
        """
        return self.execute(sql, (user_id,), fetchall=True)

    def manage_subscription(self, is_subscribed, telegram_id):
        sql = """
            UPDATE users SET is_subscribed = %s WHERE telegram_id = %s
        """
        self.execute(sql, (is_subscribed, telegram_id), commit=True)

    def clear_user_cart(self, user_id):
        sql = """
            DELETE FROM cart WHERE owner = %s;
        """
        self.execute(sql, (user_id,), commit=True)