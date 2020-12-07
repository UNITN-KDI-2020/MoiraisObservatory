import scrapy

class ViatorSpider(scrapy.Spider):

    name = 'viator_spider'

    start_urls = [
        "https://www.viator.com/en-GB/tours/Trento/Rio-Black-Canyoning/d29399-122889P4",
        "https://www.viator.com/en-GB/tours/Trento/Private-Day-Tour-by-Car-the-Great-Dolomites-Road/d29399-44040P11",
        "https://www.viator.com/en-GB/tours/Trento/Fun-Climb/d29399-122889P1",
        "https://www.viator.com/en-GB/tours/Trento/Rafting-Extra/d29399-65122P2",
        "https://www.viator.com/en-GB/tours/Trento/River-Rafting-for-Families/d29399-65122P1",
        "https://www.viator.com/en-GB/tours/Trento/Via-Ferrata-Rio-Ruzza/d29399-122889P13",
        "https://www.viator.com/en-GB/tours/Trento/Palvico-Canyoning/d29399-122889P9",
        "https://www.viator.com/en-GB/tours/Trento/The-glacial-lakes-of-the-Cevedale/d29399-155124P18",
        "https://www.viator.com/en-GB/tours/Trento/Via-Ferrata-Colodri-2-0/d29399-122889P5",
        "https://www.viator.com/en-GB/tours/Trento/8-DAY-TOURS-IN-THE-DOLOMITES-BY-MOUNTAIN-BIKE/d29399-184972P3",
        "https://www.viator.com/en-GB/tours/Trento/Rental-and-tours-with-Electric-bike-guide-on-Monte-Bondone-or-Pine-on-the-lakes/d29399-172840P1",
        "https://www.viator.com/en-GB/tours/Trento/Crosscountry-Bike-Route-to-Campo-from-Malcesine-Lake-Garda/d29399-46400P2",
        "https://www.viator.com/en-GB/tours/Trento/Yoga-individual-lessons/d29399-205236P5",
        "https://www.viator.com/en-GB/tours/Trento/Private-Day-Tour-by-car-The-Heart-of-the-Dolomites-from-Trento/d29399-44040P17",
        "https://www.viator.com/en-GB/tours/Trento/Easy-Bike-Route-with-MBT-Guide-on-Monte-Baldo-the-Red-Tour/d29399-46400P1",
        "https://www.viator.com/en-GB/tours/Trento/Discovering-Monte-Baldo-ridge-from-Lake-Garda/d29399-266588P4",
        "https://www.viator.com/en-GB/tours/Lake-Garda/Lake-Garda-Tour/d27338-29282P11",
        "https://www.viator.com/en-GB/tours/Lake-Garda/Dolomites-tour-from-Lake-Garda/d27338-29282P10",
        "https://www.viator.com/en-GB/tours/Lake-Garda/Lake-Garda-Tour-by-Coach/d27338-167354P4"
    ]

    def parse(self, response):
        
        # Deriving the basic fields
        title = response.xpath("//h1[@id='productTitle']/text()").extract_first()
        duration = response.xpath("//div[@class='d-flex d-md-inline-flex align-items-center text-nowrap mr-md-4 pb-2 pt-2'][1]/span//text()").extract_first()
        category = response.xpath('//nav[@aria-label="breadcrumb"]/ol/li[@class="breadcrumb-item"][last()]/a/span/text()').extract_first()
        dep_place = response.xpath("//h3[text()='Departure Point']//following-sibling::text()[contains(., 'Italy')]").extract_first()
        
        if dep_place is None:
            dep_place = response.xpath('//h3[text()="Departure Point"]//following-sibling::div/text()[contains(., "Italy")]').get()

        img_src = response.xpath("//img[@class='hero-image-initial embed-responsive-item photo'][1]/@src").get()

        # Extracting included items in the trip
        inclusions = []
        for item in response.xpath("//div[@class='inclusions-content ']/div[@class='py-1 inclusions-exclusions-item d-flex']"):
            element = item.xpath('.//div[2]/text()').get()
            inclusions.append(element)

        dep_time = response.xpath('//div[@class="vcs-departure-times"]//text()').get()
        rating_overall = response.xpath('//div[@class="overall-rating-number"]/text()').get()
        rating_total = response.xpath('//div[@class="overall-rating-total"]/text()').get()

        # Calendar dates on which the trip is available
        dates = response.xpath('//div[@class="col-sm-12 col-md-4 col-lg-12 mb-3 h-100 btn-block pr-md-3 pr-lg-0 small availabilityCalendar date-picker-wrapper price-calendar"]/input/@data-enabled-dates').getall()

        # Assembling histogram values and respective frequencies with regard to the rating
        rating_hist = {}
        for item in response.xpath("//div[@class='histogram-rating']"):
            k = item.xpath("./@data-rating").get()
            v = item.xpath("./@data-count").get()
            rating_hist[k] = v

        price = response.xpath('//div[@class="text-left"]/div[@class="mb-1 from-price-container"]/p/span[@class="font-weight-normal price-font"]/text()').extract_first()

        yield {
            'title': title,
            'duration': duration,
            'category': category,
            'dep_place': dep_place,
            'dep_time': dep_time,
            'img_src': img_src,
            'inclusions': inclusions,
            'rating_overall': rating_overall,
            'rating_total': rating_total,
            'rating_hist': rating_hist,
            'price': price,
            'dates': dates
        }