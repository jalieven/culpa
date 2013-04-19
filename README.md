     _______  __   __  ___      _______  _______
    |       ||  | |  ||   |    |       ||       |
    |       ||  | |  ||   |    |    _  ||   _   |
    |       ||  |_|  ||   |    |   |_| ||  | |  |
    |      _||       ||   |    |    ___||  |_|  |
    |     |  |  o o  ||   |___ |   |    |       |
    |     |_ |   T   ||       ||   |    |   _   |
    |_______||_______||_______||___|    |__| |__|


A tool for blaming developers when they do harmful things to the organisation and generate some some shame in them
through a speaking/flapping/flashing Karotz rabbit.
Culpa also provides an event-stream for back-reference or root-cause-analyses.

Culpa monitors different subsystems and their metrics:

* **Bamboo build server**: Build failed? Less tests than before? More tests than before? And who did this?
* **Sonar code analyses server**: Project coverage went down? Blocking or critical violations popped up? Who is culpable?
* **Zabbix system monitoring server**: Load on a server went through the ceiling? Not enough memory?

Culpa will generate events when stuff changes for the worse (praise can be generated as well). These events can be viewed
as a stream and will be acted upon by the Karotz rabbit.

Prerequisites/dependencies
--------------------------


sudo pip install redis
sudo pip install hiredis
sudo pip install apscheduler
sudo pip install flask
sudo pip install flask-restful
sudo pip install flufl.enum
sudo pip install jsonpickle
sudo pip install jsonschema
sudo pip install beautifulsoup4


Configuration
-------------

Everything that can be configured in Culpa is located in the file culpa-config.json
