# UMM Laundy API

This api is built using [Flask](https://www.fullstackpython.com/flask.html), which is a simple python web-framework.

Hosting:
======
The project is currently hosted on my personal Vultr account. This isn't necesarily costing me money, so I am happy to keep hosting it for the time being. 

For longevity though, it would be good to move hosting (as well as this repository) somewhere else.

I am not going to publicly post the IP here, cause I want to avoid any issues. You can contact me if you would like access.

Routes:
======


See the [format](##format) section for json specifications.

`/` default route. Prints some information about routes.

`/rooms` prints a list of rooms

`/machines` prints a list of all machines

`/rooms/<room>/machines` prints a list of machines, sorted by room

`/machines/<machine>` prints a specific machine, as indexed by its id.

`/update_machine` takes machine specification. This machine will now be served up from the other endpoints. A reload will clear this list, meaning a fresh run will have no machines. Machines will be populated as their status' change. 

Format
======

**Rooms:**

This is a static list. Edit in [config.json](app/config.json).

```JSON
[
  {
  	"id": "gay",
  	"name": "Gay Hall"
  },
  {
  	"id": "independence",
  	"name": "Independence Hall"
  }
  .
  .
  . etc
]
```

**Machines:**

This list is generated by posts to `update_machine`, and is cleared on reload.
```JSON
[{
	"id": "080258ae-ec80-11e9-8788-902b34113095",
	"name": "ready-cerulean-kakapo",
	"type": "dryer",
	"running": true,
	"status": "normal",
	"room_id": "green_prairie"
}, {
	"id": "080258af-ec80-11e9-8788-902b34113095",
	"name": "wiggy-linen-mist",
	"type": "washer",
	"running": false,
	"status": "normal",
    "room_id": "the_apartments"
	}
  .
  .
  . etc
]
```
Adding machines
======
This API is designed specifically to work agnostically to the machine list. The API is meant as a json-mirror, which simply forwards the current list of machines, filtered somewhat. The current list of machines is simply whichever machines have send update POSTS since the app came online.

To add new machines, simply setup the correct JSON payloads, and the app will mirror these machines.

The idea is that json payloads will be sent via IFTTTs webhook system. When the IOT-plug drops bellow, or rises above certain power threshholds, it will send a json packet to the `update_machine` list.

This packet should be formed as the json for a single machine:
```JSON
{
	"id": "080258ae-ec80-11e9-8788-902b34113095",
	"name": "ready-cerulean-kakapo",
	"type": "dryer",
	"running": true,
	"status": "normal",
	"room_id": "green_prairie"
}
```
This json can be created using the utility functions.

The idea is that two IFTTT rules will be created for each new laundry plug: one to detect powering down, one to detect powering up.

Names:
======

As you can see, each machine has a "name" slot. This is currently filled with silly random-gen names, but they can be handpicked later if desired. This is meant as a human-readable UUID for the machine, so you can easily identity machines.

Generating new machines
======

This repo also contains two python utility scripts, both found in the `app/utility` folder.

`generate_machine.py`: This script will print the json for a new machine, based on inputs.

`generate_random_machine.py`: This script will create a random machine.

Running the server
======

Before you can run the server, you need to install flask:
> Consider using a venv

`pip3 install flask`

Then you can run:

`FLASK_APP=run.py`

`flask run`

Testing the server:
======

If you turn off security in config.py, you can use curl or similar to test adding machines:

`curl -d <machine> -X POST -H "Content-Type: application/json" http://<url>/update_machine`