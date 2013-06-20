from pyramid.view import view_config
from socketio.namespace import BaseNamespace

import gevent

class EventStreamNamespace(BaseNamespace):
    def initialize(self):
        print 'Init EventStreamNamespace'
	self.emit('socket_event', {
                "_id": {
                        "$oid": "51c1d9afe4b03a888418ea58"
                },
                "occurrence": "2013/06/27 18:17:36",
                "tags": [
                        "HACK"
                ],
                "judgement": [
                    "HEROLIKE"
                ],
                "instigators": [
                    "jalie"
                ],
                "message": "SocketIO is awesome!",
                "comments": [
                        {
                                "userid": "jalie",
                                "timestamp": "2013/06/19 18:18:04",
                                "message": "Hellz Yeah!"
                        }
                ]
                })
        #self.spawn(self.job_send_event)

    def job_send_event(self):
        while True:
	    self.emit('socket_event', {
    		"_id": {
        		"$oid": "51c1d9afe4b03a888418ea58"
    		},
    		"occurrence": "2013/06/27 18:17:36",
    		"tags": [
        		"HACK"
    		],
    		"judgement": [
    		    "HEROLIKE"
    		],
    		"instigators": [
    		    "jalie"
    		],
    		"message": "SocketIO is awesome!",
    		"comments": [
        		{
            			"userid": "jalie",
            			"timestamp": "2013/06/19 18:18:04",
            			"message": "Hellz Yeah!"
        		}
    		]
		})
	    gevent.sleep(10)
        

@view_config(route_name='socketio')
def socketio(request):
    from socketio import socketio_manage
    socketio_manage(request.environ, {'/eventstream': EventStreamNamespace},
                    request=request)

@view_config(route_name='home', renderer='templates/index.html')
def my_view(request):
    return {'project': 'culpa'}
