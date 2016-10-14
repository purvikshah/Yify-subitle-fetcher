import scrapy
import urlparse
import urllib
#from selenium import webdriver
#from scrapy.pipelines.files import *
accepted_languages = ('English', 'French', 'Spanish', 'German', 'Italian', 'Greek')
accepted_prints = ('720p', '1080p', 'BluRay')
class Filetodw(scrapy.Item):
	file_urls = scrapy.Field()
	files = scrapy.Field()

class Downloads(scrapy.Spider):
	name = 'download'

	def __init__(self):
		thesebaseurls = []
		for x in xrange(1,4):
			pass
			thesebaseurls.append('http://www.yifysubtitles.com/browse/page-%d'%(x))

		self.start_urls = thesebaseurls

	def parse(self, response): 
		download_links = response.xpath("//*[@id='main-left']/div/ul/li/a/@href").extract()
		#print download_links
		for link in download_links:
			subtitle_url =  'http://www.yifysubtitles.com' + link
			#print subtitle_url
			yield scrapy.Request(subtitle_url,self.extract_sub)
			#break
			#Filetodw(file_urls=['http://www.tvsubtitles.net/download-308887.html', 'http://www.ietf.org/images/ietflogotrans.gif'])

	def extract_sub(self, response):
		new_links = response.xpath("//*[@id='movie-info']/div[2]/ul/li/a/@href").extract()
		for link in new_links:
			link = 'http://www.yifysubtitles.com' + link
			#print link
			yield scrapy.Request(link, self.final_extract)
		
		#print '---------------------------------------'

	def final_extract(self, response):
		language = response.xpath("//*[@id='movie-info-main']/div/div[3]/span[2]/text()").extract()
		movie_name = response.xpath("//*[@id='movie-info-main']/div/div[1]/h2/text()").extract()
		url = response.xpath("//*[@id='movie-info-main']/div/a/@href").extract()
		some = url[0]
		urlzip = some[38:]
		#print language
		if language[0] in accepted_languages:
			urllib.urlretrieve(some, urlzip)
			print urlzip
		#print url
		#yield Filetodw(file_urls=url)