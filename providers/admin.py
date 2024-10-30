from django.contrib import admin
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'email', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'contact_number', 'email')  # Enable search by name, contact number, and email

admin.site.register(Provider, ProviderAdmin)