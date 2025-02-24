from django.contrib import admin
from library.models import *



class BookInline(admin.StackedInline):
    model = Book
    extra = 0
    classes = ['collapse']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ['pk','firstname', 'lastname', 'rate', 'is_deleted']
    list_display_links = ['firstname', 'lastname']
    actions = ['soft_delete', 'soft_backup']


    @admin.action(description='Soft delete')
    def soft_delete(self, request, queryset):
        queryset.update(is_deleted=True)

    @admin.action(description='Soft back')
    def soft_backup(self, request, queryset):
        queryset.update(is_deleted=False)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        "name",
        'surname',
        'email',
        'gender',
        'birth_date',
        'role',
        'is_active',
        'libraries',
    ]

    list_display = (
        "name",
        'surname',
        'age',
    )

    class Meta:
        model = Category
        fields = "__all__"
