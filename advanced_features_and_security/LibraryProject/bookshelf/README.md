## Permissions and Groups Setup

### Custom Permissions
In the `Book` model, custom permissions have been defined:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

### User Groups
Three groups are configured:
- `Viewers`: Can only view books.
- `Editors`: Can view, create, and edit books.
- `Admins`: Have full control over books, including deleting them.

### Enforcing Permissions
Permissions are enforced in views using Django's `@permission_required` decorator and `PermissionRequiredMixin` for class-based views.

### Testing
To test the setup, create users and assign them to different groups. Attempt to access various views to ensure permissions are correctly applied.
