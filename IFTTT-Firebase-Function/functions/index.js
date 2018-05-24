const functions = require('firebase-functions');
const firebase = require('firebase');

var config = {}
config.apiKey = functions.config().db.apikey;
config.authDomain = functions.config().db.authdomain;
config.databaseURL = functions.config().db.databaseurl;
config.projectId = functions.config().db.projectid;
config.storageBucket = functions.config().db.storagebucket;

firebase.initializeApp(config);

exports.iftttToRealtimeDatabase = functions.https.onRequest((request, response) => {

    const email = request.body.email;
    const userid = request.body.userid;
    const topic = request.body.topic;
    const value = request.body.value;
    const password = functions.config().account.password;
    const secret =   functions.config().account[userid].secret;

    if (request.body.secret != secret) {
        response.send("error");
        return;
    }

    firebase.auth().signInWithEmailAndPassword(email, password)
        .then(user => {
            firebase.database().ref("/mqtt/" + topic).set("").then(function() {
                firebase.database().ref("/mqtt/" + topic).set(value);
                response.send("topic: " + value);
            })
        })
        .catch(error => {
            response.send("error");
        });
});
