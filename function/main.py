from flask import escape, abort
import functions_framework, json

@functions_framework.http
def da_cart(request):
    if request.method == "HEAD":
        print("HEAD shot")
        return "head shot ;-)"
    elif request.method == "POST":
        content_type = request.headers.get('content-type')

        if content_type == None:
            print("WARNING: no content type defined")
        else:
            if content_type == "application/json":
                request_json = request.get_json(silent=True)
                
                if request_json and "thrivecart_secret" in request_json:
                    da_secret = request_json["thrivecart_secret"]
                    #this will change to an actual secret not in code
                    #this is just a test of the flow
                    if da_secret != "TESTSECRET":
                        raise ValueError("ERROR: request not from da")
                else:
                    raise ValueError("JSON is invalid, or missing a property")
                    #print("JSON is invalid, or missing a property")
                
                da_event = request_json["event"]
                print(f"DATA: {da_event}")

            else:
                return abort(405)

        return "deniseanne.com success"
    else:
        return abort(405)