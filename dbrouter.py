class dbRouter1:
    def db_for_read(self, model, **hints):
        """モデルの読み込みに使用するデータベースを指定します。"""
        if model._meta.app_label == 'app2':
            return 'mysql'
        return 'default'

    def db_for_write(self, model, **hints):
        """モデルの書き込みに使用するデータベースを指定します。"""
        if model._meta.app_label == 'app2':
            return 'mysql'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """オブジェクト間の関係作成を許可するかどうかを決定します。"""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """マイグレーションをどのデータベースに適用するかを指定します。"""
        if app_label == 'app2':
            return db == 'mysql'
        return db == 'default'