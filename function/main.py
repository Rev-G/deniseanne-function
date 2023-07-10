from flask import escape, abort
import functions_framework, json

@functions_framework.http
def hello_get(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    
    if request.method == "HEAD":
        print("HEAD shot")
        return "head shot ;-)"
    elif request.method == "POST":
        content_type = request.headers.get('content-type')

        if content_type == None:
            print("WARNING: no content type defined")
        else:
            if content_type == "application/x-www-form-urlencoded":
                da_event = request.form.get("event")
                print(f"DATA: {da_event}")
            else:
                print(f"WARNING: Unknown content type: {content_type}")

        return "deniseanne.com cart function"
    else:
        return abort(405)