from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    action = models.CharField(max_length=100)  # e.g., 'LOGIN', 'USER_CREATE', 'EXPORT_REPORT'
    module = models.CharField(max_length=50)   # e.g., 'hrm', 'inventory', 'accounts'
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        user_str = self.user.username if self.user else "Anonymous"
        return f"{user_str} - {self.action} at {self.timestamp}"


def get_client_ip(request):
    if not request:
        return None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def log_action(user, action, module, description, ip_address=None):
    """
    Utility function to log a system audit action.
    """
    try:
        AuditLog.objects.create(
            user=user if user and user.is_authenticated else None,
            action=action,
            module=module,
            description=description,
            ip_address=ip_address
        )
    except Exception as e:
        # Prevent logging errors from crashing the main flow
        print(f"Failed to write audit log: {e}")


# ────────────────────────────────────────────────────────
# Signals to log Auth events
# ────────────────────────────────────────────────────────

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    log_action(
        user=user,
        action='LOGIN',
        module='auth',
        description=f"User '{user.username}' successfully logged in.",
        ip_address=ip
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    log_action(
        user=user,
        action='LOGOUT',
        module='auth',
        description=f"User '{user.username if user else 'Unknown'}' logged out.",
        ip_address=ip
    )

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    ip = get_client_ip(request)
    username = credentials.get('username', 'Unknown')
    log_action(
        user=None,
        action='LOGIN_FAILED',
        module='auth',
        description=f"Failed login attempt for username '{username}'.",
        ip_address=ip
    )
