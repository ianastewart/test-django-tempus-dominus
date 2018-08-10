# test-django-tempus-dominus
Small app to fully test django-tempus-dominus datetimepicker functionality.

There is a bug in Firefox that does not show up in Chrome or Edge.

* Start the app locally and create a record with a date, time and datetime.
* Go back to the list page
* Click the saved record to open it
* The fields show the correct values
* Press the browser refresh button
* On Chrome & Edge, the screen refreshes and shows the same data as before
* On Firefox, the fields are cleared!
* Press refresh again - the data reappears

Sometimes a full datetime gets shown in the date field and if that happens a javascript recursion error occurs, but only in Firefox.

I think this must be to do with a subtle difference in the way that events are handled but I cannot pin it down.
