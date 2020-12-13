## Formal Modelling

### 1. Namespaces for the Domain

Our transition to the formalization phase is marked by our undertaking in search of already existing vocabulary terminologies that would cover the clumsy etypes defined in the informal modelling phase and the namespaces containing them. This is in an attempt to bring, as closer as we could, the gap between our rough sketch for the event domain and the commonly acknowledged standard for the same domain, so that we could get stuck by a better idea to improve the current model. 

The most frequent term *'Event'* in the EER at our disposal possesses relatively a fewer number of senses, ruling out the most of our search space in [Linked Open Vocabularies](https://lov.linkeddata.es/dataset/lov).

![Event vocabularies](vocabs.png)

As demonstrated in the search result capture, there are two possible formal schemas for us to appropriate into our application. 

* At first glance, [schema.org](http://schema.org/Event) appears to fit the profile we're looking for the most parts because it is a widespread shared terminology-space and the predicates belonging there are able to cover the majority of our object (and data) properties, which means our data integration to a bigger knowledge graphs could be guarenteed and it increases the chance that concepts and senses in the UKC-KB are located way more accurately if we start from this namespace. Unfortunately, the problem arises when it comes to the sub-event categorization. It is true that we enumerated our event types instead of creating subcategories for each, just like [schema:Event](http://schema.org/Event) offers, such as detaching off *'TheaterEvent', 'MusicEvent' and 'DanceEvent'*. However, as in the argument from the previous phase, the scarcity of mining tools for extracting essential and defining properties for each subtype led to the decision to leave them under the same entity type. For example, let us say, we wish to derive *'producers', 'cast', 'stage designer'* from the description (e.g. body paragraph) property of *'TheaterEvent'* entity. Not only they are written in human natural language, but also they vary in ideosyncrasies authors display them in, making it impossible for us to write regex expressions to filter them out. In addition, although we could use APIs for named entity recognition, these cannot manage to contextualize what they have captured even if the entity in the description and its type have been recollected.
* On the other hand, [event](http://motools.sourceforge.net/event/event.html) is a lightweight ontology that incorporates [foaf](http://xmlns.com/foaf/0.1/), [time](http://www.w3.org/2006/time#) and [geo](http://www.w3.org/2003/01/geo/wgs84_pos#) to represent its key connections. Given our circumstances, assuming the unorthodox semantic representation we have of the touristic event domain, it is a better choice to embrace this ontology providing us a customization flexibility with respect to dividing the parent class into unfamiliar application-specific subevents. Though it is in no way the best schematization, considering the project period, lack of data diversity and the amount of effort necessary to fragment the properties into smaller ones as described above, we assume our assertions up to the point provided sufficient rational causalities in our decision-making.

![L4 schema knowledge graph (to be modified)](ontology_graph.png)

* Finally, another substantial part of our application, the data representation regarding transit feed system, is covered by [gtfs](http://vocab.gtfs.org/gtfs.ttl#) ontology. Given the datasets, we are sure to decorate them with the classes provided by the namespace. Nonetheless, it doesn't put forward the object properties connecting the domains and ranges, apparently due to changeability in their designs.

### 2. Annotation with the UKC

*[Loading the concept decorations from KOS...]*