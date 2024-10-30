from django.contrib import admin
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('title', 'description')  # Enable search by title and description
    list_filter = ('category',)  # Filter by category

admin.site.register(Task, TaskAdmin)