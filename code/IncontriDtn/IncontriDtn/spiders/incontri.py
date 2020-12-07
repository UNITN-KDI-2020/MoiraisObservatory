import scrapy

class IncontriSpider(scrapy.Spider):

    name = 'Incontri'

    start_urls = [
        "https://www.trentotoday.it/eventi/mauro-corona-filmfestival-2020.html", 
        "https://www.trentotoday.it/eventi/mart-pasolini.html", 
        "https://www.trentotoday.it/eventi/trentino-tree-agremeent-2020.html", 
        "https://www.trentotoday.it/eventi/mascherine-labarca-covid.html", 
        "https://www.trentotoday.it/eventi/sandro-formica-economia-felicita.html", 
        "https://www.trentotoday.it/eventi/muse-settembre-2020.html", 
        "https://www.trentotoday.it/eventi/festival-sport-2020.html", 
        "https://www.trentotoday.it/eventi/dolomiti-incontri-san-martino.html", 
        "https://www.trentotoday.it/eventi/viot-muse-estate.html", 
        "https://www.trentotoday.it/eventi/castelli-gioco-oca-2020.html", 
        "https://www.trentotoday.it/eventi/archeologia-estate-2020.html", 
        "https://www.trentotoday.it/eventi/nuvolette-rovereto-2020.html", 
        "https://www.trentotoday.it/eventi/biblioteca-coronavirus-prestiti.html", 
        "https://www.trentotoday.it/eventi/biblioteca-prestiti-coronavirus.html", 
        "https://www.trentotoday.it/eventi/muse-universita-coronavirus.html", 
        "https://www.trentotoday.it/eventi/festival-economia-2020.html", 
        "https://www.trentotoday.it/eventi/musei-gioco-2020.html", 
        "https://www.trentotoday.it/eventi/fisv-days-scuola-scienza.html", 
        "https://www.trentotoday.it/eventi/spasso-per-trento-2020.html", 
        "https://www.trentotoday.it/eventi/muse-iorestoacasa-2020.html"
    ]

    def parse(self, response):
        
        # The title extraction
        title = response.xpath('//h1[@class="entry-title"]/text()').get()
        rating = 0

        # The rating collection
        star_elems = response.xpath("//*[local-name() = 'svg'][@class='icon medium icon-star icon-star--coloured']").getall()
        rating = len(star_elems)
        
        
        # Derivation of meta information
        meta = {}
        for field in response.xpath('//ul[@class="u-unstyled details-list"]/li'):
            k = field.xpath('.//span/text()').get()
            v = [txt.strip() for txt in field.xpath('.//dl//text()').getall() if txt.strip() != ""]
            meta[k] = v
        
        # Extraction of the argomenti
        materia = []
        for argomento in response.xpath('//a[@class="btn block-btn default-btn rounded-btn"]/text()'):
            materia.append(argomento.get())

        # Image resource identifier
        img_url = response.xpath('//figure[@class="entry-media"]/a/@href').extract_first()

        # Body paragraph accumulation
        paragraphs = []
        for paragraph in response.xpath('//div[@class="entry-content-body"]/p/text()'):
            paragraphs.append(paragraph.get())

        yield {
            'title': title,
            'rating': rating,
            'meta': meta,
            'materia': materia,
            'figure': img_url,
            'body': paragraphs
        }