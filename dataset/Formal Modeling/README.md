## Formal Modelling

### Namespaces for Event Domain

Our transition to the formalization phase is marked by our undertaking in search of already existing vocabulary terminologies that would cover the clumsy etypes defined in the informal modelling phase and the namespaces containing them. This is in an attempt to bring, as closer as we could, the gap between our rough sketch for the event domain and the commonly acknowledged standard for the same domain, so that we could get stuck by a better idea to improve the current model. 

The most frequent term *'Event'* in the EER at our disposal possesses relatively a fewer number of senses, ruling out the most of our search space in [Linked Open Vocabularies](https://lov.linkeddata.es/dataset/lov).

![Event vocabularies](vocabs.png)

As demonstrated in the search result capture, there are two possible formal schemas for us to appropriate into our application. 

* At first glance, [schema.org](http://schema.org/Event) appears to fit the profile we're looking for the most parts because it is a widespread shared terminology-space and the predicates belonging there are able to cover the majority of our object (and data) properties, which means our data integration to a bigger knowledge graphs could be guarenteed and it increases the chance that concepts and senses in the UKC-KB are located way more accurately if we start from this namespace. Unfortunately, the problem arises when it comes to 