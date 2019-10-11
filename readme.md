# UMM Laundy API

This api is built using [Flask](https://www.fullstackpython.com/flask.html), which is a simple web-framework.

Json files can be found in the [static folder](app/static).

All routes are of type GET.

## Hosting:
The project currently isn't hosted anywhere, but eventually it will be hosted on Heroku. Everyone can connect to it from any computer. Example API call:
`116.132.247.33/rooms/gay/machines`
## Routes:
See the [format](##format) section, or the [static folder](app/static) for json specifications.

`/` default route. Prints some information about routes.

`/rooms` prints a list of rooms

`/machines` prints a list of all machines

`/rooms/<room>/machines` prints a list of machines, sorted by room

`/machines/<machine>` prints a specific machine, as indexed by its id.

## Format
Please view the [static folder](app/static) for the full json.

Rooms:
```
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

Machines:

```
[{
	"id": "080258ae-ec80-11e9-8788-902b34113095",
	"name": "ready-cerulean-kakapo",
	"type": "dryer",
	"running": true,
	"status": "normal",
	"position": {
		"x": 0,
		"y": 0
	},
	"room_id": "green_prairie"
}, {
	"id": "080258af-ec80-11e9-8788-902b34113095",
	"name": "wiggy-linen-mist",
	"type": "washer",
	"running": false,
	"status": "normal",
	"position": {
		"x": 0,
		"y": 0
	},
  "room_id": "the_apartments"
  .
  .
  . etc
]
```

## Position

As you can see in the format above, machines come with a `x` and `y` position argument. This is currently set to 0, but eventually this will be used to show positioning of specific machines.

The scale will be 0-6, or a 7x7 grid, which seems to be the right granularity to communicate the positioning.
