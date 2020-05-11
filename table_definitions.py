EVENT_TABLE_DEFINITIONS = {
    "users.campaigns.Conversion": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("app_id", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("conversion_behavior_index", "integer"),
        ("conversion_behavior", "text"),
        ("message_variation_id", "text"),
        ("send_id", "text"),
    ],
    "users.campaigns.EnrollInControl": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("send_id", "text"),
    ],
    "users.canvas.Conversion": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("app_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("conversion_behavior_index", "integer"),
        ("conversion_behavior", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
    ],
    "users.canvas.Entry": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("in_control_group", "boolean"),
    ],
    "users.messages.email.Send": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
    ],
    "users.messages.email.Delivery": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
        ("sending_ip", "text"),
    ],
    "users.messages.email.Open": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
        ("user_agent", "text"),
    ],
    "users.messages.email.Click": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
        ("url", "text"),
        ("user_agent", "text"),
    ],
    "users.messages.email.Bounce": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
        ("sending_ip", "text"),
    ],
    "users.messages.email.SoftBounce": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
        ("sending_ip", "text"),
    ],
    "users.messages.email.MarkAsSpam": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
        ("user_agent", "text"),
    ],
    "users.messages.email.Unsubscribe": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
        ("email_address", "text"),
    ],
    "users.behaviors.subscriptiongroup.StateChange": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("channel", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("email_address", "text"),
        ("phone_number", "text"),
        ("subscription_group_id", "text"),
        ("subscription_status", "text"),
    ],
    "users.messages.pushnotification.Send": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("app_id", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("platform", "text"),
        ("device_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
    ],
    "users.messages.pushnotification.Open": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("app_id", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("platform", "text"),
        ("os_version", "text"),
        ("device_model", "text"),
        ("device_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
    ],
    "users.messages.pushnotification.IosForeground": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("app_id", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("platform", "text"),
        ("device_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
    ],
    "users.messages.pushnotification.Bounce": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("app_id", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("platform", "text"),
        ("device_id", "text"),
        ("send_id", "text"),
        ("dispatch_id", "text"),
    ],
    "users.messages.inappmessage.Impression": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("card_id", "text"),
        ("send_id", "text"),
        ("app_id", "text"),
        ("platform", "text"),
        ("os_version", "text"),
        ("device_model", "text"),
        ("device_id", "text"),
    ],
    "users.messages.inappmessage.Click": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("button_id", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("card_id", "text"),
        ("send_id", "text"),
        ("app_id", "text"),
        ("platform", "text"),
        ("os_version", "text"),
        ("device_model", "text"),
        ("device_id", "text"),
    ],
    "users.messages.inappmessage.Impression":[
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("card_id", "text"),
        ("send_id", "text"),
        ("app_id", "text"),
        ("platform", "text"),
        ("os_version", "text"),
        ("device_model", "text"),
        ("device_id", "text"),
    ],
    "users.messages.contentcard.Impression": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("app_id", "text"),
        ("content_card_id", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
        ("platform", "text"),
        ("os_version", "text"),
        ("device_model", "text"),
        ("device_id", "text"),
    ],
    "users.messages.newsfeedcard.Impression": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("card_id", "text"),
        ("app_id", "text"),
        ("platform", "text"),
        ("os_version", "text"),
        ("device_model", "text"),
        ("device_id", "text"),
    ],
    "users.messages.newsfeedcard.Click": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("card_id", "text"),
        ("app_id", "text"),
        ("platform", "text"),
        ("os_version", "text"),
        ("device_model", "text"),
        ("device_id", "text"),
    ],
    "users.messages.webhook.Send": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("timezone", "text"),
        ("campaign_id", "text"),
        ("campaign_name", "text"),
        ("message_variation_id", "text"),
        ("canvas_id", "text"),
        ("canvas_name", "text"),
        ("canvas_variation_id", "text"),
        ("canvas_step_id", "text"),
        ("send_id", "text"),
    ],
    "users.behaviors.Uninstall": [
        ("id", "text"),
        ("user_id", "text"),
        ("external_user_id", "text"),
        ("time", "integer"),
        ("app_id", "text"),
    ],
    "users.behaviors.subscriptiongroup.StateChange": [
        ("id", "integer"),
        ("user_id", "integer"),
        ("external_user_id", "integer"),
        ("channel", "integer"),
        ("time", "integer"),
        ("timezone", "integer"),
        ("campaign_id", "integer"),
        ("campaign_name", "integer"),
        ("message_variation_id", "integer"),
        ("canvas_id", "integer"),
        ("canvas_name", "integer"),
        ("canvas_variation_id", "integer"),
        ("canvas_step_id", "integer"),
        ("send_id", "integer"),
        ("email_address", "integer"),
        ("phone_number", "integer"),
        ("subscription_group_id", "integer"),
        ("subscription_status", "integer")
    ]
}