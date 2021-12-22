from django.contrib.auth import authenticate, get_user_model
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import permissions
import base64
import binascii
import jwt
import requests

class ExampleAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        user = None
        auth = authentication.get_authorization_header(request).split()
        auth_token = auth[1]
        if not auth or auth[0].lower() != b'bearer':
            return None
        if len(auth) == 1:
            msg = _('Invalid basic header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid basic header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)
        try:
            #jwt.decode(<encoded token>,<secret key>,<algorthm>)
            # decodedPayload = jwt.decode(auth_token, None, None)
            # decodedPayload = jwt.decode(auth_token, verify=False)
            # {'user_id': 1, 'username': 'admin', 'exp': 1640118567, 'email': 'admin', 'orig_iat': 1640075367}
            hed = {'Authorization': 'Bearer ' + str(auth_token.decode("utf-8"))}
            url = 'http://authentication-service:8080/auth/user'
            response = requests.get(url, headers=hed)
            user_obj = response.json()
            user = self.create_or_update_user(user_obj)
        except:
            msg = _('Invalid Token.')
            raise exceptions.AuthenticationFailed(msg)
        
        return (user, None)
    
    def create_or_update_user(self, user_obj):
        User = get_user_model()
        groups = user_obj.pop('groups', None)
        user_permissions = user_obj.pop('user_permissions', None)
        # TODO: Update Permissions
        try:
            auth_user = User.objects.get(id=user_obj['id'])
        except User.DoesNotExist:
            user_obj['username'] = user_obj['email']
            user_obj.pop('phone_number', None)
            auth_user = User.objects.create_user(**user_obj)
        return auth_user


class CustomPermission(permissions.BasePermission):
    """
    Custom permission 
    """

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False