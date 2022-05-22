import urllib.request
import wikipedia

while True:
    with open('in-pipe.txt', 'r+') as pipe:
        read_data = pipe.read()
        pipe.truncate(0)
        pipe.seek(0)

    if read_data:
        try:

            # Using .search() to return more accurate result than using .page() method
            name = wikipedia.search(read_data)[0]

            # Turned off auto-suggest & use more accurate name from .search()
            page = wikipedia.page(title=name, auto_suggest=False)

            # have matching characters for url
            url_name = name.replace(" ", "_")
            url_name = url_name.lower()

            # url length
            url_length = (float('inf'))

            # to hold the shortest url
            shortest_url = "Default: No results"

            for url in page.images:
                if ('.jpg' in url) and (url_name in url.lower()):
                    if url_length > len(url):
                        shortest_url = url
                        url_length = len(url)

            print(shortest_url)

            ## Save image & return path to image
            if url_name in shortest_url.lower():
                #Save
                with open(f'{url_name}.jpg', "wb") as fp:
                    fp.write(urllib.request.urlopen(shortest_url).read())

                #Path
                with open('out-pipe.txt', 'w+') as pipe:
                    pipe.write(f'./{url_name}.jpg')

        # Catching error
        except:
            # Report error
            with open('out-pipe.txt', 'w+') as pipe:
                pipe.write("Cannot find: " + read_data)
            
            # Some error discontinues while-loop, 'continue' helps stay in the loop
            continue