from django.contrib import admin
from .models import Game,Audit

# Register your models here.
class GameAdmin(admin.ModelAdmin):

    list_display=('id','turn','board')

class AuditAdmin(admin.ModelAdmin):
    list_display=('game', 'player','old_state','new_state','time')

admin.site.register(Game,GameAdmin)
admin.site.register(Audit,AuditAdmin)