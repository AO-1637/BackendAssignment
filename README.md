This repository contains implementation
of a django rest framework API.

The following are the important detils:

a. There are two models : User and ActivityPeriod.

b. The structure of the json data is nested, that is, each User may have
multiple ActivityPeriod objects in from a list stored to a key called
activity_periods.

c. A REST API using djangorestframework is implemented using the necessary
serializers and these serializers are used to build the relevant views.

d. The REST API facilitates get and post requests to the endpoints built.

e. A custom command called populate_db has been created. It was used to
populate the database with a dummy entry.

