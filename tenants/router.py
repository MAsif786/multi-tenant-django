from operator import imod
from .middlewares import get_current_db_name

class TenantRouter:

    def db_for_read(self, model, **hints):
        return get_current_db_name()

    def db_for_write(self, model, **hints):
        return get_current_db_name()

    def allow_relation(self, obj1, obj2, **hints):
        return get_current_db_name()

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True