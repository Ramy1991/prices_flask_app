importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
    apiKey: "AIzaSyCQYdl0vf8gKnayNRM18dbfMpYIQxzi0LI",
    authDomain: "bright-lattice-260000.firebaseapp.com",
    databaseURL: "https://bright-lattice-260000.firebaseio.com",
    projectId: "bright-lattice-260000",
    storageBucket: "bright-lattice-260000.appspot.com",
    messagingSenderId: "1014243229877",
    appId: "1:1014243229877:web:71f55e2379e3c05a8bfefc",
    measurementId: "G-275CEDTFV7"
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    // Customize notification here
    const notificationTitle = 'Background Message Title';
    const notificationOptions = {
      body: 'Background Message body.',
      icon: '/firebase-logo.png'
    };
  
    self.registration.showNotification(notificationTitle,
      notificationOptions);
});