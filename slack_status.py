"""
Service to set a Slack status.

For more details about this platform, please refer to the documentation at
https://URL/components/slack_status/
"""
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

DOMAIN = 'slack_status'
REQUIREMENTS = ['requests==0.0.1'] #what version should I put here?

CONF_STATUS_TEXT = 'text'
CONF_STATUS_EMOJI = 'emoji'

#Set default for calling the service without any data (This should clear any status/emoji)
DEFAULT_STATUS_TEXT = ''
DEFAULT_STATUS_EMOJI = ''

#Not sure if this is correct or not
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_STATUS_TEXT, default=DEFAULT_STATUS_TEXT): cv.string,
        vol.Required(CONF_STATUS_EMOJI, default=DEFAULT_STATUS_EMOJI): cv.string,
    }),
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def set_status(call):
        import requests
    	emoji = call.data.get('emoji', TEXT_STRING) #try to get the data passed into the service
    	text = call.data.get('text', EMOJI_STRING) #^^

        # hass.states.set('hello_service.hello', name)
		url = "https://slack.com/api/users.profile.set"

		payload = "{\"profile\":{\"status_text\": \""+ text +"\",\"status_emoji\": \""+ emoji +"\"}}"
		headers = {
		    'Content-Type': "application/json; charset=utf-8",
		    'Authorization': "Bearer "+ config['slack_status']['bearer_token'],
		    'Cache-Control': "no-cache",
		    }

		response = requests.request("POST", url, data=payload, headers=headers)

		print(response.text)

    hass.services.register(DOMAIN, 'set_status', set_status)

    # Return boolean to indicate that initialization was successfully.
    return True