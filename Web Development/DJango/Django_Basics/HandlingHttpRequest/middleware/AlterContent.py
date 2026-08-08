# this middleware is used to alter the content of the response before sending it to user


def AlterUserResponseMiddleware(get_response):
    def middleware(request):
        response = get_response(request)
        if response.streaming != True:
            content = "<small> regardless of what the dev wants you to see, I will always return this view</small>"
            response.content = content
        return response
    return middleware