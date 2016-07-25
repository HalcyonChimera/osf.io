var $ = require('jquery');

// initialize view model for configuring mailchimp subscriptions
var NotificationsConfig =  require('../notificationsConfig.js');
new NotificationsConfig('#selectLists', window.contextVars.mailingLists);

//initialize treebeard for notification subscriptions
var ProjectNotifications = require('../notificationsTreebeard.js');
var $notificationsMsg = $('#configureNotificationsMessage');


console.log('here')

$.ajax({
    url: '/api/v1/subscriptions',
    type: 'GET',
    dataType: 'json'
}).done( function(response) {
    new ProjectNotifications(response);
}).fail( function() {
    $notificationsMsg.addClass('text-danger');
    $notificationsMsg.text('Could not retrieve notification settings.');
});
