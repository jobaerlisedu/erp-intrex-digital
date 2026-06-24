from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password
from config.firebase import db

class FirestoreBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        try:
            # 1. Query Firestore for the user doc
            user_doc_ref = db.collection('users').document(username)
            user_doc = user_doc_ref.get()

            if user_doc.exists:
                data = user_doc.to_dict()
                firestore_hash = data.get('password')
                
                if not firestore_hash:
                    return None

                # Verify password against Firestore hash
                if check_password(password, firestore_hash):
                    # Find or create local user
                    try:
                        user = User.objects.get(username=username)
                    except User.DoesNotExist:
                        user = User(username=username)
                    
                    # Prevent signal loop back to firestore during sync
                    user._syncing = True
                    user.email = data.get('email', '')
                    user.first_name = data.get('first_name', '')
                    user.last_name = data.get('last_name', '')
                    user.is_staff = data.get('is_staff', False)
                    user.is_superuser = data.get('is_superuser', False)
                    user.is_active = data.get('is_active', True)
                    user.password = firestore_hash
                    user.save()

                    # Sync groups
                    user.groups.clear()
                    group_names = data.get('groups', [])
                    for group_name in group_names:
                        group, _ = Group.objects.get_or_create(name=group_name)
                        user.groups.add(group)

                    return user
            else:
                # 2. User not in Firestore, check local model backend.
                # If they authenticate locally, we upload/sync them to Firestore!
                try:
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        # Save to Firestore so it is synchronized
                        user_data = {
                            'username': user.username,
                            'email': user.email,
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'password': user.password,
                            'is_staff': user.is_staff,
                            'is_superuser': user.is_superuser,
                            'is_active': user.is_active,
                            'groups': [g.name for g in user.groups.all()]
                        }
                        db.collection('users').document(user.username).set(user_data)
                        return user
                except User.DoesNotExist:
                    pass

        except Exception as e:
            print(f"Error in FirestoreBackend authentication: {e}")
        
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def sync_users_from_firestore():
    """Sync all users from Firestore into the local SQLite database."""
    try:
        users_ref = db.collection('users').stream()
        for doc in users_ref:
            data = doc.to_dict()
            username = doc.id
            if not username:
                continue

            email = data.get('email', '')
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')
            password = data.get('password', '')
            is_staff = data.get('is_staff', False)
            is_superuser = data.get('is_superuser', False)
            is_active = data.get('is_active', True)
            group_names = data.get('groups', [])

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)

            user._syncing = True
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            if password:
                user.password = password
            user.is_staff = is_staff
            user.is_superuser = is_superuser
            user.is_active = is_active
            user.save()

            # Sync groups
            user.groups.clear()
            for group_name in group_names:
                group, _ = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)
    except Exception as e:
        print(f"Error syncing users from Firestore: {e}")
