import base64
import json
from datetime import datetime, timedelta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cognito_client = boto3.client('cognito-idp')
    # response = cognito_client.initiate_auth(
    #     AuthFlow="USER_PASSWORD_AUTH",
    #     ClientId="79rgfpl01bhumo22i8gppi7q36",
    #     AuthParameters={
    #         "USERNAME": "darren",
    #         "PASSWORD": "Water-Tiger-Twen-202403"
    #     }
    # )
    # access_token = response["AuthenticationResult"]["AccessToken"]
    access_token = "eyJraWQiOiJPbkw1Q3o2WFZ1V0IyNkcxNVFEYlNGYVwvam1JY1d0NVdlOG0ra1JmZ0YwND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4ZWJmMmY0ZC1hMWMzLTQ3NGItOWY0Ni04MGFhYjA1ZTU0ZjYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfS0lkY2dXM3ZGIiwiY2xpZW50X2lkIjoiNzlyZ2ZwbDAxYmh1bW8yMmk4Z3BwaTdxMzYiLCJvcmlnaW5fanRpIjoiYWZjZjI2N2YtMjhhZS00MzkyLWEzYmMtNjBiOWYyYmU1MWViIiwiZXZlbnRfaWQiOiJjNzJkN2VhZC1jMWQ0LTRjNDItOTk5Yy0xZTlhNmIxZDQwYzYiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNzExOTIwOTQ4LCJleHAiOjE3MTE5MjQ1NDgsImlhdCI6MTcxMTkyMDk0OCwianRpIjoiZjkwZThjZmEtMDUzZS00OGM5LTlmMGUtMjQxMmNlN2I5OWEzIiwidXNlcm5hbWUiOiJkYXJyZW4ifQ.p4tqo_H1vDyH9Lcekc1vPCyJGA-Kp5lT2QFSiTU9pBUbbwxP0ldyOke869ZXg960LPHK4wobtK1h5var-DTyMNqYuQnxyBxtFGJlzJA8YHxl-SVr2rAVXE4LnC_GfCDILRlmCWHSoTQMv546ijdL9rutcThXPjdiD_wOWp9rjKFNuWr5vdkrpyJOO7fY1zFjIIk-5pQc3L6E4ucabHQgVTgi_WbIwk_wHKcDIls0aivfccjdWajbZRXSio-Hit6FLsmBejaFIxutAIB_I1ijb4fW8u9gWOsSvA0iH6YMuhKYg5nHm-351iBypO37fvetPvLsIkKrXexpCT30uKbeeQ"

    # print(access_token)

    id_token = "eyJraWQiOiJmd01oUnMxOWxZcXYyZFBOaHA3cldiN1BicmVFQVlCZlJEeDBjR3NmeGs4PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI4ZWJmMmY0ZC1hMWMzLTQ3NGItOWY0Ni04MGFhYjA1ZTU0ZjYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb21cL2FwLW5vcnRoZWFzdC0xX0tJZGNnVzN2RiIsImNvZ25pdG86dXNlcm5hbWUiOiJkYXJyZW4iLCJvcmlnaW5fanRpIjoiZGExNGQwN2EtNjUwNi00ZGRmLTk3NDgtMWM2M2UxNDEwNWU0IiwiYXVkIjoiNzlyZ2ZwbDAxYmh1bW8yMmk4Z3BwaTdxMzYiLCJldmVudF9pZCI6IjNlZmRiNzE0LWFjOGQtNDRmZC05ZDllLWI1NzdmNGJlMTg0NiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzExOTI0NTU4LCJleHAiOjE3MTE5MjgxNTgsImlhdCI6MTcxMTkyNDU1OCwianRpIjoiYTkxNDhhZjMtYjk3Zi00N2I1LThkNjctNDM4ZjZmODkxMWE0IiwiZW1haWwiOiJkYXJyZW5saS5kZXZlbG9wQGdtYWlsLmNvbSJ9.stobm1yLpvnlanf8tzI7hSJcdXyT1zRKJ9Tphu5KqAU-qxj51Sis191UMrFspkimc6gL0DUMqoY0-IOt-h9BrL6YCgaLqBKTm9w__FZ9ZmnOQhbIFofQDUHO2_BOi7IEQwTuWOwDd6ova3Wlxpst8pP04KEL2FuLiHw4o_X4zodjseloMInZ15fRVy3oHZUjGwerPQoT-19_hnfqAeKeEur9mEHVVIuFRHMMM4rNw_0isihC1lFVdO6sKHzx3Kk3-0e1IGS822fOZ0dkS9iBRGniEgXi2sCBpCuYGdyrga7YsO42CRkMjEJSHhgO6ObWCFm0WMy0Mo5OuABxGGM7ew"
    # id_key = "0BGfuV0Prj7XONCrKVmgAkhTjZnG37SBwT6S5OwKDlTtx9k_BfYF8bOf_KaYAUvE6vrG-cNyTPaxVi-Xy7CPminTKG0Bferx8NiOhpBldke3RCCTuKoNi4QefXi9yEpRnWSC2okB_dOqWkPLVVl0LyadZv068_JZn4zLhKoVHEsIIXlZdiXWK83i0Pyg74v0MDGr0jeeqbdY1hiCra72eQ0UlClde4nZz0RUVLTeYIwCvSSftKXG9kChywS7aGjDV-NK7OGcodK4VJMHJqj6BAzEPPkGuGYZH3jcZQ7xPOnSdftFtA5uDKZlOFMZSspkGvEI8zvCJSPl2jePZ0gCTw"
    # padding_needed = len(id_key) % 4
    # if padding_needed:
    #     id_key += '=' * (4 - padding_needed)
    # id_key = base64.b64decode(id_key).hex()
    # id_key = "-----BEGIN PUBLIC KEY-----\n" + id_key + "\n-----END PUBLIC KEY-----"
    # print(jwt.decode(id_token, id_key, algorithms=["RS256"]))

    caroo = base64.b64decode(id_token.split(".")[1]).decode("utf-8")
    json_dict = json.loads(caroo)
    print(json_dict["exp"])
    exp_time = datetime.utcfromtimestamp(json_dict["exp"]) + timedelta(hours=2)
    is_expired = datetime.utcnow() >= exp_time
    time_diff = datetime.utcnow() - exp_time
    print(time_diff.total_seconds())
    print(is_expired)
