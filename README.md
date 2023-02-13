# lyrics_hunter
Lyrics Hunter is a python library to scrape lyrics from websites. It is a web scraping library designed to extract song lyrics from websites. The library currently only supports scraping from lyrics.com but in near future, it will support more websites.

# Installation
`pip install lyrics-hunter`

# Usage
To use Lyrics Hunter, you will first need to import the library into your Python script using the following code:

`import lyrics_hunter`

To retrieve lyrics for a particular song use the search function:

`lyrics_hunter.search(<song name>)`

This will result in a dictionary containing Song Title,  Artist, Album, Lyrics, Album Art, Artist Art, and Song Art.
`{
            'title': title,
            'artist': artist,
            'album': album,
            'lyrics': lyrics,
            'img': {
                'album': album_art,
                'artist': artist_art,
                'song': song_art
            }
}`

# Example
code:
`import lyrics_hunter

print(lyrics_hunter.search("love story"))`

output:
`{
    "title": "Love Story",
    "artist": "Taylor Swift",
    "album": "Fearless [Bonus Tracks #1]",
    "lyrics": "We were both young when I first saw you\r\nI close my eyes and the flashback starts\r\nI'm standing there on a balcony in summer air\r\n\r\nSee the lights, see the party, the ball gowns\r\nSee you make your way through the crowd\r\nAnd say hello\r\n\r\nLittle did I know\r\nThat you were Romeo, you were throwing pebbles\r\nAnd my daddy said, \"Stay away from Juliet\"\r\nAnd I was crying on the staircase\r\nBegging you, please, don't go\r\n\r\nAnd I said,\r\n\"Romeo, take me somewhere we can be alone\r\nI'll be waiting, all that's left to do is run\r\nYou'll be the prince and I'll be the princess\r\nIt's a love story, baby just say yes\r\n\r\nSo I sneak out to the garden to see you\r\nWe keep quiet 'cause we're dead if they knew\r\nSo close your eyes, escape this town for a little while\r\n'Cause you were Romeo, I was a scarlet letter\r\nAnd my daddy said \"Stay away from Juliet\"\r\nBut you were everything to me, I was begging you, please, don't go\r\n\r\nAnd I said Romeo take me somewhere we can be alone\r\nI'll be waiting, all there's left to do is run\r\nYou'll be the prince and I'll be the princess\r\nIt's a love story baby just say yes\r\n\r\nRomeo save me, they're trying to tell me how to feel\r\nThis love is difficult, but it's real\r\nDon't be afraid, we'll make it out of this mess\r\nIt's a love story, baby just say \"Yes\"\r\n\r\nOh, oh\r\n\r\nI got tired of waiting\r\nWondering if you were ever coming around\r\nMy faith in you was fading\r\nWhen I met you on the outskirts of town\r\n\r\nAnd I said\r\n\"Romeo save me, I've been feeling so alone\r\nI keep waiting for you but you never come\r\nIs this in my head? I don't know what to think\"\r\n\r\nHe knelt to the ground and pulled out a ring and said\r\n\"Marry me, Juliet, you'll never have to be alone\r\nI love you and that's all I really know\r\nI talked to your dad, go pick out a white dress\r\nIt's a love story, baby just say yes\"\r\n\r\nOh, oh,\r\nOh, oh\r\n\r\n'Cause we were both young when I first saw you.",
    "img": {
        "album": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSStwIrFMWj7RGWgnr1rOzkmTTLz0Wxl4Al3XkViHzQfSidiSJhht9bu8g&s",
        "artist": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/191125_Taylor_Swift_at_the_2019_American_Music_Awards_(cropped).png/211px-191125_Taylor_Swift_at_the_2019_American_Music_Awards_(cropped).png",
        "song": "https://upload.wikimedia.org/wikipedia/en/0/01/Taylor_Swift_-_Love_Story.png"
    }
}
`
