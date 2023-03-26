# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # Instead of array use Dictionary https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # Add key value or replace existing value
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # if key exists delete it
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            response = 'not found'
            # If key exists use value as response
            if cur_query.number in contacts:
                response = contacts[cur_query.number]
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
