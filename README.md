Set up the service in configuration.yaml:

```
slack_status:
    bearer_token: !secret bearer_token
```

Get a bearer token from https://api.slack.com/apps?new_app=1 and set at least the users.profile:write Permission Scope

You can use the service in an automation, for example:

automation:
  trigger:
    platform: state
    entity_id: device_tracker.paulus, device_tracker.anne_therese
    from: 'not_home'
    to: 'home'
  action:
    - service: slack_status.set_status
      data:
        text: "At Home"
        emoji: ":house:"
    - service: light.turn_on
	  data:
	    brightness: 150
	    rgb_color: [255, 0, 0]
	    entity_id:
	      - light.kitchen
	      - light.living_room
