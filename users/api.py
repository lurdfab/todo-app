from rest_framework.generics import GenericAPIView
from users.serializers import RegisterSerializer, LoginSerializer
from rest_framework  import response, status, permissions
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request
from .tokens import create_jwt_pair_for_user


# Create your views here.
class RegisterAPIView(GenericAPIView):

    authentication_classes = [] #we don't want the user to be authenticated before registering leave empty or specify the kind of authentication we want to use there

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

    authentication_classes = [] #we don't want the user to be authenticated before login leave empty or specify the kind of authentication we want to use there

    serializer_class = LoginSerializer

    
    def post(self, request:Request): 
        username= request.data.get('username')
        password = request.data.get('password')

        user=authenticate(username=username, password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login was succesful",
                "tokens": tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "invalid username and password"})

    def get(self, request:Request): 
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK )
     