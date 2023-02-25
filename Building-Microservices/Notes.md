# Building Microservices - Designing Fine-Grained Systems by Sam Newman

## Chapter 1 - What Are Microservices?

* "Microservices are independently releasable services that are modeled around a business domain" (Newman 3.)
* "They are a type of service-oriented architecture" (Newman 3.)
* Microservices are treated as a black box, hosting business functaionlity through connectors (API network etc..)
* Microservcies avoid teh use of shared databases, each microservice has it's own db in most cases 
* They hide information, encapsulate it
* Limiting the use of external interfaces, that allows for less change or breakage given the fact if the external inerfaces
are backward compatible then the interals can change freely.
* The Hexagonal Architecture pattern - the imprtance of keeping the internal implementation separate 
from it's external interfaces.
* Service-Oriented Architecture vs Microservices 
    * "SOA is a design approach in which multiple services collaborate to provide a certian end set of capabilities" (Newman 5.)
    * "A service hear typically means a completely separate os process" (Newman 5.)
    * Things can be service oriented however still coupled. So not microservices, ex: a bunch of services coupled to the same 
    DB
* Independent Deployability - "The idea that we can make a chagne to a microservice, deploy it and release that change to our users,
 without having to deploy any other microservices (Newman 6.)"
* To do this we need very loosely coupled microservices
* Changing more than one microservice to meet a functionality is more expensive and worse than just having a monolith
* A Microservice should be the size at which it is still easily understood
* We define microservices by business logic, a customer team owns the UI, DB and Backend for something like a customer 
profile
* When all functionality in a system must be deployed together that is considered a monolith

##### The Single-Process Monolith
* All code is packe dinto a single process. These can technically still be distributed systems reading from a db for example.

##### The Modular Monolith
* A subset of singled process monoliths. Each module can be worked on separately but still need to all be deployed together.
* Better with a decoupled db, though can work with a single db

##### The Distributed Monolith 
* Multiple services, but for whatever reason has to be all deployed together
* "A distributed system is one in which the failure of a computer you didn't even know existed can render you own computer unusable"
- Leslie Lamport

##### Advantages of Monoliths
* Much simpler
* Shared functionality can be implemented much easier
* Monoliths are not legacy their design choice can be valid

##### Log Aggregation and Distributed Tracing
* With logs of microservices all attached to different systems it can be hard to understand how they are interacting
in a production setting
* The fix for this is a log aggregation tool (I wonder if this is splunk or sumo logic?)
* Correlation ID's in which a single ID is used for a related set of service calls :D (Local motion)

##### K8 and Containers
* Run each microservice in isolation

##### Public Cloud and Serverless
* Use them lol, to reduce complexity

#### Advantages of Microservices
* Have significant more advantages than distributed systems, due to the service level or domain cohesion approach

    ##### Technology Heterogenity
    * We can pick the right tech for the job at hand. Rather than having to pick a one size fits all approach, we can 
    be more tailored
    
    ##### Robustness
    * One component of a system may fail, but it doesnt sink the ship
    * However networks can and will fail, so we need to make sure we are handling those concerns appropriately
    
    ##### Scaling
    * We can scale just the taxed service and not the whole system
    
    ##### Cost
    * Reduces in the long term increases in the short term
    
    ##### Monitoring
    * Much harder to monitor across multiple systems but less binary up or down monitoring
    
## Chapter 2 - How to Model Microservices

##### Information Hiding
* Improved Development Time - parallel development
* Comprehensibility - Each module can be understood in isolation
* Flexability - Orthogonal to each other

##### Cohesion and Coupling
* Cohesion - Code that changes together stays together, when adding functionality we want as little code to change as possible
* We want related behavior to stay together and unrelated to go elsewhere
* Coupling - A change in one service needs a change in another
* Coupling can be unavoidable, we only limit it as much as we can


Domain -  Pass-through  - Common - Content

Low/Loose Coupling    ->       High coupling

* Domain Coupling - Where one microservice needs to interact with another microservice, because the first microserivce needs to 
make use of the functionality that the other provides (Newman 41).
* Domain Coupling is largely unavoidable
* Though to much domain coupling by a single service might mean that service is doing to much
* Temporal Coupling in microservices is different from temporal coupling in application code? Basically
one microservice needs another microservice to do something at the same time. This is not a bad thing however.
I think they mean RPC here
* Pass-Through Coupling - "Describes a situation in which one microservice passes data to another microservice purely because the
data is needed by some other microserivce furth downstream" (Newman 43)
* Pass-Through Coupling is very bad :/
* Common Coupling - "When two or more microservices make use of a common set of data" (Newman 46.)
* Content Coupling - "Where upstream service reaches into internals of downstream service and changes its internal state" (Newman 49.)
* An example of content coupling would be a microservice connecting ot another's DB and then mangling with it
 
 