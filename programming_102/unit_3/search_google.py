import sys
import webbrowser

# sys.argv will capture additional info
# passed through the command line

def search(url, query=''):
    '''
    Search google for the query
    '''
    search_url = url + query
    print(search_url)
    
    webbrowser.open(search_url)

print(sys.argv)
for item in sys.argv:
    print(item)

def get_query(query_items):
    '''
    Return the concatenation of query items
    '''
    print(query_items)

def main():
    # sys.argv will capture additional info
    # passed through the command line
    # print(sys.argv)

    args = sys.argv

    # if the user entered additional text in the command line, use that text as the search query
    if len(sys.argv) > 1:
        query = ''
        for i in range(1, len(args)):

            # get the current query item
            query_item = args[i]

            # add the auery item to the query
            query += f'{query_item}'

        
        print(query)

    # q= is the query we'll be searching for
    url = 'https://www.google.com/search?q='
    query = 'python'
    search(url, query)
main()