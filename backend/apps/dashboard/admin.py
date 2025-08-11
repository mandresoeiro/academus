from django.contrib import admin

from .models import Task, TaskComment


# 🎯 Admin personalizado para o modelo Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "sector", "status", "is_done", "created_at")
    list_filter = ("sector", "status", "is_done")
    search_fields = ("title", "description")
    ordering = ("-created_at",)


# 💬 Admin para comentários vinculados à tarefa
@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ("task", "user", "short_content", "sector", "created_at")
    search_fields = ("task__title", "content", "user__username")
    list_filter = ("sector", "created_at")
    ordering = ("-created_at",)

    def short_content(self, obj):
        return obj.content[:40] + ("..." if len(obj.content) > 40 else "")

    short_content.short_description = "Comentário"
