import requests

# constant
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "foo",
    "body": "bar",
    "url": "https://jsonplaceholder.typicode.com/posts",
    "userId": 1,
    "err": {"massages": "Specific Error in response: error", "id": "1"},
}


def test_post_api():
    # Send the request to the API
    response = requests.post(url, json=payload)

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    # Parse the response JSON once
    response_data = response.json()
    try:
        # Check if there is an 'err' field in the response
        error_data = response_data.get("err", {}).get("massages") or None
        if error_data:
            raise ValueError(f"Error in response: {error_data}")

        # If the status code is not 200, raise a custom error
        if response.status_code != 200 and response.status_code != 201:
            raise ValueError(f"Expected status code 200 or 201, but got {response.status_code}")

        # Check if the title is "foo"
        if response_data.get("title") != "foo":
            raise ValueError(f"Expected title 'foo', but got {response_data.get('title')}")

        # If all checks pass, return the response data
        return {"status_code": response.status_code, "url": response_data.get("url")}
    except requests.exceptions.RequestException as error:
        # Handle issues related to the request
        raise RuntimeError(f"Error with the API request: {error}")

    except ValueError as ve:
        # Handle any custom ValueErrors (e.g., wrong status code, wrong title)
        raise ve

    except Exception as e:
        # Handle unexpected errors
        raise Exception(f"Unexpected error: {e}")


def main():
    try:
        res = test_post_api()
        print(res)
    except Exception as error:
        print(f"Error: {error}")


# Run the function
if __name__ == "__main__":
    main()
