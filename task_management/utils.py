from rest_framework.response import Response

def custom_response(success=True, data=None, message="", status=200):
    return Response({
        "success": success,
        "data": data if data is not None else [],
        "message": message
    }, status=status)