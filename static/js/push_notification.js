import { getMessaging, getToken } from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-messaging.js';
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js";


const firebaseConfig = {
    apiKey: "AIzaSyCQYdl0vf8gKnayNRM18dbfMpYIQxzi0LI",
    authDomain: "bright-lattice-260000.firebaseapp.com",
    databaseURL: "https://bright-lattice-260000.firebaseio.com",
    projectId: "bright-lattice-260000",
    storageBucket: "bright-lattice-260000.appspot.com",
    messagingSenderId: "1014243229877",
    appId: "1:1014243229877:web:71f55e2379e3c05a8bfefc",
    measurementId: "G-275CEDTFV7"
};



if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register(window.location.origin + "/firebase-messaging-sw.js", {scope: '/'}).then(initialiseState);
} else {
  console.warn('Service workers aren\'t supported in this browser.');
}

function initialiseState() {
  // Are Notifications supported in the service worker?
  if (!('showNotification' in ServiceWorkerRegistration.prototype)) {
    console.warn('Notifications aren\'t supported.');
    return;
  }

  // Check the current Notification permission.
  // If its denied, it's a permanent block until the
  // user changes the permission
  if (Notification.permission === 'denied') {
    console.warn('The user has blocked notifications.');
    return;
  }

  // Check if push messaging is supported
  if (!('PushManager' in window)) {
    console.warn('Push messaging isn\'t supported.');
    return;
  }

  // We need the service worker registration to check for a subscription
  navigator.serviceWorker.ready.then(function(serviceWorkerRegistration) {
    // Do we already have a push message subscription?
    serviceWorkerRegistration.pushManager.getSubscription()
      .then(function(subscription) {
        // Enable any UI which subscribes / unsubscribes from
        // push messages.
        var pushButton = document.querySelector('.js-push-button');
        pushButton.disabled = false;

        if (!subscription) {
          // We aren't subscribed to push, so set UI
          // to allow the user to enable push
          return;
        }

        // Keep your server in sync with the latest subscriptionId
        sendSubscriptionToServer(subscription);

        // Set your UI to show they have subscribed for
        // push messages
        pushButton.textContent = 'Disable Push Messages';
        isPushEnabled = true;
      })
      .catch(function(err) {
        console.warn('Error during getSubscription()', err);
      });
  });
}


  // ASK FOR PUSH NOTIFICATION APPROVAL

  

function askForApproval() {
  if(Notification.permission === "granted") {
    createNotification('Wow! This is great', 
                       'created by @study.tonight', 
                       'https://www.studytonight.com/css/resource.v2/icons/studytonight/st-icon-dark.png');
    subscribe();
                                          
  } else {
    
    Notification.requestPermission(permission => {
      if(permission === 'granted') {
        createNotification('Wow! This is great', 'created by @study.tonight', 'https://www.studytonight.com/css/resource.v2/icons/studytonight/st-icon-dark.png');
      }
    });
    unsubscribe();
  }
}

function createNotification(title, text, icon) {
  const noti = new Notification(title, {
    body: text,
    icon
  });
}
askForApproval();



function subscribe() {
  // Disable the button so it can't be changed while
  // we process the permission request
  var pushButton = document.querySelector('.js-push-button');
  pushButton.disabled = true;

  navigator.serviceWorker.ready.then(function(serviceWorkerRegistration) {
    serviceWorkerRegistration.pushManager.subscribe()
      .then(function(subscription) {
        // The subscription was successful
        isPushEnabled = true;
        pushButton.textContent = 'Disable Push Messages';
        pushButton.disabled = false;

        // TODO: Send the subscription.endpoint to your server
        // and save it to send a push message at a later date
        return sendSubscriptionToServer(subscription);
      })
      .catch(function(e) {
        if (Notification.permission === 'denied') {
          // The user denied the notification permission which
          // means we failed to subscribe and the user will need
          // to manually change the notification permission to
          // subscribe to push messages
          console.warn('Permission for Notifications was denied');
          pushButton.disabled = true;
        } else {
          // A problem occurred with the subscription; common reasons
          // include network errors, and lacking gcm_sender_id and/or
          // gcm_user_visible_only in the manifest.
          console.error('Unable to subscribe to push.', e);
          pushButton.disabled = false;
          pushButton.textContent = 'Enable Push Messages';
        }
      });
  });
}


function unsubscribe() {
  var pushButton = document.querySelector('.js-push-button');
  pushButton.disabled = true;

  navigator.serviceWorker.ready.then(function(serviceWorkerRegistration) {
    // To unsubscribe from push messaging, you need get the
    // subscription object, which you can call unsubscribe() on.
    serviceWorkerRegistration.pushManager.getSubscription().then(
      function(pushSubscription) {
        // Check we have a subscription to unsubscribe
        if (!pushSubscription) {
          // No subscription object, so set the state
          // to allow the user to subscribe to push
          isPushEnabled = false;
          pushButton.disabled = false;
          pushButton.textContent = 'Enable Push Messages';
          return;
        }

        var subscriptionId = pushSubscription.subscriptionId;
        // TODO: Make a request to your server to remove
        // the subscriptionId from your data store so you
        // don't attempt to send them push messages anymore

        // We have a subscription, so call unsubscribe on it
        pushSubscription.unsubscribe().then(function(successful) {
          pushButton.disabled = false;
          pushButton.textContent = 'Enable Push Messages';
          isPushEnabled = false;
        }).catch(function(e) {
          // We failed to unsubscribe, this can lead to
          // an unusual state, so may be best to remove
          // the users data from your data store and
          // inform the user that you have done so

          console.log('Unsubscription error: ', e);
          pushButton.disabled = false;
          pushButton.textContent = 'Enable Push Messages';
        });
      }).catch(function(e) {
        console.error('Error thrown while unsubscribing from push messaging.', e);
      });
  });
}

// if ('serviceWorker' in navigator) {
//     navigator.serviceWorker.register(window.location.origin + "/firebase-messaging-sw.js", {scope: '/'}).then(registration => {
//         console.log("ServiceWorker running");
//     }).catch(err => {
//         console.log(err);
//     })
//   }



// const app = initializeApp(firebaseConfig);
// // Get registration token. Initially this makes a network call, once retrieved
// // subsequent calls to getToken will return from cache.
// const messaging = getMessaging();
// getToken(messaging, { vapidKey: 'BCCQ90gHgbcJsHwGMOFcA7ZleVGWn8VRvvfiQ7_kXkQjKCtbVItTZ_jWclGCWdRvWiv9wVUnVEZu6dSSwt9A13s' }).then((currentToken) => {
//   if (currentToken) {
//     // Send the token to your server and update the UI if necessary
//     console.log(currentToken);
//     // ...
//   } else {
//     // Show permission request UI
//     console.log('No registration token available. Request permission to generate one.');
//     // ...
//   }
// }).catch((err) => {
//   console.log('An error occurred while retrieving token. ', err);
//   // ...
// });