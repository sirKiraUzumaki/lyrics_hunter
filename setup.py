import setuptools

with open("README.md", "r") as fh:
	description = fh.read()

setuptools.setup(
	name="lyrics-hunter",
	version="1.0.0",
	author="Ayush Lakra",
	author_email="ayushlakra846@gmail.com",
	packages=["lyrics-hunter", "lyrics-hunter.hunter"],
	description="Python Lyrics Scrapper",
	long_description="Lyrics Hunter is a python library to scrape lyrics from websites. It is a web scraping library designed to extract song lyrics from websites. The library currently only supports scraping from AZLyrics but in near future, it will support more websites.",
	long_description_content_type="text/markdown",
	url="https://github.com/sirKiraUzumaki/lyrics_hunter",
	license='MIT',
	python_requires='>=3.7',
	install_requires=['beautifulsoup4', 'requests']
)
