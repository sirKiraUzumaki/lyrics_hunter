import requests
from bs4 import BeautifulSoup

class hunter():
    """
    # Lyrics-Hunter - Ayush Lakra
    
    Class containing different function to scrape lyrics from different websites.
    
     - azscrapper function - scrapes lyrics from https://www.azlyrics.com
    """
    
    
    def azscrapper(song_name):
        """
        This function scrapes lyrics from AZlyrics website https://www.azlyrics.com
        This function initially finds the link to the song then calls another function to extracts the whole lyrics and other information
        
        :param song_name: Name of any song
        :type song_name: str
        :return: dictionary containing Song Title, Artist, Album name, Album art and Lyrics
        :rtype: dictionary
        example:
            azscrapper('love story')
        output:
            {
                'title': 'Love Story',
                'artist': 'Taylor Swift', 
                'album': 'Fearless', 
                'album_art': 'https://www.azlyrics.com/images/albums/699/28b9efd2b441f00110868e34ee368189.jpg',
                'lyrics': '\n\n\n\r\nWe were both young when I first saw you\nI close my eyes and the flashback starts:\nI\'m standing there\nOn a balcony in summer air\n\nSee the lights, see the party, the ball gowns\nSee you make your way through the crowd\nAnd say, "Hello."\nLittle did I know\n\nThat you were Romeo, you were throwing pebbles\nAnd my daddy said, "Stay away from Juliet."\nAnd I was crying on the staircase\nBegging you, "Please don\'t go."\nAnd I said\n\n"Romeo, take me somewhere we can be alone\nI\'ll be waiting. All there\'s left to do is run\nYou\'ll be the prince and I\'ll be the princess\nIt\'s a love story. Baby, just say \'Yes\'."\n\nSo, I sneak out to the garden to see you\nWe keep quiet \'cause we\'re dead if they knew\nSo, close your eyes\nEscape this town for a little while\nOh, oh\n\n\'Cause you were Romeo. I was a scarlet letter\nAnd my daddy said, "Stay away from Juliet."\nBut you were everything to me\nI was begging you, "Please don\'t go!"\nAnd I said\n\n"Romeo, take me somewhere we can be alone\nI\'ll be waiting. All there\'s left to do is run\nYou\'ll be the prince and I\'ll be the princess\nIt\'s a love story. Baby, just say \'Yes\'\n\nRomeo, save me. They\'re trying to tell me how to feel\nThis love is difficult but it\'s real\nDon\'t be afraid. We\'ll make it out of this mess\nIt\'s a love story. Baby, just say \'Yes\'."\n\nOh, oh, oh\n\nI got tired of waiting\nWondering if you were ever coming around\nMy faith in you was fading\nWhen I met you on the outskirts of town\nAnd I said\n\n"Romeo, save me. I\'ve been feeling so alone\nI keep waiting for you, but you never come\nIs this in my head? I don\'t know what to think."\nHe knelt to the ground and pulled out a ring and said\n\n"Marry me, Juliet. You\'ll never have to be alone\nI love you, and that\'s all I really know\nI talked to your dad. Go pick out a white dress\nIt\'s a love story. Baby, just say \'Yes\'."\n\nOh, oh, oh, oh, oh, oh\n\n\'Cause we were both young when I first saw you\n\n\n\n\n\r\n'
            }

        """
        
        
        # Original query
        Oquery = song_name 
        
        # Spliting and merging it as a single string
        query = Oquery.split(" ")
        query = "+".join(query)
        
        # Link for the search query
        link = f"https://search.azlyrics.com/search.php?q={query}&x=794b2fcf852f131da912bbad6a3c3d76ea0d1900959d90ace6a1472773191bbd"
        
        # Putting a request
        req = requests.get(link)

        # Parsing html content through BeautifulSoup
        soup = BeautifulSoup(req.text, 'html.parser')
        
        # Parsing the first song link
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        songURL = links[28]


        def extractor(URL):
            """
            This function extracts the lyrics from the given URL of azlyrics site
            
            :param URL: URL for the song
            :type URL: str
            
            example:
                lyrics("https://www.azlyrics.com/lyrics/taylorswift/lovestory.html")
                
            """
            
            req = requests.get(URL)
            soup = BeautifulSoup(req.text, 'html.parser')

            # Extracting Song Singer, Title and Album name
            info = []
            for link in soup.find_all('b'):
                info.append(link.string)
            singer = str(info[0])[0: -7]
            title = str(info[1])[1: -1]
            album = ''
            album_img = ''
            
            # Checking if the song is from an album
            if (len(info) > 2):
                # Album name
                album = str(info[2])[1: -1] 
                
                # Extracting Album Image
                img = []
                for link in soup.find_all('img'):
                    img.append(link.get('src'))
                album_img = "https://www.azlyrics.com"+img[-2]
                # print(album, album_img)
            
            # print(singer, title)

            #Extracting Lyrics
            lyrics =[]
            for link in soup.find_all('div'):
                lyrics.append(link.text)
            lyrics = str(lyrics[10]).split('if  ( /Android')
            lyrics = lyrics[0].split(f'"{title}"')[2]
            # print(lyrics)

            # Extracting Album Image
            img = []
            for link in soup.find_all('img'):
                img.append(link.get('src'))
            album_img = "https://www.azlyrics.com"+img[-2]
            # print(album_img)
            
            
            # Returns the following dictionary
            data = {
                'title': title,
                'artist': singer,
                'album': album,
                'album_art': album_img,
                'lyrics': lyrics
            }
            return data
        
        # Calling the extractor function and returning it
        return extractor(songURL)