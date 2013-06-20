TODO's
------

* Integrate AngularUI:
        * Use "animate" to add event-boxes
        * Use "validate" for event saving form
        * Use "select2" for user filtering and tag/judgement selection
        * Use "highlight" when searching/filtering in the message field
* EventJudgements determine the color of the event-box
* Toggle button per event-type: sonar, bamboo, zabbix, api, user
* Search field to search the message field
* Dropdown to filter by user
* With UserEvents also filtering through tags with labels
* Cap messages to 384 chars
* Make sure the funny/non-business-usable user-events have quotas (quotas evolve positive when your events were globally upvoted):
        * 3 quips per day
        * 2 complaint per day
* With python scikit-learn spam detection (Naive Bayes)


Functionality
-------------

A) Home page is the event-stream.
B) There is a tab/search icon that navigates to a criteria form and event-box listing
C) There is a tab/new icon that navigates to a insertion form for user-events

A) First a fetch is performed on the events-search REST-endpoint for the last events  and subsequently a websocket is opened to receive newly created events. Newer events are displayed on top (Javascript Array.unshift to put in new events on top with AngularUI's animate). When clicking on a tag, judgment, type, instigator field in the event-box one jumps to the search page with the clicked category already filled in the criteria. Maybe let the user only receive messages relevant to him defined in a profile (user-defined event-criteria). The user can also up- or down-vote the events in the stream
B) The Criteria on top of page:
	EventType dropdown 	-> if user-type: show Tag dropdown and switch repeat
				-> if sonar-type: show Project key select2
				-> if bamboo-type: show Build key select2 and switches FAILED and SUCCESS BuildStates
	Timestamp from -> until datepicker (default is last week up until now <- configurable)
	Multiple Instigator select2 (default current user)
	Judgement select2
	Message search-input
	Ordering standard dropdown: ByTime, ByRelevance

   -> When showing results the user can remove still irrelevant event-boxes and extract the whole list as a JSON file.
C) Form on top of the page with:
	Judgement select2
	Multiple Tags select2
	Link input (bootstrap has stuff for this)
	Multiple Instigators select2 (default current user)
	Message input

 -> The user must have a event-box preview when he assembles his event. When everything is valid he must get a ">> Send off" button next to the event-box with a transition that gets swiped of to the right on submit.