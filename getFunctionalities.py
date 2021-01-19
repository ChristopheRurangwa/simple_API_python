import requests
from flask import jsonify


class GetData:
    """Takes in a field; tag, will return the status code"""
    '''which in turn is used to check if the url is ok, or 200'''

    def valid_requ(param1):

        req = requests.get(f'https://api.hatchways.io/assessment/blog/posts?tag={param1}')
        return req.status_code

    # collects data from the api, based on the tag entered
    def api_fetcher(tags, sort, dire):

        req = requests.get(
            f'https://api.hatchways.io/assessment/blog/posts?tag={tags}&sortBy={sort}&direction={dire}')

        data = req.json()

        i = 0  # <- json index
        j = 1  # <-json index

        for tag in data['posts'][i]['tags']:
            if data['posts'][++i]['tags'] != data['posts'][++j]['tags']:
                json_data = data['posts']
                return str(json_data)
            return "No data found"

    '''Adds to the set 'unique_post' the json data casted into string'''

    def post_fetcher(specTag1, sort, dire):

        unique_post = set()  # <-- will not take any duplicates
        req = requests.get(
            f'https://api.hatchways.io/assessment/blog/posts?tag={specTag1}&sortBy={sort}&direction={dire}')

        data = req.json()

        i = 0  # <-json index

        for tag in data['posts'][i]['tags']:
            # adding the string value returned by the api_fetcher() method to the set to eliminate duplicates
            unique_post.add(GetData.api_fetcher('culture', sort, dire))
            unique_post.add(GetData.api_fetcher('health', sort, dire))
            unique_post.add(GetData.api_fetcher('science', sort, dire))
            unique_post.add(GetData.api_fetcher('culture', sort, dire))
            unique_post.add(GetData.api_fetcher('design', sort, dire))
            unique_post.add(GetData.api_fetcher('history', sort, dire))
            unique_post.add(GetData.api_fetcher('politics', sort, dire))
            break

        return str(unique_post)

    '''makes a get request depending on which parameters are passed in the method.
    Also the method makes sure no empty parameter will be skipped without notifying user'''

    def make_req(tag1, sort, dire):

        if tag1 == "":
            error1 = {"error": "Tags parameter is required"}
            return jsonify(error1), 400  # <-- will return status code 400 when a parameter is missing of makereq(...)
        elif sort == "":

            error2 = {"error": "sortBy parameter is invalid"}
            return jsonify(error2), 400
        elif dire == "":
            error3 = {"error": "sortBy parameter is invalid"}
            return jsonify(error3), 400

        return GetData.post_fetcher(tag1, sort, dire)
